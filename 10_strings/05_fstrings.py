# string formatting

template="Dear {}, you are awesome.Take this {} bag"

a="john"
a1=10000
b="yash"
b1=1000
c="diksha"
c1=300

s1=template .format(a,a1)
print(s1)

# f string

print(f"Dear {a} you are awesome.Take this {a1} bag")
print(f"Dear {b} you are awesome.Take this {b1} bag")
print(f"Dear {c} you are awesome.Take this {c1} bag")