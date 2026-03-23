
import streamlit as st
from supabase import create_client, Client

# 1. Điền thông tin Supabase
url = "https://xshapoewvuqykmaflmdc.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." # Giữ nguyên key dài của bạn ở đây

supabase: Client = create_client(url, key)

st.title("Phần Mềm Quản Lý Sản Xuất")
st.write("Nhập dữ liệu sản xuất trực tiếp xuống hệ thống.")

# 2. Giao diện nhập liệu
with st.form("production_form"):
    item = st.text_input("Tên sản phẩm/khuôn:")
    qty = st.number_input("Số lượng:", min_value=1, step=1)
    status = st.selectbox("Trạng thái:", ["Đạt", "Lỗi", "Đang xử lý"])
    
    submit_button = st.form_submit_button(label="Lưu dữ liệu")

# 3. Xử lý khi nhấn nút Lưu
if submit_button:
    data = {
        "item_name": item,
        "quantity": qty,
        "status": status
    }
    try:
        response = supabase.table("production_logs").insert(data).execute()
        st.success(f"Đã lưu thành công: {item} - {qty} sản phẩm")
    except Exception as e:
        st.error(f"Lỗi khi lưu dữ liệu: {e}")
