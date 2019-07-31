def expanded_form(num):
    lst_num = []
    counter = 1
    while num != 0:
        lst_num.append(num%10*counter)
        num = num //10
        counter *= 10
    lst_num=lst_num[::-1]
    lst_num=list(filter(lambda num: num!=0,lst_num))

    ret_str=''
    for i in range(len(lst_num)):
        if(i == len(lst_num)-1):
            ret_str += str(lst_num[i])
        else:
            ret_str += str(lst_num[i])+' + '
    return ret_str

print(expanded_form(300000 + 70000 + 20 + 2))

def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

print(expanded_form(300000 + 70000 + 20 + 2))
