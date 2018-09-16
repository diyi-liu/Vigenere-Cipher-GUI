# Vigenère Cipher Encoder v1.0
from graphics import *
def search(character, string):
    index = []
    for i in range(len(string)):
        if string[i] == character:
            index.append(i)
    return index
    
def encode(plaintext, key):
    plainNoSpace = "".join(plaintext.split(" "))
    length = len(plainNoSpace)
    keylength = len(key)
    cipherNoSpaceList = []
    cipherList = []
    spaceIndex = search(" ", plaintext)
    for i in range(length):
        for l in range(keylength):
            if i % keylength == l:
                cipherNum = ord(plainNoSpace[i]) + eval(key[l])
                if ord(plainNoSpace[i]) == 32:
                    cipherNoSpaceList.append(chr(32))
                elif 65 <= cipherNum <= 90 or 97 <= cipherNum <= 122:
                    cipherNoSpaceList.append(chr(cipherNum))
                else:
                    cipherNoSpaceList.append(chr(cipherNum - 26))
    cipherNoSpace = "".join(cipherNoSpaceList)
    lastj = 0
    for j in range(len(spaceIndex)):
        newStr = cipherNoSpace[lastj:spaceIndex[j]-j] + " "
        cipherList.append(newStr)
        lastj = spaceIndex[j]-j
    cipherList.append(cipherNoSpace[lastj:])
    ciphertext = "".join(cipherList)
    return ciphertext

def getWin(name, width, height):
    win = GraphWin(name, width, height)
    win.setCoords(0, 0, 4.0, 4.0)
    win.setBackground("black")
    return win

def greenText(x, y, text):
    text = Text(Point(x, y), text)
    text.setTextColor("green")
    return text

def greenButton(point, text):
    text = Text(point, text)
    text.setTextColor("green")
    return text

def getEntry(x, y, width):
    entry = Entry(Point(x, y), width)
    return entry

def encoder(response):
    win = getWin("Vigenère Cipher Encoder", 400, 300)
    plainIcon = greenText(1, 3, "Input Plaintext here:")
    plainIcon.draw(win)
    input1 = Entry(Point(3, 3), 20)
    input1.draw(win)
    keyIcon = greenText(1, 2.5, "Input Key here:")
    keyIcon.draw(win)
    input2 = Entry(Point(3, 2.5), 20)
    input2.draw(win)
    rect = Rectangle(Point(1.65, 2), Point(2.35, 1.5))
    rect.setFill("black")
    rect.setOutline("green")
    rectCenter = rect.getCenter()
    rect.draw(win)
    encodeIcon = greenButton(rectCenter, "Encode")
    encodeIcon.draw(win)
    cipherIcon = Text(Point(1, 1), "Ciphertext:")
    cipherIcon.setTextColor("green")
    cipherIcon.draw(win)
    while response == "Y":
        win.getMouse()
        plaintext = input1.getText()
        key = input2.getText()
        output = greenText(3, 1, encode(plaintext, key))
        output.draw(win)
        encodeIcon.undraw()
        resetIcon = greenButton(rectCenter, "Reset")
        resetIcon.draw(win)
        continueIcon = greenText(1, 0.5, "Encode another message? Y/N: ")
        continueIcon.draw(win)
        continueEntry = getEntry(3, 0.5, 5)
        continueEntry.draw(win)
        win.getMouse()
        response = continueEntry.getText()
        output.undraw()
        resetIcon.undraw()
        encodeIcon.draw(win)
        input1.undraw()
        input2.undraw()
        input1 = getEntry(3, 3, 20)
        input2 = getEntry(3, 2.5, 20)
        input1.draw(win)
        input2.draw(win)
        continueIcon.undraw()
        continueEntry.undraw()
    plainIcon.undraw()
    input1.undraw()
    keyIcon.undraw()
    input2.undraw()
    rect.undraw()
    resetIcon.undraw()
    encodeIcon.undraw()
    cipherIcon.undraw()
    continueIcon.undraw()
    continueEntry.undraw()
    thanks = Text(Point(2, 2), "Thanks for Using!")
    thanks.setTextColor("green")
    thanks.setSize(20)
    thanks.draw(win)
    win.getMouse()
    win.close()

def main():
    encoder("Y")

main()
