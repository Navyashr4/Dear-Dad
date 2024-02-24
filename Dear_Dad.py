import random

class Activity():
    def __init__(self) -> None:
        self.energies = ["coquette", "dark academia"]
        self.places = ["Harper", "home"]
        self.verbs = ["Cook"]
    
    def generate_activity_prompt(self):
        # Randomly pick parameters
        energy = random.choice(self.energies)
        place = random.choice(self.places)
        verb = random.choice(self.verbs)

        # Construct and return the prompt
        prompt = f"{verb.capitalize()} at {place}. {energy.capitalize()}!"
        return prompt

    def add_energy(self, energy):
        self.energies.append(energy)
    
    def add_verb(self, verb):
        self.verbs.append(verb)
    
    def add_place(self, place):
        self.places.append(place)


if __name__ == "__main__":
    # Generate and print the activity prompt
    activity = Activity()
    activity_prompt = activity.generate_activity_prompt()
    print(activity_prompt)
