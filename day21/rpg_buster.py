import re
import copy

boss_stats = [] #hitpoint, damage, armor
player_stats = [100, 0 , 0]

# price, attack, defense
weapons = [[8,4,0], [10,5,0], [25,6,0], [40,7,0], [74,8,0]]
armors = [[0,0,0],[13,0,1],[31,0,2],[53,0,3],[75,0,4],[102,0,5]]
rings = [[0,0,0],[0,0,0],[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]

def win_fight(boss, player):
	while boss[0] > 0 and player[0] > 0:
		boss[0] -= max(player[1]-boss[2], 1)
		if boss[0] <= 0:
			return True
		player[0] -= max(boss[1]-player[2], 1)
		if player[0] <= 0:
			return False


with file('input.txt') as input_file:
	shop_regex = '(\w+.+?)\s+?(\d+)\s+?(\d+)\s+?(\d+)'
	for line in input_file:
		boss_stats.append(int(re.search('(\d+)', line).group(1)))

	cheapest_equipment_cost = 999999999
	highest_equipment_cost = 0
	equiped_stats = [100,0,0]

	for weapon in weapons:
		for armor in armors:
			for i in range(0, len(rings)):
				equiped_stats[2] = player_stats[2] + rings[i][2]
				for j in range(i+1, len(rings)):
					equiped_stats[1] = player_stats[1] + weapon[1] + rings[i][1] + rings[j][1]
					equiped_stats[2] = player_stats[2] + armor[2] + rings[i][2] + rings[j][2]
					cost = weapon[0] + armor[0] + rings[i][0] + rings[j][0]

					if win_fight(copy.deepcopy(boss_stats), copy.deepcopy(equiped_stats)):
						if cost < cheapest_equipment_cost:
							cheapest_equipment_cost = cost
					else:
						if cost > highest_equipment_cost:
							highest_equipment_cost = cost
						

	print cheapest_equipment_cost
	print highest_equipment_cost
