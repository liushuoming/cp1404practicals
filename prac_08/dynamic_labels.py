
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

class NameListApp(App):
    def build(self):
        return Builder.load_file("dynamic_labels.kv")

    def load_names(self):
        names = ["Alice", "Bob", "Charlie", "Diana"]
        box = self.root.ids.names_box
        box.clear_widgets()  # Optional: clear previous entries
        for name in names:
            box.add_widget(Label(text=name))

    def clear_names(self):
        self.root.ids.names_box.clear_widgets()

if __name__ == "__main__":
    NameListApp().run()
