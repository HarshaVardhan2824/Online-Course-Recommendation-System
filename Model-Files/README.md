# Model Files

This folder contains the serialized objects required by the Streamlit application.

## Files

### `course_df.pkl`
Processed course-level data used by the recommendation system.

### `cosine_sim.pkl`
Cosine similarity matrix used to identify similar courses.

### `course_indices.pkl`
Mapping between course names and their index positions.

These files allow the deployed application to load the processed data and similarity information without rebuilding the recommendation models every time.
