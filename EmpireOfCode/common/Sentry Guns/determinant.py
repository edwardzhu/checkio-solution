def golf(m):
 l,s=len(m),0
 if l==1:
  return m[0][0]
 elif l==2:
  return m[0][0]*m[1][1]-m[0][1]*m[1][0]
 else:
   for i in range(l):
    s+=m[0][i]*golf(r(m,0,i))*(-1)**i
   return s
r=lambda m,i,j:[c[0:j]+c[j+1:] for c in m if m.index(c)!=i]

if __name__ == '__main__':
   # These "asserts" using only for self-checking and not necessary for auto-testing
   assert golf([[4,3], [6,3]]) == -6, "First"
   assert golf([[1, 3, 2],
                 [1, 1, 4],
                 [2, 2, 1]]) == 14, "Second"
   print("All done? Earn rewards by using the 'Check' button!")