# Tip: Use list comprehension instead of raw for loops

odd = []
for i in range(20):
  odd.append(i+(i+1))
print(odd)

print()

odder = [i+(i+1) for i in range(20)]
print(odder)
