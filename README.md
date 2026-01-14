# 📌 **Project: Fake News Detector (Machine Learning + NLP)**

This project is a web-based Fake News Detection system that uses **Natural Language Processing (NLP)** and **Machine Learning** to classify news articles as **Real** or **Fake**.
The web interface is built using **Streamlit** and the model is deployed on **Streamlit Cloud** for public access.

---

## 🚀 **Features**

* Classifies news as **Real** or **Fake**
* Uses TF-IDF vectorization for text processing
* Logistic Regression classifier for prediction
* Clean and user-friendly web UI
* Lightweight and fast inference

---

## 🧠 **Machine Learning Workflow**

1. **Dataset Collection**

   * Dataset contains real and fake news articles with labels.

2. **Text Preprocessing**

   * Lowercasing
   * Stopword removal
   * Vectorization using **TF-IDF**

3. **Model Training**

   * Trained using **Logistic Regression**
   * Saved using **Joblib** for deployment

4. **Deployment**

   * Frontend/UI: **Streamlit**
   * Hosting: **Streamlit Cloud**

---

## 🛠 **Tech Stack**

| Component     | Technology            |
| ------------- | --------------------- |
| Language      | Python                |
| UI Framework  | Streamlit             |
| ML Model      | Logistic Regression   |
| NLP           | TF-IDF (Scikit-Learn) |
| Deployment    | Streamlit Cloud       |
| Serialization | Joblib                |

---

## 📂 **Project Structure**

```
fake-news-detector/
│
├── app.py
├── lr_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
├── notebook/
│   └── training.ipynb
├── Fake.csv (Fake news data)
├── True.csv (True news data)

```

---

## 📦 **Installation (Local Setup)**

Clone the repository:

```bash
git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## 🌐 **Live Demo**

> 🔗 Add your deployed Streamlit URL here once deployed
> Example:

```
https://yourusername-fake-news-detector.streamlit.app
```

---

## 📊 **Results**

* Achieved high accuracy on validation data
* Performs well on real-world text inputs

---

## 🎯 **Future Enhancements**

* Add confidence scores for predictions
* Use BERT transformer for improved accuracy
* Support news URLs via web scraping
* Collect real-time news data via APIs

---

## 🤝 **Contributing**

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📄 **License**

This project is for educational and research purposes.
No commercial usage of dataset or model without permission.

---

## 👤 **Author**

**Name:** Rituraj Kanchan
*AI/ML Developer & Internship Trainee*

