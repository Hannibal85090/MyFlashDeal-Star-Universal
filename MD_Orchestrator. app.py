import json
import hashlib
import sys

class FlashDealOrchestrator:
    """
    نظام التنسيق المركزي لمشروع FlashDeal.
    المهمة: الربط الآمن بين الوكلاء (Star, Portal, App).
    القاعدة: إحكام المنطق، سلامة الأقواس، وسرعة التنفيذ.
    """
    
    def __init__(self, config_data: dict):
        # استخدام البيانات المباشرة لضمان الفاعلية في التجربة الأولى
        self.config = config_data
        self.is_authorized = False
        print("[System]: تم تفعيل وكيل التنسيق بنجاح.")

    def secure_handshake(self, agent_id: str, received_token: str) -> bool:
        """
        إجراء أمني محكم (Handshake) للتحقق من هوية الوكيل الطالب.
        """
        # توليد مفتاح التحقق بناءً على معرف الوكيل (منطق إجرائي)
        secret_base = f"FD_{agent_id}_2026"
        valid_hash = hashlib.sha256(secret_base.encode()).hexdigest()
        
        if received_token == valid_hash:
            self.is_authorized = True
            print(f"[Auth]: تم التحقق من الوكيل {agent_id}. الدخول آمن.")
            return True
        else:
            print(f"[Security Warning]: محاولة دخول غير مصرح بها من {agent_id}!")
            return False

    def execute_logic(self, payload: dict):
        """
        تنفيذ العمليات المالية (Talk. Pay. Done.) مع ضمان عدم التعارض.
        """
        if not self.is_authorized:
            print("[Error]: العمليات محظورة. يرجى إتمام التحقق الأمني أولاً.")
            return

        try:
            # التأكد من وجود المفاتيح الأساسية لتجنب خلل Key Error
            action = payload.get("action", "unknown")
            amount = payload.get("amount", 0)
            
            if action == "payment":
                print(f"[Action]: تنفيذ عملية دفع بمبلغ {amount} USDC...")
                print("[Status]: Talk. Pay. Done. (تَحَدَّثْ. ادْفَعْ. تَمَّ.)")
            else:
                print(f"[Info]: تم استلام أمر غير مالي: {action}")
                
        except Exception as error:
            print(f"[Critical Error]: خلل في الإجراء البرمجي: {str(error)}")

# --- قسم التجربة المخبرية (Test Suite) ---
if __name__ == "__main__":
    # 1. إعداد بيانات تجريبية (تلافي خلل الملفات الخارجية في أول تجربة)
    test_config = {"version": "2.0.0", "mode": "Hackathon-Test"}
    
    # 2. تشغيل الوكيل
    agent = FlashDealOrchestrator(test_config)
    
    # 3. تجربة التحقق الأمني (إحكام الـ Token)
    test_agent_id = "STAR_01"
    correct_token = hashlib.sha256(f"FD_{test_agent_id}_2026".encode()).hexdigest()
    
    # 4. التنفيذ الإجرائي
    if agent.secure_handshake(test_agent_id, correct_token):
        agent.execute_logic({"action": "payment", "amount": 50})
