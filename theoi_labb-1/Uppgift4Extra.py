def ramanujan(n):
    lim = int(round(n**(1/3))) #Testar vad största talet är som är under n när det är upphöjt till 3
    a = 0 #Startvärde för a
    solutions = [] #Introducerar en tom lista med lösningar
    while a <= lim: #Loopar tills alla alternativ är testade
        b = int(round((n - a**3)**(1/3))) #Tar differansen av n och a^3, tar sedan kubroten av detta och avrundar till en integer.
        if a <= b: #Motverkar att lösningar dupliceras (tex a=x, b=y och a=y, b=x)
            if a**3 + b**3 == n: #Testar om det givna värdet på b ger ett exakt svar
                solutions.append((a,b)) #Lägger till lösningsparet i listan av lösningar som en tuple
        else: a = lim #Gör a till lim om a>b vilket betyder att inga nya lösningar kommer hittas, while loopen kommer brytas
        a += 1 #Höjer a med 1 för att testa med nya värdet
    print(solutions) #Skriver ut resultat när alla lösningar hittats
