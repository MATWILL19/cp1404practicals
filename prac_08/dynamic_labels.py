"""CP1404 - prac_08 - dynamic labels"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Dynamically create a list of labels from a list of strings"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ("Anton","Bruno","Caesar","Dora","Emil")

    def build(self):
        """Construct the app"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a list of labels from a list of strings"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
