golf=lambda h,a=0,b=0:min(abs(x[0]-a+1j*(x[1]-b))+golf(h-{x},*x) for x in h) if len(h)!=0 else 0


if __name__ == '__main__':
   # These "asserts" using only for self-checking and not necessary for auto-testing
   def almost_equal(checked, correct, significant_digits=2):
       precision = 0.1 ** significant_digits
       return correct - precision < checked < correct + precision

   assert almost_equal(golf({(2, 2), (2, 8), (8, 8), (8, 2), (5, 5)}), 23.31)
   assert almost_equal(golf({(2, 2), (4, 4), (6, 6), (8, 8), (9, 9)}), 12.73)
   print("Earn cool rewards by using the 'Check' button!")