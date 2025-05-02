import streamlit as st

st.set_page_config(page_title="StyleMind Prompt Generator", layout="wide")
st.title("📝 StyleMind AI – Outfit Prompt Generator")
st.write("Generate rich, styled fashion prompts for use in AI tools like DALL·E, Midjourney, or for design moodboards.")

# --- User Input Form ---
with st.form("prompt_form"):
    occasion = st.selectbox("What is the occasion?", [
        "Date Night", "Office Meeting", "Beach Day", "Wedding Guest", "Travel", "Casual Outing", "Party", "Brunch"],
        help="Select the occasion for which the outfit is being generated.")
    
    gender = st.selectbox("Gender", ["Male", "Female", "Unisex"], help="Choose the gender for the outfit.")
    
    season = st.selectbox("Season", ["Summer", "Winter", "Spring", "Autumn"], help="Choose the season to match the outfit.")
    
    style = st.selectbox("Style Type", [
        "Casual", "Formal", "Streetwear", "Business Casual", "Beachwear", "Smart Casual"], 
        help="Select the style type of the outfit.")
    
    reference = st.selectbox("Fashion Inspiration Reference:", [
        "None", "Outfits from Euphoria characters", "Timothée Chalamet street style", "Gigi Hadid off-duty looks", 
        "Old Money aesthetic from TikTok", "Pinterest flat lays", "Zara catalog 2024", "Uniqlo minimalist ads", 
        "Instagram fashion influencers", "Emily in Paris aesthetic", "Met Gala celebrity themes"],
        help="Select a fashion inspiration reference, if any.")
    
    custom = st.text_area("Custom Notes (optional)", placeholder="e.g. include an oversized blazer or earthy tones",
                          help="Add any specific styling preferences here.")
    
    submitted = st.form_submit_button("Generate Outfit Prompt")

# --- Processing Form Submission ---
if submitted:
    if not (occasion and gender and season and style):  # Simple validation
        st.warning("Please make sure all fields are selected.")
    else:
        prompt = (
            f"A styled fashion concept featuring a {gender.lower()} outfit designed for a {occasion.lower()} during the {season.lower()} season. "
            f"The fashion aesthetic is {style.lower()}, aligned with seasonal trends and color harmony.\n\n"

            f"Scene 1: A Pinterest-style flat lay arranged on a soft beige or light gray background. Include a cohesive set of fashion items such as topwear, bottomwear, footwear, and 2–3 accessories. "
            f"Do not specify brand names or colors; allow for creative interpretation. Layout should be neat and visually appealing with soft directional lighting and natural shadows.\n\n"

            f"Scene 2: A mannequin fully dressed in the **exact same outfit shown in Scene 1**, including all topwear, bottomwear, footwear, and accessories. Ensure the outfit on the mannequin perfectly matches the flat lay in color, material, and style. The mannequin should be posed in a minimalist studio setting with neutral lighting. Emphasize the textures, folds, and flow of different fabrics, with attention to stitching and silhouette. Present the look in a polished, editorial fashion style." 
        )

        if reference != "None":
            prompt += f"\n\nVisual inspiration is drawn from {reference.lower()}, known for its influence on fashion culture and contemporary styling."

        if custom.strip():
            prompt += f"\n\nAdditional styling notes: {custom.strip()}"

        st.success("Here is your outfit prompt:")
        st.markdown("### Fashion Prompt")
        st.code(prompt, language="text")
