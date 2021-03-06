import media
import fresh_tomatoes


toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = media.Movie(
    "Avatar", "A marine on an alien planet",
    "https://sco.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print(avatar.storyline)

first_man = media.Movie(
    "First Man", "NASA's mission to land a man on the moon",
    "https://en.wikipedia.org/wiki/File:First_Man_(film).png",
    "https://www.youtube.com/watch?v=w4GtJB5WAlQ")
#first_man.show_trailer()

school_of_rock = media.Movie(
    "School of Rock", "Using rock music to learn",
    "http://upload.wikimedia.org/wikipedia/en/1/11School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie(
    "Ratatouille", "A rat dreams of being a chef",
    "http://upload.wikimedia.org/wikipedia/en/5/50RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie(
    "Midnight in Paris", "Storyline",
"http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
    "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie(
    "Hunger Games", "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris,
          hunger_games]
# creates movie website
#fresh_tomatoes.open_movies_page(movies)
# print class documentation
print(media.Movie.__doc__)
# print class name
print(media.Movie.__name__)
# print module where class was defined
print(media.Movie.__module__)