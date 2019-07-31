import sys
#Your task is to sort a given string.
#Each word in the string will contain a single number.
#This number is the position the word should have in the result.
#Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

#If the input string is empty, return an empty string.
#The words in the input String will only contain valid consecutive numbers.

#sentence = '4of Fo1r pe6ople g3ood th5e the2'
#sentence = 'Thi1 is2 T4est'
#sentence = 'tak2e chil3d a1s'
#sentence = '1 2 3 4 5 6 7 8 9'
sentence = 'perso2n fro4m h3e the1re'
list_sentence = []
dict_place = {}
add_word = ''
number = int
i=0
if not sentence:
    sys.exit()
for word in sentence:
    i += 1
    #creez cuvintele, daca apare whitespace setez cuvantul '' si adaug in lista ce am strans
    if word != ' ':
        add_word += word
        print(add_word)
        #verific ce cifre am
        try:
            type(int(word))
            number = int(word)
        except ValueError:
            pass
        if  i == len(sentence):
            dict_place [number] = add_word
            print('ADD:',add_word)
       
    else:
        print('ADD:',add_word)
        dict_place [number] = add_word
        add_word =''
print(dict_place)
sentence = ''
#iteraam prin dictionarul sortat
for x,y in sorted(dict_place.items()):
    list_sentence.append(y)
for i in range(0,len(list_sentence)):
    if i == len(list_sentence):
        sentence += list_sentence[i]
        break
    else:
        sentence += list_sentence[i] + ' '

print (sentence.rstrip(' '))
