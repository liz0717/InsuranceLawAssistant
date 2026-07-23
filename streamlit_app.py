import streamlit as st
from modules.law_parser import split_articles
from modules.pdf_reader import extract_text_from_pdf

st.set_page_config(
    page_title="Insurance Law Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Insurance Law Assistant")

st.markdown("---")

st.subheader("法規版本比較")

old_pdf = st.file_uploader(
    "請上傳舊版法規",
    type="pdf"
)

new_pdf = st.file_uploader(
    "請上傳新版法規",
    type="pdf"
)

if old_pdf:

    st.success("舊版 PDF 上傳成功")

    old_text = extract_text_from_pdf(old_pdf)

    st.subheader("舊版法規內容")

    articles = split_articles(old_text)

    for article in articles:

        st.markdown("---")

        st.subheader(article.title)

        st.text(article.content)

if new_pdf:

    st.success("新版 PDF 上傳成功")

    new_text = extract_text_from_pdf(new_pdf)

    st.subheader("新版法規內容")

    articles = split_articles(new_text)

    for article in articles:

        st.markdown("---")

        st.subheader(article.title)

        st.text(article.content)
