def fun(name):
    print('hai,',name)

print(id(fun))
f=fun
print(id(f))
fun("ravi")
f("gprec")
del fun
fun('cse')
