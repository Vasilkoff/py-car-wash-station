class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
    pass


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.income = 0

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center),
            1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            self.income += self.calculate_washing_price(car)
            car.clean_mark = self.clean_power

    def serve_cars(self, cars_list: list[Car]) -> int:
        for car in cars_list:
            self.wash_single_car(car)

        return self.income

    def rate_service(self, rate: float) -> None:
        self.count_of_ratings += 1
        new_rating = (self.average_rating + (
            rate - self.average_rating
        ) / self.count_of_ratings
        )
        self.average_rating = round(new_rating, 1)

    pass
