from dis import dis

def some(x):
    return x/5

var = lambda x: x/5

# print(some(7))
# print(var(7))

print(dis(some))
print(dis(var))
