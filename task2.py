# Программа для проверки истинности утверждения not (x V y V z) = not x ⋀ not y ⋀ not z

def is_statement_right(x, y, z):
    return not (x or y or z) == (not x and not y and not z)

predicate_x = str(input("Введите значение предиката X: "))
predicate_y = str(input("Введите значение предиката Y: "))
predicate_z = str(input("Введите значение предиката Z: "))

result = is_statement_right(predicate_x, predicate_y, predicate_z)
if result == True:
    print("Утверждение верно")
else:
    print("Утверждение ложно")








