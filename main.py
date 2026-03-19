import streamlit as st

st.set_page_config(page_title="Mukund Kumar | ML Portfolio", layout="wide")

# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp{
background:#0f172a;
color:#f8fafc;
font-family:Inter,sans-serif;
}

.block-container{
max-width:1100px;
padding-top:40px;
}

/* NAVBAR */

.navbar{
display:flex;
justify-content:space-between;
align-items:center;
padding:14px 0;
border-bottom:1px solid #334155;
margin-bottom:40px;
}

.nav-title{
font-size:20px;
font-weight:600;
}

.nav-menu{
color:#94a3b8;
font-size:14px;
}

/* HERO */

.hero{
padding:20px 0 40px 0;
}

.hero-title{
font-size:46px;
font-weight:700;
margin-bottom:10px;
}

.hero-sub{
font-size:18px;
color:#94a3b8;
margin-bottom:24px;
max-width:600px;
}

/* BUTTON */

.button{
background:#3b82f6;
color:white !important;
padding:10px 18px;
border-radius:6px;
text-decoration:none !important;
margin-right:10px;
font-size:14px;
}

.button:hover{
background:#22d3ee;
color:#0f172a !important;
}

/* METRICS */

.metric-card{
background:#1e293b;
border:1px solid #334155;
border-radius:8px;
padding:18px;
text-align:center;
}

.metric-number{
font-size:28px;
font-weight:600;
}

.metric-label{
font-size:13px;
color:#94a3b8;
}

/* PROJECTS */

.project-grid{
margin-top:30px;
}

.project-card{
background:#1e293b;
border:1px solid #334155;
border-radius:8px;
padding:18px;
margin-bottom:20px;
}

.project-title{
font-size:18px;
font-weight:600;
margin-bottom:6px;
}

.project-category{
font-size:13px;
color:#94a3b8;
margin-bottom:10px;
}

.project-desc{
font-size:14px;
margin-bottom:12px;
}

.tech{
display:inline-block;
background:#334155;
padding:4px 8px;
border-radius:4px;
font-size:12px;
margin:2px;
}

.accuracy{
color:#10b981;
font-weight:600;
}

/* CONTACT */

.contact-box{
background:#1e293b;
border:1px solid #334155;
padding:16px;
border-radius:8px;
text-align:center;
}

.contact-box a{
color:#3b82f6;
text-decoration:none;
}

/* FOOTER */

