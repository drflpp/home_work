class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)

rect_1 = Rectangle(1, 5)
rect_2 = Rectangle(3, 5)
rect_3 = Rectangle(4, 4)

for el in [rect_1, rect_2, rect_3]:
    print('Area:', el.area(), "Perimeter:", el.perimeter())


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return a + b
    def multiplication(self):
        return a*b
    def division(self):
        return a/b
    def subtraction(self):
        return a - b

class Button:
    def __init__(self, text, loc = None):
        self.text = text
        self.loc = loc
    def click(self):
        print(f'Клик по кнопке {self.text}')

text_box = Button('Text Box')
check_box = Button('Check Box')
radio_button = Button('Radio Button')
web_tables = Button('Web Tables')
buttons = Button('Buttons')
links = Button('Links')
broken_links_images = Button('Broken Links - Images')
upload_and_download = Button('Upload and Download')
dynamic_properties = Button('Dynamic Properties')

for el in [text_box, check_box, radio_button,
           web_tables, buttons, links,
           broken_links_images, upload_and_download, dynamic_properties]:
    el.click()

class Car:

    def __init__(self, color = None, type=None, year=None):
        self.color = color
        self.type = type
        self.year = year

    def start_car(self):
        print('Автомобиль заведен')
    def turning_car_off(self):
        print('Автомобиль заглушен')
    def set_color(self, color):
        self.color = color
        print(f'Цвет автомобиля изменен на {self.color}')
    def set_yaer(self, year):
        self.year = year
        print(f'Год выпуска автомобиля изменен на {self.year}')
    def set_type(self, type):
        self.type = type
        print(f'Тип автомобиля изменен на {self.type}')

car = Car()
car.start_car()
car.set_color('blue')

