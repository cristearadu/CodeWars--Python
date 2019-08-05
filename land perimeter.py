#https://www.codewars.com/kata/land-perimeter/train/python
#searching for delimitations of the perimeter
#i am not interested in the inside
#algoritm recursiv de cautare dupa X 
#si pe urma opresc cautarile si merg la urmatoarea pozitie pe j
#bag intr-o lista ca merg in stanga, dreapta sus sau jos etc
#imi pastrez o alta lista unde stockez pozitiile deja mentionate ca sa le omit
def land_perimeter(arr):
    
    #X = 4 m in perimetrus
    #Fiecare X adiacent scade 2 in perimetru
    total_perimeter = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == "X":
                total_perimeter += 4
                if (x != len(arr) - 1) and (arr[x + 1][y] == 'X'):
                    total_perimeter -= 1
                if (x != 0) and (arr[x - 1][y] == 'X'):
                    total_perimeter -= 1
                if (y != len(arr[0]) - 1) and (arr[x][y + 1] == 'X'):
                    total_perimeter -= 1
                if (y != 0) and (arr[x][y - 1] == 'X'):
                    total_perimeter -= 1
    return f"Total land perimeter: {total_perimeter}"


def land_perimeter(arr):
    I, J = len(arr), len(arr[0])

    P = 0
    for i in range(I):
        for j in range(J):
            if arr[i][j] == 'X':
                if i == 0 or arr[i - 1][j] == 'O': P += 1
                if i == I - 1 or arr[i + 1][j] == 'O': P += 1
                if j == 0 or arr[i][j - 1] == 'O': P += 1
                if j == J - 1 or arr[i][j + 1] == 'O': P += 1

print(land_perimeter(
['XXOXX',
 'XXOOX',
 'OXXXX',
 'OOOOO',
 'OOOOO'] ))


#print(land_perimeter(
#['XXOXO',
# 'XOOXO',
# 'OOOXO',
# 'XXOXO',
# 'OXOOO'] ))
#print(24)
