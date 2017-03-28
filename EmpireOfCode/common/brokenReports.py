import re
golf = lambda r:sum([(ord(i[0])-65)*9+int(i[1]) for i in re.findall(r'[A-Z][1-9]', r)])


if __name__ == '__main__':
   # These "asserts" using only for self-checking and not necessary for auto-testing
   assert golf("ASDA1,BB22D01C1") == 31
   assert golf("B1,C2,D3") == 60
   print("Earn cool rewards by using the 'Check' button!")