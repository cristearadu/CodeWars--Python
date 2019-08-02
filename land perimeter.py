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
    


    def find_perimeter(ignore_list):
        perim = 0
        ignore_list_final = []
        perim_list = []
        for elem in ignore_list:
            done = False
            perim_list.append(elem)
            while done == False and elem not in ignore_list_final:

                if(elem[0]-1,elem[1]) in ignore_list and (elem[0]-1,elem[1]) not in ignore_list_final:
                    print('up')
                    perim_list.append((elem[0]-1,elem[1]))
                    ignore_list_final.append((elem[0]-1,elem[1])) 
                elif (elem[0]+1,elem[1]) in ignore_list and (elem[0]+1,elem[1]) not in ignore_list_final:
                    print('down')
                    perim_list.append((elem[0]+1,elem[1]))
                    ignore_list_final.append((elem[0]+1,elem[1]))  

                elif(elem[0],elem[1]+1) in ignore_list and (elem[0],elem[1]+1) not in ignore_list_final:
                    print('right')
                    perim_list.append((elem[0],elem[1]+1))
                    ignore_list_final.append((elem[0],elem[1]+1)) 

                elif(elem[0],elem[1]-1) in ignore_list and (elem[0],elem[1]-1) not in ignore_list_final:
                    print('left')
                    erim_list.append((elem[0],elem[1]-1))
                    ignore_list_final.append((elem[0],elem[1]-1)) 
                else:
                    done = True

    find_perimeter(ignore_list)
        
    return f"Total land perimeter: "
print(land_perimeter(
['XXOOO',
 'XXOXO',
 'OXXXO',
 'OOOOO',
 'OOOOO'] ))


#print(land_perimeter(
#['XXOXO',
# 'XOOXO',
# 'OOOXO',
# 'XXOXO',
# 'OXOOO'] ))
#print(24)
