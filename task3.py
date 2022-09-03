# Программа, которая принимает на вход координаты точки в системе координат и выдает номер
# четверти плоскости, в которой находится точка
coordinate_x = int(input("Введите координаты точки X: "))
coordinate_y = int(input("Введите координаты точки Y: "))
if coordinate_x > 0 and coordinate_y > 0:
    print(f"- x = {coordinate_x}; y = {coordinate_y} -> 1")
elif coordinate_x < 0 and coordinate_y > 0:
    print(f"- x = {coordinate_x}; y = {coordinate_y} -> 2")
elif coordinate_x < 0 and coordinate_y < 0:
    print(f"- x = {coordinate_x}; y = {coordinate_y} -> 3")
elif coordinate_x > 0 and coordinate_y < 0:
    print(f"- x = {coordinate_x}; y = {coordinate_y} -> 4")
elif coordinate_x == 0 and coordinate_y != 0:
    print(f"Точка с заданными координатами расположена на оси Y")
elif coordinate_x != 0 and coordinate_y == 0:
    print(f"Точка с заданными координатами расположена на оси X")
elif coordinate_x == 0 and coordinate_y == 0:
    print(f"Точка является началом координат (точка O)")