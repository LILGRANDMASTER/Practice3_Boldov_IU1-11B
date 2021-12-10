
def prize_count(c, max_bonus):
	sum = 0
	for el in c:
		sum += el // max_bonus

	return sum



n = int(input())
m = int(input())
c = []

for i in range(0,n):
	x = int(input())
	c.append(x)

left = 0
right = 10000000000000000000000

while(left + 1 < right):
	mid = (left + right)//2
	
	if prize_count(c, mid) < m:
		right = mid
	else:
		left = mid


print(left)