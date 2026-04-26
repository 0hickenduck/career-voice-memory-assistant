import streamlit as st
from db import init_db, save_record, get_records

# Initialize database when the app starts
init_db()

st.title("Career Voice Memory Assistant")

st.write(
    "Record your career events, study notes, and interview practice logs."
)

category = st.selectbox(
    "カテゴリを選んでください",
    ["event", "study", "interview", "other"],
)

text = st.text_area("今日の就活・学習内容を入力してください")

if st.button("保存"):
    if text.strip() == "":
        st.warning("内容を入力してください。")
    else:
        # For now, we use a mock summary.
        # Later, this will be replaced by a real LLM summary.
        summary = f"要約: {text[:50]}..."

        save_record(category, text, summary)
        st.success("保存しました")

st.subheader("過去の記録")

records = get_records()

if not records:
    st.info("まだ記録がありません。")
else:
    for record in records:
        record_id, created_at, category, raw_text, summary = record

        with st.expander(f"{created_at} / {category}"):
            st.write("**Summary**")
            st.write(summary)

            st.write("**Original Text**")
            st.write(raw_text)