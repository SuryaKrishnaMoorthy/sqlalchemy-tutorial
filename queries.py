from datetime import date

from actor import Actor
from contact_details import ContactDetails
from movie import Movie
from base import Session

session = Session()

movies = session.query(Movie) \
    .filter(Movie.release_date > date(2015, 1, 1)) \
    .all()

print('###Recent movies')
for movie in movies:
    print(f'{movie.title} was released on after 2015')
print('')

the_rock_movies = session.query(Movie) \
    .join(Actor, Movie.actors) \
    .filter(Actor.name == 'Dwayne Johnson') \
    .all()

print('###Dwayne Johnson movies')
for movie in the_rock_movies:
    print(f'The Rock starred in {movie.title}')
print('')

glendale_stars = session.query(Actor) \
    .join(ContactDetails) \
    .filter(ContactDetails.address.ilike('%glendale%')) \
    .all()

print('###Actors living in Glendale')
for actor in glendale_stars:
    print(f'{actor.name} lives in Glendale')
print('')
