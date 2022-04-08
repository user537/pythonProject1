"""a = 1


def func():
    global a
    a = a + 1
    print(a)

func()
func()
func()
print(a)
"""

myVariable = 1


def addOne(myParameter):
    myParameter += 1
    print(myParameter)


addOne(
    myVariable
)
print(myVariable)
myVariable = 50
addOne(
    myVariable
)
addOne(
    myVariable
)
print(myVariable)