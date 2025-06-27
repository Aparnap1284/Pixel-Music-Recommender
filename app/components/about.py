import streamlit as st

def show_about():
    st.markdown("""
    <div class="section pixel-card">
      <h2 class="block-title">📚 ABOUT VIBETRACK AI</h2>
      <p style="text-align:justify; font-family: var(--font-pixel);">
        Pixel VibeTrack is your personal AI-DJ — merging pixel art vibes with machine learning magic. Tell us about your video, and we’ll drop the perfect soundtrack 🎧
      </p>
      <h3>🎮 HARMONY OF CODE + ART</h3>
      <ul>
        <li>🧠 Smart recommendations via transformer models</li>
        <li>🎨 Retro pixel animations & neon themes</li>
        <li>💡 Built for creators, students, reel lovers—and you!</li>
      </ul>
      <h3>🛣️ ROADMAP</h3>
      <ul>
        <li>✅ Now: Mood + genre-based playlists</li>
        <li>🚀 Soon: Spotify API, User Auth, Live suggestions</li>
        <li>✨ Future: Pixel dashboard, auto thumbnails & stats</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)
