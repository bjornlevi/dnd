import itertools

ability_points = 25
ability_cost = {8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:7, 15:9}
ability_scores = [8,9,10,11,12,13,14,15]


def calculate_ability_cost(scores):
	points = 0
	for score in scores:
		points += ability_cost[score]
	return points

def subsets(n,m):
	perms = itertools.combinations_with_replacement(ability_scores,n)
	for i in perms:
		if calculate_ability_cost(i) == m:
			yield i

sets = subsets(6,ability_points)

for s in sets:
	print(s)