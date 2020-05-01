def test(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)

lst = [1,2,3,4,5] # 리스트
dict = {'a':1,'b':2,'c':3,'d':4}
tuple = (1,2,3,4,5,)
st = {1,2,3,4,1,2,3,4,5}

#test(lst,tuple,dict)
#print(type(st),st)
#test(*st)
test(lst, tuple, st, **dict)
