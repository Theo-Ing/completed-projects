n = int(input("Vilket tal ska kubsummor hittas till? ")) #Introducerar talet vi vill hitta kubsummor till
wantedSolutions = int(input("Hur många lösningar söker du? "))
lim = int(n**(1/3)) #Testar vad största talet är som är under n när det är upphöjt till 3
a = 0 #Startvärde för a
solutionCounter = 0 #Räknar antalet lösningar som hittats
while a <= lim: #Loopar tills alla alternativ är testade
    b = int(round((n - a**3)**(1/3))) #Tar differansen av n och a^3, tar sedan kubroten av detta och avrundar till en integer.
    if a <= b: #Motverkar att lösningar dupliceras (tex a=x, b=y och a=y, b=x)
        if a**3 + b**3 == n: #Testar om det givna värdet på b ger ett exakt svar
            print("a =", a, "& b =", b)
            solutionCounter += 1
            if solutionCounter == wantedSolutions:
                break #Bryter while loopen tidigt om önskat antal lösningar har hittats

    if a == lim: #Informerar om antalet lösningar som hittades när sista genomgången av while loopen är gjord om inte önskat antal lösningar hittades.
        if solutionCounter==0:
            print("Inga lösningar hittades")
        else:
            print("Endast", solutionCounter, "lösning(ar) hittades")
    a += 1 #Höjer a med 1 för att testa med nya värdet
