#https://www.codewars.com/kata/land-perimeter/train/python
#searching for delimitations of the perimeter
#i am not interested in the inside
def land_perimeter(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            
            if i < len(arr)-1 :
                if arr[i][j] == 'X' and (arr[i][j+1] == 'X' or arr[i+1][j] == 'X'):
                    print('found')
                
    return f"Total land perimeter: "

print(land_perimeter(
['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO'] ))
print(24)
