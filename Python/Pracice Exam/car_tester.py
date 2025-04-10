from car import Car

def tester(filename):
    cars_list = []
    with open(filename) as file:
        for line in file:
            data = line.strip().split()
            if len(data) ==4:
                color, engine_type, gas_tank, odometer = data
                car = Car(color, engine_type, int(gas_tank), int(odometer))
                cars.append(car)

    return cars_list

cars = tester("cars.txt")

for car in cars:
        print(car)

