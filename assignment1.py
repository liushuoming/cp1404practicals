def main():
    print("Must-See Movies 1.0 - by Your Name")
    movies = load_movies(FILENAME)
    print(f"{len(movies)} movies loaded from {FILENAME}")
