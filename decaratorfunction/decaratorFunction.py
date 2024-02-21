def my_decorator(func):
    def wrapper():
        print("fonksiyondan önceki işlemler")
        func()
        print("fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator
def sayHello():
    print("Hello")
@my_decorator
def sayGreeting():
    print("greeting")

sayHello()