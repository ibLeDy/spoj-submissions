from sys import stdin, stdout

n, k = [int(i) for i in stdin.readline().split()]
nums = [int(stdin.readline()) for _ in range(n)]
divisible = [True if num % k == 0 else False for num in nums]
stdout.write(str(divisible.count(True)))
