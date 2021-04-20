from models.models import *
from sqlalchemy import *

class AirlineManager:
	def __init__(self, sess):
		self.sess = sess

	def select_airline_by_id(self, id):
		return self.sess.query(Airline).filter(
			Airline.id == id).one_or_none()

	def select_airlines(self):
		return self.sess.query(Airline).all()

	def insert_airline(self, name, country, id = None):
		self.sess.add(Airline(name, country))

	def delete_airline_by_id(self, id):
		airline = self.get_airline_by_id()
		if airline:
			self.sess.delete(airline)

	def insert_airline_from_csv(self, header, data):
		airline = Airline()
		airline.from_csvfile(header,data)
		self.sess.add(airline)

class FlightManager:
	def __init__(self, sess):
		self.sess = sess

	def select_flight_by_id(self, id):
		return self.sess.query(Flight).filter(
			Flight.id == id).one_or_none()

	def select_flights(self):
		return self.sess.query(Flight).all()

	def insert_flight(self, departure_date_time, arrival_date_time, time,
					departure_airport, arrival_airport, airplane, airline_id, 
					id = None):
		self.sess.add(Flight(departure_date_time, arrival_date_time, time,
					departure_airport, arrival_airport, airplane, airline_id))

	def delete_flight_by_id(self, id):
		flight = self.get_flight_by_id()
		if flight:
			self.sess.delete(flight)

	def insert_flight_from_csv(self, header, data):
		flight = Flight()
		flight.from_csvfile(header, data)
		self.sess.add(flight)

class TicketManager:
	def __init__(self, sess):
		self.sess = sess

	def select_ticket_by_id(self, id):
		return self.sess.query(Ticket).filter(
			Ticket.id == id).one_or_none()

	def select_tickets(self):
		return self.sess.query(Ticket).all()

	def insert_ticket(self, seat, is_booking, price, class_ticket, flight_id,
						id = None):
		self.sess.add(Ticket(seat, is_booking, price, class_ticket, flight_id))

	def delete_ticket_by_id(self, id):
		ticket = self.get_ticket_by_id()
		if ticket:
			self.sess.delete(ticket)

	def insert_ticket_from_csv(self, header, data):
		ticket = Ticket()
		ticket.from_csvfile(header, data)
		self.sess.add(ticket)

class TransitivePointManager:
	def __init__(self, sess):
		self.sess = sess

	def select_transitive_point_by_id(self, id):
		return self.sess.query(TransitivePoint).filter(
			TransitivePoint.id == id).one_or_none()

	def select_transitive_points(self):
		return self.sess.query(TransitivePoint).all()

	def insert_transitive_point(self,airport, arrival_date_time, 
								departure_date_time, flight_id, id = None):
		self.sess.add(TransitivePoint(airport, arrival_date_time, 
										departure_date_time, flight_id))

	def delete_transitive_point_by_id(self, id):
		transitive_point = self.get_airline_by_id()
		if transitive_point:
			self.sess.delete(transitive_point)

	def insert_transitive_point_from_csv(self, header, data):
		transitive_point = TransitivePoint()
		transitive_point.from_csvfile(header, data)
		self.sess.add(transitive_point)
