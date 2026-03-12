from Core.Security import MyFlashDealStarSecurity
from Hardware.DeviceManager import FlashDealHardware
from Modules.Inclusivity import UniversalInclusivity

class FlashDealStarUniversal:
    def __init__(self):
        self.security = MyFlashDealStarSecurity()
        self.hardware = FlashDealHardware()
        self.logic = UniversalInclusivity()
        self.slogan = "Talk. Pay. Done."

    def start_transaction(self, user_id, auth_data, distance):
        if self.hardware.proximity_check(distance) and self.security.verify_biometric(auth_data):
            token = self.security.generate_secure_token(user_id)
            return f"{self.slogan} | Token: {token}"
        return "Access Denied"

# تشغيل المحرك العالمي
fds_star = FlashDealStarUniversal()
