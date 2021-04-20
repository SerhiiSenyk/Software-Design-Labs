import csv
import random
from models.models import *
from randomtimestamp import randomtimestamp

class CSV_generator:
	airports = ['Lviv', 'Kyiv', 'Kharkiv', 'London', 'Warsaw', 'Paris',
				'Wasinghton', 'LA', 'New-York', 'Gdansk']
	def generate_airlines(self, filename='airlines.csv', count_rows = 100):
		names = ['Lviv Airlines', 'British Airways', 'Deutsche Lufthansa',
                 'Delta Air Lines', 'Emirates', 'Ryanair', 'Ukraine Airlines', 
                 'Virgin Atlantic',  'Austrian Airlines']
		counries = ['Ukraine', 'USA', 'Emirates', 'German', 'Austria']

		with open(filename, 'a', newline='') as csvfile:
			csvfile.write('airlines\n')
			fieldnames = ['name', 'country']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for i in range(count_rows):	
				writer.writerow({'name': random.choice(names),
								'country': random.choice(counries)})

	def generate_flights(self, filename = 'flights.csv', count_rows = 100):
		airplanes =  ['Airbus A380', 'Boeing 747', 'Boeing 777','Airbus A340', 
			'Yakovlev Yak-40', 'Tupolev Tu-154', 'Airbus A340']
		with open(filename, 'a', newline='') as csvfile:
			fieldnames = ['departure_date_time', 'arrival_date_time', 'time', 
				 'departure_airport', 'arrival_airport', 'airplane',
				 'airline_id']
			csvfile.write('flights\n')
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for i in range(count_rows):
				writer.writerow({'departure_date_time': randomtimestamp(2018), 
								'arrival_date_time': randomtimestamp(2018),
								'time': get_random_time(),
								'departure_airport': random.choice(self.airports),
								'arrival_airport': random.choice(self.airports),
								'airplane': random.choice(airplanes),
								'airline_id': random.randint(1, 100)})
	def generate_tickets(self, filename = 'tickets.csv', count_rows = 100):
		class_tickets = ['first', 'business', 'economy', 'premium economy']
		with open(filename, 'a', newline='') as csvfile:
			fieldnames = ['seat', 'is_booking', 'price', 'class_ticket', 
				'flight_id']
			csvfile.write('tickets\n')
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for i in range(count_rows):	
				writer.writerow({'seat': str(random.randint(1, 200)),
								 'is_booking': str(random.randint(0, 1)),
								 'price': str(random.randint(10, 1000)),
								 'class_ticket': random.choice(class_tickets),
								 'flight_id': random.randint(1, 100)})

	def generate_transitive_points(self, filename = 'transitive_points.csv', 
								count_rows = 100):
		names = ['Lviv Airlines', 'British Airways', 'Deutsche Lufthansa',
                 'Delta Air Lines', 'Emirates', 'Ryanair', 'Ukraine Airlines', 
                 'Virgin Atlantic',  'Austrian Airlines']
		counries = ['Ukraine', 'USA', 'Emirates', 'German', 'Austria']

		with open(filename, 'a', newline='') as csvfile:
			fieldnames = ['airport', 'arrival_date_time', 'departure_date_time',
				 'flight_id']
			csvfile.write('transitive_points\n')
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for i in range(count_rows):	
				writer.writerow({'airport': random.choice(self.airports),
								 'arrival_date_time': randomtimestamp(2018), 
								 'departure_date_time': randomtimestamp(2018),
								 'flight_id': random.randint(1, 100)})
						
	def generate_all_csv(self, filename, count_rows = 1000):
		with open(filename, 'w', newline='') as csvfile:
			csvfile.close()
		self.generate_airlines(filename, count_rows)
		self.generate_flights(filename, count_rows)
		self.generate_tickets(filename, count_rows)
		self.generate_transitive_points(filename, count_rows)

def get_random_time():
    hour = str(random.randint(0, 23))
    minute = str(random.randint(0, 59))
    return hour+':'+minute
