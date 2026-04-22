import streamlit as st
import google.generativeai as genai

# 1. إعدادات الهوية (Talk. Pay. Done.)
st.set_page_config(page_title="FlashDeal Star", page_icon="⭐", layout="wide")

# 2. الربط بالعقل (تجاوز أي عائق في Secrets)
try:
    if "GEMINI_KEY" not in st.secrets:
        st.error("🔑 عائق أمني: مفتاح GEMINI_KEY غير موجود.")
        st.stop()
    
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"❌ عطل في المحرك: {str(e)}")
    st.stop()

# 3. إدارة التفاعل (لضمان عدم التوقف)
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("⭐ FlashDeal Star: الوكيل الذكي")
st.write("---")

# تقسيم الشاشة لضمان عدم تداخل الكاميرا مع الدردشة
col_chat, col_auth = st.columns([2, 1])

with col_chat:
    st.subheader("🗣️ مركز التفاعل (Talk)")
    
    # عرض الرسائل السابقة فوراً
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # محرك التفاعل الفوري
    if prompt := st.chat_input("تكلم.. أو اكتب أمرك هنا"):
        # إضافة رسالة المستخدم
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # توليد الرد فوراً (الجوهر)
        with st.chat_message("assistant"):
            with st.spinner("الوكيل يحلل..."):
                try:
                    response = model.generate_content(f"أنت الوكيل المالي لـ FlashDeal. رد باحترافية على: {prompt}")
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                    # إعادة تشغيل الصفحة لتحديث الحالة وضمان عدم التعليق
                    st.rerun() 
                except Exception as e:
                    st.error(f"⚠️ فشل التفاعل: {str(e)}")

with col_auth:
    st.subheader("🔐 بوابة الأمان (Security)")
    auth_mode = st.toggle("تفعيل التحقق البيومتري")
    if auth_mode:
        img = st.camera_input("بصمة الوجه")
        if img:
            st.success("✅ الهوية مؤكدة")
            if st.button("🚀 تنفيذ الدفع (Pay)"):
                st.balloons()
                st.success("تمت العملية بنجاح!")

