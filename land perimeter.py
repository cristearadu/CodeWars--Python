#https://www.codewars.com/kata/land-perimeter/train/python
#searching for delimitations of the perimeter
#i am not interested in the inside
#algoritm recursiv de cautare dupa X 
#si pe urma opresc cautarile si merg la urmatoarea pozitie pe j
#bag intr-o lista ca merg in stanga, dreapta sus sau jos etc
#imi pastrez o alta lista unde stockez pozitiile deja mentionate ca sa le omit
def land_perimeter(arr):
    
    total_perimeter = 0
    ignore_list = []

    def find_X(arr,i,j):
        to_go_list = []
        if(i,j) not in ignore_list:
            ignore_list.append((i,j))

    

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i < len(arr)-1:
                if arr[i][j] == 'X':
                    #find_X(arr,i,j)
                    ignore_list.append((i,j))
    

    print(ignore_list)

 
    def find_perimeter(ignore_list):
        length = 0
        width = 0
        i = 0
        j = 0
        done = False
        
        while elem in ignore_list:
            pass
        #perimetru simplu de patrat sau dreptunghi
    find_perimeter(ignore_list)
        
        
            
    return f"Total land perimeter: {total_perimeter}"
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
