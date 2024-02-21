# def authStatus(page):
#
#     def inner(role):
#         if role=="Admin":
#             return"{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz.".format(role, page)
#     return inner
# user1=admin_user=authStatus("Product Edit")
# print(user1("User"))

def process(process_name):
    def total(*args):
        result = 0
        for i in args:
            result += i
        return result

    def multiplication(*args):
        result = 1
        for i in args:
            result *= i
        return result

    if process_name == "total":
        return total
    else:
        return multiplication


total = process("total")
print(total(1, 3, 5, 7, 9))

multiplication=process("multiplication")
print(multiplication(1,3,5,6,7))
