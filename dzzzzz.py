#1 Задание
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def __str__(self):
#         return (f"Это {self.brand}, {self.model}, {self.year}-года")
# car1 = Car("Kia", "Ceed", 2014)
# car2 = Car("Toyota", "Supra", 1993)
# print(car2)

#2 Задание
# class Book:
#     def __init__(self, author, name, year):
#         self.author = author
#         self.name = name
#         self.year = year
#     def __str__(self):
#         return (f" Это {self.author}, {self.name}, {self.year}-года")
# book1 = Book("Lev_Tolstoy", "War_and_peace", 1863)
# book2 = Book("Dostoevskiy", "Prestuplenie_i_Nakazanie", 1866)
#print(book1)
#print(book2)


#3 Задание
class Stadium:
    def __init__(self, name, city,):
        self.city = city
        self.name = name
    def __str__(self):
        return (f"Это {self.name}, в городе {self.city}")
stadium1 = Stadium("Ak_Bar_Arena", "Kazan")
stadium2 = Stadium("Luzhniki", "Moscow")
print(stadium1, stadium2)