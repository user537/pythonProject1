#множественное присваивание значений aka распаковка кортежа
x, y = (1, 5.6)
print(x,y)

#булев boolean тип данных принимает два возможных значения - true, false
my_true = True
my_false = False
print(type(my_true))

# функции, которые приводят значения к указанному типу:
# str() int() float() bool()

x = float(x)
print(x, type(x))

# не округляет, а отбрасывает дробную часть!
y = int(y)
print(y, type(y))

# привести к строке
y = str(y)
print(y, type(y))

# а шо будет?
# 0 это ложь, вранье и провокация
y = bool(y)
print(y, type(y))