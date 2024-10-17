try:
    a = "10"
    b = 10
    print(a+b)
except TypeError:
    print("Valores não compatíveis.")
else:
    pass

try:
    a = 10
    b = 0
    div = a/b
    print(div)
except ZeroDivisionError:
    print("Valor impossível")
else:
    pass
