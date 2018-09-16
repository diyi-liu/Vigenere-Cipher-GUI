from graphics import *
def decode(ciphertext, key):
    length = len(ciphertext)
    keylength = len(key)
    plainlist = []
    for i in range(length):
        for l in range(keylength):
            if i % keylength == l:
                plainNum = ord(ciphertext[i]) - eval(key[l])
                if 65 <= plainNum <= 90 or 97 <= plainNum <= 122:
                    plainlist.append(chr(plainNum))
                else:
                    plainlist.append(chr(plainNum + 26))
    plaintext = "".join(plainlist)
    return plaintext

def decoder():
    win = GraphWin("Vigenere Cipher Decoder", 400, 300)
    win.setCoords(0, 0, 4.0, 4.0)
    win.setBackground("black")
    cipherIcon = Text(Point(1, 3), "Input Ciphertext here:")
    cipherIcon.setTextColor("green")
    cipherIcon.draw(win)
    input1 = Entry(Point(3, 3), 20)
    input1.draw(win)
    keyIcon = Text(Point(1, 2.5), "Input Key here:")
    keyIcon.setTextColor("green")
    keyIcon.draw(win)
    input2 = Entry(Point(3, 2.5), 20)
    input2.draw(win)
    rect = Rectangle(Point(1.65, 2), Point(2.35, 1.5))
    rect.setFill("black")
    rect.setOutline("green")
    rectCenter = rect.getCenter()
    rect.draw(win)
    decodeIcon = Text(rectCenter, "Decode")
    decodeIcon.setTextColor("green")
    decodeIcon.draw(win)
    plainIcon = Text(Point(1, 1), "Plaintext:")
    plainIcon.setTextColor("green")
    plainIcon.draw(win)
    win.getMouse()
    ciphertext = input1.getText()
    key = input2.getText()
    output = Text(Point(3, 1), decode(ciphertext, key))
    output.setTextColor("green")
    output.draw(win)
    decodeIcon.undraw()
    clearIcon = Text(rectCenter, "Clear")
    clearIcon.setTextColor("green")
    clearIcon.draw(win)
    i = 0
    while i in range(1):
        win.getMouse()
        clearIcon.undraw()
        output.undraw()
        decodeIcon = Text(rectCenter, "Decode")
        decodeIcon.setTextColor("green")
        decodeIcon.draw(win)
        win.getMouse()
        ciphertext = input1.getText()
        key = input2.getText()
        output = Text(Point(3, 1), decode(ciphertext, key))
        output.setTextColor("green")
        output.draw(win)
        decodeIcon.undraw()
        clearIcon = Text(rectCenter, "Clear")
        clearIcon.setTextColor("green")
        clearIcon.draw(win)
        
decoder()
