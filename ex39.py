states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
	'CA':'Los Angeles',
	'MI':'Detroit',
	'FL':'Miami'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print 'NY State has: ', cities['NY']
print 'OR State has: ', cities['OR']

print '-' * 10
print 'Michigan is abbreviated as ', states['Michigan']
print 'Florida is abbreviated as ', states['Florida']

print '-' * 10
print 'Michigan is abbreviated as ', cities[states['Michigan']]
print 'Florida is abbreviated as ', cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])