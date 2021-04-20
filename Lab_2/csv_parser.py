import csv

class CSV_reader:
	def parser(self, filename='data.csv'):
		with open(filename) as csvfile:
			lines = csvfile.readlines()
			lines = [line[:-1] for line in lines if line.endswith('\n')]
			airlines_index = lines.index('airlines')
			flight_index = lines.index('flights')
			tickets_index = lines.index('tickets')
			points_index = lines.index('transitive_points')
			csvfile.seek(0)
			airlines_header = lines[airlines_index + 1]
			airlines_list = lines[airlines_index + 2: flight_index]
			flights_header = lines[flight_index + 1]
			flights_list = lines[flight_index + 2: tickets_index]
			tickets_header = lines[tickets_index + 1]
			tickets_list = lines[tickets_index + 2: points_index]
			points_header = lines[points_index + 1]
			points_list =  lines[points_index + 2:]	
		return {
				'airlines': (airlines_header,airlines_list),
				'flights': (flights_header, flights_list),
				'tickets': (tickets_header, tickets_list),
				'transition_points': (points_header, points_list)
			}

	
	def csv_parser(self, filename='data.csv'):
		with open(filename) as csvfile:
			fieldnames = ['name', 'country']
			lines = csvfile.readlines()
			lines = [line[:-1] for line in lines if line.endswith('\n')]
			index = lines.index('flights')
			print('index = ', index)
			reader = csv.DictReader(csvfile, fieldnames=fieldnames)
			for row in reader:
				print(row['name'])