try:
    n=4
    res=100/n
except ZeroDivisionError:
    print("you can't divide by zero")
else:
    print("result is",res)
finally:
    print("execution complete")    
x=-1
if x>0:
    raise Exception("sorry no number before zero")    