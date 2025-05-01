import streamlit as st

st.set_page_config(page_title="StyleMind Prompt Generator", layout="centered")
st.title("📝 StyleMind AI – Outfit Prompt Generator")
st.write("Use this tool to generate descriptive outfit prompts for AI image tools.")

# --- User Input Form ---
with st.form("prompt_form"):
    occasion = st.selectbox("What is the occasion?", [
        "Date Night", "Office Meeting", "Beach Day", "Wedding Guest", "Travel", "Casual Outing", "Party", "Brunch"])
    gender = st.selectbox("Gender", ["Male", "Female", "Unisex"])
    season = st.selectbox("Season", ["Summer", "Winter", "Spring", "Autumn"])
    style = st.selectbox("Style Type", [
        "Casual", "Formal", "Streetwear", "Business Casual", "Beachwear", "Smart Casual"])
    submitted = st.form_submit_button("Generate Prompt")

# --- Generate Prompt ---
if submitted:
    prompt = f"A flat lay of a {style.lower()} outfit for a {gender.lower()} attending a {occasion.lower()} in {season.lower()}. Include topwear, bottomwear, shoes, and 1–2 accessories. Display on a clean background in Pinterest-style aesthetic."
    st.success("Here is your generated prompt:")
    st.code(prompt, language="text")
