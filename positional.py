def add(a,b):
    print("a=",a)
    print("b=",b)
    return a+b
result=add(5,4)
print("sum=",result)    

def student_info(name,roll,marks):
    print("name:",name)
    print("roll:",roll)
    print("marks:",marks)
student_info("ravi",101,80)

def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("simple interst:",si)
simple_interest(5000,2,2)

def multiply(a,b):

    return a*b
multiply(5)    


def check_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative") 
    else:
        print("zero")
    check_value(0)
    check_value(6)
    check_value(-8)           

def odd_even(no):
    if(no%2==0):
        print("even..!")
    else:
        print("odd..!")    
    odd_even(56)  