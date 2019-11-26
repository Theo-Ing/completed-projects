import allaUppgifter

if __name__ == '__main__':
    menu = {}
    menu["1"] = [lambda text: allaUppgifter.visk(text), "Viskspråket"]
    menu["2"] = [lambda text: allaUppgifter.rovare(text), "Rövarspråket"]
    menu["3"] = [lambda text: allaUppgifter.reverseRov(text), "Röversätt"]
    menu["4"] = [lambda text: allaUppgifter.bebis(text), "Bebisspråket"]
    menu["5"] = [lambda text: allaUppgifter.all(text), "Allspråket"]
    menu["6"] = [lambda text: allaUppgifter.fikon(text), "Fikonspråket"]
    while True:
        for x in menu.keys(): print(x + ":", menu[x][1])
        print("7: Avsluta program")
        choice = input("> ")
        if choice == "7":
            break
        else:
            print(menu[choice][0](input("Text: ")))
        print()