def palindrome(r):
    e = len(r)-1
    s = 0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

r = (2,1)

if(palindrome(r)):
    print("the tuple is flip flop")
else:
    print("the tuple is not flip flop!!!")


