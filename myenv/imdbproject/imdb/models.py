from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField

# Create your models here.
GENRE_CHOICES = (
				('Action', 'action'),
				('Adult', 'adult'),
				('Adventure', 'adventure'),
				('Animation', 'animation'),
				('Biography', 'biography'),
				('Comedy', 'comedy'),
				('Crime', 'crime'),
				('Documentary', 'documentary'),
				('Drama', 'drama'),
				('Family', 'family'),
				('Fantasy', 'fantasy'),
				('Film-Noir', 'film-Noir'),
				('Game-Show', 'game-Show'),
				('Historical', 'historical'),
				('Historical Fiction', 'historical Fiction'),
				('Horror', 'horror'),
				('Music', 'music'),
				('Musical', 'musical'),
				('Mystery', 'mystery'),
				('News', 'news'),
				('Reality-TV', 'reality-TV'),
				('Romance', 'romance'),
				('Sci-Fi', 'sci-Fi'),
				('Short', 'short'),
				('Sport', 'sport'),
				('Talk-Show', 'talk-Show'),
				('Thriller', 'thriller'),
				('War', 'war'),
				('Western', 'western'),
			)

class Movieinfo(models.Model):
	"""docstring for Movieinfo"""
	popularity = models.FloatField('Popularity', validators = [MinValueValidator(0.0), MaxValueValidator(100.0)])
	director = models.CharField('Director', max_length=100)
	imdb_score = models.FloatField('Score', validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
	name = models.CharField('Name', max_length=100)
	genre = MultiSelectField('Genre', choices=GENRE_CHOICES,
							null=True, blank=True)

	def __str__(self):
		return '%s - %s - %s - %s - %s' %(self.name, self.director, self.imdb_score, self.popularity, self.genre)
