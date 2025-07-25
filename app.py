import streamlit as st
import pandas as pd
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# ----------------------------
# Theme Toggle (Light / Dark)
# ----------------------------
theme = st.radio("Choose Theme", ["Light", "Dark"], horizontal=True)

if theme == "Dark":
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #0e1117;
                color: white;
            }
            .css-1d391kg { color: white; }
            .css-1v0mbdj p, .css-1v0mbdj { color: white !important; }
        </style>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# Load Book Dataset
# ----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(r"A:\BookRecommendation\book.csv")  # ✅ Replace path if needed
    df = df[['title', 'authors', 'description']].dropna()
    return df

books = load_data()

# ----------------------------
# TF-IDF Cosine Similarity
# ----------------------------
@st.cache_resource
def compute_similarity(data):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data['description'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim

cosine_sim = compute_similarity(books)
indices = pd.Series(books.index, index=books['title']).drop_duplicates()

# ----------------------------
# Google Books API Cover Image
# ----------------------------
def get_book_cover(title):
    try:
        url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{title}"
        response = requests.get(url)
        data = response.json()
        if "items" in data:
            return data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
    except:
        pass
    return "https://via.placeholder.com/120x180.png?text=No+Image"

# ----------------------------
# Recommendation Logic
# ----------------------------
def recommend_books(title, cosine_sim=cosine_sim):
    idx = indices.get(title)
    if idx is None:
        return pd.DataFrame()
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Top 5
    book_indices = [i[0] for i in sim_scores]
    return books.iloc[book_indices][['title', 'authors']]

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("📚 Book Recommendation System")
st.markdown("Get book recommendations based on content similarity (TF-IDF).")

selected_book = st.selectbox("Choose a book title:", books['title'].values)

if st.button("Recommend"):
    st.subheader("📖 Recommended Books:")
    recommendations = recommend_books(selected_book)
    if recommendations.empty:
        st.warning("No recommendations found.")
    else:
        for _, row in recommendations.iterrows():
            col1, col2 = st.columns([1, 4])
            with col1:
                img_url = get_book_cover(row['title'])
                st.image(img_url, width=100)
            with col2:
                st.markdown(f"**{row['title']}**  \nby *{row['authors']}*")
