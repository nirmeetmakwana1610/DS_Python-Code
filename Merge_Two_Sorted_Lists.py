a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

c = []

i = 0
j = 0

while i < len(a) and j < len(b):

    if a[i] < b[j]:
        c = c + [a[i]]
        i = i + 1
    else:
        c = c + [b[j]]
        j = j + 1

while i < len(a):
    c = c + [a[i]]
    i = i + 1

while j < len(b):
    c = c + [b[j]]
    j = j + 1

print(c)
