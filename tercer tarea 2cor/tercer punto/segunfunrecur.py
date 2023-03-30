# segunda funcion recursiva 

def k(n,p):
    if n == 1:
        return p
    else:
        return n*p + k(n-1,p)
r = k(6,8)
print(r)

