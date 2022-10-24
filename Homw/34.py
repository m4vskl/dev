myTuple = ("4", "11","20")
listoftuple= list(myTuple)

listoftuple[0] = "41"
listoftuple[1] = "18"
listoftuple[2] = "25"

myTuple= tuple(listoftuple)
print(myTuple)