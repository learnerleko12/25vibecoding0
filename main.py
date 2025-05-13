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

# 🧠 MBTI 이모지 사전
mbti_emojis = {
    "ISTJ": "📘", "ISFJ": "🧺", "INFJ": "🔮", "INTJ": "📊",
    "ISTP": "🛠️", "ISFP": "🎨", "INFP": "📖", "INTP": "🧪",
    "ESTP": "🎤", "ESFP": "🎉", "ENFP": "🌍", "ENTP": "🧩",
    "ESTJ": "📈", "ESFJ": "👩‍👧‍👦", "ENFJ": "🗣️", "ENTJ": "🚀"
}

# 💼 MBTI별 직업 추천 사전
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

# 📘 MBTI별 과고 진학 관련 상담 메시지
science_high_message = {
    "INTJ": "🔍 깊이 있는 사고와 목표 지향적인 성향 덕분에 과학고 진학에 유리해요. 수학과 과학에 대한 탐구를 지속하세요!",
    "INTP": "🧪 논리적 사고와 문제 해결 능력이 뛰어나 과학고에서의 연구 활동에 적합해요. 프로젝트형 학습에 익숙해지는 것도 좋아요.",
    "INFJ": "📚 학문적인 열정과 몰입 능력 덕분에 과학 분야에서도 깊이 있는 성장을 할 수 있어요. 자신의 관심 분야를 조기에 탐색해 보세요.",
    "ISTJ": "📘 성실하고 체계적인 학습 태도는 과학고 학업에 큰 도움이 됩니다. 꾸준한 준비가 관건이에요!",
    "ISTP": "🔧 실험과 실습을 좋아하는 당신! 과학고에서 실용적인 과학 탐구 활동을 즐길 수 있어요.",
    "ENTP": "🧩 창의적 문제 해결력은 융합과학 분야에서 빛을 발합니다. 다양한 분야에 호기심을 가져보세요!",
    "ENTJ": "🚀 도전적이고 목표 지향적인 성격으로 과학고에서도 리더 역할을 할 수 있어요. 수학적 사고력 향상에 집중해 보세요."
}

# ✅ 사용자 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 ✨", mbti_types)

# 📌 선택한 MBTI에 맞는 이모지 가져오기
selected_mbti_emoji = mbti_emojis[selected_mbti]

# 🚀 추천 결과
st.markdown("---")
st.subheader(f"{selected_mbti_emoji} {selected_mbti} 유형에게 어울리는 직업은...?")

for job in mbti_career[selected_mbti]:
    st.markdown(f"- {job}")

# 📘 과고 진학 관련 조언
if selected_mbti in science_high_message:
    st.markdown("🧑‍🔬 **과학고 진학을 꿈꾼다면?**")
    st.info(science_high_message[selected_mbti])

# 💌 하단 메시지
st.markdown("---")
st.markdown("👩‍🎓 **모든 유형이 소중해요!** 자신의 성격을 이해하고, 다양한 진로를 탐색해보세요 😊")
