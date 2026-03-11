import streamlit as st
import time

# --- 1. الإعدادات والسمة الفخمة ---
st.set_page_config(page_title="MyFlashDeal Star Universal", page_icon="🌟", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #050505; color: #ffffff; }
    .stButton>button { 
        width: 100%; border-radius: 10px; 
        background: linear-gradient(135deg, #001f3f 0%, #001122 100%); 
        color: white; border: 1px solid #004080; font-weight: bold; padding: 12px;
    }
    .alpha-card { padding: 15px; border: 1px solid #ff4b4b; border-radius: 10px; background: #1a0000; margin-top: 10px; }
    .status-badge { padding: 5px 10px; border-radius: 5px; font-size: 0.8em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# إدارة حالة النظام (Session State)
if 'menu' not in st.session_state: st.session_state.menu = "الرئيسية"
if 'car_status' not in st.session_state: st.session_state.car_status = "Disconnected"
if 'sim_status' not in st.session_state: st.session_state.sim_status = "Inactive"
if 'engine_on' not in st.session_state: st.session_state.engine_on = False

# --- 2. أزرار التنقل العلوية ---
st.title("⚡ MyFlashDeal Star Universal")
cols = st.columns(5)
if cols[0].button("🛡️ الأمان"): st.session_state.menu = "الأمان"
if cols[1].button("📋 الشفافية"): st.session_state.menu = "الشفافية"
if cols[2].button("⚡ الصفقة"): st.session_state.menu = "الصفقة"
if cols[3].button("🤖 جيمين"): st.session_state.menu = "جيمين"
if cols[4].button("❓ المساعدة"): st.session_state.menu = "المساعدة"

st.write("---")

# --- 3. محتوى الأقسام التفاعلية ---

if st.session_state.menu == "الأمان":
    st.header("🛡️ نظام أمان سوني الذكي")
    st.info("تشفير SHA-256 نشط. يتم الآن فحص البصمة الصوتية والمكانية.")
    st.progress(100)

elif st.session_state.menu == "الشفافية":
    st.header("📋 تقرير الامتثال العالمي")
    st.table({"الدولة": ["الإمارات 🇦🇪", "إيطاليا 🇮🇹"], "التوثيق": ["قانوني كامل", "مطابق للمعايير"]})

elif st.session_state.menu == "جيمين":
    st.header("🤖 الوكيل الذكي (Multimodal)")
    t1, t2 = st.tabs(["🎙️ Talk", "⌨️ Chat"])
    with t1:
        if st.button("🎤 تفعيل المصدح (Listen)"):
            st.success("جاري الاستماع لآمر النجمة...")
    with t2:
        st.text_input("أمر كتابي:")

elif st.session_state.menu == "الصفقة":
    st.header("⚡ إتمام الصفقة")
    if st.button("تأفيذ (Done)"):
        st.balloons()
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3")
        st.success("تمت العملية بنجاح. معرف الشهادة: UNIV-STAR-2026")

elif st.session_state.menu == "المساعدة":
    st.header("❓ الدعم الفني")
    st.write("لربط السيارة، تأكد من تفعيل وضع Master Alpha من القائمة الجانبية.")

else:
    st.markdown("### 🏠 لوحة التحكم الرئيسية")
    st.write("النظام جاهز. اختر قسماً من الأعلى للبدء.")

# --- 4. القائمة الجانبية (The Core Master Alpha) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    st.header("My FlashDeal Star")
    
    access_level = st.radio("مستوى الوصول:", ["مستخدم عادي", "Master Alpha 🔓"])
    
    if access_level == "Master Alpha 🔓":
        key = st.text_input("رمز الدخول العالي:", type="password")
        if key == "MFS-2026-X99-ALPHA-SECURE-DEAL":
            st.markdown("<div class='alpha-card'>", unsafe_allow_html=True)
            st.subheader("🛰️ Hardware Control")
            
            # التحكم في الـ SIM
            st.write(f"📶 SIM Card: **{st.session_state.sim_status}**")
            if st.button("تنشيط FlashDeal SIM"):
                st.session_state.sim_status = "Active & Encrypted"
                st.rerun()
            
            st.write("---")
            
            # التحكم في السيارة
            st.write(f"🚗 Vehicle: **{st.session_state.car_status}**")
            if st.session_state.car_status == "Disconnected":
                if st.button("🔗 ربط مع جهاز السيارة"):
                    with st.spinner("جاري الاقتران..."):
                        time.sleep(1.5)
                        st.session_state.car_status = "Connected (BT/LTE)"
                        st.rerun()
            else:
                if not st.session_state.engine_on:
                    if st.button("⚙️ تشغيل المحرك"):
                        st.session_state.engine_on = True
                        st.rerun()
                else:
                    st.success("🔥 المحرك يعمل الآن")
                    if st.button("🛑 إيقاف المحرك"):
                        st.session_state.engine_on = False
                        st.rerun()
                st.button("🔓 فتح الأبواب")
            
            st.markdown("</div>", unsafe_allow_html=True)
        elif key != "":
            st.error("الرمز غير صحيح")

st.sidebar.write("---")
st.sidebar.caption("Talk. Pay. Done.")
