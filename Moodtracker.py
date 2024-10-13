import streamlit as st
import datetime

# Title of the app
st.title("Mood Tracker")

# Initialize session state for mood history if not already done
if 'mood_history' not in st.session_state:
    st.session_state.mood_history = []

# Mood options
mood_options = ["Happy", "Sad", "Neutral", "Angry", "Excited", "Bored"]

# User input for mood
st.subheader("Log Your Mood")
selected_mood = st.selectbox("How do you feel today?", mood_options)
log_mood = st.button("Log Mood")

# Log the mood if button is pressed
if log_mood:
    today = datetime.date.today()
    st.session_state.mood_history.append((today, selected_mood))
    st.success(f"Mood logged: {selected_mood} on {today}")

# Display mood history
st.subheader("Mood History")
if st.session_state.mood_history:
    for entry in st.session_state.mood_history:
        st.write(f"{entry[0]}: {entry[1]}")
else:
    st.write("No mood entries yet.")
