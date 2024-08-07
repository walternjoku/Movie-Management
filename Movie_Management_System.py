import random

class Movies:

    #the constructor method sets the direction of the movie methods and operations
    def __init__(self, title, year, genre, release_date, movie_ID):
        self.title = title
        self.year = year
        self.genre = genre
        self.release_date = release_date
        self.movie_ID = movie_ID 


    #the code sets the title of the movie
    def set_title(self, title):
        self.title = title

    #the code below sets the year of the movie
    def set_year(self, year):
        self.year = year

    #the code sets the genre of the movie
    def set_genre(self, genre):
        self.genre = genre

    #the code sets the release date of the movie
    def set_release_date(self, release_date):
        self.release_date = release_date

    #the code sets the movie_ID
    def set_movie_ID(self):
        self.movie_ID = movie_ID

    #the code below returs the title of the movie to the user
    def get_title(self):
        return self.title

    #the method below returns the year of the movie to the user
    def get_year(self):
        return self.year

    #the code returns the genre of the movie to the user
    def get_genre(self):
        return self.genre

    #the code returns the release date of the movie
    def get_release_date(self):
        return self.release_date

    #the code below returns a movie_ID with a continously randomized number
    def get_movie_ID(self):
        return self.movie_ID

    #the code below returns the movie details to the user
    def get_movie_details(self):
        return (f"{self.title}, {self.year}, {self.genre}, {self.release_date}, {self.movie_ID}")


class MovieList(Movies):

    #The empty list below, collects the list of movies 
    list_of_movies = []

    #the constructor method sets the direction of the MovieList operations
    def __init__(self, title, year, genre, release_date, movie_ID):
        super().__init__(title, year, genre, release_date, movie_ID)#the __init__contructor super() inherits all the methods and operations of the class Movies

    #The add movie method add movies to the list via their title and can be accessed via title, year, genre, and release_date
    def add_movie(self, title, year, genre, release_date):
        self.list_of_movies.append(title)

    #the get all movies returns all the movies in a list via their title
    def get_all_movies(self):
        return (str(self.list_of_movies).upper())

    #The method removes a movie or movies from the list
    def remove_movie(self, title):

        retain = "yes"
        delete = "no"

        #The variable m checks for repeated movie titles
        m = self.list_of_movies.count(self.title)

        if m == 1:
            return (self.list_of_movies.remove(title)), print((str(self.list_of_movies).upper()))
         #The code below informs the user if there are more than one name in the list with the option of removing one or keeping both
        elif m >= 2:
            print((f"The movies' title {title} appeared more than once in the list."))
            r = input("Type yes to keep both of them or no to remove one of them: ")
            if (r.lower()).strip() == (retain.lower()).strip():#This code ensures that the users input to keep both duplicates is implemented
                print("Great! Both movies are kept.")
                print((str(self.list_of_movies).upper()))#This code returns the list_of_movies without removing the duplicate
            elif (r.lower()).strip() == (delete.lower()).strip():#This code ensures that the users input to remove one duplicate is implemented
                self.list_of_movies.remove(title),print((str(self.list_of_movies).upper()))#This code returns the list_of_movies after removing the duplicate
            else:
                print()
        else:
            print()


    #the count method returns the number of movies in the list of movies that have been added
    def calculate_number_of_movies(self):
        return len(self.list_of_movies)


class Actors:

    #the constructor method sets the direction of the actors methods and operations
    def __init__(self, first_name, surname, gender, date_of_birth):
        self.first_name = first_name
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth

    #the code below sets the firstname of the actor
    def set_first_name(self, first_name):
        self.first_name = first_name

    #the code below sets the surname of the actor
    def set_surname(self, surname):
        self.surname = surname

    #the code sets the gender of the actor
    def set_gender(self, gender):
        self.gender = gender

    #the code below sets the date of birth of the actor
    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    #the code below returns the firstname of the actor
    def get_first_name(self):
        return (self.first_name).upper()

    #the code returns the surname of the actor
    def get_surname(self):
        return (self.surname).upper()

    #the code forms the fullname of the actor by a combination of his firstname and surname
    def get_fullname(self):
        return (f"{self.first_name}" + " " + f"{self.surname}").upper()

    #the code returns the gender of the actor
    def get_gender(self):
        return (self.gender).upper()

    #the code below returns the date of birth of the actor
    def get_date_of_birth(self):
        return (self.date_of_birth).upper()

    #the get_email constructs email based on the actors firstname and surname with a . inbetween
    def get_email(self):
        return (f"{self.first_name}" "." f"{self.surname}" + "@hollywood.com").lower()

class ActorsList(Actors):

    #The empty list below, collects the list of actors 
    list_of_actors = []

    #the constructor method sets the direction of the ActorsList operations
    def __init__(self, first_name, surname, gender, date_of_birth):
        super().__init__(first_name, surname, gender, date_of_birth)#the __init__contructor super() inherits all the methods and operations of the class Actors

    #The add actors method add actors to the list via their firstnames
    def add_actors(self, first_name):
        self.list_of_actors.append(first_name)

    #the get all actors returns all the actors in a list via their firstnames
    def get_all_actors(self): 
        return (str(self.list_of_actors).upper())

    #The remove method removes one or more actors' name and informs the user to choose whether to keep or remove an actors name that occured more than once
    def remove_actor(self, first_name):
        keep = "yes"
        remove = "no"

        #The variable x checks for repeated actors' first_names  
        x = self.list_of_actors.count(self.first_name)

        #The statement removes an actor from the list_of_actors if the appeared only once and returns the remaining list
        if x == 1:
            return (self.list_of_actors.remove(first_name)), print((str(self.list_of_actors).upper()))

        #The code below informs the user if there are more than one name in the list with the option of removing one or keeping both
        elif x >= 2:
            print((f"The actors' firstname {first_name} appeared more than once in the list."))
            q = input("Type yes to keep both of them or no to remove one of them: ")
            if (q.lower()).strip() == (keep.lower()).strip():#This code ensures that the users input to keep both duplicates is implemented
                print("Great! Both actors are kept.")
                print((str(self.list_of_actors).upper()))#This code returns the list_of_actors without removing the duplicate
            elif (q.lower()).strip() == (remove.lower()).strip():#This code ensures that the users input to remove one duplicate is implemented
                self.list_of_actors.remove(first_name),print((str(self.list_of_actors).upper()))#This code returns the list_of_actors after removing the duplicate
            else:
                print()
        else:
            print()

    #the count method returns the number of actors in the list of actors that have been added
    def count_number_of_actors(self):
        return (f"The number of actors is {len(self.list_of_actors)}")

    #the code below returns the actors details to the user
    def access_actors_details(self, first_name):
        return (f"The actors' first name is, {self.first_name}, his surname is, {self.surname}, he's of a {self.gender} gender, and his date of birth is {self.date_of_birth}.")





