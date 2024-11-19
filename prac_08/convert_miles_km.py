"""CP1404 - prac_08 - convert miles to kilometres"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
MILE_TO_KM = 1.60934

class ConvertDistance(App):
    """Convert miles to kilometres"""
    output_km = StringProperty()

    def build(self):
        """Construct the app"""
        self.title = "Convert miles to kilometers program"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_km = ""
        return self.root

    def handle_calculate(self, text):
        """Handle calculation (could be button press or other call)."""
        print("handle calculate")
        miles = self.convert_number(text)
        self.convert_mile_to_km(miles)

    def convert_mile_to_km(self, miles):
        """Convert miles to kilometres"""
        self.output_km = str(miles * MILE_TO_KM)

    def handle_increment(self, text, increment):
        """Increase miles by 1"""
        miles = self.convert_number(text) + increment
        self.root.ids.input_number.text = str(miles)

    def convert_number(self, text):
        """Convert text to number"""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertDistance().run()