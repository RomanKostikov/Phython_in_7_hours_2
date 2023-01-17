list_of = [['Adam', 29], ['Jonny', 3*1/12], ['Jess', 25]]
# обыкновенная запись
# def s(x):
#     return x[1]

# r = sorted(list_of, key=s)
# ламбда+сортед
# r = sorted(list_of, key=lambda x: x[1])
# print(r)

# ламбда+филтер
x = list(filter(lambda x: x[1] > 18, list_of))

print(x)