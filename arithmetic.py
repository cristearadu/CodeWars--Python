def arithmetic(a, b, operator):
    return{
        'add': a+b,
        'subtract': a-b,
        'multiply': a*b,
        'divide': a/b
    }[operator]
print(arithmetic(10,3,'add'))

def arithmetic(a,b,operator):
    dict_op_a_b ={
        'add': a+b,
        'subtract': a-b,
        'multiply': a*b,
        'divide': a/b
    }
    return dict_op_a_b[operator]
print(arithmetic(10,3,'subtract'))

