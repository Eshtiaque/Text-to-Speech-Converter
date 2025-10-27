# app.py

import streamlit as st
from gtts import gTTS
import io
import os

# --- Page Configuration and Title (Layout set to WIDE) ---
st.set_page_config(
    page_title="Text-to-Speech Converter",
    layout="wide", # Set to wide layout to maximize screen width
    initial_sidebar_state="collapsed"
)

# --- Settings and Title (Top of the page) ---
st.title("🗣️ Text-to-Speech Converter")
st.markdown("---")

# Create a container for the settings panel aligned to the top right
with st.container():
    # Columns to push the settings to the far right
    col_empty, col_settings = st.columns([4, 1])
    
    with col_settings:
        st.caption("⚙️ Language")
        # Language Selection Options
        lang_options = {
            "English 🇺🇸": "en", 
            "Bengali 🇧🇩": "bn", 
            "Hindi 🇮🇳": "hi", 
            "French 🇫🇷": "fr", 
            "Spanish 🇪🇸": "es",
            "German 🇩🇪": "de",
            "Japanese 🇯🇵": "ja"
        }
        selected_lang_name = st.selectbox(" ", list(lang_options.keys()), key="lang_select", label_visibility="collapsed")
        lang_code = lang_options[selected_lang_name]

st.markdown("---") 

# --- Input and Output Division (Three Equal Columns) ---

# Three equal columns for Text Input, File Upload, and Output
col_text_input, col_file_upload, col_output = st.columns(3) 

# --- 1. TEXT INPUT COLUMN ---
with col_text_input:
    # New Subheader for Input
    st.subheader("📝 Input Text") 
    st.caption("1️⃣ Type Text Directly")
    input_text = st.text_area(
        " ", # Empty label
        height=175, 
        placeholder=f"Type message in {selected_lang_name}...",
        key="direct_input_text",
        label_visibility="collapsed"
    )

# --- 2. FILE UPLOAD COLUMN ---
with col_file_upload:
    # Adding vertical space to align with subheader in col_text_input
    st.markdown("## &nbsp;") 
    st.caption("2️⃣ Upload File")
    uploaded_file = st.file_uploader(" ", type="txt", key="file_uploader", label_visibility="collapsed")
    st.markdown("<br>", unsafe_allow_html=True) 
    
    # Changed st.warning to HTML markdown for grey color
    st.warning('Only .txt files are supported')


# --- Conversion Logic ---
text_to_convert = ""
source_of_text = ""

if uploaded_file is not None:
    try:
        text_to_convert = uploaded_file.read().decode("utf-8")
        source_of_text = "from file upload"
    except Exception as e:
        # Error will be handled below
        pass 
elif input_text:
    text_to_convert = input_text
    source_of_text = "from direct input"


# --- 3. OUTPUT COLUMN (The new placement for the Output subheader) ---
with col_output:
    # New Subheader for Output
    st.subheader("🔊 Audio Output") 
    st.caption("3️⃣ Generation Result")
    output_placeholder = st.empty()
    output_placeholder.info("Click 'Generate Audio' below.")


st.markdown("---")


# --- Main Function: Generate Audio ---
@st.cache_data(show_spinner=False)
def generate_audio(text_content, lang_code):
    audio_bytes_io = io.BytesIO()
    tts = gTTS(text_content, lang=lang_code)
    tts.write_to_fp(audio_bytes_io)
    audio_bytes_io.seek(0)
    return audio_bytes_io

# --- Generate Button (Full Width, below all columns) ---
if st.button("🚀 Generate Audio", type="primary", use_container_width=True):
    # Logic is executed and results are written directly to the output column
    
    # Check if text exists
    if not text_to_convert or len(text_to_convert.strip()) == 0:
        output_placeholder.warning("⚠️ Enter text or upload file.")
    elif len(text_to_convert) > 5000:
        output_placeholder.error("Text is too long! (Max 5000 chars recommended).")
    else:
        # --- Output Generation and Display ---
        with output_placeholder.container(): # Use container to clear placeholder
            with st.spinner(f'⏳ Generating...'):
                try:
                    audio_data = generate_audio(text_to_convert, lang_code)
                    
                    st.success(f"✅ Generated in {selected_lang_name}!")
                    
                    # Playback and Download are shown sequentially in the output column
                    st.audio(audio_data, format="audio/mp3")

                    st.download_button(
                        label="⬇️ Download MP3 File",
                        data=audio_data,
                        file_name=f"TTS_Output_{lang_code}.mp3",
                        mime="audio/mp3",
                        use_container_width=True
                    )
                    st.caption("Note: Uses default high-quality voice by Sajid")

                except Exception as e:
                    st.error(f"❌ Error: {e}")
                    st.caption("Tip: Check text length or unsupported characters.")

# --- End of the app ---