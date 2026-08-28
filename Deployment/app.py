import streamlit as st
import pickle

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Online Course Recommendation System",
    page_icon="🎓",
    layout="centered"
)

# -----------------------------
# Load Files
# -----------------------------
course_df = pickle.load(open("course_df.pkl", "rb"))
cosine_sim = pickle.load(open("cosine_sim.pkl", "rb"))
course_indices = pickle.load(open("course_indices.pkl", "rb"))

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📌 Project Information")

st.sidebar.write("""
### Recommendation Technique
- Content-Based Filtering
- TF-IDF Vectorization
- Cosine Similarity

### Dataset
- 100,000 Records
- 20 Unique Courses
""")

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend_courses(course_name):

    idx = course_indices[course_name]

    similarity_scores = list(enumerate(cosine_sim[idx]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[1:6]

    course_indexes = [i[0] for i in similarity_scores]

    return course_df['course_name'].iloc[course_indexes]

# -----------------------------
# Title
# -----------------------------
st.title("🎓 Online Course Recommendation System")

st.write("""
Select a course from the dropdown below.

This system recommends similar online courses based on:

• Course Name

• Instructor

• Difficulty Level

using TF-IDF Vectorization and Cosine Similarity.
""")

# -----------------------------
# Dropdown
# -----------------------------
selected_course = st.selectbox(
    "Select a Course",
    sorted(course_df["course_name"].unique())
)

# -----------------------------
# Recommendation Button
# -----------------------------
if st.button("Recommend Courses"):

    recommendations = recommend_courses(selected_course)

    st.success(f"Top {len(recommendations)} Recommended Courses")

    for i, course in enumerate(recommendations, start=1):
        st.write(f"{i}. {course}")

st.markdown("---")
st.caption("Developed by Harsha Vardhan | Data Science Project")