import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Jothiroopa D | Data Analyst", page_icon="📊", layout="wide")

# Hide Streamlit's own header/footer/padding so only the portfolio shows
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

BASE = Path(__file__).parent


def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


html = (BASE / "index.html").read_text(encoding="utf-8")
css = (BASE / "style.css").read_text(encoding="utf-8")
js = (BASE / "script.js").read_text(encoding="utf-8")

# Inline CSS and JS (the page runs inside an iframe, so relative files won't load)
html = html.replace('<link rel="stylesheet" href="style.css" />', f"<style>{css}</style>")
html = html.replace('<script src="script.js"></script>', f"<script>{js}</script>")

# Inline the photo and resume so they work inside the iframe
photo = BASE / "images" / "profile.jpg"
if photo.exists():
    html = html.replace("images/profile.jpg", "data:image/jpeg;base64," + b64(photo))

resume = BASE / "Resume_jothiroopad.pdf"
if resume.exists():
    html = html.replace(
        'href="Resume_jothiroopad.pdf"',
        'href="data:application/pdf;base64,' + b64(resume) + '"',
    )

components.html(html, height=950, scrolling=True)
