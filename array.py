#array - список имеющий заранее определенную длинну. Нужно для сохранения памяти. Но не в питоне

#set - список. Литералы:
[]
[1]
[1,2,3]
["1","a","c"]
[[1,2,3],2,8]

#Операции со списками:
#Сложение:
A = [1,2,3] +[1,2,3]
print(A)
#Умножение - результат, список, повторяемый на сколько его умножили
B = [1,2,3] * 3
print(B)

#Методы списков:
#Индексы - обращение по индексам. Ответ - элемент. Индекс - число в квадратных скобках.
C = [1,2,3]
print(C[1])
print(C[-1])
#Пример: У меня есть список из пользователей
A = ["Васян","Петян","Лёха"]
print(A[0])
#Пример -  написал массив, список продуктов.
grossery_list = ["Мазик", "Кепчук", "Дошик", "Энергетик"]
grossery_list[0] += "+"
grossery_list[-2] += "+"
print(grossery_list)

#Пример - удаление, добавление элементов:
for_smoking = ["tobako", "gum", "filters"]
del for_smoking[0]
del for_smoking[1]
for_smoking.append("weed")
for_smoking.append("tobako")
for_smoking.append("gum")
#У нас питон, у нас списки, а не массивы, вообще поебать
print(for_smoking)

#Добавить сразу дохуя:
for_smoking = ["tobako", "gum", "filters"]
for_smoking.extend([1,2,3])
for_smoking.append(["odin","dva"])
#Обращение к вложенному списку, к его конкретному элементу
print(for_smoking[-1][1])
#удалит весь список
del for_smoking[6]
print(for_smoking)

#Метод pop
fruits = ["banana","mango", "apple", "watermelon"]

#pop - удаляет и возвращает удаленный элемент
print(fruits.pop())
print(fruits)

#pop может принимать аргумент - индекс(если говорить о списках)
print(fruits.pop(1))
print(fruits)
#Шо там у нас осталось?
print(len(fruits))

#string - по алфавиту, int - от меньшего к большему
fruits.sort()
print(fruits)

numbers = [1, 3, 9, 7]
#Вызываем метод sort у списка
numbers.sort()
print(numbers)
#Вызываем встроенную функцию sorted, в которую передаем список
print(sorted(numbers))

#Слайсинг
#нихуя не включительно, а по-другому
print(numbers[0:1])
print(numbers[0:-2])
print(numbers[0:2])

#Генератор списков
weapons = ["melee", "shotgun", "rifle", "handgun"]
print([gun*2 for gun in weapons])
print(["Today's gun is {}".format(g) for g in weapons])
#БЛЯЯЯЯЯЯЯЯ
print([g for g in weapons if "shot" in g])
print([g for g in weapons if "gun" in g])

print(["Today's gun is {}".format(g) for g in weapons if "shot" in g])

#Фильтрация функциональным способом:
#print(list(filter()))

#Можно 'распаковать' список
weapons = ["melee", "shotgun", "rifle", "handgun"]
a, b, c, d = weapons
print(c)