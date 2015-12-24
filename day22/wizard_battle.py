import re
import time

lowest_cost = 9999999999999
best_spells = []

# MUCH faster than deepcopy
def spell_copy(spells):
	return {'recharge' : [x for x in spells['recharge']],
			'poison' : [x for x in spells['poison']],
			'shield' : [x for x in spells['shield']],
			'magic missile' : [x for x in spells['magic missile']],
			'drain' : [x for x in spells['drain']]}

def cast(player, boss, spells, spell):
	if spells[spell][2] > 0 or spells[spell][0] > player[1]:
		return -1

	if spell == 'magic missile':
		boss[0] -= 4
		player[1] -= spells[spell][0]
		return spells[spell][0]

	elif spell == 'drain':
		boss[0] -= 2
		player[0] += 2
		player[1] -= spells[spell][0]
		return spells[spell][0]

	elif spell == 'shield':
		player[1] -= spells[spell][0]
		spells[spell][2] = spells[spell][1]
		return spells[spell][0]

	elif spell == 'poison':
		player[1] -= spells[spell][0]
		spells[spell][2] = spells[spell][1]
		return spells[spell][0]

	elif spell == 'recharge':			
		player[1] -= spells[spell][0]
		spells[spell][2] = spells[spell][1]
		return spells[spell][0]

def apply_effects(player, boss, spells):
	if spells['shield'][2] > 0:
		player[2] = 7
		spells['shield'][2] -= 1
	if spells['poison'][2] > 0:
		boss[0] -= 3
		spells['poison'][2] -= 1
	if spells['recharge'][2] > 0:
		player[1] += 101
		spells['recharge'][2] -= 1

def remove_effects(player, spells):
	if spells['shield'][2] == 0:
		player[2] = 0


def play(player, boss, spells, hard_game=False, mana_used=0, is_player_turn=True, used_spells=[]):
	global lowest_cost
	global best_spells

	if mana_used >= lowest_cost or player[0] <= 0:	#check for win/lose or if the current game is worse than one done in the past
		return
	elif boss[0] <= 0:
		lowest_cost = mana_used
		best_spells = used_spells
		print mana_used
		return

	if hard_game and is_player_turn:	#health penalty for playing on hard
		player[0] -= 1

	apply_effects(player, boss, spells)	#apply passive effects if applicable

	if player[0] <= 0:	#check for win/lose again
		return
	elif boss[0] <= 0:
		lowest_cost = mana_used
		best_spells = used_spells
		print mana_used
		return

	if is_player_turn:
		for spell in ['poison', 'recharge', 'shield', 'drain', 'magic missile']: # try every spell
			new_player = [x for x in player]
			new_boss = [x for x in boss]
			new_spells = spell_copy(spells)
			cost = cast(new_player, new_boss, new_spells, spell)

			if cost == -1:
				continue

			remove_effects(new_player, spells)	#remove the effect of shield, quick and dirty implementation
			play(new_player, new_boss, new_spells, hard_game, cost + mana_used, False, used_spells + [spell])	#next turn -> boss
	else:	#boss turn
		new_player = [x for x in player]
		new_player[0] -= max(boss[1] - player[2], 1)
		remove_effects(new_player, spells)
		play(new_player, boss, spells, hard_game, mana_used, True, used_spells)	#next turn -> player


with file('input.txt') as input_file:
	spells = {'recharge' : [229, 5, 0], 'poison' : [173, 6, 0], 'shield' : [113, 6, 0], 'magic missile' : [53, 0, 0], 'drain' : [73, 0, 0]}
	boss_stats = [] #hitpoint, damage
	player_stats = [50, 500, 0] #hitpoint, mana, armor

	for line in input_file:
		boss_stats.append(int(re.search('(\d+)', line).group(1)))

	start_time = time.time()

	play([x for x in player_stats], [x for x in boss_stats], spell_copy(spells), False)
	print 'To beat the boss on normal, it took this much mana:', lowest_cost
	print 'These are the spells used, in order:', best_spells
	print 'It took this many seconds to figure all of this out:', time.time() - start_time

	start_time = time.time()
	lowest_cost = 99999999
	best_spells = []

	play([x for x in player_stats], [x for x in boss_stats], spell_copy(spells), True)
	print 'To beat the boss on hard, it took this much mana:', lowest_cost
	print 'These are the spells used, in order:', best_spells
	print 'It took this many seconds to figure all of this out:', time.time() - start_time