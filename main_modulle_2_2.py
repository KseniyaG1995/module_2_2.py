first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
thrid = int(input('Введите третье число: '))

if first == second and second == thrid and first == thrid:
    print(3)
elif first == second or second == thrid or first == thrid:
    print(2)
else:
    print(0)