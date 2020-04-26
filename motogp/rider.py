class rider():
    def __init__(self, fullname, number):
        super().__init__()
        self.fullname = fullname
        self.number = number


def create_rider(fullname, number):
    rider = rider(fullname, number)

    return rider
