#https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
def increment_string(strng):
    import re
    patt = r"([0-9]+)"
    out = re.search(patt,strng)
        
    if out:
        out = out.group()
        index = strng.find(out)
        return f"{strng[:index]}{out[:-1]}{int(out[-1]) + 1 }"     
    else:
        return strng + "1"


print(increment_string("foobar001"))
#print(increment_string("bar"))
