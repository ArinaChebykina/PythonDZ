n = int(input())
dict = {}
for i in range(n):
    word, pair = input().split()
    dict[word] = pair
    dict[pair] = word
find_synonym = input()
print(dict[find_synonym])
