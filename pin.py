import re
def validate_pin(pin):
    try:
        if int(pin) < 0:
            return False
        patt = r"\D|\'\b"
        out = re.search(patt,pin)
        if (out):
            return False
        
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False
    except:
        return False

print(validate_pin('1234'))

def validate_pin(pin):
    return len(pin) in (4,6) and pin.isdigit()
print(validate_pin('+1234'))

print(ord('+'))
