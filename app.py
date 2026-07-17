Python
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Thẩm định Tín dụng", layout="centered")

st.title("🏦 UFM Credit App")
st.subheader("Công cụ thẩm định khách hàng cá nhân")

with st.sidebar:
    st.header("⚙️ Thiết lập dữ liệu")
    amount = st.slider("Số tiền vay (triệu VNĐ)", 10, 2000, 500)
    income = st.number_input("Thu nhập hàng tháng (triệu VNĐ)", 10.0)
    debt = st.number_input("Dư nợ hiện tại (triệu VNĐ)", 0.0)
    term = st.selectbox("Thời hạn vay (tháng)", [12, 24, 36, 60])

monthly_pay = (amount / term) + (amount * 0.008)
dti = ((monthly_pay + debt) / income) * 100 if income > 0 else 0

col1, col2 = st.columns(2)
col1.metric("Tỷ lệ DTI", f"{dti:.1f}%")

if dti < 35:
    st.success("✅ Hồ sơ đạt yêu cầu")
else:
    st.warning("⚠️ Cần bổ sung tài sản")

df = pd.DataFrame({'Danh mục': ['Gốc lãi', 'Dư nợ cũ'], 'Giá trị': [amount/term, debt]})
fig = px.pie(df, values='Giá trị', names='Danh mục', hole=0.4)
st.plotly_chart(fig, use_container_width=True)