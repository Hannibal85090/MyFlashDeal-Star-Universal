class FlashDealHardware:
    def __init__(self):
        self.device_id = "FDS-STAR-2026"
        self.is_car_device_active = False
        self.sim_status = "Disconnected"

    def proximity_check(self, distance: float):
        # التفعيل التلقائي عند الاقتراب (Range & Vicinity)
        if distance <= 5.0:
            self.is_car_device_active = True
            return True
        return False

    def link_special_sim(self, sim_id: str):
        # التعاقد مع شركات الاتصالات لإصدار SIM خاص بـ FlashDeal
        self.sim_status = f"Active FlashDeal SIM: {sim_id}"
        return True
