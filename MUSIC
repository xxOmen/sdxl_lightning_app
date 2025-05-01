# Streamlit App – Multi-Style Music Prompt Generator

import streamlit as st

st.set_page_config(page_title="Music Prompt Generator", layout="centered")
st.title("🎵 AI Music Prompt Generator")
st.write("Generate prompts for music AI tools like Suno, Udio, MusicLM, or custom lyric/song projects.")

# --- User Input Form ---
with st.form("music_form"):
    genre = st.selectbox("Select a genre:", [
        "Lo-fi", "Hip-Hop", "Ambient", "Pop", "Rock", "Electronic", "Classical", "Jazz", "Folk", "Trap", "Chillwave", "Synthwave"
    ])
    mood = st.selectbox("Select a mood:", [
        "Chill", "Energetic", "Melancholic", "Romantic", "Epic", "Dark", "Uplifting", "Dreamy", "Nostalgic", "Aggressive"
    ])
    use_case = st.selectbox("What's it for?", [
        "Background music for a video", "Vocal track with lyrics", "Instrumental beat for production",
        "Podcast intro/outro", "Game soundtrack", "Meditation music"
    ])
    vocal = st.selectbox("Vocal style (if needed):", [
        "None (instrumental only)", "Male vocal", "Female vocal", "Vocal duet", "Synth voice", "Rap vocals"
    ])
    custom_notes = st.text_area("Any specific themes, instruments, or references?", placeholder="e.g. flute intro, inspired by Billie Eilish")
    submitted = st.form_submit_button("Generate Music Prompt")

if submitted:
    prompt = f"{mood} {genre} music designed for {use_case.lower()}."

    if vocal != "None (instrumental only)":
        prompt += f" Features {vocal.lower()} with expressive delivery."

    prompt += " Includes stylistic elements that fit the scene or emotional tone."

    if custom_notes.strip():
        prompt += f" Additional notes: {custom_notes.strip()}"

    st.success("Your music prompt:")
    st.code(prompt, language="text")
