BOOK RECOMMENDATION SYSTEM

# 📚 Book Recommendation System

## 🔍 Overview

This project is a **Content-Based Book Recommendation System** built using **Streamlit**. It uses **TF-IDF** and **Cosine Similarity** on book descriptions to recommend similar books. Additionally, it features:
- 📖 **Google Books API integration** for cover images
- 🌗 **Dark/Light theme toggle**
- 💡 A user-friendly Python-powered interface without needing HTML/CSS

---

## 🧠 Features

| Feature               | Description |
|----------------------|-------------|
| 🔍 Book Selection     | Select a book from a dropdown to get similar recommendations |
| 🤖 Content-Based ML  | Uses TF-IDF and cosine similarity to compute recommendations |
| 🖼️ Book Cover Images | Integrates with Google Books API to fetch cover images |
| 🌗 Dark/Light Mode    | Toggle between dark and light UI themes (Streamlit-based) |
| ⚡ Fast UI            | Built using Streamlit for quick interaction and no frontend coding |

---

## ?? Folder Structure

```
BookRecommendation/
├── app.py              # Main Streamlit app
├── book.csv            # Dataset containing title, authors, description
└── README.md           # Documentation (this file)
```

---

## 🗂️ Dataset

The dataset file `book.csv` must contain the following **columns**:

| Column Name  | Description                         |
|--------------|-------------------------------------|
| `title`      | Book title                          |
| `authors`    | Book author(s)                      |
| `description`| Short book summary (used for ML)    |

You can use a sample dataset or real-world data (e.g., from [Goodbooks-10k](https://github.com/zygmuntz/goodbooks-10k)).

---

## ⚙️ Installation & Setup

### 1. Install dependencies

Make sure Python 3.7+ is installed. Then install packages:

```bash
pip install streamlit pandas scikit-learn requests
```

### 2. Run the App

```bash
streamlit run app.py
```

Then visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🚀 How It Works

1. **TF-IDF Vectorization**: The book descriptions are vectorized using TF-IDF.
2. **Cosine Similarity**: Computes similarity between books.
3. **User Input**: You choose a book title from a dropdown.
4. **Top 5 Matches**: Based on description similarity, it shows 5 similar books.
5. **Cover Images**: Uses Google Books API to fetch and display book covers.

---

## 🧪 Sample Data

Here’s a preview of a small `book.csv`:

```csv
title,authors,description
Harry Potter and the Sorcerer's Stone,J.K. Rowling,Harry discovers he is a wizard...
The Hobbit,J.R.R. Tolkien,A hobbit joins a quest to defeat a dragon...
1984,George Orwell,A dystopian future under surveillance...
```

---

## 📦 Future Improvements

- 🔐 User login & personalized recommendations
- ⭐ Save favorite books per user
- 🔁 Add collaborative filtering (user-based)
- 🎨 Custom themes and UI enhancements
- ☁️ Deploy to cloud (e.g., Render, HuggingFace Spaces)

---

## 👩‍💻 Built With

- [Streamlit](https://streamlit.io/)
- [Scikit-learn](https://scikit-learn.org/)
- [Google Books API](https://developers.google.com/books)
- [Pandas](https://pandas.pydata.org/)

---

## 📸 Screenshots








---

## 🏁 Conclusion

This project demonstrates how to build a full-stack recommendation system using Python and Streamlit, with zero frontend coding. It’s fast, interactive, and ideal for showcasing in portfolios or deploying for real users.

