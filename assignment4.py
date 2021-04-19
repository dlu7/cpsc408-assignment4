import mysql.connector
from faker import Faker
import csv

# generate data
def generate():
    fake = Faker()

    # user input for file name
    file_name = input("Enter a name for the file [ex. 'movies']: ")
    file = file_name + ".csv"

    # user input to choose how many records to generate
    num = int(input("Enter how many records you want to generate: "))

    # genres
    genre = ['action', 'animation', 'comedy', 'crime', 'drama', 'fantasy',
             'horror', 'musical', 'romance', 'science fiction', 'sports']

    # movie content rating
    content_rating = ['G', 'PG', 'PG-13', 'R', 'NC-17']

    # creating and writing to file
    with open(file, "w", newline = "") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['MovieID', 'MovieTitle', 'YearReleased', 'Genre', 'ContentRating',
                         'Director', 'RunningTime', 'Actor1', 'Actor2', 'Actor3', 'Actor4', 'AvgRating',
                         'UserID', 'FirstName', 'LastName', 'Email', 'UserRating', 'UserReview'])

        for x in range(num):
            writer.writerow([fake.pyint(min_value = 1, max_value = num),
                            fake.text(max_nb_chars = 30),
                            fake.year(),
                            fake.word(ext_word_list = genre),
                            fake.word(ext_word_list = content_rating),
                            fake.name(),
                            fake.time(),
                            fake.name(),
                            fake.name(),
                            fake.name(),
                            fake.name(),
                            fake.pydecimal(right_digits = 1, min_value = 1, max_value = 10),
                            fake.pyint(min_value=1, max_value=num),
                            fake.first_name(),
                            fake.last_name(),
                            fake.email(),
                            fake.pydecimal(right_digits = 1, min_value = 1, max_value = 10),
                            fake.sentences(nb = 3)])

        print("Generation of fake data complete.")

# establish database connection
db = mysql.connector.connect(
    host="34.94.182.22",
    user="myappuser",
    passwd="barfoo",
    database="dlu_db"
)

# executing MySQL statements
def import_data():
    mycursor = db.cursor()
    file = input("Enter file name to import data [ex. 'movies.csv']: ")
    with open(file) as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            # inserting by table in database

            # Movie Table
            movie_input = (row["MovieTitle"], row["YearReleased"], row["Genre"], row["ContentRating"],
                           row["Director"], row["RunningTime"], row["Actor1"], row["Actor2"], row["Actor3"],
                           row["Actor4"], row["AvgRating"])

            mycursor.execute("INSERT INTO Movie(Title, Year, Genre, ContentRating,"
                             "Director, RunningTime, Actor1, Actor2, Actor3, Actor4, AvgRating)"
                             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", movie_input)
            db.commit()

            # User Table
            user_input = (row["FirstName"], row["LastName"], row["Email"])
            mycursor.execute("INSERT INTO User(FirstName, LastName, Email)"
                             "VALUES (%s, %s, %s);", user_input)
            db.commit()

            # Planned Table
            planned_input = (row["UserID"], row["MovieID"])
            mycursor.execute("INSERT INTO Planned(UserID, MovieID)"
                             "VALUES (%s, %s);", planned_input)
            db.commit()

            # Watched Table
            watched_input = (row["UserID"], row["MovieID"])
            mycursor.execute("INSERT INTO Watched(UserID, MovieID)"
                             "VALUES (%s, %s);", watched_input)
            db.commit()

            # UserRating Table
            rating_input = (row["UserID"], row["MovieID"], row["UserRating"], row["UserReview"])
            mycursor.execute("INSERT INTO UserRating(UserID, MovieID, Rating, Review)"
                             "VALUES (%s, %s, %s, %s);", rating_input)
            db.commit()

        print("Import complete.")

# options
def main():
    print("\n           Options            ")
    print("--------------------------------")
    print("1. Generate fake data")
    print("2. Import data")
    print("3. Exit program")
    print("--------------------------------")
    return input("Choose a corresponding number: ")

# user is able to choose what they want to do and reprompt list of options until they quit
user_input = ""
while user_input != "3":
    user_input = main()

    if user_input == '1':
        generate()
    elif user_input == '2':
        import_data()
    elif user_input == '3':
        print("Goodbye!")
        quit()
    else:
        print("Invalid option, please try again.")

db.close()