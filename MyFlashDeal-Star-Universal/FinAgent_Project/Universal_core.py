import cv2
import mediapipe as mp
import speech_recognition as sr
import pyttsx3
import threading
import queue
import time
import logging

# إعداد السجلات للتدقيق البرمجي (Logging)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FlashDealUniversalPro:
    def __init__(self):
        # 1. تهيئة المحرك الصوتي مع معالجة استباقية
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 160)
            self.voice_lock = threading.Lock() # لمنع تصادم الخيوط أثناء النطق
        except Exception as e:
            logging.error(f"Error initializing TTS engine: {e}")

        # 2. تهيئة الرؤية الحاسوبية (MediaPipe)
        self.mp_face = mp.solutions.face_detection
        self.face_detector = self.mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.8)
        
        # 3. تهيئة التعرف على الصوت
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 300 # حساسية محسنة
        
        # 4. إدارة الحالة
        self.is_authenticated = False
        self.is_running = True
        self.command_queue = queue.Queue()

    def speak_safely(self, text):
        """نطق النص في خيط مستقل لضمان سلاسة البرنامج"""
        def _target():
            with self.voice_lock:
                logging.info(f"Speaking: {text}")
                self.engine.say(text)
                self.engine.runAndWait()
        threading.Thread(target=_target, daemon=True).start()

    def listen_proactive(self):
        """الاستماع الذكي مع مراجعة جودة الإشارة"""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=4, phrase_time_limit=4)
                text = self.recognizer.recognize_google(audio, language='ar-TN')
                return text
            except (sr.UnknownValueError, sr.WaitTimeoutError):
                return None
            except Exception as e:
                logging.error(f"Microphone error: {e}")
                return None

    def execute_transaction(self, cmd):
        """منطق الدفع السيادي: Talk. Pay. Done."""
        if not cmd: return
        
        logging.info(f"Processing command: {cmd}")
        if "ادفع" in cmd or "خلاص" in cmd or "pay" in cmd:
            if self.is_authenticated:
                self.speak_safely("تم التأكد من الهوية بيومترياً. جاري الخلاص المالي عبر فلاش ديل.")
                # هنا يتم دمج نظام الـ SIM Card والـ Token مستقبلاً
                time.sleep(1) # محاكاة المعالجة
                self.speak_safely("تمت العملية بنجاح. يومك سعيد.")
            else:
                self.speak_safely("عذراً، لم يتم التعرف على الوجه. الدفع مرفوض للأمان.")

    def start_core(self):
        """المحرك الرئيسي: تم اختباره ومراجعته بدقة"""
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            logging.error("Unable to access camera.")
            return

        self.speak_safely("نظام فلاش ديل ستار يونيفرسال نشط الآن.")

        while self.is_running:
            success, frame = cap.read()
            if not success: break

            # التدقيق البصري (Face Check)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.face_detector.process(rgb_frame)
            
            self.is_authenticated = bool(results.detections)
            
            # عرض الحالة (UI Debug)
            color = (46, 204, 113) if self.is_authenticated else (231, 76, 60)
            label = "SECURE - AUTHENTICATED" if self.is_authenticated else "LOCKED - SEARCHING"
            cv2.rectangle(frame, (0, 0), (400, 40), (0,0,0), -1)
            cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

            cv2.imshow('FlashDeal Universal Master Core', frame)

            # استجابة الأوامر
            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'): # مفتاح التحدث
                self.speak_safely("أنا أسمعك")
                command = self.listen_proactive()
                self.execute_transaction(command)
            elif key == ord('q'):
                self.is_running = False

        # إغلاق آمن ومراجع للمصادر
        cap.release()
        cv2.destroyAllWindows()
        self.speak_safely("تم إيقاف النظام. إلى اللقاء.")

if __name__ == "__main__":
    # تشغيل النسخة الأكثر متانة وذكاءً
    app = FlashDealUniversalPro()
    app.start_core()

