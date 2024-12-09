import streamlit as st

st.title('st.form')

# 'with' 표기법을 사용한 전체 예시
st.header('1. 토스트 주문서')
st.subheader('토스트 가게')

with st.form('my_form'):
    st.subheader('**토스트 주문하기**')

    # 입력 위젯
    bread_val = st.selectbox('빵의 종류', ['우유식빵', '호밀빵'])
    bread_roast_val = st.select_slider('빵의 굽기', ['없음', '약간 구움', '적당함', '약간 바삭함', '바삭함'])
    toast_type_val = st.selectbox('토스트 종류', ['에그마요', '베이컨', 'BLT', '햄치즈', '야채'])
    event_val = st.selectbox('리뷰 이벤트', ['우유', '콜라', '사이다', '아이스티'])
    serving_type_val = st.selectbox('서빙 형식', ['배달', '픽업', '가게 내 취식'])
    ownbowl_val = st.checkbox('자신의 다회용기 가져오기')

    # 모든 양식은 제출 버튼을 가져야 함
    submitted = st.form_submit_button('제출')

if submitted:
    st.markdown(f'''
        ☕ 주문하신 내용:
        - 빵의 종류: `{bread_val}`
        - 빵의 굽기: `{bread_roast_val}`
        - 토스트 종류: `{toast_type_val}`
        - 리뷰 이벤트: `{event_val}`
        - 서빙 형식: `{serving_type_val}`
        - 자신의 다회용기 가져오기: `{ownbowl_val}`
        ''')
else:
    st.write('☝️ 주문하세요!')




# 객체 표기법을 사용한 짧은 예시
st.header('2. 토스트 개수')

form = st.form('my_form_2')
toast_num_val = form.slider('값 선택')
form.form_submit_button('제출')

#모든 양식은 st.form_submit_button을 포함해야 함.
#st.button과 st.download_button은 양식에 추가할 수 없습니다.

st.write('주문할 토스트의 개수: ', toast_num_val)
