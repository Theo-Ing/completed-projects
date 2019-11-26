import sys
import math

def calculate_traingle_area():
    a = int(input("Första sidlängd: "))
    b = int(input("Andra sidlängd: "))
    c = int(input("Tredje sidlängd: "))
    if a+b<c or a+c<b or b+c<a:
        print("This ain't no triangle you dummy!")
        sys.exit()
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area:", area)

def sekund_konverterare():
    sekund = int(input("Hur många sekunder? "))
    restSek = sekund
    dag = 0
    timma = 0
    minut = 0
    if restSek>86400:
        dag = restSek//86400
        restSek = restSek - 86400*dag
    if restSek>3600:
        timma = restSek//3600
        restSek = restSek - 3600*timma
    if restSek>60:
        minut = restSek//60
        restSek = restSek - 60*minut
    print(sekund, "sekunder är lika med:", dag, "dag(ar),", timma, "h,", minut, "min,", restSek, "sekunder")

def siffersumma():
    tal = input("Vilket tal ska siffersumman beräknas till? ")
    total = 0
    for num in tal:
        total += int(num)
    print("Siffersumma:", total)

def harmsum():
    n = int(input("Hur många termer? "))
    summa=0.0
    for i in range(1, n+1):
        summa = summa + (1/i)
    print("Summan är:", summa)

def antal_termer():
    malsumma = float(input("Vilket värde ska summan överskrida? "))
    n = 0
    summa=0
    while malsumma>summa:
        n += 1
        summa += 1/n
    print(n, "stycken termer behövs för att summan ska överskrida", malsumma)

def check_duplicates():
    inputList = input("Give me a list ").split(" ")
    inputList.sort()
    for i in range(len(inputList)-1):
        if inputList[i]==inputList[i+1]:
            print("There is atleast one duplicate!")
            break

def chess_board():
    n=0
    row = 0
    while row < 8:
        n=row
        for i in range (1, 9):
            if n%2==0:
                print("*", end=' ')
            else:
                print(" ", end=' ')
            n += 1
        print()
        row += 1


def menu():
    print("Options")
    print("1: Triangelarea")
    print("2: Sekundkonvertering")
    print("3: Siffersumma")
    print("4: Harmsum")
    print("5: Antal termer")
    print("6: Leta duplicates")
    print("7: Chess")
    print("8: Exit")
    return int(input("Ditt val: "))

while True:
    n = menu()
    if n == 1:
        calculate_traingle_area()
    elif n == 2:
        sekund_konverterare()
    elif n == 3:
        siffersumma()
    elif n == 4:
        harmsum()
    elif n == 5:
        antal_termer()
    elif n == 6:
        check_duplicates()
    elif n == 7:
        chess_board()
    elif n == 8:
        break
    else:
        print(n, "är inte ett giltigt val.")
    print()
#calculate_traingle_area(3, 4, 5)
#sekund_konverterare()
#siffersumma()
#harmsum()
#antal_termer()
