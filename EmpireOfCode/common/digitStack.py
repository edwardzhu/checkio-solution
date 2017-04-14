def golf(c):
 s,r=[],0
 for i in c:
  if "PUSH" in i:s+=[int(i[-1])]
  if s:
   if "POP" in i:r+=s.pop()
   if "PEEK" in i:r+=s[-1]
 return r

if __name__ == '__main__':
   # These "asserts" using only for self-checking and not necessary for auto-testing
   assert golf(("PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK")) == 8, "Example"
   assert golf(("POP", "POP")) == 0, "PopPop"
   assert golf(("PUSH 9", "PUSH 9", "POP")) == 9, "Push 9"
   assert golf(()) == 0, "Empty"
   print("All done? Earn rewards by using the 'Check' button!")