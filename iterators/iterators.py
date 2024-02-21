liste=[1,2,3,4,5]
iterator= iter(liste)

while True:
    try:
        element=next(iterator)
        print(element)
    except StopIteration:
        break