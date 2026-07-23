import streamlit as st

st.set_page_config(
    page_title="Insurance Law Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Insurance Law Assistant")

st.markdown("---")

st.subheader("法規版本比較")

old_pdf = st.file_uploader(
    "請上傳舊版法規 PDF",
    type=["pdf"],
    key="old"
)

new_pdf = st.file_uploader(
    "請上傳新版法規 PDF",
    type=["pdf"],
    key="new"
)

if old_pdf and new_pdf:
    st.success("✅ PDF 已成功上傳！")

    if st.button("開始比較"):
        st.info("🚧 功能開發中...")
