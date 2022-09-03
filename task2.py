# Программа для проверки истинности утверждения not (x V y V z) = not x ⋀ not y ⋀ not z

def statement_check(x, y, z):
    first_statement = not (x or y or z)
    second_statement = not x and not y and not z
    if first_statement == second_statement:
        statement = True
    else:
        statement = False
    return statement

predicate_x = str(input("Введите значение предиката X: "))
predicate_y = str(input("Введите значение предиката Y: "))
predicate_z = str(input("Введите значение предиката Z: "))

result = statement_check(predicate_x, predicate_y, predicate_z)
if result == True:
    print("Утверждение верно")
else:
    print("Утверждение ложно")








