def add2num(x,y):
    return x+y
def sub2num(x,y):
    return x-y
def mul2num(x,y):
    return x*y
def div2num(x,y):
    return x/y
if __name__=="__main__":
    a = int(input("Enter num1"))
    b = int(input("Enter num2"))
    sum = add2num(a,b)
    diff  = sub2num(a,b)
    pro = mul2num(a,b)
    divis = div2num(a,b)
    print("addition ",sum)
    print("subtraction ",diff)
    print("multiplication ",pro)
    print("division ",divis)