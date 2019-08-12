def func_outer():
    x = 2
    print('x equals', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('local x change to', x)


func_outer()
