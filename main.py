import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

#Load dataset
data = pd.read_csv('study_scores.csv')

#train model
x = data[['Hours']]
y = data['Score']
model = LinearRegression()
model.fit(x, y)

# Streamlit UI
st.title('📚 Study Score Predictor AI')
st.write("👋 Welcome! This AI predicts your exam score based on how long you studied.")
st.write("📌 Just enter your study time below 👇 and click Predict!")

hours = st.number_input('Hours_studied:', 0.0, 24.0, step=0.1)

if st.button('Predict'):
    prediction = model.predict([[hours]])
    score = prediction[0]
    
    st.success(f'Predicted score: {prediction[0]:.2f}')

    if score >= 85:
        st.balloons()
        st.write("Great job! You're a study beast.")
    elif score >= 70:
        st.write("🧠 Nice! You're doing well.")
    elif score >= 50:
        st.write("📚 Keep studying — you're getting there!")
    else:
        st.write("😅 Try to study more next time.")

#footer
st.markdown("---")
st.caption("Made with ❤️ by Dafiq Elhaq | Powered by Streamlit + Scikit-learn")

