def square_digits(num):
    final_number=''
    for ch in str(num):
        final_number += str(int(ch)**2)
    return int(final_number)

print(square_digits(9119))

def square_digits(num):
    return int(''.join(str(int(x)**2) for x in str(num)))
print(square_digits(9119))
