class Thermostat:
    min_temp = 15.0
    max_temp = 30.0
    device_count = 0
    def __init__(self, location, initial_temp):
        self.location = location
        if initial_temp >= Thermostat.min_temp and \
        initial_temp <= Thermostat.max_temp:
            self.current_temp = initial_temp
            print(f"\nTemperature set to {self.current_temp}°C\n")
        else:
            self.current_temp = Thermostat.min_temp
            print(f"Initial temperature out of range. Set to minimum.\n")
        self.readings = [self.current_temp]
        Thermostat.device_count += 1
    def set_temperature(self, new_temp):
        if new_temp >= Thermostat.min_temp and \
        new_temp <= Thermostat.max_temp:
            self.current_temp = new_temp
            self.readings.append(new_temp)
            print(f"Temperature set to {new_temp}°C\n")
        else:
            print(f"\nTemperature {new_temp}°C is out of allowed range (15.0-30.0)\n")
    def get_average_temp(self):
        length = len(self.readings)
        if length != 0:
            avg = sum(self.readings) / length
            return avg
        return 0
    def display_status(self):
        print(f"Thermostat in {self.location}: {self.current_temp}°C\n Reading count: {len(self.readings)}\n Average temperature: {self.get_average_temp()}°C\n")
    def is_comfortable(self):
        if 20 <= self.current_temp <= 25:
            print("True")
        else:
            print("False")
thermostat1 = Thermostat("Living Room", 22)
thermostat2 = Thermostat("Garage", 10)
thermostat1.set_temperature(26.5)
thermostat1.set_temperature(35)
thermostat1.display_status()
thermostat2.display_status()
thermostat1.is_comfortable()
print(f"\n{Thermostat.device_count}\n")