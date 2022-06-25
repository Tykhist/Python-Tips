# Tip: Iterate with enumerate() instead of range(len(x))

data = ["hi", 1, chr(222), 47, "my", True, "lie", 0.21]
for i in range(len(data)):
  print(f"#{i+1}: {data[i]} ({type(data[i])})")

print()

for index, i in enumerate(data):
  print(f"#{index+1}: {i} ({type(i)})")
