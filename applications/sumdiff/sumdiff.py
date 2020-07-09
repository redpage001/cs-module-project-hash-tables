"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)
lookup_table = dict()

def f(x):
    return x * 4 + 6

# Your code here
for i in range(len(q) - 1):
    for j in range(i, len(q)):
        lookup_table[(q[i], "+", q[j])] = f(q[i]) + f(q[j])
        lookup_table[(q[i], "-", q[j])] = f(q[i]) - f(q[j])
        lookup_table[(q[j], "-", q[i])] = f(q[j]) - f(q[i])

print(lookup_table)