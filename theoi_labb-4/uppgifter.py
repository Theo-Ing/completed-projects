#Uppgift1
def txt_to_list(txt):
    '''Opens a text file and returns a list of all words in the file.'''
    with open(txt, encoding = 'utf8') as f:
        txtFile = f.read()
    return txtFile.split()

# Uppgift1
LIST = txt_to_list("ordlista.txt")

#Uppgift2
def lin_search(v, target):
    '''Returns True if the list v contains target and False otherwise.'''
    for word in v:
        if target == word:
            return True
    return False

#Uppgift3
def lin_search_kup(source):
    '''Returns a string of all words that have a "kupering"
    and its "kuperingar" in the sorted list v, separated by "/".
    Undefined behaviour if v is not sorted'''
    words = source[0:]  # Creates a clone of list so that we can remove objects from it without ramifications
    for element in words:
        foundPair = False
        matches = [element]
        for i in range(1, 5):
            kup = element[i:] + element[:i]
            if lin_search(words, kup):
                matches.append(kup)
                words.remove(kup)  # Removes the found pair in order to avoid duplicates
                foundPair = True
        if foundPair:
            print("/".join(matches))

#Binärsökning
def bin_search(li, x):
    '''Returns True if the sorted list li contains x and False otherwise.
    Undefined behaviour if v is not sorted'''
    x = x.lower()
    lo = 0
    hi = len(li)-1
    while lo <= hi:
        mid = (lo+hi)//2
        print(li[mid])
        #print(hi-lo)
        if x < li[mid]:
            hi = mid - 1
        elif x > li[mid]:
            lo = mid + 1
        else:
            return True
    return False

#Uppgift5
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

def br_search_kup(source):
    '''Returns a string of all matches to target
    and its "kuperingar" in the sorted list v, separated by "/".
    Undefined behaviour if v is not sorted'''
    words = source[0:] #Creates a clone of list so that we can remove objects from it without ramifications
    for element in words:
        foundPair = False
        matches = [element]
        for i in range (1,5):
            kup = element[i:] + element[:i]
            if br_search(words, kup):
                matches.append(kup)
                words.remove(kup) #Removes the found pair in order to avoid duplicates
                foundPair = True
        if foundPair:
            print("/".join(matches))

def uppgift_2():
    '''Function for task 2'''
    while True:
        element = input("Uppgift 2: Ditt ord (skriv 'quit' för att avsluta): ")
        if element == "quit": break
        if lin_search(LIST, element.lower()):
            print(element + " finns!")
        else:
            print(element + " finns ej :(")
    print()

def uppgift_3():
    '''Function for task 3'''
    lin_search_kup(LIST)
    print()

def uppgift_4():
    '''Function for task 4'''
    while True:
        element = input("Uppgift 4: Ditt ord (skriv 'quit' för att avsluta): ")
        if element == "quit": break
        if bin_search(LIST, element):
            print(element + " finns!")
        else:
            print(element + " finns ej :(")
    print()

def uppgift_5():
    '''Function for task 5'''
    while True:
        element = input("Uppgift 5: Ditt ord (skriv 'quit' för att avsluta): ")
        if element == "quit": break
        if br_search(LIST, element):
            print(element + " finns!")
        else:
            print(element + " finns ej :(")

def uppgift_6():
    '''Function for task 6'''
    br_search_kup(LIST)
    print()

def binsok_calc(i):
    '''Gives minimum and maximum number of searches in a list of length i
    needed to find wether an element is contained in the list with the
    help of binary searching'''
    counter = 0
    while i > 0:
        i = i//2 - 1
        counter += 1
    print("Antal sökningar: min = 1, max =", counter)

def main():
    # uppgift_2()
    #uppgift_3()
    # uppgift_4()
    binsok_calc(2510)
    # uppgift_5()
    #uppgift_6()

if __name__ == '__main__':
    main()