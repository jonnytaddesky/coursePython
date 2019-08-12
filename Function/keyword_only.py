def total(initial=5, *numbers, extra_number):
    count = initial
    for nubmer in numbers:
        count += nubmer
    count += extra_number
    print(count)


total(10, 1, 2, 3, extra_number=50)
