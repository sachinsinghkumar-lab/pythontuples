#creating a tuple with different data tyoes
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

#creating a tuple
tuplex = (4,6,2,8,3,1)
print(tuplex)
#tuplets are IMMUTABLE so you CANNOT add new elements and stuff
#using merge of tuples with the +OPERATOR you can add element
tuplex = tuplex+(9,)
print(tuplex)

#counts the number of occourences of item "50" from tuple
tuple1 = (50,10,60,70,50)
print(tuple1.count(50))

#creating another tuple
tuplex = (2,4,3,4,3,5,6,3,3,1)

#used tuple [start:stop] using the 0, 1, 2 3, 4 order in lists which is inclusive to stop and start 
_slice = tuplex[3:5] #takes the 3rd and 5th (4th and 6th) item
#is exclusive
print(_slice)
#if the start index isnt defined, it is taken from the very beggining
_slice = tuplex[:6]
_slice = tuplex[2:]
print(_slice)