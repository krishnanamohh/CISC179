from .ElectronicDevice import ElectronicDevice

class Laptop(ElectronicDevice):
    def __init__(self, power_source, manufacturer, operating_system, ram, screen_size, resolution):
        super().__init__(power_source, manufacturer)
        self.operating_system = operating_system
        self.ram = ram
        self.screen_size = screen_size
        self.resolution = resolution

    def display_info(self):
        laptop_info = [
            "Laptop Information:",
            f"Power Source: {self.power_source}",
            f"Manufacturer: {self.manufacturer}",
            f"Operating System: {self.operating_system}",
            f"RAM: {self.ram}",
            f"Screen Size: {self.screen_size}",
            f"Resolution: {self.resolution}"
        ]
        return laptop_info

    def browse_internet(self):
        print("Browsing the internet on the laptop.")
