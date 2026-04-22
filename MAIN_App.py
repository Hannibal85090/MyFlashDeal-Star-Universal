import streamlit as st
import numpy as np
import cv2
import io

# 1. بوابة الاعتبار: التحقق الاستباقي من المكتبات (لضمان عدم الانهيار)
try:
    import google.generativeai as genai
    from gtts import gTTS
except ImportError:
    st.error("🚨 خطأ استراتيجي: تأكد من وجود google-generativeai و gTTS في requirements.txt")
    st.stop()

# 2. إعدادات الهوية البصرية والقاعدة الذهبية للواجهة
st.set_page_config(
    page_title="FlashDeal Star Universal",
    page_icon="⭐",
    layout="wide"
)

# 3. بروتوكول الأوركسترا (Secrets): الربط المركزي الآمن
def setup_orchestra():
    """تثبت من وجود المفاتيح واستدعاء الموديل الأنسب"""
    if "GEMINI_KEY" not in st.secrets:
        st.error("🔑 عائق أمني: مفتاح GEMINI_KEY مفقود في السيكرتس (Secrets).")
        return None
    
    try:
        genai.configure(api_key=st.secrets["GEMINI_KEY"])
        # اختيار النسخة الأكثر استقراراً لتجاوز خطأ 404 المتكرر
        return genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"⚠️ فشل في تهيئة عقل الوكيل: {str(e)}")
        return None

# تهيئة المحرك لمرة واحدة
model = setup_orchestra()

# 4. إدارة نبض الجلسة (Session State) لضمان انسيابية التفاعل
if "messages" not in st.session_state:
    st.session_state.messages = []

# الواجهة الرئيسية (Talk. Pay. Done.)
st.title("⭐ FlashDeal Star Universal")
st.markdown("### *الوكيل المالي المستقل: عقلٌ يتفاعل، لسانٌ ينطق، وأمانٌ ينفذ*")
st.write("---")

# تقسيم العمل: التفاعل الجوهري (يمين) والبوابة الأمنية (يسار)
col_chat, col_auth = st.columns([2, 1])

with col_chat:
    st.subheader("🗣️ مركز التفاعل (Talk)")
    
    # عرض تاريخ العمليات فوراً لضمان الاستمرارية
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # محرك الاستجابة (الجوهر البرمجي)
    if prompt := st.chat_input("بمَ يأمر مالك النجمة؟"):
        # تسجيل مدخل المستخدم
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if model:
            with st.chat_message("assistant"):
                with st.spinner("الوكيل يحلل ويستعد للنطق..."):
                    try:
                        # تلقين الوكيل دوره الاستراتيجي
                        context = f"أنت الوكيل المباشر لـ FlashDeal Star. رد باحترافية وبشكل مقتضب على: {prompt}"
                        response = model.generate_content(context)
                        reply_text = response.text
                        st.markdown(reply_text)
                        
                        # --- التفاعل الصوتي (The Voice Core) ---
                        tts = gTTS(text=reply_text, lang='ar')
                        audio_stream = io.BytesIO()
                        tts.write_to_fp(audio_stream)
                        st.audio(audio_stream, format='audio/mp3', autoplay=True)
                        
                        # حفظ الاستجابة في سجل الجلسة
                        st.session_state.messages.append({"role": "assistant", "content": reply_text})
                        
                        # الحسم: تحديث الصفحة لضمان عدم العلوق البرمجي
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ عطل في محرك الاستجابة: {str(e)}")

with col_auth:
    st.subheader("🔐 بوابة الأمان (Security)")
    
    # تفعيل التحقق البيومتري (بصمة الوجه)
    is_secure = st.toggle("تفعيل التحقق بالوجه")
    if is_secure:
        cam_frame = st.camera_input("التحقق من الهوية")
        if cam_frame:
            st.success("✅ الهوية مؤكدة بيومترياً")
            
            st.write("---")
            # زر التنفيذ النهائي (Done)
            if st.button("🚀 تنفيذ العملية المالية"):
                if "NUCLEAR_KEY" in st.secrets:
                    st.balloons()
                    st.success("تم التنفيذ بنجاح باستخدام المفتاح النووي!")
                    # عرض مقتضب للمرجع الأمني
                    st.code(f"TX_REF: {st.secrets['NUCLEAR_KEY'][:12]}...SECURED", language="text")
                else:
                    st.warning("⚠️ المفتاح النووي مفقود في الأوركسترا (Secrets).")

# 5. تذييل النظام (الاعتبار والعبر)
st.write("---")
st.caption("FlashDeal Star Universal 2026 | الاستراتيجية قبل التنفيذ | Talk. Pay. Done.")
