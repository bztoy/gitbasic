class bike():

    # Engine configuration
    engine_v4 = 'V4'
    engine_i4 = 'I4'

    def __init__(self, engine_type, code):
        super().__init__()

        self.engine_type = engine_type
        self.code = code
        self.engine_status = ''

    def engine_ignition(self, mode):
        if self.engine_status == mode:
            return f"The engine is already {self.engine_status}"
        else:
            self.engine_status = mode
        pass

    def show_enging_status(self):
        return f"the engine status is {self.engine_status}"

    def show_bike_detail(self):
        return f"Bike name is {self.code}, the engine config is {self.engine_type}"


class ducati(bike):
    def __init__(self, version):
        super().__init__(bike.engine_v4, 'DesmosediciGP')
        self.version = version


class honda(bike):
    def __init__(self, version):
        super().__init__(bike.engine_v4, 'RC213V')
        self.version = version


class suzuki(bike):
    def __init__(self):
        super().__init__(bike.engine_i4, 'GSX-RR')


class yamaha(bike):
    def __init__(self, version):
        super().__init__(bike.engine_i4, 'YZR-M1')
        self.version = version


class aprilia(bike):
    def __init__(self):
        super().__init__(bike.engine_v4, 'RS-GP')


class ktm(bike):
    def __init__(self):
        super().__init__(bike.engine_v4, 'RC16')
