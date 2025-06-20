

FILENAME = "wimbledon.csv"


def read_wimbledon_data(filename):
    """Read the CSV file and return a list of rows, excluding the header."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip the header
        return [line.strip().split(",") for line in in_file]


def count_champions(data):
    """Return a dictionary of champions and their win counts."""
    champion_to_wins = {}
    for year, country, champion in data:
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def get_countries(data):
    """Return a sorted set of unique countries."""
    return sorted({country for _, country, _ in data})


def main():
    """Main program to process and display Wimbledon champions data."""
    data = read_wimbledon_data(FILENAME)

    champion_to_wins = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_to_wins.items()):
        print(f"{champion} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()
