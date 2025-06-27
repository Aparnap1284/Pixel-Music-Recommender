import streamlit as st
from streamlit.components.v1 import html

def theme_toggle():
    html("""
      <div class="theme-toggle">
        <button onclick="toggleTheme()">🌓 THEME</button>
      </div>
      <script>
        const saved = localStorage.getItem('theme') || 'dark';
        document.documentElement.setAttribute('data-theme', saved);
        function toggleTheme() {
          const now = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
          document.documentElement.setAttribute('data-theme', now);
          localStorage.setItem('theme', now);
        }
      </script>
    """, height=60)
