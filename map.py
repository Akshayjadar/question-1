num = (1, 2, 3, 4, 5, 6, 7)
print("original_list:",num)
result = map(lambda x : x+x+x, num)
print(list(result))