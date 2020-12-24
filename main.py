import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):    # Holds all of our design elements
    def __init__(self, **kwargs):  # **kwargs defines that we can take as many arguments as we want
        super(MyGrid, self).__init__(**kwargs)
        self.inside = GridLayout()  # Creating a new layout (or frame in tkinter) so we can center the submit button
        self.inside.cols = 2  # Number of columns - Every one of those exists in default kivy or APP

        self.inside.add_widget(Label(text="Name:  "))  # Adds a widget like in tkinter
        self.name = TextInput(multiline=False)  # Input of the widget + Stay in one line
        self.inside.add_widget(self.name)  # Run the widget

        self.inside.add_widget(Label(text="Last name:  "))  # Last name widget
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Email:  "))  # Email widget
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.inside.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline=False)
        self.inside.add_widget(self.password)

        self.add_widget(self.inside)
        self.cols = 1

        self.submit = Button(text="Submit", font_size=40)  # Submit button
        self.submit.bind(on_press=self.pressed)  # When pressed do this function
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text  # access the context of the input
        last = self.lastName.text
        email = self.email.text

        print("Name:", name, "Last name: ", last, "Email: ", email)
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""

    def check_pass(self, instance):
        password = self.passowrd.text
        if len(password) > 6:
            pass
            




class MyApp(App):  # Allows us to build the window + graphics
    def build(self):  # The main interface
        return MyGrid()


if __name__ == "__main__":
    MyApp().run() 
