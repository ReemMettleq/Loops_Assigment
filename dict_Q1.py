keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = {}
for item1 in keys:
    for item2 in values:
        dictionary[item1] = item2
        values.remove(item2)
        break
print(dictionary)
