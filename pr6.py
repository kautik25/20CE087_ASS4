#AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond
#  with the input order of appearance of the word. See the sample input/output for clarification. 
x = int(input())
arr = []
for i in range(x):
    y = input()
    arr.append(y)
set1 = set(arr)
print(len(set1))

arr2 = []
arr3 = []
for i in arr:
    if i in arr2:
        pass
    else:
        arr2.append(i)
        arr3.append(arr.count(i))

for k in arr3:
    print(k, end=' ')