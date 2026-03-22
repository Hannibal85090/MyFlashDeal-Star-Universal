import hashlib
import secrets
import time
from dataclasses import dataclass
from enum import Enum
import pandas as pd # أضفنا pandas لمعالجة الجداول في الواجهة

class TransactionStatus(Enum):
    PENDING = "pending"
    AUTHORIZED = "authorized"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class FlashToken:
    token_id: str
    secure_hash: str
    expiration: float
    metadata: dict

class FlashDealCore:
    def __init__(self, security_level="high"):
        self._vault = {}
        self.security_level = security_level

    # --- دالة التنظيف الجديدة (التي طلبناها) ---
    def sanitize_vault_data(self):
        """تحويل الـ Vault إلى DataFrame نظيف للعرض في الصورة ١"""
        if not self._vault:
            return pd.DataFrame(columns=["Token ID", "Status", "Expiration", "Owner"])
        
        data = []
        for tid, token in self._vault.items():
            # حساب الوقت المتبقي ليكون العرض منطقياً
            remaining = round(token.expiration - time.time(), 2)
            status = "Active" if remaining > 0 else "Expired"
            
            data.append({
                "Token ID": tid,
                "Status": status,
                "Security Level": self.security_level.upper(),
                "Owner": token.metadata.get("owner", "Unknown"),
                "Last Sync": "Just Now"
            })
        
        df = pd.DataFrame(data)
        # تنظيف نهائي لضمان الدقة
        df.fillna("N/A", inplace=True)
        return df

    def generate_mutual_token(self, user_id: str, transaction_value: float):
        raw_seed = f"{user_id}{transaction_value}{secrets.token_hex(16)}{time.time()}"
        secure_hash = hashlib.sha3_512(raw_seed.encode()).hexdigest()
        token_id = f"FDS-{secrets.token_urlsafe(12)}"
        
        new_token = FlashToken(
            token_id=token_id,
            secure_hash=secure_hash,
            expiration=time.time() + 300,
            metadata={"val": transaction_value, "owner": user_id}
        )
        
        self._vault[token_id] = new_token
        return token_id

    # بقية الدوال الخاصة بالبصمة الصوتية (Talk. Pay. Done.) كما هي لضمان الاستقرار
    def validate_voice_intent(self, voice_signature: str, command: str):
        intent_map = {"pay": True, "send": True, "transfer": True}
        words = command.lower().split()
        is_valid = any(word in intent_map for word in words)
        return is_valid and self._verify_biometric_sync(voice_signature)

    def _verify_biometric_sync(self, signature: str):
        return len(signature) > 32

    def execute_secure_transaction(self, token_id: str):
        if token_id not in self._vault: return TransactionStatus.FAILED
        token = self._vault[token_id]
        if time.time() > token.expiration: return TransactionStatus.FAILED
        return TransactionStatus.COMPLETED

# Instance للعمل المتوازي عالي الجودة
flash_deal_star = FlashDealCore(security_level="ultra")
