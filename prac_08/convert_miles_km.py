"""CP1404 - prac_08 - convert miles to kilometres"""
from kivy.app import App
from kivy.lang import Builder

class ConvertDistance(App):
    """Convert miles to kilometres"""

    def build(self):
        """Construct the app"""
        self.title = "Convert miles to kilometers program"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_mil_to_km(self):


ConvertDistance().run()