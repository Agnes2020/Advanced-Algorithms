from collections import Counter
# importing counter function


def matchingSocks( n, arr):
    n = Counter(arr)
    sum(i//2 for i in n.values())


n = input()
arr = list(map(int, input().split()))
print(matchingSocks(n, arr))
