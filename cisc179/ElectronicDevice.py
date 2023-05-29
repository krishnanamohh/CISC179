class ElectronicDevice:
    def __init__(self, power_source, manufacturer):
        self.power_source = power_source
        self.manufacturer = manufacturer
        self.is_on = False

    def turn_on(self):
        print("The electronic device is now turned on.")
        self.is_on = True

    def turn_off(self):
        print("The electronic device is now turned off.")
        self.is_on = False

    def diplay_info(self):
        pass