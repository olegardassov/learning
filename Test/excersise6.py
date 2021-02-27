list1 = [1, 2, 9, 3, 4, 7, 9]
list2 = [1 , 2 ,4 ,6 ,4 ,6]
max_count = 0
new_list = []
for num in list1:
    if list1.count(num) > max_count:
        max_count = list1.count(num)

for num in list1:
    if list1.count(num) == max_count:
        new_list.append(num)
        new_list = list(set(new_list))

print(new_list)

