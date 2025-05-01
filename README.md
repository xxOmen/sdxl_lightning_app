# StyleMind AI – Outfit Generator (SDXL-Lightning)

This Streamlit app uses Hugging Face's **ByteDance/SDXL-Lightning** model to generate stylish outfit visuals based on user input.

## Features
- Select outfit preferences: occasion, gender, season, and style
- Generates AI outfit images using Hugging Face's SDXL-Lightning model

## Setup Instructions

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Add your Hugging Face API key in `.streamlit/secrets.toml`:
```toml
HF_API_KEY = "your_huggingface_api_key_here"
```

3. Run the app:
```bash
streamlit run stylemind_app_sdxl.py
```

## Model Used
- [ByteDance/SDXL-Lightning](https://huggingface.co/ByteDance/SDXL-Lightning)