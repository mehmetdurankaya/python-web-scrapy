def exponantion(n):

    def inner(power):
        return n**power
    return inner
two = exponantion(2)
result=two(4)
three = exponantion(3)
print(two(3))
print(three(4))
