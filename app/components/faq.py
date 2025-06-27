import streamlit as st

def show_faq():
    st.markdown("""
      <div class="section pixel-card">
        <h2 class="block-title">❓ FREQUENTLY ASKED QUESTIONS</h2>
    """, unsafe_allow_html=True)

    faqs = [
      ("How does it work?", "We use transformer models to match your caption & genre with emotional song metadata—analyzing vibe via AI."),
      ("Can I choose genre?", "Yes! Choose from 15+ genres (Lo‑Fi to Synthwave), and the AI gives playlist accordingly."),
      ("Is the data real?", "Absolutely! We’ve curated 10,000+ songs with verified mood tags. Updated weekly."),
      ("Is my data secure?", "100% private: caption data is processed on‑the‑fly and never stored. End‑to‑end encryption at all times."),
      ("Can I suggest features?", "Of course! Use the Contact page or tweet '@PixelVibeTrack' with #FeatureRequest.")
    ]
    for q, a in faqs:
        with st.expander(f"🎵 {q}", expanded=False):
            st.write(a)

    st.markdown("</div>", unsafe_allow_html=True)
