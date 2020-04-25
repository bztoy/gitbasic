class ecu():
    def __init__(self, brand):
        super().__init__()
        self.brand = brand
        self.max_clock = '1200'
        self.bus = 'CAN'
