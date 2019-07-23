from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger

restaurant1 = Restaurant(name="Urban Burger")
session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(name="Panda Green ")
session.add(restaurant1)
session.commit()

restaurant1 = Restaurant(name="Thyme for That Vegetarian Cuisine")
session.add(restaurant1)
session.commit()

restaurant1 = Restaurant(name="Tony's Bistro")
session.add(restaurant1)
session.commit()


restaurant1 = Restaurant(name="Andala's")
session.add(restaurant1)
session.commit()

restaurant1 = Restaurant(name="Auntie Ann's Dinner")
session.add(restaurant1)
session.commit()

restaurant1 = Restaurant(name="Cocina Y Amor")
session.add(restaurant1)
session.commit()


 