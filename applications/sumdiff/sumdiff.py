"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)
positive_lookup_table = dict()
negative_lookup_table = dict()

def f(x):
    return x * 4 + 6

# Your code here
for i in range(len(q) - 1):
    for j in range(i, len(q)):
        positive_lookup_table[(q[i], "+", q[j])] = f(q[i]) + f(q[j])
        positive_lookup_table[(q[j], "+", q[i])] = f(q[j]) + f(q[i])
        negative_lookup_table[(q[i], "-", q[j])] = f(q[i]) - f(q[j])
        negative_lookup_table[(q[j], "-", q[i])] = f(q[j]) - f(q[i])

for positive_key, positive_value in positive_lookup_table.items():
    for negative_key, negative_value in negative_lookup_table.items():
        if positive_value == negative_value:
            print(f"f({positive_key[0]}) + f({positive_key[2]}) = f({negative_key[0]}) - f({negative_key[2]})")