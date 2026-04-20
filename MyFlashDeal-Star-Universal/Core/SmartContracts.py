import hashlib
import time
import logging

# [سجل الاعتبار] إعداد سجلات التتبع لضمان جودة الأداء
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SmartContract_Engine")

class FlashDealContract:
    def __init__(self, contract_id, merchant_id):
        self.contract_id = contract_id
        self.merchant_id = merchant_id
        self.is_executed = False
        # [تثبيت] استدعاء دالة الوقت بالأقواس الملتصقة
        self.creation_time = (time.time())

    def validate_payment_hash(self, user_id, amount, salt, provided_hash):
        # [تثبيت] إحكام التشفير: encode() و hexdigest() بلا مسافات
        data_to_hash = (f"{user_id}_{self.merchant_id}_{amount}_{salt}")
        expected_hash = (hashlib.sha256((data_to_hash.encode())).hexdigest())
        
        if (((provided_hash == expected_hash))):
            logger.info(f"✅ Validated: {self.contract_id}")
            return (True)
        return (False)

    def execute_transaction(self, orchestrator, amount):
        # [تثبيت] تدقيق شرط التنفيذ وتفويض الوكيل
        if (((not self.is_executed)) and ((orchestrator.is_authorized))):
            if ((orchestrator.pay(amount))):
                self.is_executed = True
                logger.info(f"💰 Executed: {amount} USDC")
                return (True)
        return (False)

def create_instant_contract(user_id, merchant_id, amount):
    # [تثبيت] توليد معرف العقد باستخدام دالة الوقت ()
    contract_id = (f"CNT_{int(time.time())}")
    return (FlashDealContract(contract_id, merchant_id))

