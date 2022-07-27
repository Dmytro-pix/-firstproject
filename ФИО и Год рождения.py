fio = input("Ведите ваше ФИО: ")
year = int(input("Введите ваш год рождения: "))
print("ФИО:",fio,"\nГод рождения:",year)
age = 2022 - year
v = int(input("У вас уже был ДР в етом году?\n1)да\n2)нет\nВаш выбор:  "))
if v == 2 and year > 1935 and year < 2023:
    print("Вам",age,"лет")
elif v == 2 and year > 1935 and year < 2023:
    print("Вам",age-1,"лет")
else:
    print("Вы рептилойд")
pol = input("Введите ваш пол: ")
print("Пол:",pol)
country = input("Введите вашу страну прожывания :  ")
phone = input("Ведите ваш номер тл.:  ")
print("Номер тл:",phone)
