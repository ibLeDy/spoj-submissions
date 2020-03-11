from sys import stdin, stdout

n, k = [int(i) for i in stdin.readline().split()]
stdout.write(str(sum(1 for num in stdin.read().split() if int(num) % k == 0)))
