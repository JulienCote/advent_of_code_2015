love_chart = {}
attendees = []

max_love = 0

def seating_permutations(remaining_attendees, current_attendee, first_attendee , love=0):
    global max_love
    if len(remaining_attendees) == 0:
        love += love_chart[current_attendee, first_attendee] + love_chart[first_attendee, current_attendee]
        if max_love < love:
            max_love = love
    else:
        for attendee in remaining_attendees:
            seating_permutations([x for x in remaining_attendees if x != attendee], attendee, first_attendee, love + love_chart[current_attendee, attendee] + love_chart[attendee, current_attendee])

with open('input.txt') as input_file:
    for line in input_file:
        split_line = line.rstrip('\n').rstrip('.').split(' ') #  0, 2, 3, 10
        love_chart[split_line[0], split_line[10]] = int(split_line[3]) if split_line[2] == 'gain' else int(split_line[3]) * -1

        if split_line[0] not in attendees:
            attendees.append(split_line[0])

    first_seat = attendees[0]
    seating_permutations([x for x in attendees if x != first_seat], first_seat, first_seat)

    print 'Maximum love for all others is : ' + str(max_love)

    for attendee in attendees:
        love_chart[attendee, 'me'] = 0
        love_chart['me', attendee] = 0

    attendees.append('me')

    max_love = 0
    seating_permutations([x for x in attendees if x != first_seat], first_seat, first_seat)

    print 'Maximum love for all of us is : ' + str(max_love)