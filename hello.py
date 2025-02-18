def Hello(n): print(f"Hello {n}")

print("Hello World")
for i in range(10):
    s = str(i)
    for j in range(i - 1, 0, -1):
        s += ' '
        s += str(j)
    print(s)

