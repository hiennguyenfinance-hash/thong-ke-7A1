import pandas as pd
import streamlit as st

st.set_page_config(page_title="Thống kê 7A1", layout="centered")

st.markdown("<h2 style='text-align: center;'>BẢNG THỐNG KÊ NHIỆM VỤ LỚP 7A1</h2>", unsafe_allow_html=True)
st.write("Kính mời quý phụ huynh chọn một nhiệm vụ trong danh sách bên dưới để xem tiến độ đăng ký.")

data = {
    "Nhiệm vụ": ["Trang trí lớp", "Chuẩn bị văn nghệ", "Mua đồ ăn nhẹ", "Dọn dẹp cuối giờ", "Chụp ảnh/Quay phim"],
    "Số người đăng ký": [5, 8, 3, 4, 2]
}
df = pd.DataFrame(data)

danh_sach = ["Tất cả"] + df["Nhiệm vụ"].tolist()
lua_chon = st.selectbox("Vui lòng chọn nhiệm vụ:", danh_sach)

if lua_chon != "Tất cả":
    filtered_df = df[df["Nhiệm vụ"] == lua_chon]
else:
    filtered_df = df

st.bar_chart(filtered_df.set_index("Nhiệm vụ"))
