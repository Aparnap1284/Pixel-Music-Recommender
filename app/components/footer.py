import streamlit as st

def show_footer():
    st.markdown("""
      <div class="footer">
        <p>🎨 Designed with pixels & AI by <strong>Aparna Patel</strong></p>
        <p>
          <a href='https://www.linkedin.com/in/aparna-patel-69b0b7308/' target='_blank'>🔗 LinkedIn</a> |
          <a href='https://github.com/Aparnap1284/pixel-vision' target='_blank'>💻 GitHub</a>
        </p>
        <p>© 2025 Pixel VibeTrack AI. All rights reserved.</p>
      </div>
    """, unsafe_allow_html=True)
