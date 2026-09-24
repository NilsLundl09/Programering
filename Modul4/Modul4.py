word = input("Skriv ditt ord:")
while True:
    print(word)
    word = input("Skriv ditt ord:")
    if word == "q":
        break
print("Avslutade systemet")
time = 0
word = input("Skriv någonting:")
for i in range(10):
    print(word)
print("Skriver ut siffor upp till 10")
for i in range(10):
    print(i+1)
y = int(input("Skriv ett värde:"))
for i in range(y):
    print(i+1)
#System för gångertabell
for i in range(1,13):
    for x in range(1,11):
        print(x * i)

