ids = {'user1': [213, 213, 213, 15, 213], 
       'user2': [54, 54, 119, 119, 119], 
       'user3': [213, 98, 98, 35]}
ids_total =list(ids.values())
user1 = ids_total[0]
user2 = ids_total[1]
user3 = ids_total[2]
ids_total = set(user1 + user2 + user3)
print(ids_total)