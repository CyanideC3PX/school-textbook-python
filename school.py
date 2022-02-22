#Programme-1 print

x = 12
y = 45

print(x)
print(y)

#Programme-2 sum

a = 23
b = 420
sum = a + b

print(sum)

#Programme-3 peri and area of circle

#2 pi r & pi r^2

r = int((input("The radius of circle: ")))
pi = float(3.14)

areaofcircle = float((pi * r * r))
print(areaofcircle)

radius = int((input("Put your radius for perimeter: ")))
perimeterofcircle = float(2 * pi * r)
print(perimeterofcircle)

#Programme-4 Simple intrest

#prt/100

principle = int((input("Input your principle: ")))
rate = float((input("Input your rate in '%': ")))
time_period = float((input("Input your time period in years: ")))

S_I = float((principle*rate*time_period)/100)

print(S_I)

#Programme-5 sum with input

number1 = float((input ("number1: ")))
number2 = float((input("number2: ")))

sum2 = number1 + number2 #Can't have another variable as sum, as it would overrite and create a mess

print("sum of {0} and {1} is: {2}" .format(number1, number2, sum2))

#Programme-6 Heroines formula triangle area

side1 = int((input("Input side1: ")))
side2 = int((input("Input side2: ")))
side3 = int((input("Input side3: ")))

semi_perimeter = int((side1 + side2 + side3)/2)

area_of_triangle = float((semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))) ** 0.5

print(area_of_triangle)

#Programme-7 interchange values of variables

c = int(input("Enter value for c: "))
d = int(input("Enter value for d: "))
e = (int())

e = c
c = d
d = e

print("Value of c and d is {0} and {1}" .format(c, d))


#Programme-8 volume of cylinder pi * r**2 * h

height = float(input("Input height for cylinder: "))
radius_cylinder = float(input("Input your radius for cylinder"))

cylinder_volume = float(pi * radius_cylinder ** 2 * height)

print(cylinder_volume)
