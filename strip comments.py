#https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python
def solution(string,markers):
    words = string.split('\n')
    
    for i,line in enumerate(words):
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index]
        words[i] = line.rstrip(' ')

    return '\n'.join(words)
print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
#print("apples, pears\ngrapes\nbananas")
#print("#########################")
#print(solution("a #b\nc\nd $e f g", ["#", "$"]))
#print("a\nc\nd")
