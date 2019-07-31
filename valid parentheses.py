#Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function
#should return true if the string is valid, and false if it's invalid.
#0 <= input.length <= 100



def valid_parentheses(string):
    if not string:
        return True
    ret_val = 0
    for ch in string:
        if ch == "(":
            ret_val += 1
        elif ch == ")":
            ret_val -= 1
        if ret_val < 0:
            return False
        return True if ret_val == 0 else False
                
    return (True if dict_parentheses["("] == dict_parentheses[")"] else False)

#print(valid_parentheses("("))#False
#print(valid_parentheses("  ("))#False
#print(valid_parentheses("()"))#True
#print(valid_parentheses("(())((()())())"))#True
print(valid_parentheses(")test"))#False
print(valid_parentheses("hi(hi)()"))#True
print(valid_parentheses(""))#True
print(valid_parentheses(")("))
