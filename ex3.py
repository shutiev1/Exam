# 3 Создайте класс IceCream (для заказа мороженого с добавкой или без),
# принимающий 1 аргумент при инициализации (отвечающий за добавку к мороженому).
# В этом классе реализуйте метод info_about_icecream(), выводящий на печать «Мороженное и {ДОБАВКА}»
# в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое».

class IceCream:
    def __init__(self, dobavka):
            self.dobavka = dobavka

    def info_about_icecream(self):
        if self.dobavka:
            print(f"Мороженное и {self.dobavka}")
        else:
            print('Обычное мороженное')


a = IceCream(None)
a.info_about_icecream()



