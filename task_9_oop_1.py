from task_9_checks import Checks
class Input(Checks):

    def __init__(self,loc, text):
        self.loc = loc
        self.text = text

search = Input('at home', 'yandex')

print(search.loc)

class Button(Checks):
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
menu = Button('at header', 'menu')

class Title(Checks):

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
discount = Title('at main', '25% off')

class Link(Checks):
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
next_page = Link('down', '>>')

print(menu.loc, '--', menu.text)

class Page(Checks):

    def __init__(self, url):
        self.url = url

    def get(self):
        return self.url
home = Page("\my_computer\my_folder\my_file")

print(home.get())

class Soda:
    def __init__(self, adding = None):
        self.adding = adding
    def show_my_drink(self):
        if self.adding:
            print(f"Soda and {self.adding}")
        else:
            print('Just Soda')

s_soda = Soda('strawberry')
soda = Soda()

print(soda.show_my_drink(), s_soda.show_my_drink())

for el in [search, menu, discount, next_page]:
    print(el.check_text())