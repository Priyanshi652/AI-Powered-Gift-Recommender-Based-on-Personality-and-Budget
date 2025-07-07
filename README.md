# AI-Powered-Gift-Recommender-Based-on-Personality-and-Budget


A personalized gift suggestion system using **Artificial Intelligence (AI)** and **Machine Learning (ML)** based on the recipient's **personality** and **budget**. This project aims to solve a common real-world problem: "What should I gift someone that suits them and fits my budget?"

---

## 📌 Table of Contents

* [Demo](#demo)
* [Problem Statement](#problem-statement)
* [Proposed Solution](#proposed-solution)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Installation](#installation)
* [How to Run](#how-to-run)
* [System Architecture](#system-architecture)
* [Model Details](#model-details)
* [Results](#results)
* [Future Scope](#future-scope)
* [Screenshots](#screenshots)
* [Contributors](#contributors)

---

## 🧩 Demo

Try the app locally using Streamlit:

```
streamlit run app.py
```

---

## ❓ Problem Statement

Choosing a thoughtful gift is difficult — especially when you're unsure about someone's preferences or your budget is limited. Most gifting platforms offer generic suggestions, not personalized ones. The aim is to help users find suitable gifts based on the **recipient's personality** and their **budget** using AI.

---

## ✅ Proposed Solution

This project offers a smart and lightweight web app that:

* Takes **personality traits** and **budget** as inputs
* Uses an ML model to **predict the most suitable gift category**
* Displays a list of recommended gifts under that category and budget
* (Optional) Supports voice input (removed in this version)

---

## 🎯 Features

* Personality-based classification of gifts
* Budget filtering
* ML-powered gift category prediction (Random Forest Classifier)
* Responsive web app using Streamlit
* Easily expandable product dataset

---

## 💻 Tech Stack

| Component     | Tool/Library                |
| ------------- | --------------------------- |
| Language      | Python 3.10+                |
| UI Framework  | Streamlit                   |
| ML Library    | scikit-learn                |
| Data Handling | pandas                      |
| Model Storage | joblib                      |
| Deployment    | Localhost / Streamlit Cloud |

---

## 🛠 Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/ai-gift-recommender.git
cd ai-gift-recommender
```

2. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

```
streamlit run app.py
```

Make sure `app.py` is in your working directory.

---

## 🧠 System Architecture

```
User Input (personality + budget)
        ↓
Label Encoding
        ↓
Trained RandomForest Model
        ↓
Predicted Gift Category
        ↓
Filtered Gift List (≤ budget)
        ↓
Streamlit UI Output
```

---

## 🤖 Model Details

* **Algorithm**: Random Forest Classifier
* **Input Features**: Encoded `personality_type`, `budget`
* **Target**: Gift category (multi-class)
* **Training**: Performed on a small but diverse labeled dataset
* **Serialization**: Model and encoders stored using `joblib`

---

## 📊 Results

* ML model accurately predicts gift categories based on limited inputs
* Streamlit app displays correct gift recommendations for multiple test cases
* Fast response and easy to use, even on low-end systems

---

## 🔮 Future Scope

* Use NLP embeddings to understand broader personality descriptions
* Export gift recommendations to PDF or send via email
* Integrate live pricing/product APIs from Flipkart, Amazon
* Save user profiles for more intelligent suggestions over time
* Build mobile app version using React Native or Flutter

---

## 🖼 Screenshots

*Add screenshots of:*

* Home page-![07 07 2025_19 14 20_REC](https://github.com/user-attachments/assets/03b5bb6d-d2ce-4657-8315-a9a0c1bc923e)
* Input form -![07 07 2025_19 13 26_REC](https://github.com/user-attachments/assets/9665d822-d5a3-4289-91cf-e8b23e554595)


---

## 👩‍💻 Contributors

| Name                   | Role               |
| ---------------------- | ------------------ |
| Your Name              | priyanshi| data aspirant


---

## 🙌 Acknowledgments

* Streamlit Team for a wonderful UI framework
* scikit-learn for ML algorithms
* AICTE for supporting innovation in internships

---

> Built with ❤️ as an internship project to solve real-world problems using AI and ML
