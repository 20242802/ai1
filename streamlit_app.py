import streamlit as st
import pandas as pd

# 타이틀 설정
st.title("안녕하세요")

# 서브타이틀
st.subheader("안녕히계세요")

# 표 데이터 생성
data = {
    '이름': ['홍길동', '전우치', '원재쌤'],
    '나이': [25, 30, 22],
    '직업': ['활빈당', '절도', '정보']
}
df = pd.DataFrame(data)

# 표 출력
st.write("기본적인 표:")
st.dataframe(df)

# HTML 메시지 출력
st.markdown("""
    <div style="background-color: lightblue; padding: 10px;">
        <h3>HTML 스타일링 메시지</h3>
        <p>Streamlit에서는 Markdown을 사용하여 HTML 태그를 삽입하고 스타일을 지정할 수 있습니다.</p>
    </div>
""", unsafe_allow_html=True)

# 추가적인 텍스트
st.write("Streamlit을 활용한 빠른 웹 애플리케이션 개발!")
