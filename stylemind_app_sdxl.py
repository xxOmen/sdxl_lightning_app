import streamlit as st
import pandas as pd
import random

# Page config
st.set_page_config(page_title="StyleMind AI – Outfit Prompt Generator", layout="wide")
st.title("📝 StyleMind AI – Outfit Prompt Generator")
st.write("Create unique, AI-powered fashion prompts with personalized suggestions and real-time inspiration.")

# Sample user profile data (for simplicity in this example)
user_data = {
    "username": ["user1", "user2"],
    "style": ["Casual", "Formal"],
    "favorite_colors": ["Blue", "Black"],
    "body_type": ["Athletic", "Slim"]
}

# User Profile
user_df = pd.DataFrame(user_data)
user_profile = st.sidebar.selectbox("Select Your Fashion Profile", user_df['style'].unique())

# User Input Form
with st.form("prompt_form"):
    occasion = st.selectbox("What is the occasion?", [
        "Date Night", "Office Meeting", "Beach Day", "Wedding Guest", "Casual Outing", "Travel", "Party", "Brunch"])
    
    gender = st.selectbox("Gender", ["Male", "Female", "Unisex"])
    
    season = st.selectbox("Season", ["Summer", "Winter", "Spring", "Autumn"])
    
    style = st.selectbox("Style Type", ["Casual", "Formal", "Streetwear", "Business Casual", "Beachwear", "Smart Casual"])
    
    reference = st.selectbox("Fashion Inspiration Reference:", ["None", "Pinterest", "Met Gala", "Instagram Influencers"])
    
    custom = st.text_area("Custom Notes (optional)", placeholder="e.g. Include an oversized blazer or earthy tones")
    
    submit_button = st.form_submit_button("Generate Outfit Prompt")

# Generate Outfit Prompt
if submit_button:
    prompt = f"A styled {gender.lower()} outfit for a {occasion.lower()} in the {season.lower()} season. "
    prompt += f"The style is {style.lower()}, reflecting seasonal trends and harmonizing colors."

    if reference != "None":
        prompt += f"\nVisual inspiration comes from {reference.lower()}."

    if custom.strip():
        prompt += f"\nCustom notes: {custom.strip()}"

    st.write("### Fashion Prompt")
    st.code(prompt, language="text")

    # Add AI-Generated Outfit Image Preview (mocked)
    outfit_image = f"generated_outfit_images/{random.randint(1, 10)}.jpg"
    st.image(outfit_image, caption="Generated Outfit Example")

    # Shopping Links
    st.write("You can purchase similar outfits from the following stores:")
    st.markdown("[Shop ASOS](https://www.asos.com) | [Shop Zara](https://www.zara.com) | [Shop Amazon](https://www.amazon.com)")

    # Real-Time Fashion Inspiration Feed
    st.write("### Fashion Inspiration")
    st.write("Check out the latest trends from Instagram, Pinterest, and more!")

    # Fashion Challenges
    st.write("### Fashion Challenges")
    st.write("Submit your outfit for the Weekly Fashion Challenge!")

    # Social Sharing
    st.write("### Share Your Outfit")
    st.write("Share your outfit with your friends on social media!")
    
    if st.button('Share on Instagram'):
        st.write("Outfit shared on Instagram!")
