some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicate={}
# for item in some_list:
#     if item not in duplicate:
#         duplicate[item] = 0
#     elif duplicate[item] == 0:
#         duplicate[item] += 1
# for key, value in duplicate.items():
#     if value == 1:
#         print(f'{key} ', end='')

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)