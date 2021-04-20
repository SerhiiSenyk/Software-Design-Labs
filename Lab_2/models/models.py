from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from datetime import time



Base = declarative_base()

class Flight(Base):
	__tablename__ = 'flights'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	departure_date_time = Column('departure_date_time', DATETIME, 
							  nullable=False)
	arrival_date_time = Column('arrival_date_time', DATETIME, nullable=False)
	time = Column('time',  Time, nullable=False)
	departure_airport = Column('departure_airport', VARCHAR(45), nullable=False)
	arrival_airport = Column('arrival_airport', VARCHAR(45), nullable=False)
	airplane = Column('airplane', VARCHAR(45), nullable=False)
	airline_id = Column('airline_id', Integer, ForeignKey('airlines.id'))#many to one
	transitive_points = relationship("TransitivePoint") #one to many
	tickets = relationship('Ticket') #one to many

	def __init__(self, departure_date_time=None, arrival_date_time=None, 
			  time=None, departure_airport=None, arrival_airport=None, 
			  airplane=None, airline_id=None):
		self.departure_date_time = departure_date_time
		self.arrival_date_time = arrival_date_time
		self.time = time
		self.departure_airport = departure_airport
		self.arrival_airport = arrival_airport
		self.airplane = airplane
		self.airline_id = airline_id

	def __str__(self) -> str:
		return self.get_flight().__str__()

	def get_flight(self):
		return {
			'id': self.id,
			'departure_date_time': str(self.departure_date_time),
			'arrival_date_time': str(self.arrival_date_time),
			'time': str(self.time),
			'departure_airport': self.departure_airport,
			'arrival_airport' : self.arrival_airport,
			'airplane': self.airplane,
			'airline_id': self.airline_id
		}

	def str_to_datetime(self, str, format='%d-%m-%Y %H:%M:%S'):
		return datetime.strptime(str, format)

	def from_csvfile(self, header: str, data: str, sep=','):
		list_header = header.split(sep)
		list_data = data.split(sep)
		for header, data in zip(list_header, list_data):
				setattr(self, header, data)
				if header == 'departure_date_time':
					self.departure_date_time = Flight.str_to_datetime(self, data)
				if header == 'arrival_date_time':
					self.arrival_date_time = Flight.str_to_datetime(self, data)
				if header == 'time':
					self.time = Flight.str_to_datetime(self, data, '%H:%M').time()
					
class Ticket(Base):
	__tablename__ = 'tickets'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	seat = Column('seat', VARCHAR(45), nullable=False)
	is_booking = Column('is_booking', BOOLEAN, nullable=False)
	price = Column('price', Integer, nullable=False)
	class_ticket = Column('class', Integer, nullable=False)
	flight_id =  Column('flight_id', Integer, ForeignKey('flights.id'))#many to one

	def __init__(self, seat = None, is_booking = None, price = None,
			 class_ticket = None, flight_id = None):
		self.seat = seat
		self.is_booking = is_booking
		self.price = price
		self.class_ticket = class_ticket
		self.flight_id = flight_id

	def __str__(self) -> str:
		return self.get_ticket().__str__()

	def get_ticket(self):
		return {
			'id': self.id,
			'seat': self.seat,
			'is_booking': self.is_booking,
			'class_ticket':self.class_ticket,
			'flight_id': self.flight_id
		}

	def from_csvfile(self, header: str, data: str, sep=','):
		list_header = header.split(sep)
		list_data = data.split(sep)
		for header, data in zip(list_header, list_data):
				setattr(self, header, data)
				if self.is_booking != None:
					self.is_booking = int(self.is_booking)

class TransitivePoint(Base):
	__tablename__ = 'transitive_points'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	airport = Column('airport', VARCHAR(45), nullable=False)
	arrival_date_time = Column('arrival_date_time', Date, nullable=False)
	departure_date_time = Column('departure_date_time', Date, nullable=False)
	flight_id = Column('flight_id', Integer, ForeignKey('flights.id'))

	def __init__(self, airport = None, arrival_date_time = None,
			 departure_date_time = None, flight_id = None):
		self.airport = airport
		self.arrival_date_time = arrival_date_time
		self.departure_date_time = departure_date_time
		self.flight_id = flight_id

	def __str__(self) -> str:
		return self.get_transitive_point().__str__()

	def get_transitive_point(self):
		return {
			'id': self.id,
			'airport': self.airport,
			'arrival_date_time': str(self.arrival_date_time),
			'departure_date_time': str(self.departure_date_time),
			'flight_id': self.flight_id
		}

	def str_to_datetime(self, str, format='%d-%m-%Y %H:%M:%S'):
		return datetime.strptime(str, format)

	def from_csvfile(self, header: str, data: str, sep=','):
		list_header = header.split(sep)
		list_data = data.split(sep)
		for header, data in zip(list_header, list_data):
				setattr(self, header, data)
				if header == 'departure_date_time':
					self.departure_date_time = Flight.str_to_datetime(self, data)
				if header == 'arrival_date_time':
					self.arrival_date_time = Flight.str_to_datetime(self, data)

class Airline(Base):
	__tablename__ = 'airlines'
	id = Column('id', Integer, primary_key=True, autoincrement=True)
	name = Column('name', VARCHAR(45), nullable=False)
	country = Column('country', VARCHAR(45), nullable=False)
	flights = relationship('Flight')

	def __init__(self, name = None, country = None):
		self.name = name
		self.country = country

	def __str__(self) -> str:
		return self.get_airline().__str__()

	def get_airline(self):
		return {
			'id': self.id,
			'name': self.name,
			'country': self.country
		}

	def from_csvfile(self, header: str, data: str, sep=','):
		list_header = header.split(sep)
		list_data = data.split(sep)
		for header, data in zip(list_header, list_data):
				setattr(self, header, data)