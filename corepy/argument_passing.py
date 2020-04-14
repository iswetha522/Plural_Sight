m = [9, 15, 24]
def modify(k): # k is formal argument reference
    k.append(39)
    print("k =", k)

modify(m) # m is actual argument reference
print("m =", m)
