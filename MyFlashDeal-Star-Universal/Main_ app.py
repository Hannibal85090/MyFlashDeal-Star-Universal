import streamlit as st
import cv2
import hashlib
import time
import mediapipe as mp
import os
import sys

# [سجل الاعتبار] معالجة تعارض المسارات لضمان رؤية مجلد Core في كل البيئات
base_path = (os.path.dirname(os.path.abspath(__file__)))
if ((base_path not in sys.path)):
    sys.path.append(base_path)

# [تثبيت] محاولة استدعاء العقد الذكي مع معالجة الخطأ إملائياً وبرمجياً
try:
    from Core.SmartContracts import create_instant_contract
except (ImportError, ModuleNotFoundError):
    st.error("⚠️ تنبيه: مجلد Core أو ملف SmartContracts غير متاح. يرجى التأكد من وجود ملف __init__.py")

class FlashDealSystem:
    def __init__(self):
        self.balance = 1500.0
        self.is_verified = False
        # [تثبيت] الأقواس ملتصقة بالدالة التنفيذية
        self.timestamp_id = str(int(time.time()))

    def verify_token(self, token_input, gesture_status):
        """التحقق من التوكن وإيماءة اليد معاً"""
        # [تثبيت] منع تعارض المسافات في سلسلة التشفير
        secure_data = (f"FLASH_{self.timestamp_id}")
        expected_hash = (hashlib.sha256(secure_data.encode()).hexdigest())
        
        if (((token_input == expected_hash)) and ((gesture_status == "OK"))):
            self.is_verified = True
            return (True)
        return (False)

def main():
    st.set_page_config(page_title="My FlashDeal Star", layout="wide")
    st.title("⚡ My FlashDeal Star | السيادة المالية")
    st.write("---")

    # تهيئة الحالة (Session State) لمنع إعادة التحميل العشوائي
    if (("system" not in st.session_state)):
        st.session_state["system"] = FlashDealSystem()

    col_cam, col_data = st.columns([2, 1])

    with col_cam:
        st.subheader("🛡️ محرك التحقق البصري")
        run_engine = st.checkbox("بدء المسح الأمني (Camera)")
        video_feed = st.empty()

        if (run_engine):
            video_capture = (cv2.VideoCapture(0))
            # إعداد Mediapipe للتعرف على اليد
            with mp.solutions.hands.Hands(min_detection_confidence=0.8) as hands_engine:
                while (run_engine):
                    success, frame = (video_capture.read())
                    if ((not success)):
                        break

                    # تحويل الألوان ومعالجة الصورة
                    rgb_frame = (cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                    results = (hands_engine.process(rgb_frame))
                    
                    current_gesture = "NONE"
                    if (results.multi_hand_landmarks):
                        for hand_lms in results.multi_hand_landmarks:
                            mp.solutions.drawing_utils.draw_landmarks(frame, hand_lms, mp.solutions.hands.HAND_CONNECTIONS)
                            # [تثبيت] حساب المسافة بين الإبهام والسبابة بدقة الأقواس
                            x_dist = (hand_lms.landmark[4].x - hand_lms.landmark[8].x)
                            y_dist = (hand_lms.landmark[4].y - hand_lms.landmark[8].y)
                            if ((((x_dist**2) + (y_dist**2))**0.5) < 0.06):
                                current_gesture = "OK"

                    video_feed.image(frame, channels="BGR", use_container_width=True)

                    if (current_gesture == "OK"):
                        # توليد توكن لحظي للمطابقة
                        tkn = (hashlib.sha256(f"FLASH_{st.session_state['system'].timestamp_id}".encode()).hexdigest())
                        if (st.session_state["system"].verify_token(tkn, "OK")):
                            st.success("✅ تم التحقق من الهوية والإيماءة")
                            time.sleep(1)
                            break
                    time.sleep(0.01) # موازنة الأداء ومنع التعليق
            
            video_capture.release()

    with col_data:
        st.subheader("📊 بيانات المحفظة")
        st.metric(label="الرصيد المتاح", value=(f"{st.session_state['system'].balance} USDC"))
        
        st.write("---")
        payment_amount = 100.0
        if (st.button(f"دفع {payment_amount} USDC الآن")):
            if (st.session_state["system"].is_verified):
                # [تثبيت] استدعاء العقد الذكي من Core للتنفيذ النهائي
                try:
                    contract = (create_instant_contract("ALI_ARFAOUI", "MERCHANT_X", payment_amount))
                    st.session_state["system"].balance -= payment_amount
                    st.balloons()
                    st.success(f"تمت العملية بنجاح! رقم العقد: {contract.contract_id}")
                    time.sleep(2)
                    st.rerun()
                except NameError:
                    st.warning("تم تنفيذ الدفع محلياً (العقد الذكي غير متصل)")
            else:
                st.error("❌ عذراً، يجب إتمام التحقق البصري أولاً")

if (__name__ == "__main__"):
    main()

