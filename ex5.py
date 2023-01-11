# 5 Создать класс Animal и определить в нем метод make_a_sound(). Метод должен вывоводить
# строку "Издает звук"
# Cоздать классы Cat и Dog с методами scratch() и dig() соответственно.
# Метод scratch должен выводить строку "Царапать мебель".
# Метод dig должен выводить строку "Рыть землю".
# в классах Cat и Dog переопределите метод make_a_sound() базового класса Animal.
# (Cat: make_a_sound() -> '<...>', Dog: make_a_sound() -> '<...>')

class Animal:
    def make_a_sound(self):
        print('Издаёт звук')


class Cat(Animal):
    def make_a_sound(self):
        return 'Мяу-Мяу'

    def scratch(self):
        return ('Царапать мебель')


class Dog(Animal):
    def make_a_sound(self):
        return 'Гав-гав'

    def dig(self):
        return 'Рыть землю'


animal = Animal()
cat = Cat()
dog = Dog()


animal.make_a_sound()
print(f'Cat: {cat.make_a_sound()} {cat.scratch()}')
print(f'Dog: {dog.make_a_sound()} {dog.dig()}')



