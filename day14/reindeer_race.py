import copy

reindeers = {}
race_time = 2503

def distance_based_race():
    winner_distance = 0
    for reindeer in reindeers.values():
        full_cycle = race_time // (reindeer[1] + reindeer[2])
        remaining_time_last_cycle = race_time % (reindeer[1] + reindeer[2])
        remaining_distance_last_cycle = remaining_time_last_cycle if remaining_time_last_cycle <= reindeer[1] else reindeer[1]

        competitor_distance =  reindeer[0] * ((full_cycle * reindeer[1]) + remaining_distance_last_cycle)

        if competitor_distance > winner_distance:
            winner_distance = competitor_distance
    return winner_distance

def point_based_race():
    reindeers_state = copy.deepcopy(reindeers)

    for timer in range(0, race_time):
        leaders = []
        for reindeer in reindeers:
            if reindeers_state[reindeer][1] > 0:
                reindeers_state[reindeer][3] += reindeers_state[reindeer][0]
                reindeers_state[reindeer][1] -= 1
            elif reindeers_state[reindeer][2] > 0:
                reindeers_state[reindeer][2] -= 1
                if reindeers_state[reindeer][2] == 0:
                    reindeers_state[reindeer][1] = reindeers[reindeer][1]
                    reindeers_state[reindeer][2] = reindeers[reindeer][2]

            if leaders == [] or reindeers_state[leaders[0]][3] == reindeers_state[reindeer][3]:
                leaders.append(reindeer)
            elif reindeers_state[leaders[0]][3] < reindeers_state[reindeer][3]:
                leaders = [reindeer]

        for leader in leaders:
            reindeers_state[leader][4] += 1

    winner_points = 0
    for reindeer in reindeers_state.values():
        if reindeer[4] > winner_points:
            winner_points = reindeer[4]

    return winner_points

with open('input.txt') as input_file:
    for line in input_file:
        split_line = line.rstrip('\n').rstrip('.').split(' ') #  0, 3, 6, 13
        reindeers[split_line[0]] = [int(split_line[3]), int(split_line[6]), int(split_line[13]), 0, 0]
        
print distance_based_race()

print point_based_race()