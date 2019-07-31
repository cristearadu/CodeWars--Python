#https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python
def solution(string,markers):
    new_word = ''
    for i in range(len(string.split('\n')):
        print (i)
    for elem,word in range(markers), string.split('\n'):
        #for word in string.split('\n'):
        if elem in word:
            word = word[:word.index(elem)]
            word = word.strip()
            word += '\n'
            new_word += word
            print("IF::"+word)
        else:
            print("ELSE::"+word)
            new_word += word + '\n'
    return new_word
print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
#print("apples, pears\ngrapes\nbananas")
#print("#########################")
#print(solution("a #b\nc\nd $e f g", ["#", "$"]))
#print("a\nc\nd")
