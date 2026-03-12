class FlashDealHardware:
    def __init__(self):
        self.is_car_device_active = False
        self.sim_status = "Disconnected"

    def proximity_check(self, distance: float):
        # يفتح السيارة أو الجهاز عند الاقتراب (نطاق 5 أمتار)
        return distance <= 5.0

    def link_special_sim(self, sim_id: str):
        self.sim_status = f"Active: {sim_id}"
        return True
