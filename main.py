import streamlit as st

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌟")

# 🧸 제목
st.title("🌈 MBTI로 알아보는 나의 직업 추천")
st.write("당신의 MBTI 유형을 선택하면 어울리는 직업을 추천해드릴게요! 🧑‍🏫💼🧑‍🔬")

# 📋 MBTI 목록
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# ✅ 사용자 선택
user_mbti = st.selectbox("당신의 MBTI를 선택하세요 ✨", mbti_types)

# 💡 MBTI별 직업 추천 사전
mbti_career = {
    "ISTJ": ["🧾 회계사", "🏛️ 공무원", "🛠️ 기술자"],
    "ISFJ": ["👩‍⚕️ 간호사", "🏫 교사", "🧑‍🍳 요리사"],
    "INFJ": ["🧑‍🎨 작가", "🧑‍💼 심리상담가", "📚 교육 컨설턴트"],
    "INTJ": ["👨‍💻 데이터 과학자", "🧠 전략 컨설턴트", "📈 기획자"],
    "ISTP": ["🔧 엔지니어", "🚗 자동차 정비사", "🧗‍♂️ 익스트림 스포츠 선수"],
    "ISFP": ["🎨 디자이너", "🎶 음악가", "🌿 플로리스트"],
    "INFP": ["📖 소설가", "🎭 예술가", "🧑‍🏫 청소년 지도사"],
    "INTP": ["🧪 연구원", "💻 프로그래머", "🧠 AI 엔지니어"],
    "ESTP": ["🎤 방송인", "📢 마케터", "🚓 경찰관"],
    "ESFP": ["🎬 배우", "🎉 이벤트 플래너", "👠 패션 스타일리스트"],
    "ENFP": ["🌍 사회운동가", "🎙️ 아나운서", "🛫 여행 기획자"],
    "ENTP": ["💼 창업가", "🎮 게임 개발자", "🧩 기획자"],
    "ESTJ": ["🏢 관리자", "📊 프로젝트 매니저", "💼 영업 관리자"],
    "ESFJ": ["🏫 교사", "👨‍👩‍👧‍👦 사회복지사", "💇‍♀️ 뷰티 전문가"],
    "ENFJ": ["🗣️ 강연가", "📚 교육자", "🌟 인재 개발 전문가"],
    "ENTJ": ["🚀 기업 CEO", "📊 전략기획가", "📣 브랜드 매니저"]
}

# 🚀 추천 결과
if user_mbti:
    st.subheader(f"🧭 {user_mbti} 유형에게 어울리는 직업은?")
    for job in mbti_career[user_mbti]:
        st.markdown(f"- {job}")

# 🌟 하단 메시지
st.markdown("---")
st.markdown("👩‍🎓 **모든 유형이 소중해요!** 자신의 성격을 이해하고, 다양한 진로를 탐색해보세요 😊")
