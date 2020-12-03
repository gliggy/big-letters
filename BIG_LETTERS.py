import cv2
import easygui
carte = cv2.imread("ABCD.png")
#text = "LA VIE EST BONNE"
text = easygui.enterbox("type something.")
for letter in text:
    order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    i = order.index(letter)
    j = (i//6)*10
    i = (i%6)*10
    for y in range(j, j+10):
        row = ""
        for x in range(i, i+10):
            pix = carte[y, x, 0]
            row += letter if pix <1 else " "
        print (row)
