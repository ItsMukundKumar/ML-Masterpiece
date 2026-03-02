import streamlit as st

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="ML Model Portfolio",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Machine Learning Project Portfolio")
st.write("A curated collection of my deployed Machine Learning and NLP applications.")
st.divider()


# --------------------------------------------------
# Reusable Model Card
# --------------------------------------------------
def model_card(model_name, description, app_link, tags):
    with st.container(border=True):
        st.subheader(model_name)

        tag_cols = st.columns(len(tags))
        for col, tag in zip(tag_cols, tags):
            col.caption(tag)

        st.write(description)
        st.link_button("🚀 Open App", app_link)


# --------------------------------------------------
# Portfolio Grid
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    model_card(
        "Personality Type Predictor",
        "Predicts personality type (Introvert, Extrovert, Ambivert) using behavioral "
        "and lifestyle attributes with Logistic Regression.",
        "https://itsmukundkumar-personality-predictor-app-f750g6.streamlit.app/",
        ["ML", "Classification", "Logistic Regression"],
    )

with col2:
    model_card(
        "Review Sentiment Predictor",
        "Analyzes product reviews and predicts sentiment (Positive / Negative) "
        "using Natural Language Processing and Machine Learning.",
        "https://itsmukundkumar-amazon-review-sentiment-app-zwvhe2.streamlit.app/",
        ["NLP", "Sentiment Analysis", "ML"],
    )

col3, col4 = st.columns(2)

with col3:
    model_card(
        "Email Spam Predictor",
        "Detects spam emails using NLP techniques and a Naive Bayes classifier "
        "with a Streamlit web interface.",
        "https://2xh22dza5wuhlkenaxgs2o.streamlit.app/",
        ["NLP", "Naive Bayes", "Text Classification"],
    )

with col4:
    model_card(
        "Heart Disease Predictor",
        "Predicts the likelihood of heart disease based on medical input features "
        "using KNN and StandardScaler preprocessing.",
        "https://heart-disease-predictor-bkwqb76thesgxdhmtyo5m9.streamlit.app/",
        ["Healthcare", "KNN", "Classification"],
    )

# --------------------------------------------------
# NEW ROW (Academic Performance Predictor)
# --------------------------------------------------
col5, col6 = st.columns(2)

with col5:
    model_card(
        "Academic Performance Predictor",
        "Predicts student GPA based on study habits, attendance, parental support, "
        "and extracurricular activities using KNN Regression.",
        "https://itsmukundkumar-academic-performance-predictor-main-xknn83.streamlit.app/",
        ["Education", "KNN Regression", "StandardScaler"],
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.divider()
st.caption("© 2026 | Built with Streamlit by Mukund Kumar")