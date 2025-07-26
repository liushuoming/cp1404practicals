

class Band:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, musician):
        """Add a Musician to the band."""
        self.members.append(musician)

    def __str__(self):
        members_str = ', '.join(str(member) for member in self.members)
        return f"{self.name} ({members_str})"

    def play(self):
        for member in self.members:
            if member.instruments:  # assuming Musician has an 'instruments' list
                for instrument in member.instruments:
                    print(f"{member.name} is playing: {instrument}")
            else:
                print(f"{member.name} needs an instrument!")
