import streamlit as st
import cv2
import hashlib
import time
import mediapipe as mp
import numpy as np

# [الفحص الإجرائي] إعدادات واجهة FlashDeal Star السيادية
st.set_page_config(page_title="FlashDeal Star", layout="wide", page_icon="⚡")
st.title("⚡ My FlashDeal Star | Agentic Economy")
st.markdown("### **Talk. Pay. Done.**")

# [الفحص الفعلي] إدارة الحالة لضمان استمرارية النظام
if (("wallet_balance" not in st.session_state)):
    st.session_state["wallet_balance"] = 1500.0
if (("is_authorized" not in st.session_state)):
    st.session_state["is_authorized"] = False

# تقسيم الشاشة باحترافية
col_cam, col_info = st.columns([2, 1])

with col_cam:
    st.subheader("🛡️ التحقق البصري الآمن")
    run_scan = st.toggle("تفعيل الماسح الأمني (Security Scan)")
    display_window = st.empty()

    if (run_scan):
        cap = (cv2.VideoCapture(0))
        with mp.solutions.hands.Hands(min_detection_confidence=0.7) as hands:
            while (run_scan):
                ret, frame = (cap.read())
                if ((not ret)): break
                
                # تحليل الإيماءة لفك قفل المحفظة
                rgb_frame = (cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                res = (hands.process(rgb_frame))
                
                if (res.multi_hand_landmarks):
                    for lm in res.multi_hand_landmarks:
                        mp.solutions.drawing_utils.draw_landmarks(frame, lm, mp.solutions.hands.HAND_CONNECTIONS)
                        # حساب المسافة الفعلية بين الإبهام والسبابة للتوثيق
                        p1 = np.array([lm.landmark[4].x, lm.landmark[4].y])
                        p2 = np.array([lm.landmark[8].x, lm.landmark[8].y])
                        dist = (np.linalg.norm(p1 - p2))
                        
                        if (dist < 0.05):
                            st.session_state["is_authorized"] = True
                            st.toast("✅ تم التوثيق بنجاح")

                display_window.image(frame, channels="BGR", use_container_width=True)
                if (st.session_state["is_authorized"]): break
                time.sleep(0.01)
        cap.release()

with col_info:
    st.subheader("💳 محفظة الوكيل")
    st.metric(label="USDC Balance", value=(f"{st.session_state['wallet_balance']}"))
    
    st.divider()
    if (st.button("تأكيد دفع (100 USDC)")):
        if (st.session_state["is_authorized"]):
            st.session_state["wallet_balance"] -= 100.0
            st.balloons()
            st.success("تم تنفيذ العقد الذكي بنجاح! ✅")
            st.session_state["is_authorized"] = False # إعادة تأمين النظام
            time.sleep(2)
            st.rerun()
        else:
            st.error("❌ عذراً، النظام مقفل. مطلوب إيماءة التوثيق أولاً.")

st.caption("Developed by Ali Arfaoui | FlashDeal Star Project 2026")
