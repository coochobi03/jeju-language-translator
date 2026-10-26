
import streamlit as st

st.set_page_config(
    page_title="말ᄒᆞ당 - 제주어 번역기",
    page_icon="🌊"
)

st.title("🌊 말ᄒᆞ당")
st.subheader("내 말을 제주어로!")

st.write(
    "표준어로 하고 싶은 말을 입력해 보세요. "
    "제주어로 바꾸는 번역기를 준비하고 있어요."
)

text = st.text_area(
    "번역할 문장",
    placeholder="예: 오늘 날씨가 좋아서 바다에 가고 싶어."
)

if st.button("제주어로 바꾸기"):
    if text.strip():
        st.info("입력 성공! 다음 단계에서 제주어 번역 모델을 연결할 거예요.")
        st.write("입력한 문장:", text)
    else:
        st.warning("먼저 문장을 입력해 주세요.")

st.caption("제주어를 기록하고 배우며, 일상에서 사용하는 것을 돕는 프로젝트")
