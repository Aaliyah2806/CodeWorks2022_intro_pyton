set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set3 = set1.intersection(set2)
if set3:
  print("Two sets have items in common: "+ str(set3))

else:
  print("Two sets have no items in common: ")
