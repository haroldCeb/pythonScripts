print("Por favor ingresa la cadena de texto: ")
sentence = input()
array = sentence.split(" ")

key_list = []
value_list = []

for x in range (0, len(array)):
    word = array[x]
    word = word.strip()

    chars = len(word)
    key_list.append(chars)

    if(chars % 2 == 0):
        value_list.append(True)
    else:
        value_list.append(False)


#Metodo para diferenciar los elementos repetidos de la lista
for x in range (len(key_list)):
    char = key_list[x]

    if(key_list.count(char) > 1):

        indexes = []

        for i in range (len(key_list)):
            if key_list[i] == char:
                indexes.append(i)

        
        for j in range (len(indexes)):
            index = indexes[j]
            key_list[index] = str(key_list[index]) + "_" + str(j+1)


dictionary = dict(zip(key_list, value_list))

print("El diccionario resultante es: ")
print(dictionary)