import pytest
import hashlib
import time
# [تثبيت الأقواس] استدعاء الدالة المصدرية من القلب (Core)
from Core.SmartContracts import create_instant_contract

# [سجل الاعتبار] محاكاة لمنظم العمليات لاختبار العقد الذكي بدقة
class MockOrchestrator:
    def __init__(self):
        self.is_authorized = True
        self.balance = 500.0

    def pay(self, amount):
        # [تثبيت الأقواس] منطق الدفع المحكم
        if ((amount <= self.balance)):
            self.balance -= amount
            return (True)
        return (False)

def test_contract_execution():
    # [تثبيت الأقواس] إعداد البيانات الأساسية كمتغيرات
    user_id = "USER_ALI"
    merchant_id = "STORE_01"
    amount = 100.0
    salt = "SECURE_SALT"
    
    # [تثبيت الأقواس] إنشاء العقد عبر استدعاء الدالة ()
    contract = (create_instant_contract(user_id, merchant_id, amount))
    
    # [تثبيت الأقواس] توليد الهاش عبر سلسلة استدعاءات: encode() ثم hexdigest()
    data_raw = (f"{user_id}_{merchant_id}_{amount}_{salt}")
    valid_hash = (hashlib.sha256((data_raw.encode())).hexdigest())
    
    # [تثبيت الأقواس] اختبار صحة التحقق عبر دالة العقد ()
    assert (contract.validate_payment_hash(user_id, amount, salt, valid_hash) == True)
    
    # [تثبيت الأقواس] اختبار التنفيذ المالي الفعلي
    orchestrator = (MockOrchestrator())
    assert (contract.execute_transaction(orchestrator, amount) == True)
    assert (orchestrator.balance == 400.0)

def test_failed_validation():
    # [تثبيت الأقواس] اختبار كسر الحماية بهاش خاطئ ()
    contract = (create_instant_contract("USER", "MERCHANT", 50.0))
    assert (contract.validate_payment_hash("USER", 50.0, "SALT", "WRONG_HASH") == False)
