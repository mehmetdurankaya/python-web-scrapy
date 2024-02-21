def greeting(name):
    print("hello",name)

# print(greeting("Mehmet Duran Kaya"))
# print(greeting) # bellekteki adresi: 0x0000020C72FEA020

sayHello= greeting
# print(sayHello) # 0x00000195776BA020
# print(greeting) # 0x00000195776BA020

# del sayHello
# print(greeting) # 0x000001D87AD4A020 sayHello silindi ancak adres silinmedi

# encapsulation
# def outer(num1):
#     print("outer")
#     def inner_increment(num1):
#         print("inner")
#         return num1 + 1
#     num2=inner_increment(num1)
#     print(num1,num2)
# outer(10)

# inner_factorial() fonksiyonu factorial() fonksiyonu ile çağrılabiliyor
def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")
    if not number >=0:
        raise ValueError("number must be zero or positive")
    def inner_factorial(number):
        if number<= 1:
            return 1
        return number * inner_factorial(number-1)
    return inner_factorial(number)
try:
    print(factorial(5))
except Exception as ex:
    print(ex)


# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print (factorial(5))

