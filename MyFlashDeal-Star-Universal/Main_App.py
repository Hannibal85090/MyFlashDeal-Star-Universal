from Core.Security import MyFlashDealStarSecurity
from Hardware.DeviceManager import FlashDealHardware
from Modules.Inclusivity import UniversalInclusivity

class FlashDealStarUniversal:
    def __init__(self):
        self.security = MyFlashDealStarSecurity()
        self.hardware = FlashDealHardware()
        self.logic = UniversalInclusivity()
        self.slogan = "Talk. Pay. Done."

    def run_system_check(self, user_id, auth_data, distance):
        # التحقق من القرب + البصمة + التوكن المتبادل
        if self.hardware.proximity_check(distance):
            if self.security.verify_biometric(auth_data):
                token = self.security.generate_secure_token(user_id)
                mutual = self.security.initiate_mutual_handshake()
                return f"Success! {self.slogan} | Token: {token} | Mutual: {mutual}"
        return "Access Denied: Please check proximity or biometrics."

# التشغيل التجريبي
fds_star = FlashDealStarUniversal()
