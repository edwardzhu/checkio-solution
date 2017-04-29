# import math as m
# def golf(h,w):
#  e,p,t=abs(h*h-w*w)**0.5/h,m.pi*w,m.asin if w<h else m.asinh
#  return round(h*w*p/6,2),round(p/2*(w+h/e*t(e))if w!=h else p*w,2)

from cmath import*
def golf(C,A):e=sqrt(1-A*A/C/C);return round(pi/6*A*A*C,2),round(pi*A*abs(A+(e and C*asin(e)/e-A)/2),2)

if __name__ == '__main__':
   # These "asserts" using only for self-checking and not necessary for auto-testing
   assert list(golf(4, 2)) == [8.38, 21.48]
   assert list(golf(2, 2)) == [4.19, 12.57]
   assert list(golf(2, 4)) == [16.76, 34.69]
   print("All set? Click 'Check' to review your code and earn rewards!")