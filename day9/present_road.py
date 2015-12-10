#!/usr/bin/python2.7

import re

cities = {}
smallest_cost = 999999999
biggest_cost = 0

class city:
	def __init__(self, name):
		self.name = name
		self.roads = {}

	def __repr__(self):
		return str(self.roads) + '\n'

	def add_road(self, destination, cost):
		self.roads[destination] = cost
		if destination not in cities:
			new_destination = city(destination)
			cities[destination] = new_destination
			new_destination.add_road(self.name, cost)
		elif self.name not in cities[destination].get_destinations():
			cities[destination].add_road(self.name, cost)

	def get_destinations(self):
		return list(self.roads.keys())

	def get_road_cost(self, destination):
		return self.roads[destination]

def extremum_road_cost(cities_to_visit, current_city='', cost=0):
	global smallest_cost
	global biggest_cost

	if len(cities_to_visit) == 0:
		if cost < smallest_cost:
			smallest_cost = cost
		elif cost > biggest_cost:
			biggest_cost = cost
	else:
		if current_city == '':
			for first_city in cities_to_visit:
				extremum_road_cost([x for x in cities_to_visit if x != first_city], first_city)
		else:
			for city in cities_to_visit:
				extremum_road_cost([x for x in cities_to_visit if x != city], city, cost + cities[current_city].get_road_cost(city))

with open('input.txt') as input_file:
	regex = '^(\w+) \w+ (\w+) = (\d+)'
	for line in input_file:
		split_line = re.search(regex, line)
		if split_line.group(1) not in cities:
			new_city = city(split_line.group(1))

			new_city.add_road(split_line.group(2), int(split_line.group(3)))
			cities[split_line.group(1)] = new_city
		else:
			cities[split_line.group(1)].add_road(split_line.group(2), int(split_line.group(3)))

extremum_road_cost(cities.keys())
print 'shortest_path: ' + str(smallest_cost)
print 'longest_path: ' + str(biggest_cost)