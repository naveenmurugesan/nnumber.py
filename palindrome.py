my_str=int(input())
my_str=my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
  print(" It is a palindrome")
 else:
 print("enter the number between <=1000")
