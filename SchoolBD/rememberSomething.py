print("Я ПОДЕБИЛ ЭТОТ ПИТОН " + "ВОНЮЧИЙ " "НА ИЗЯН") #конкатенация, т.е. сложение строк
print("Я ПОДЕБИЛ ЭТОТ ПИТОН {} НА ИЗЯН".format("ВОНЮЧИЙ")) #форматирование

print("Name = {}, Surname = {} ".format("Vasyan","Petrosyan"))
print("Name = {}, Surname = {} ".format("Vasyan","Petrosyan","Huesyan"))

def check1(num):
    if num.strip().isdigit():
        print("The Input is Number")
    else:
        print("The Input is string")
x = (input("Enter your age:"))
check1(x)