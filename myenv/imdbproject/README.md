IMDB
----

The Internet Movie Database is an online database of information related to films, television programs, tv-shows etc.

Getting Started with IMDB
-------------------------

For a standard installation please follow the /imdbproject/requirement.txt file.

Functionality
-------------

In this project 2 level of acccess are there.

1 Admin Level
	- Add movie
	- Remove movie
	- Edit movie

2 User Level
	- View movie

Features
--------

From User Interface
-------------------

Home Page:

	1 User can create a new account and login into this site.

Movie Info Page:

	1 Without login user can not see movie information.
	2 After login user can see all movie information like movies name, director, score, popularity and genre.

Search Movie Page:

	1 Without login user can see only few informations like movie name, director and genre.

	2 I have included search criteria by movie name and director.

	For eg: Search by 
	Movie Name = Titanic

	Movie Name	 Director		Genre
	Titanic		 James Cameron	[u'Drama', u'History', u'Romance']

	Director Name = James Cameron

	Movie Name					Director		Genre
	Titanic						James Cameron	[u'Drama', u'History', u'Romance']
	The Terminator				James Cameron	[u'Action', u'Sci-Fi', u'Thriller']
	Aliens						James Cameron	[u'Action', u'Sci-Fi', u'Thriller']
	Terminator 2 : Judgment Day	James Cameron	[u'Action', u'Sci-Fi', u'Thriller']

Contact Page:

	Users can contact to the imdb administrator via send him/her feedback.

Dropdown Link:

	When user is login at that time only Logout link will show to logout from your account.
	When user signout, Signup and Login link link will show to login to the account or signup to this site.









