#encrypt_this("Hello") == "72olle"
#encrypt_this("good") == "103doo"
#encrypt_this("hello world") == "104olle 119drlo"

'''Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter needs to be converted to its ASCII code.
The second letter needs to be switched with the last letter
Keepin' it simple: There are no special characters in input.'''

def encrypt_this(text):
    text = list(text.split())
    new_text = []
    for word in text:
        if len(word) > 2:
            word = str(ord(word[0])) + word[-1] + word[2:-1] + word[1]
            new_text.append(word)
        elif len(word) == 2:
            word = str(ord(word[0])) + word[1]
            new_text.append(word)
        elif len(word) == 1:
            word = str(ord(word))
            new_text.append(word)
    return ' '.join(new_text)


# Best answer
def swapper(w):
    print(w if len(w) < 2 else w[-1] + w[1:-1] + w[0])
    return w if len(w) < 2 else w[-1] + w[1:-1] + w[0]
def encrypt_this(text):
    return ' '.join(w if not w else str(ord(w[0])) + swapper(w[1:]) for w in text.split())
 
print(encrypt_this("hello world"))
print(encrypt_this("A wise old owl lived in an oak"))
