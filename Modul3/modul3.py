#Höjdcheck för grönalund med try
print("Höjdcheck")
try:
    höjd = int(input("Skriv din höjd (cm):"))
    if höjd >= 140 and höjd <= 195:
        print("Välkommen in")
    else:
        print("Du är för kort/lång. GÅ HEM!")
except ValueError:
    print("Du måste skriva siffror inte tecken. Enhet behövs inte skrivas.")
#BMI kalkylator med try
print("BMI Kalkylator")
try:
    vikt = float(input("Skriv din vikt här (k):"))
    längd = float(input("Skriv din längd här (cm):"))
    bmi = vikt / (längd ** 2)
    print("Ditt BMI är:")
    print(bmi)
except ValueError:
    print("Skriv siffror")
#PROGRAM FÖR RADIEN PÅ EN CIRKEL
print("Ränka ut arean för en cirkel")
try:
    radie = float(input("Skriv radien:"))
    area = radie * radie * 3.14 
    print("Area =", area, "cm²")
except ValueError:
    print("Fel. Du måste använda siffror")
#TÄRNING
print("Kastar en tärning")
import random
dice = random.randint(1,6)
print("Slår tärning...")
print(dice)
#Flera tärningar
try:
    antal = int(input("Välj hur många tärningar du vill kasta:"))
    print("Kastar tärningar...")
    for x in range(antal):
        print(random.randint(1,6))
except ValueError:
    print("Fel, skriv siffror")
print("Slut")