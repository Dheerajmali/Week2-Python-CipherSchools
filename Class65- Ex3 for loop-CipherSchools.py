# practice for loop
# ask user name and count each character
# "Dheeraj Mali"
# D : 1
# h : 1
# e : 2
# e : 2
# r : 1 
# a : 2
# j : 1
#   : 1
# M : 1
# a : 2
# l : 1
# i : 1

name = input("enter your name :")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]
