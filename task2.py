# Программа для проверки истинности утверждения not (x V y V z) = not x ⋀ not y ⋀ not z

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f"{x} {y} {z} {not (x or y or z) == (not x and not y and not z)}")







