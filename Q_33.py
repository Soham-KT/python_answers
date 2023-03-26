dic={}
n=int(input("Enter range: "))
for i in range(n):
    ki, val=input("Enter key, value: ").split()
    dic[ki]=val

for i in dic:
    print(i, dic[i])
print("\n")

for k, v in dic.items():
    print(k, v)
print("\n")

print(dic.keys())
print(dic.values())
print(dic.items())