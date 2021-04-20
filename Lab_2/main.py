from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from controllers.controllers import Controller
from models.models import Base
from csv_writer import *

def main():
	csv_generator = CSV_generator()
	csv_generator.generate_all_csv(filename='data.csv')
	sess = connect_to_sqlite_db()
	controller = Controller(sess)
	controller.load_from_csv('data.csv')
	sess.commit()
	print('\n-------Airlines table--------\n')
	for airline in controller.select_airlines()[:10]:
		print(airline)
	print('\n-------Flights table--------\n')
	for flight in controller.select_flights()[:10]:
		print(flight)
	print('\n-------Tickets table--------\n')
	for ticket in controller.select_tickets()[:10]:
		print(ticket)
	print('\n-------Transitive Points table--------\n')
	for transitive_points in controller.select_transitive_points()[:10]:
		print(transitive_points)

def connect_to_sqlite_db(path_db = 'flight.db'):
    engine = create_engine('sqlite:///' + path_db, echo = True)
    Base.metadata.drop_all(bind = engine)
    Base.metadata.create_all(bind = engine)
    Session = sessionmaker(bind = engine)
    return Session()

if __name__ == '__main__':
    main()

