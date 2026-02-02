import streamlit as st
import math

# 1. ฟังก์ชันสำหรับแสดงหน้าต่างสรุปผล (Pop-up)
@st.dialog("ใบสรุปรายการประมาณการ")
def show_summary_dialog(final_billed, selected_items):
    st.write("### รายการอุปกรณ์และบริการ:")
    if selected_items:
        for item in selected_items:
            # แสดงเฉพาะชื่อและจำนวนตามที่ตกลงกันไว้
            st.write(f"✅ {item['name']} จำนวน {item['qty']} รายการ")
    else:
        st.write("ยังไม่ได้เลือกรายการอุปกรณ์")
    
    st.divider()
    # แสดงราคาสุทธิที่ปัดเศษแล้ว
    st.info(f"## ราคาที่เสนอผู้ใช้ไฟ: {final_billed:,.0f} บาท")
    st.write("*(ราคานี้รวมค่าแรง ค่าปลดสับ และอุปกรณ์เรียบร้อยแล้ว)*")

def main():
    st.set_page_config(page_title="ระบบคำนวณค่าบริการ", layout="wide")
    
    # เปลี่ยนชื่อหัวข้อหลักตามที่คุณต้องการ
    st.title("ประมาณการติดตั้งอุปกรณ์ป้องกันและบำรุงรักษาหม้อแปลง")
    st.divider()

    # --- ส่วนที่ 1: ค่าแรงพนักงาน ---
    st.header("ค่าแรงพนักงาน")
    staff_data = [
        {"level": "พชง.3", "rate": 87.77},
        {"level": "พชง.4", "rate": 103.48},
        {"level": "พชง.5", "rate": 125.30},
        {"level": "พชง.6", "rate": 164.19},
    ]
    total_wage = 0
    cols_h = st.columns([2, 2, 2, 2, 2])
    cols_h[0].write("**ระดับ**"); cols_h[1].write("**ราคา/ชม**")
    cols_h[2].write("**ชั่วโมง**"); cols_h[3].write("**จำนวนคน**"); cols_h[4].write("**รวม**")

    for s in staff_data:
        c1, c2, c3, c4, c5 = st.columns([2, 2, 2, 2, 2])