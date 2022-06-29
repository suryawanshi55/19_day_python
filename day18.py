# e={}
# print(e,type(e)){}     # <class 'dict'>
# f={1,4.5,"hello"}     (...... set is mutable,modification can made......)
# print(f,type(f))      #   {1, 'hello', 4.5} <class 'set'>
# print(type(f))         #<class 'set'>
# print(type(4.5))       # <class 'float'>
# print(type("hello"))      frozenset({1, 4.5, 'hello'})
# (...frozen is immutable,modification can not be made.....)
# m={6,7,8}
# n=3,5,4
# m.add(n)
# print(m)                   # {8, (3, 5, 4), 6, 7}
# t={2,"hello",5,8.7}
# y=7,9,2
# t.add(y)
# print(t)                 #set()
# p={3,"hello",34}
# p.clear()
# print(p)               #set()
# a={4,3,5,7};r={8,9,6,4};u={3,5,6,7}
# print(a.intersection(r))   # {4}
# print(a.intersection(u))   # {3, 5, 7}
# print(r.intersection(a))   # {4}
# print(r.intersection(u))    #{6}
# print(u.intersection(a))   #{3, 5, 7}
# g={'hello','hi','hey'}
# h={3,5,6}
# print(g.union(h))     {'hey', 'hi', 3, 5, 6, 'hello'}
# print(h.union(g))      {3, 5, 6, 'hello', 'hi', 'hey'}
# y={4,6,7,8}
# e={9,3,2,4}
# f={3,6,8,9}
# y.update(f)
# print(y){3, 4, 6, 7, 8, 9}
# f.update(e)
# print(f)      {2, 3, 4, 6, 8, 9}
# e={55,43,21,12}
# s={87,67,21,43}
# print(s.difference(e))     {67, 87}
# print(e.difference(s))       {12, 55}
# z={98,34,55,43,86,20}
# z.discard(55)
# print(z)       {98, 34, 20, 86, 43}
# z.discard(98)
# print(z)     {34, 20, 86, 55, 43)
# b={"hello","hey","hiii"}
# b.pop()
# print(b)    {'hey', 'hiii'}
# v={3,5,8,1,9}
# v.pop()
# print(v)   {3, 5, 8, 9}
# c={4,3,2,1}
# k={6,5,7}
# r={3,4,5,0}
# print(c.isdisjoint(k))   # True
# print(c.isdisjoint(r))   # False
# print(r.isdisjoint(c))    # False
# print(r.isdisjoint(k))     # False
# print(k.isdisjoint(c))      #True
a={5,6,7,8}
s={3,4,5}
w={9,8,7,6}
# print(a.issubset(w))    False
print(a.issubset(s))