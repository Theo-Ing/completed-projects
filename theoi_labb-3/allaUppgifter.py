#!/usr/bin/python
# coding=utf-8
import sys

kons = "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM"
vow = "aeiouyåäöAEIOUYÅÄÖ"

def visk(text):
    output = ""
    capital = True #Keeps track of wether letter should be capital.
    for tkn in text:
        if tkn in vow: pass
        elif tkn in ".":
            output += tkn
            capital = True
        elif tkn in " ":
            output += tkn
        else:
            if capital: output += tkn.upper()
            else: output += tkn
            capital = False
    return output

def rovare(text):
  output = ""
  for tkn in text:
    if tkn in kons: output += tkn + "o" + tkn.lower()
    else: output += tkn
  return output

def reverseRov(text):
    output = ""
    rovCounter = 0
    for tkn in text:
        if rovCounter>0:
            rovCounter -= 1
        elif tkn in kons:
            output += tkn
            rovCounter = 2
        else:
            output += tkn
    return output

def all(text):
    for char in text:
        if char in ".,!:;":
            text = text.replace(char, "")
    words = text.lower().split()
    output = ""
    for word in words:
        counter = 0
        consonants = ""
        for char in word:
            if char in vow:
                output += word[counter:] + word[:counter] + "all "
                break
            elif counter == len(word)-1:
                output += consonants + char + "all "
            else:
                counter += 1
                consonants += char
    return output

def bebis(text):
    words = text.lower().split()
    output = []
    for word in words:
        currentWord = ""
        counter = 0
        for char in word:
            if char in vow:
                for i in range(0, 3):
                    currentWord += word[:counter+1]
                break
            else:
                counter += 1
        output.append(currentWord)
    return " ".join(output)

def fikon(text):
    for char in text:
        if char in ".,!:;":
            text = text.replace(char, "")
    words = text.lower().split()
    output = ""
    for word in words:
        counter = 0
        for char in word:
            if char in "åäöÅÄÖ":
                output += "fi" + word[counter + 2:] + word[:counter + 2] + "kon "
                break
            elif char in vow:
                output += "fi"+word[counter+1:]+word[:counter+1]+"kon "
                break
            else: counter+=1
    return output


def main():
    text = sys.stdin.read()
    a = sys.argv[1]
    menu = {}
    menu["-v"] = lambda text: visk(text)
    menu["-r"] = lambda text: rovare(text)
    menu["-b"] = lambda text: bebis(text)
    menu["-a"] = lambda text: all(text)
    menu["-f"] = lambda text: fikon(text)
    print(menu[a](text))

if __name__ == '__main__':
    main()