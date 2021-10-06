#В питоне переменные пишутся в нижнем регистре с андерскорами


"""
Основная инструкция:
#    Вложенный блок инструкций
#Пример:
#if 5 > 2:
# print("Five is greater than two!")
"""

"""
отсновные парадигмы программирования
обьект это сущность, у которой есть атрибуты, может выполнять глаголы
a = 1, где a сущность, 1 атрибут, а глагол где? Или я не пони?
функциональное - сущности и атрибуты, а глаголы отдельно. Нужно с ними позаимодействовать, например C
"""


#python высокоуровневый. Все они основаны на ассемблере

#типы данных:

#изменяемый -

#a = 1
#b = a
# b это ссылка на a, но не в питоне, нам похуй


#>>> a = 1
#>>> id(a)
#5752544744
#>>> a = 1+4
#>>> id(a)
#5752544648
#>>>

# у всех стандартных типов данных есть литерал и функция, приводящая к этому типу данных

a = "123" #обьявили string
a = float(a) #из этой переменной сделали int
#a = int("123") #тоже самое, только одной строкой

#float его литерал - число, с плавающей точкой, делать можно тоже что и с int, его фунуция это float

#boolean - его литералы - True, False, функцией является bool
#print(bool(0))
#print(bool(1))
#print(bool(2)) #все что не 0 - True
#print(bool(""))
#print(bool("qwe"))
#print(bool([]))
#print(bool([1]))
#print(not True)
#print(not False)
#print(True is True)
#print(False is True)
#print(True and True)
#print(False or True)
#print(True or False)
#print(False or False or True)

#string - строка, в питоне не изменяемый тип данных. Литералом строки является ' " '' "" ''' """
#у строк есть форматирование
#print("Hello {}".format("zalupa"))
#print("{} пахнет {}".format("Жасмин", "немытой жопой"))
#print("My age is {}".format(123))

#test = "Hello from {country_name}".format(country_name="Russia")
#print(test)


#template example
#smell_template = "{} пахнет {}"
#print(smell_template.format("Жасмин", "залупой"))

#age = 25
#print(f"my age is {age}")

#print("""
#в
#тройных
#можно
#писать
#многострочно
#""")

#a = 'ssdfg'
#a = "sdfsdf"
#a = '''sdfgsdfgdfsgdsfgdsfgfsg'''
#a = '"'

#a = "Hello"
#b = "World!"
#print(a + " " + b)

#kek
#a = "test "
#b = 2
#print(a * b)

#зачем нужна индексация?
#a = "Hello World!"
#print(a[0])
#print(a[-12])

#срезы
#print("qweqwe"[1:5])
#print("qweqwe"[-5:-1])


#еще есть кортеж - tuple че это вообще за ебатория-тоооооо
fs = ([1,2,3])
print(t)


#Casting - If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

