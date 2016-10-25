import media
import fresh_tomatoes
a_river = media.Movie(
    "A River Runs Through It",
    "two brothers growing up in Montana",
    "https://goo.gl/V2vZLV",
    "https://www.youtube.com/watch?v=9WHdEZbIRpc")  # noqa
up = media.Movie(
    "Up",
    "A lonely old man and an orphan scout go on a journey in a balllon-hoisted \
        house",
    "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
    "https://www.youtube.com/watch?v=qas5lWp7_R0")
kung_fu_panda = media.Movie(
    "Kung Fu Panda",
    "Po and the rest of his Furious-Five gang defend ancient China from a \
        villain",
    "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
    "https://www.youtube.com/watch?v=PXi3Mv6KMzY")
chicken_run = media.Movie(
    "Chicken Run",
    "A cocky American rooster saves the coup from turning into chicken pies",
    "https://upload.wikimedia.org/wikipedia/en/0/00/Chicken_run_ver1.jpg",
    "https://www.youtube.com/watch?v=jVdlxwX6A7g")
dr_zhivago = media.Movie(
    "Dr. Zhivago",
    "an epic from Russia in early twentieth century",
    "https://goo.gl/qlcwEI",
    "https://www.youtube.com/watch?v=wAWrXTn5Www")
modern_times = media.Movie(
    "Modern Times",
    "Charlie Chaplin illuminates industrialization",
    "http://www.moma.org/explore/inside_out/inside_out/wp-content/uploads/2010/11/Modern-Times.jpg",
    "https://www.youtube.com/watch?v=GLeDdzGUTq0")
ratatouille = media.Movie(
    "Rata Touille",
    "About the beauty of food and life in simplicity",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")
movies = [a_river, up, kung_fu_panda, chicken_run, dr_zhivago, modern_times,
          ratatouille]
fresh_tomatoes.open_movies_page(movies)
