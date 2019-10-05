n = int(input())
ordem = list(map(int, input().split()))
cruzamento = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if ordem[i] > ordem[j]:
            cruzamento += 1
print(cruzamento)