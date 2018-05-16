name_list = ["a", "b", "c"]

name_list2=["找","孙子"]
name_list.append("d")

name_list.insert(1,"李四")

name_list.extend(name_list2)

print(name_list)

name_list.pop()
name_list.remove("a")
# name_list.copy()
print(name_list)
print(len(name_list))
print(name_list.count("b"))
#name_list3=name_list.copy()
name_list3=name_list
print(id(name_list),id(name_list3))
for name in name_list:
    print(name,end=" ")
