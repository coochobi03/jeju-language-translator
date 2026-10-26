
import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

st.set_page_config(
    page_title="말ᄒᆞ당 - 제주어 번역기",
    page_icon="🌊"
)

st.title("🌊 말ᄒᆞ당")
st.subheader("내 말을 제주어로!")

st.write(
    "표준어로 하고 싶은 말을 입력하면 "
    "제주어 번역 결과를 보여 줍니다."
)

@st.cache_resource
def load_model():
    name = "Junhoee/Kobart-Jeju-translation"
    tokenizer = AutoTokenizer.from_pretrained(name)
    model = AutoModelForSeq2SeqLM.from_pretrained(name)
    model.eval()
    return tokenizer, model

text = st.text_area(
    "번역할 문장",
    placeholder="예: 오늘 날씨가 좋아서 바다에 가고 싶어."
)

if st.button("제주어로 바꾸기", type="primary"):
    if not text.strip():
        st.warning("먼저 문장을 입력해 주세요.")
    else:
        try:
            with st.spinner("제주어로 번역하고 있어요..."):
                tokenizer, model = load_model()
                inputs = tokenizer(
                    "[표준] " + text.strip(),
                    return_tensors="pt",
                    truncation=True,
                    max_length=128
                )
                with torch.no_grad():
                    outputs = model.generate(
                        **inputs,
                        max_new_tokens=128,
                        num_beams=4
                    )
                result = tokenizer.decode(
                    outputs[0],
                    skip_special_tokens=True
                )

            st.markdown("### 번역 결과")
            st.success(result)
            st.caption(
                "AI 번역은 실제 제주어 표현과 다를 수 있습니다. "
                "정확한 표현인지 확인해 주세요."
            )
        except Exception:
            st.error(
                "번역 모델을 불러오지 못했어요. "
                "잠시 후 다시 시도하거나 오류 로그를 확인해 주세요."
            )

st.caption("제주어를 기록하고 배우며, 일상에서 사용하는 것을 돕는 프로젝트")
