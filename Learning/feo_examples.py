# ---пример 1, глобальная переменная в функции
myVariable = 1


def addOne():
    global myVariable
    myVariable += 1
    print(myVariable)


addOne()
print(myVariable)
myVariable = 50
addOne()
addOne()
print(myVariable)
# ---пример 2, объявление переменной в функции
myVariable = 1


def addOne():
    myVariable = 1
    myVariable += 1
    print(myVariable)


addOne()
print(myVariable)
myVariable = 50
addOne()
addOne()
print(myVariable)
# ---пример 3, передача параметра функции
myVariable = 1


def addOne(myParameter):
    myParameter += 1
    print(myParameter)


addOne(myVariable)
print(myVariable)
myVariable = 50
addOne(myVariable)
addOne(myVariable)
print(myVariable)