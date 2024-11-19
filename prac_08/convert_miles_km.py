"""CP1404 - prac_08 - convert miles to kilometres"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class ConvertDistance(App):
    """Convert miles to kilometres"""
    output_km = StringProperty()

    def build(self):
        """Construct the app"""
        self.title = "Convert miles to kilometers program"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_km = "Convert miles to kilometers"
        return self.root

    def convert_mil_to_km(self):
        """Convert miles to kilometres"""
        self.root.ids.output_label.text = f"{self.root.ids.input_number.text}"

    def handle_increment(self, text, increment):
        """Increase miles by 1"""
        miles = self.convert_mil_to_km(text) + increment

    def convert_number(text):
        """Convert text to number"""
        try:
            return int()


ConvertDistance().run()