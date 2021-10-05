class RequestDTO:
    def __init__(self,username,password):
        self.username = username
        self.password = password
def handler(request:RequestDTO):
    return f"{request.username}'s password is {request.password}"
print(handler(RequestDTO("sdfsdfsfdg","sdfdsfsdf")))

#data transfer object

#стандартные типы данных
#приколы для создания пользовательских типов данных
#изучить работу с функциями


class zapros:
    def __init__(self,a,b):
        self.a = a
        self.b = b
zapros_instance = zapros("https://pepyaka.ru", "1.1.0.1")
print(zapros_instance.a)
print(zapros_instance.b)