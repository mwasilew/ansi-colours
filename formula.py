import math

for i in range(16, 232):
    x = i - 10
    b = (x % 6) * 51
    g = ((math.floor(float(x/6)) - 1) % 6) * 51
    r = (math.floor(float((x - 6)/36) ) % 6) * 51
    print(f"| {i} | rgb({r}, {g}, {b}) |")

for i in range(232, 256):
    x = i - 232
    s = 8 + (10 * x)
    print(f"| {i} | rgb({s}, {s}, {s}) |")
