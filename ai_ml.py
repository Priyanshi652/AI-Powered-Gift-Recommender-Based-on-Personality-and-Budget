# Project: AI-Powered Gift Recommender Based on Personality, Budget (Without Voice Input)
# Tools Used: Python, Streamlit, pandas, scikit-learn (ML), joblib

# ---------------------------
# Step 1: Data Preparation & ML Model Training
# ---------------------------

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Expanded dataset with ML-ready format
ml_data = pd.DataFrame({
    'personality_type': [
        'emotional', 'active', 'organized', 'nature-lover', 'curious',
        'calm', 'adventurous', 'creative', 'tech-savvy',
        'foodie', 'movie-lover', 'calm', 'adventurous', 'organized'
    ] * 3,
    'budget': [300, 1800, 500, 350, 700, 400, 1100, 600, 1300, 400, 3000, 900, 2000, 800] * 3,
    'gift_category': [
        'Home', 'Fitness', 'Work', 'Nature', 'Fun', 'Relaxation', 'Travel', 'Art', 'Tech',
        'Food', 'Entertainment', 'Fitness', 'Adventure', 'Home'
    ] * 3
})

# Encode text to numbers
le_personality = LabelEncoder()
le_category = LabelEncoder()

ml_data['personality_encoded'] = le_personality.fit_transform(ml_data['personality_type'])
ml_data['category_encoded'] = le_category.fit_transform(ml_data['gift_category'])

# Train model
X = ml_data[['personality_encoded', 'budget']]
y = ml_data['category_encoded']
model = RandomForestClassifier()
model.fit(X, y)

# Save encoders and model
joblib.dump(model, 'gift_model.pkl')
joblib.dump(le_personality, 'personality_encoder.pkl')
joblib.dump(le_category, 'category_encoder.pkl')

# Load final gift dataset for recommendation
gift_data = pd.DataFrame({
    'gift_name': [
        'Personalized Mug', 'Fitness Band', 'Leather Notebook', 'Plant Kit', 'Puzzle Set',
        'Scented Candle', 'Travel Backpack', 'Sketching Kit', 'Bluetooth Speaker',
        'Cookbook', 'Mini Projector', 'Yoga Mat', 'Adventure Coupon', 'LED Desk Lamp'
    ],
    'category': [
        'Home', 'Fitness', 'Work', 'Nature', 'Fun',
        'Relaxation', 'Travel', 'Art', 'Tech',
        'Food', 'Entertainment', 'Fitness', 'Adventure', 'Home'
    ],
    'price': [
        299, 1799, 499, 349, 699,
        399, 1099, 549, 1299,
        399, 2999, 899, 1999, 799
    ]
})

# ---------------------------
# Step 2: ML-Based Gift Category Prediction
# ---------------------------

def ml_predict_category(personality, budget):
    model = joblib.load('gift_model.pkl')
    enc_pers = joblib.load('personality_encoder.pkl')
    enc_cat = joblib.load('category_encoder.pkl')

    if personality not in enc_pers.classes_:
        return None

    personality_encoded = enc_pers.transform([personality])[0]
    predicted_cat_encoded = model.predict([[personality_encoded, budget]])[0]
    predicted_category = enc_cat.inverse_transform([predicted_cat_encoded])[0]
    return predicted_category

# ---------------------------
# Step 3: Streamlit Interface (Without Voice Input)
# ---------------------------

import streamlit as st

st.set_page_config(page_title="AI Gift Recommender", layout="centered")
st.title("🎁 AI + ML Gift Recommender")
st.write("Find the perfect gift using personality and budget.")

st.subheader("Enter Personality Type")
personality_input = st.selectbox("Choose Personality Type", options=le_personality.classes_)

budget_input = st.number_input("Enter your budget (INR):", min_value=100, max_value=5000, step=100)

if st.button("🎯 Get Recommendations",key="get_recommendations_btn") and personality_input:
    predicted_category = ml_predict_category(personality_input.lower(), budget_input)
    if predicted_category is None:
        st.warning("Sorry, personality not recognized by model. Try another keyword like 'creative', 'calm', etc.")
    else:
        st.info(f"ML Predicted Category: {predicted_category}")
        matched_gifts = gift_data[(gift_data['category'] == predicted_category) & (gift_data['price'] <= budget_input)]
        if not matched_gifts.empty:
            st.subheader("Recommended Gifts:")
            st.write(matched_gifts)
        else:
            st.warning("No gifts available under this category and budget.")
elif st.button("🎯 Get Recommendations"):
    st.warning("Please enter the personality type first.")

# ---------------------------
# Step 4: Optional Enhancements
# ---------------------------
# - Replace manual dataset with real scraped product data (Flipkart/Amazon APIs)
# - Use embeddings/NLP for broader personality inputs
# - Export recommendations as PDF or send via email
# - Store user preferences for personalized future suggestions
