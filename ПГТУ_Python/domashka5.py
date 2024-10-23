s1 = 'abcdabcd'
s2 = 'cdcdef'
set_values = set()
set_values2 = set()
for word in s1:
    set_values.add(word)
for word in s2:
    set_values2.add(word)
unique_values = len(set_values.intersection(set_values2))
print(unique_values)