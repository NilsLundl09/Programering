#Alla Räknesätt
print(3 + 4)
tal = (5 - 3)
print( tal / 2)
print(2 * 3)
print( 3 ** 2)
print( 9 // 2)
print()
# ** Betyder upphöjt, // Betyder delat och tar bort decimaler % Resten vid division

Name = input("Skriv ditt namn här:")
Last_Name = input("Skriv ditt efternamn här:")
Age = input("Skriv din ålder här:")
print(Name + " " + Last_Name + "," + " " + Age)
#Miniräknare
X = int(input("Skriv första talet här:"))
Y = int(input("Skriv andra talet här:"))
print("Svar:")
print(X * Y)

#BMI kalkylator
vikt = float(input("Skriv din vikt här (kg):"))
längd = float(input("Skriv din längd här (cm):"))
bmi = vikt / (längd ** 2)
print("Ditt BMI är:")
print(bmi)

#Livet i veckor
ålder = int(input("skriv din ålder:"))
print("Din ålder i veckor är:")
print(ålder * 52)
#Viktomvandlare
kg = float(input("Vikt i kg:"))
print("vikt i lbs:")
print(kg * 2.2046)