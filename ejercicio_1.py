print("Por favor ingresa la cadena de texto: ")
sentence = input()
array = sentence.split(",")

newSentence = []
newSentenceString = ""

for x in range (0, len(array)):
    indexWord = array[x]
    indexWord = indexWord.strip()
    if "ca_" in indexWord:
        newIndexWord = indexWord.replace("ca_", "")
        newSentence.append(newIndexWord.upper());
    else:
        newSentence.append(indexWord);

for x in range (0, len(newSentence)):
    newSentenceString = newSentenceString + newSentence[x]
    if x != len(newSentence)-1:
        newSentenceString = newSentenceString + ", "

print("Sentencia original: " + sentence)
print("Sentencia modificada: " + newSentenceString)





    

