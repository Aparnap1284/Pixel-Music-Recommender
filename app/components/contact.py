import streamlit as st

def show_contact():
    st.markdown("""
    <div class="section pixel-card">
      <h2 class="block-title">📬 CONTACT</h2>
      <p>If you'd like to connect or share feedback:</p>
      <ul>
        <li>👩‍💻 <strong>Aparna Patel</strong></li>
        <li>🔗 <a href='https://www.linkedin.com/in/aparna-patel-69b0b7308/' target='_blank'>LinkedIn</a></li>
        <li>💻 <a href='https://github.com/Aparnap1284/pixel-vision' target='_blank'>GitHub</a></li>
        <li>📧 Email: (available on request)</li>
      </ul>
      <p style='font-size:0.9rem;'>We’d 💜 to hear from you!</p>
    </div>
    """, unsafe_allow_html=True)
