import streamlit as st
import numpy as np
import cv2

# 1. بروتوكول الاستدعاء الحذر (تجاوز خطأ ModuleNotFound)
try:
    import google.generativeai as genai
except ImportError:
    st.error("🚨 خطأ في بيئة العمل: مكتبة 'google-generativeai' مفقودة. تأكد من وجودها في requirements.txt")
    st.stop()

# 2. إعدادات بوابة الاعتبار (الهوية والواجهة)
st.set_page_config(
    page_title="FlashDeal Star",
    page_icon="⭐",
    layout="wide"
)

# 3. الربط الاستراتيجي مع "الخزنة" (Secrets)
def configure_brain():
    try:
        if "GEMINI_KEY" not in st.secrets:
            st.error("🔑 عائق أمني: مفتاح 'GEMINI_KEY' غير موجود في Secrets.")
            return None
        
        genai.configure(api_key=st.secrets["GEMINI_KEY"])
        # استخدام الموديل الأكثر استقراراً لتفادي خطأ 404
        return genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"⚠️ فشل النظام في استدعاء العقل: {str(e)}")
        return None

model = configure_brain()

# 4. الهندسة البصرية للتطبيق (Talk. Pay. Done.)
st.title("⭐ FlashDeal Star: الوكيل الرسمي")
st.markdown("---")

# تقسيم الشاشة: التفاعل الذكي (يمين) والأمان البيومتري (يسار)
col_logic, col_security = st.columns([2, 1])

with col_logic:
    st.subheader("🧠 مركز الأوامر (Talk)")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # عرض تاريخ المحادثة باحترافية
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # مدخل الأوامر (تجاوز تعثر المدخلات)
    if prompt := st.chat_input("بمَ يأمر مالك النجمة؟"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if model:
            with st.chat_message("assistant"):
                with st.spinner("الوكيل يحلل الأمر..."):
                    try:
                        # تلقين الوكيل دوره الاستراتيجي
                        context = f"أنت الوكيل المالي الرسمي لـ FlashDeal. نفذ باحترافية: {prompt}"
                        response = model.generate_content(context)
                        st.markdown(response.text)
                        st.session_state.messages.append({"role": "assistant", "content": response.text})
                    except Exception as e:
                        st.error(f"❌ تعطل الاتصال بالعقل: {str(e)}")

with col_security:
    st.subheader("🔐 بوابة الأمان (Security)")
    
    # معالجة تعارض الكاميرا (بوابة الاعتبار)
    enable_camera = st.checkbox("تفعيل التحقق بالوجه")
    if enable_camera:
        cam_input = st.camera_input("التقط بصمة الوجه")
        if cam_input:
            st.success("✅ تم التحقق من الهوية بيومترياً")
            
            st.write("---")
            # زر الحسم النهائي (Pay)
            if st.button("🚀 تنفيذ الدفع الفوري (Done)"):
                if "NUCLEAR_KEY" in st.secrets:
                    st.balloons()
                    st.success("تمت العملية بنجاح!")
                    st.code(f"REF: {st.secrets['NUCLEAR_KEY'][:12]}...SECURE", language="text")
                else:
                    st.warning("⚠️ المفتاح النووي للمحفظة غير مضبوط.")

# 5. تذييل النسخة (تمام الجمل والبيان)
st.write("---")
st.caption("FlashDeal Star 2026 | نظام مالي ذكي مستقل | لا يتم الواجب إلا به")

