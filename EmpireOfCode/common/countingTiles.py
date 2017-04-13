def golf(r):
 s=p=0
 c=int(-(-r//1))
 for i in range(c):
  y=max(r**2-(i+1)**2,0)**0.5
  s+=y//1
  p+=c-y//1
  c=-(-y//1)
 return s*4,p*4

if __name__ == '__main__':
   # These "asserts" using only for self-checking and not necessary for auto-testing
   assert isinstance(golf(1), (list, tuple))
   assert list(golf(2)) == [4, 12]
   assert list(golf(3)) == [16, 20]
   assert list(golf(2.1)) == [4, 20]
   assert list(golf(2.5)) == [12, 20]
   print("All done? Earn rewards by using the 'Check' button!")