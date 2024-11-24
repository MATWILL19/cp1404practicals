from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a fancy taxi object"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialize a fancy txi instance"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def get_fare(self):
        """Get the price of a current fare"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string with the taxi model, fuel, odometer"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
