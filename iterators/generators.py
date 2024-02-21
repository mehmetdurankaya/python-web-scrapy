# def cube():
#
#     for i in range(5):
#         yield i**3
#
# for i in cube():
#     print(i)
# liste= [i**3 for i in range(5)]

generator= (i**3 for i in range(5))
for i in generator:
    print(i)