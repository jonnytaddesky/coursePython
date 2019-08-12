def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count


print(total(10, 4, 7, 1, vegetables=50, fruits=100))

print(10+1+2+3)
print(50+100)
