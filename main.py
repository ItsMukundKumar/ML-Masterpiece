import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Mukund Kumar | ML Portfolio",
    page_icon="🤖",
    layout="wide",
)

# --------------------------------------------------
# PROJECT DATA (UNCHANGED)
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
        "code": "#",
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
    "description": "Predicts disease risk using lifestyle and health metrics such as BMI, sleep, blood pressure, and cholesterol.",
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
    "description": "Predicts the most suitable drug for a patient based on medical attributes like age, sex, blood pressure, cholesterol, and Na_to_K ratio.",
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
    "description": "Predicts the resale price of a used car based on features such as car name, year, fuel type, transmission, and kilometers driven.",
    "algorithm": "Decision Tree Regressor",
    "dataset": "Car Dataset",
    "problem": "Regression",
    "accuracy": "81%",
    "tech": ["Python", "Scikit-learn", "Pandas", "Streamlit"],
    "deploy": "Streamlit",
    "demo": "https://itsmukundkumar-old-car-price-predictor-main-vb4yzk.streamlit.app/",
    "code": "https://github.com/ItsMukundKumar/Old-Car-Price-Predictor",
    }
]

# --------------------------------------------------
# METRICS
# --------------------------------------------------

num_projects = len(projects)
algorithms = len(set(p["algorithm"] for p in projects))
deployed = len(projects)

# --------------------------------------------------
# GLOBAL CSS
# --------------------------------------------------

st.markdown(
"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

html, body, [class*="css"]  {
font-family: 'Inter', sans-serif;
}

.stApp{
background: linear-gradient(135deg,#020617,#0f172a,#1e293b);
color:white;
}

/* HERO */

.hero{
text-align:center;
padding-top:40px;
padding-bottom:20px;
}

.hero-title{
font-size:52px;
font-weight:800;
background: linear-gradient(90deg,#6366f1,#22d3ee);
-webkit-background-clip:text;
color:transparent;
}

.hero-sub{
color:#94a3b8;
font-size:20px;
}

/* METRICS */

.metric-box{
background: rgba(255,255,255,0.05);
padding:25px;
border-radius:16px;
text-align:center;
border:1px solid rgba(255,255,255,0.1);
}

/* PROJECT CARDS */

.card{
background: rgba(255,255,255,0.05);
border-radius:18px;
padding:22px;
border:1px solid rgba(255,255,255,0.1);
margin-bottom:20px;
transition:0.25s;
backdrop-filter:blur(8px);
}

.card:hover{
transform:translateY(-6px);
border:1px solid #6366f1;
}

/* BADGES */

.badge{
display:inline-block;
padding:5px 10px;
border-radius:12px;
background:#1e293b;
font-size:12px;
margin:3px;
border:1px solid #334155;
}

/* BUTTONS */

.btn{
display:inline-block;
padding:10px 16px;
border-radius:10px;
background:#6366f1;
color:white !important;
text-decoration:none !important;
font-size:14px;
font-weight:600;
}

.btn:hover{
background:#4f46e5;
color:white !important;
text-decoration:none !important;
}

/* SIDEBAR NAVIGATION */

section[data-testid="stSidebar"]{
background: linear-gradient(180deg,#020617,#0f172a);
}

div[role="radiogroup"] > label {
background: rgba(255,255,255,0.04);
padding:12px 14px;
margin-bottom:8px;
border-radius:10px;
border:1px solid rgba(255,255,255,0.08);
transition: all 0.2s ease;
cursor:pointer;
}

div[role="radiogroup"] > label:hover{
background: rgba(99,102,241,0.2);
border:1px solid #6366f1;
}

div[role="radiogroup"] label[data-checked="true"]{
background: linear-gradient(90deg,#6366f1,#22d3ee);
border:1px solid #6366f1;
color:white;
font-weight:600;
}

</style>
""",
unsafe_allow_html=True,
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.markdown("### Menu")

page = st.sidebar.radio(
"",
["🏠 Home", "📊 Projects", "📬 Contact"]
)



# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if page == "🏠 Home":

    st.markdown(
"""
<div class="hero">
<div class="hero-title">Mukund Kumar</div>
<div class="hero-sub">Machine Learning Developer • Data Analyst • Python Developer</div>
</div>
""",
unsafe_allow_html=True
)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
f"""
<div class="metric-box">
<h2>{num_projects}</h2>
Projects
</div>
""",
unsafe_allow_html=True)

    with c2:
        st.markdown(
f"""
<div class="metric-box">
<h2>{algorithms}</h2>
Algorithms
</div>
""",
unsafe_allow_html=True)

    with c3:
        st.markdown(
f"""
<div class="metric-box">
<h2>{deployed}</h2>
Deployed Apps
</div>
""",
unsafe_allow_html=True)

    st.write("")

    st.markdown(
"""
I build machine learning applications that transform **data into meaningful predictions and insights**.

**Focus Areas**

• Machine Learning  
• Data Analysis  
• Predictive Modeling  
• ML Deployment
"""
)

# --------------------------------------------------
# PROJECTS
# --------------------------------------------------

elif page == "📊 Projects":

    st.title("Machine Learning Projects")

    search = st.text_input("Search Projects")

    categories = ["All"] + sorted(set(p["category"] for p in projects))
    category = st.selectbox("Filter by Category", categories)

    filtered = []

    for p in projects:
        if category != "All" and p["category"] != category:
            continue
        if search and search.lower() not in p["title"].lower():
            continue
        filtered.append(p)

    cols = st.columns(2)

    for i, project in enumerate(filtered):

        with cols[i % 2]:

            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.subheader(project["icon"] + " " + project["title"])

            st.write(project["description"])

            st.write("**Algorithm:**", project["algorithm"])
            st.write("**Accuracy:**", project["accuracy"])

            tech_html = "".join(
                [f'<span class="badge">{t}</span>' for t in project["tech"]]
            )

            st.markdown(tech_html, unsafe_allow_html=True)

            with st.expander("Project Details"):
                st.write("Dataset:", project["dataset"])
                st.write("Problem:", project["problem"])
                st.write("Deployment:", project["deploy"])

            st.markdown(
f"""
<a class="btn" href="{project["demo"]}" target="_blank">Live Demo</a>
&nbsp;
<a class="btn" href="{project["code"]}" target="_blank">GitHub</a>
""",
unsafe_allow_html=True
)

            st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# CONTACT
# --------------------------------------------------

elif page == "📬 Contact":

    st.title("Connect")

    st.markdown(
"""
Interested in **machine learning projects**, **data analysis**, or **collaboration opportunities**.

Feel free to reach out.
"""
)

    st.markdown(
"""
<a class="btn" href="https://github.com/ItsMukundKumar" target="_blank">GitHub</a>

<a class="btn" href="https://www.linkedin.com/in/mukund-kumar-shah/" target="_blank">LinkedIn</a>
""",
unsafe_allow_html=True
)