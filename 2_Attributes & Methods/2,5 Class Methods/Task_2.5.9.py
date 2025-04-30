class Driver:

    @staticmethod
    def calculate_fuel_costs(distance, fuel, price):
        result = price * (fuel / 100) * distance
        print(round(result, 2))

        # код ниже пожалуйста не удаляйте
vasya = Driver()
vasya.calculate_fuel_costs(3, 7, 50)
vasya.calculate_fuel_costs(100, 7, 50)
vasya.calculate_fuel_costs(50, 7, 50)




