# пример без генератора
# def some():
#     list_text = []
#     with open('text.txt', encoding='utf-8') as r:
#         for x in r:
#             list_text.append(x)
#     return list_text
# пример с генератором
def some():
    with open('text.txt', encoding='utf-8') as r:
        for x in r:
            yield x

# for i in some():
#     print(i.split())


p = some()

for i in p:
    print(i)
