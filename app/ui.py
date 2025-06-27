import streamlit as st
import os, sys
from PIL import Image
import base64  # Ensure this is at the top of your script

# Add backend path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.recommend_music import MusicRecommendationSystem
from app.components.header import show_header
from app.components.footer import show_footer
from app.components.about import show_about
from app.components.contact import show_contact
from app.components.faq import show_faq
#from app.components.theme_toggle import theme_toggle

# Setup
st.set_page_config(page_title="Pixel VibeTrack 🎮", page_icon="🎧", layout="wide")

# Retro font
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Load CSS
css_path = os.path.join(os.path.dirname(__file__), "styles.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Mood Emoji Map
mood_emojis = {
    "romantic": "❤️", "happy": "😊", "sad": "😢", "energetic": "⚡",
    "chill": "🧘", "angry": "😠", "emotional": "😭", "uplifting": "🌈", "default": "🎵"
}

# Assets dir
ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))

# Navigation
if 'page' not in st.session_state:
    st.session_state.page = "Home"

def show_navigation():
    st.markdown('<div class="nav-horizontal">', unsafe_allow_html=True)
    cols = st.columns(4)
    pages = [("🏠 HOME", "Home"), ("📚 ABOUT", "About"), ("❓ FAQ", "FAQ"), ("📬 CONTACT", "Contact")]
    for i, (label, page) in enumerate(pages):
        if cols[i].button(label, key=f"nav_{page.lower()}"):
            st.session_state.page = page
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    show_header()
    #theme_toggle()
    show_navigation()

    if st.session_state.page == "Home":
        st.markdown('<div class="block-title">🎮 FROM PIXELS TO PLAYLISTS</div>', unsafe_allow_html=True)

        recommender = MusicRecommendationSystem("dataset/reels_dataset.csv")
        if recommender.initialize():
            st.error("❌ Failed to load model.")
            return

        with st.form("recommend_form"):
            st.markdown('<div class="block-title mood">🎙️ DESCRIBE YOUR VIDEO</div>', unsafe_allow_html=True)

            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown("<label class='music-title'>🎬 Your Video Vibe:</label>", unsafe_allow_html=True)
                caption = st.text_area(" ", "A romantic walk under stars 🌌", height=100)

                st.markdown("<label class='music-title'>🎧 Pick a Genre:</label>", unsafe_allow_html=True)
                genre = st.selectbox(" ", recommender.get_unique_genres())

            with col2:
                st.markdown("<h3 class='pixel-heading glitch'>🎭 Mood Preview</h3>", unsafe_allow_html=True)

                mood_gif = os.path.join(ASSETS_DIR, "mood_preview.gif")
                if os.path.exists(mood_gif):
                    st.markdown(f'<img src="data:image/gif;base64,{base64.b64encode(open(mood_gif, "rb").read()).decode()}" class="mood-preview" alt="Mood Preview" />', unsafe_allow_html=True)
                else:
                    st.warning("⚠️ Default mood preview GIF not found.")
                st.caption("🔍 Mood preview always live")

            submit = st.form_submit_button("🔍 Generate Playlist")

        if submit:
            with st.spinner("🧠 Analyzing your vibe..."):
                results, mood = recommender.recommend(caption, genre)
                mood_lower = mood.lower()
                emoji = mood_emojis.get(mood_lower, mood_emojis["default"])

                st.markdown(f'<div class="block-title mood">🎧 Mood Detected: {emoji} {mood.title()}</div>', unsafe_allow_html=True)
                st.markdown('<div class="block-title">🔥 Top Tracks</div>', unsafe_allow_html=True)
                for _, row in results.iterrows():
                    title, genre_tag, mood_tag = row['Title'], row['Genre'], row['Mood']
                    yt_url = row.get('YouTubeLink', f"https://youtube.com/results?search_query={title.replace(' ','+')}")

                    mood_img_path = os.path.join("assets", f"{mood_tag.lower()}.jpg")
                    encoded_img = ""
                    if os.path.exists(mood_img_path):
                        with open(mood_img_path, "rb") as img_file:
                            img_bytes = img_file.read()
                            encoded_img = f"data:image/jpeg;base64,{base64.b64encode(img_bytes).decode()}"

                        # Now display the card with embedded image
                    st.markdown(f"""
                    <div class="music-card">
                    <img src="{encoded_img}" alt="{title}" />
                    <div>
                        <p class="music-title">{title}</p>
                        <p class="track-meta">
                        <span class="genre-tag">{genre_tag}</span>
                        <span class="genre-tag">{mood_tag}</span>
                        </p>
                        <div class="track-actions">
                        <a href="{yt_url}" target="_blank">▶ YouTube</a>
                        </div>
                    </div>
                    </div>
                    """, unsafe_allow_html=True)

    elif st.session_state.page == "About":
        show_about()
    elif st.session_state.page == "FAQ":
        show_faq()
    elif st.session_state.page == "Contact":
        show_contact()

    show_footer()

if __name__ == "__main__":
    main()
