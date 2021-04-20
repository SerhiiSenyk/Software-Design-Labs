from managers.managers import *
from csv_parser import *
from csv_writer import *

class Controller:
	def __init__(self, sess):
		self.airline_manager = AirlineManager(sess)
		self.flight_manager = FlightManager(sess)
		self.ticket_manager = TicketManager(sess)
		self.transitive_point_manager = TransitivePointManager(sess)

	def select_airline_by_id(self, id):
		return self.airline_manager.select_airline_by_id(id)

	def select_airlines(self):
		return self.airline_manager.select_airlines()

	def insert_airline(self, name, country):
		self.airline_manager.insert_airline(name, country)

	def delete_airline_by_id(self, id):
		self.airline_manager.delete_airline_by_id(self, id)

	def select_flight_by_id(self, id):
		return self.flight_manager.select_flight_by_id(id)

	def select_flights(self):
		return self.flight_manager.select_flights()

	def insert_flight(self, departure_date_time, arrival_date_time, time,
					departure_airport, arrival_airport, airplane, airline_id):
		self.flight_manager.insert_flight(departure_date_time, 
			arrival_date_time, time, departure_airport, arrival_airport, 
			airplane, airline_id)

	def delete_flight_by_id(self, id):
		self.flight_manager.delete_flight_by_id(self, id)

	def select_ticket_by_id(self, id):
		return self.ticket_manager.select_ticket_by_id(id)

	def select_tickets(self):
		return self.ticket_manager.select_tickets()

	def insert_ticket(self, seat, is_booking, price, class_ticket, flight_id):
		self.ticket_manager.insert_ticket(seat, is_booking, price, class_ticket,
											flight_id)

	def delete_ticket_by_id(self, id):
		self.ticket_manager.delete_ticket_by_id(self, id)

	def select_transitive_point_by_id(self, id):
		return self.transitive_point_manager.select_airline_by_id(id)

	def select_transitive_points(self):
		return self.transitive_point_manager.select_transitive_points()

	def insert_transitive_point(self, airport, arrival_date_time, 
								departure_date_time, flight_id):
		self.transitive_point_manager.insert_transitive_point(airport, 
						arrival_date_time, departure_date_time, flight_id)

	def delete_transitive_point_by_id(self, id):
		self.transitive_point_manager.delete_transitive_point_by_id(self, id)

	def load_from_csv(self, filename):
		parsed_csv = CSV_reader().parser('data.csv')
		airline_headers, airline_data = parsed_csv['airlines']
		flight_headers, flight_data = parsed_csv['flights']
		ticket_headers, ticket_data = parsed_csv['tickets']
		points_headers, points_data = parsed_csv['transition_points']
		for data in airline_data:
			self.airline_manager.insert_airline_from_csv(airline_headers, data)
		for data in flight_data:
			self.flight_manager.insert_flight_from_csv(flight_headers, data)
		for data in ticket_data:
			self.ticket_manager.insert_ticket_from_csv(ticket_headers, data)
		for data in points_data:
			self.transitive_point_manager.\
				insert_transitive_point_from_csv(points_headers, data)
