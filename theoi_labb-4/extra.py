def txt_to_list(txt):
    '''Opens a text file and returns a list of all words in the file.'''
    with open(txt, encoding = 'utf8') as f:
        txtFile = f.read()
    return txtFile.split()

LIST = txt_to_list("ordlista.txt")

def lin_search(v, target):
    '''Returns True if the list v contains target and False otherwise.'''
    for word in v:
        if target == word:
            return True
    return False

def br_search(v, target):
    """Returns True if the sorted list v contains target and False otherwise.
    Undefined behaviour if v is not sorted"""
    hi = len(v) - 1
    mid = hi//2
    if hi < 0:
        return False
    if v[mid] < target:
        return br_search(v[mid+1:hi+1], target)
    elif v[mid] > target:
        return br_search(v[0:mid], target)
    else: return True

def search_kup(source, function):
    '''Returns a string of all words that have a "kupering"
    and its "kuperingar" in the sorted list v, separated by "/".
    Undefined behaviour if v is not sorted'''
    words = source[0:] #Creates a clone of list so that we can remove objects from it without ramifications
    for element in words:
        foundPair = False
        matches = [element]
        for i in range (1,5):
            kup = element[i:] + element[:i]
            if function(words, kup):
                matches.append(kup)
                words.remove(kup) #Removes the found pair in order to avoid duplicates
                foundPair = True
        if foundPair:
            print("/".join(matches))

def kup_menu():
    '''Menu for Kupering'''
    menu2 = {}
    menu2["1"] = [lambda: search_kup(LIST, lin_search), "Linear search"]
    menu2["2"] = [lambda: search_kup(LIST, br_search), "Binary search"]
    for x in menu2.keys(): print(x + ":", menu2[x][1])
    choice = input("> ")
    menu2[choice][0]()
    print()

def riffle_help(deck):
    '''Returns a perfect riffle shuffle of given deck'''
    firstHalf = 0
    secondHalf = len(deck)//2
    deckAfterShuffle = []
    for i in range(0,len(deck)//2):
        deckAfterShuffle.append(deck[firstHalf])
        deckAfterShuffle.append(deck[secondHalf])
        firstHalf += 1
        secondHalf += 1
    return deckAfterShuffle

def check_sort(li):
    '''Checks if li is sorted and returns "True" if it is, false otherwise.'''
    if len(li) <= 1:
        return True
    return li[0] <= li[1] and check_sort(li[1:])

def riffle():
    '''Counts how many riffle shuffles are necessary
    in order for the deck to return to original state'''
    cards = int(input("How many cards in the deck (even)? "))
    if cards%2 != 0:
        print("Not an even integer!")
        print()
        return
    deck = list(range(cards))
    counter = 0
    while True:
        shuffled = riffle_help(deck)
        counter += 1
        #print(shuffled)
        if check_sort(shuffled):
            print(counter, "shuffles are necessary to return to the decks original state.")
            break
        else: deck = shuffled


def main():
    menu={}
    menu["1"] = [lambda: kup_menu(), "Kup search"]
    menu["2"] = [lambda: riffle(), "Riffle shuffle"]
    while True:
        for x in menu.keys(): print(x + ":", menu[x][1])
        print("3: Exit")
        choice = input("> ")
        if choice == "3":
            break
        else:
            menu[choice][0]()
        print()

if __name__ == '__main__':
    main()