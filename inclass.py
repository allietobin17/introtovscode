orders = ["Coffee", "Tea", "Coffee", "Smoothie", "Tea", "Coffee", "Water"]

counts = {}

#for drink in orders:
   ## if drink in counts:
     #   counts[drink] += 1 #if key exists, it will add
    #else:
      #  counts[drink] = 1 #if does not exist, it will creat key pair

for drink in orders:
    counts[drink] = counts.get(drink, 0) +1

print(counts)