.footer{
margin-top:50px;
border-top:1px solid #334155;
padding-top:20px;
text-align:center;
font-size:14px;
color:#94a3b8;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PROJECT DATA
# --------------------------------------------------
projects = [
    {
        "title": "Personality Type Predictor",
        "icon": "🧠",
        "category": "Machine Learning",
        "description": "Predicts personality type using behavioral attributes.",
        "algorithm": "Logistic Regression",
        "dataset": "Behavior Dataset",
        "problem": "Classification",
        "accuracy": "87%",
        "tech": ["Python", "Scikit-learn", "Pandas", "Streamlit"],
        "deploy": "Streamlit",
        "demo": "https://itsmukundkumar-personality-predictor-app-f750g6.streamlit.app/",
        "code": "https://github.com/ItsMukundKumar/personality-predictor",
    },
    {
        "title": "Review Sentiment Predictor",
        "icon": "💬",
        "category": "NLP",
        "description": "Predicts sentiment from product reviews.",
        "algorithm": "Naive Bayes",
        "dataset": "Amazon Reviews",
        "problem": "Sentiment Analysis",
        "accuracy": "89%",
        "tech": ["Python", "NLP", "Scikit-learn", "Streamlit"],
        "deploy": "Streamlit",
        "demo": "https://itsmukundkumar-amazon-review-sentiment-app-zwvhe2.streamlit.app/",
        "code": "https://github.com/ItsMukundKumar/amazon-review-sentiment",
    },
    {
        "title": "Email Spam Predictor",
        "icon": "📧",
        "category": "NLP",
        "description": "Detects spam emails using NLP techniques.",
        "algorithm": "Naive Bayes",
        "dataset": "Email Dataset",
        "problem": "Text Classification",
        "accuracy": "95%",
        "tech": ["Python", "NLP", "Scikit-learn", "Streamlit"],
        "deploy": "Streamlit",
        "demo": "https://2xh22dza5wuhlkenaxgs2o.streamlit.app/",
        "code": "https://github.com/ItsMukundKumar/Spam-Email-Prediction-",
    },
    {
        "title": "Heart Disease Predictor",
        "icon": "❤️",
        "category": "Healthcare",
        "description": "Predicts heart disease risk using medical attributes.",
        "algorithm": "KNN",
        "dataset": "Healthcare Dataset",
        "problem": "Classification",
        "accuracy": "86%",
        "tech": ["Python", "KNN", "Pandas", "Streamlit"],
        "deploy": "Streamlit",
        "demo": "https://heart-disease-predictor-bkwqb76thesgxdhmtyo5m9.streamlit.app/",
        "code": "https://github.com/ItsMukundKumar/Heart-Disease-Predictor",
    },
    {
        "title": "Academic Performance Predictor",
        "icon": "🎓",
        "category": "Education",
        "description": "Predicts GPA using study habits and attendance.",
        "algorithm": "KNN Regression",
        "dataset": "Student Dataset",
        "problem": "Regression",
        "accuracy": "91%",
        "tech": ["Python", "Regression", "Pandas", "Streamlit"],
        "deploy": "Streamlit",
        "demo": "https://itsmukundkumar-academic-performance-predictor-main-xknn83.streamlit.app/",
        "code": "https://github.com/ItsMukundKumar/Academic-Performance-Predictor",
    },
    {
        "title": "Loan Approval Predictor",
        "icon": "💰",
        "category": "Finance",
        "description": "Predicts loan approval using financial attributes.",
        "algorithm": "Naive Bayes",
        "dataset": "Loan Dataset",
        "problem": "Classification",
        "accuracy": "88%",
        "tech": ["Python", "ML", "Pandas", "Streamlit"],
        "deploy": "Streamlit",
        "demo": "https://itsmukundkumar-loan-approval-prediction-app-znbfex.streamlit.app/",
        "code": "https://github.com/ItsMukundKumar/Loan-Approval-Prediction",
    },
    {
        "title": "Disease Risk Predictor",
        "icon": "🩺",
        "category": "Healthcare",
        "description": "Predicts disease risk using lifestyle and health metrics.",
        "algorithm": "Decision Tree",
        "dataset": "Health Lifestyle Dataset",
        "problem": "Classification",
        "accuracy": "85%",
        "tech": ["Python", "Decision Tree", "Scikit-learn", "Streamlit"],
        "deploy": "Streamlit",
        "demo": "https://itsmukundkumar-disease-risk-predictor-main-ssjkjh.streamlit.app/",
        "code": "https://github.com/ItsMukundKumar/disease-risk-predictor",
    },
    {
        "title": "Drug Classification Predictor",
        "icon": "💊",
        "category": "Healthcare",
        "description": "Predicts the most suitable drug for a patient.",
        "algorithm": "Decision Tree",
        "dataset": "Drug Dataset",
        "problem": "Classification",
        "accuracy": "91%",
        "tech": ["Python", "Decision Tree", "Scikit-learn", "Streamlit"],
        "deploy": "Streamlit",
        "demo": "https://itsmukundkumar-drug-classification-predictor-main-lr6e9a.streamlit.app/",
        "code": "https://github.com/ItsMukundKumar/Drug-Classification-Predictor",
    },
    {
        "title": "Old Car Price Predictor",
        "icon": "🚗",
        "category": "Machine Learning",
        "description": "Predicts used car resale price.",
        "algorithm": "Decision Tree Regressor",
        "dataset": "Car Dataset",
        "problem": "Regression",
        "accuracy": "81%",
        "tech": ["Python", "Scikit-learn", "Pandas", "Streamlit"],
        "deploy": "Streamlit",
        "demo": "https://itsmukundkumar-old-car-price-predictor-main-vb4yzk.streamlit.app/",
        "code": "https://github.com/ItsMukundKumar/Old-Car-Price-Predictor",
    },
    {
        "title": "USA Housing Price Predictor",
        "icon": "🏠",
        "category": "Machine Learning",
        "description": "Predicts house prices using regression.",
        "algorithm": "Decision Tree Regressor",
        "dataset": "USA Housing Dataset",
        "problem": "Regression",
        "accuracy": "79%",
        "tech": ["Python", "Scikit-learn", "Pandas", "Streamlit"],
        "deploy": "Streamlit",
        "demo": "https://itsmukundkumar-usa-house-price-predictor-main-x8ifkz.streamlit.app/",
        "code": "https://github.com/ItsMukundKumar/USA-House-Price-Predictor",
    },
    {
    "title": "Food Delivery Time Predictor",
    "icon": "🚚",
    "category": "Machine Learning",
    "description": "Predicts food delivery time using distance, weather, traffic, time of day, vehicle type, preparation time, and courier experience.",
    "algorithm": "Random Forest Regressor",
    "dataset": "Food Delivery Dataset",
    "problem": "Regression",
    "accuracy": "R² Score: 0.779",
    "tech": ["Python", "Scikit-learn", "Pandas", "Streamlit"],
    "deploy": "Streamlit",
    "demo": "https://itsmukundkumar-food-delivery-times-main-vvhy8p.streamlit.app/",
    "code": "https://github.com/ItsMukundKumar/Food-Delivery-Times",
},
{
    "title": "Student Exam Score Predictor",
    "icon": "📊",
    "category": "Machine Learning",
    "description": "Predicts student exam scores using study hours, attendance, sleep habits, and learning methods.",
    "algorithm": "XGBoost Regressor",
    "dataset": "Student Performance Dataset",
    "problem": "Regression",
    "accuracy": "R² Score: 0.73",
    "tech": ["Python", "XGBoost", "Scikit-learn", "Pandas", "Streamlit"],
    "deploy": "Streamlit",
    "demo": "https://itsmukundkumar-student-exam-score-prediction-main-p1uvwi.streamlit.app/",
    "code": "https://github.com/ItsMukundKumar/Student-Exam-Score-Prediction",
},
{
    "title": "Movie Recommendation System",
    "icon": "🎬",
    "category": "NLP",
    "description": "Recommends similar movies using content-based filtering with TF-IDF and cosine similarity.",
    "algorithm": "TF-IDF + Cosine Similarity",
    "dataset": "TMDB Movies Dataset",
    "problem": "Recommendation System",
    "accuracy": "Content-based similarity (Top-10 recommendations)",
    "tech": ["Python", "NLP", "Scikit-learn", "Pandas", "Streamlit"],
    "deploy": "Streamlit",
    "demo": "https://itsmukundkumar-movie-recommendation-system-main-iegscs.streamlit.app/",
    "code": "https://github.com/ItsMukundKumar/Movie-Recommendation-System",
}
]

# --------------------------------------------------
# METRICS
# --------------------------------------------------

num_projects=len(projects)
algorithms=len(set(p["algorithm"] for p in projects))
deployed=len(projects)

# --------------------------------------------------
# NAVBAR
# --------------------------------------------------

st.markdown("""
<div class="navbar">
<div class="nav-title">Mukund Kumar</div>
<div class="nav-menu">Machine Learning Portfolio</div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown("""
<div class="hero">

<div class="hero-title">
Machine Learning Developer
</div>

<div class="hero-sub">
Building predictive applications and data-driven solutions using Python and modern machine learning tools.
</div>

<a class="button" href="https://github.com/ItsMukundKumar/">View Projects</a>
<a class="button" href="https://github.com/ItsMukundKumar/ML-Masterpiece">GitHub</a>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# METRICS
# --------------------------------------------------

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown(f"""
<div class="metric-card">
<div class="metric-number">{num_projects}</div>
<div class="metric-label">Projects</div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown(f"""
<div class="metric-card">
<div class="metric-number">{algorithms}</div>
<div class="metric-label">Algorithms</div>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""
<div class="metric-card">
<div class="metric-number">{deployed}</div>
<div class="metric-label">Deployed Apps</div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PROJECTS
# --------------------------------------------------

st.markdown("## Projects")

cols = st.columns(2)

for i,p in enumerate(projects):

    tech="".join([f"<span class='tech'>{t}</span>" for t in p["tech"]])

    with cols[i%2]:

        st.markdown(f"""
<div class="project-card">

<div class="project-title">{p["title"]}</div>
<div class="project-category">{p["category"]}</div>

<div class="project-desc">{p["description"]}</div>

Algorithm: {p["algorithm"]}<br>
Accuracy: <span class="accuracy">{p["accuracy"]}</span>

<br><br>

{tech}

<br><br>

<a class="button" href="{p["demo"]}">Live Demo</a>
<a class="button" href="{p["code"]}">GitHub</a>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# CONTACT
# --------------------------------------------------

st.markdown("## Contact")

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
<div class="contact-box">
<a href="https://github.com/ItsMukundKumar">GitHub</a>
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="contact-box">
<a href="https://www.linkedin.com/in/mukund-kumar-shah/">LinkedIn</a>
</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="contact-box">
<a href="mailto:youremail@gmail.com">Email</a>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
© 2026 Mukund Kumar — Machine Learning Developer
</div>
""", unsafe_allow_html=True)