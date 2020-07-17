"""
    Project name: Assignment2
    Author: Patrick D
    Date created: 2020-07-16
    Date last modified: 2020-07-16
    Python Version: 3.7.4
    Purpose: Create characters for a game with user input
"""


# Declaring class name
class Char:
    """Create a new character"""

    # Class constructor
    def __init__(self, name):
        self.name = name


class RaceElf(Char):
    """Class for general class actions"""
    # Class constructor
    def __init__(self, name):
        # Call init method from parent class Char
        super().__init__(name)
        # Child class attribute stealth modifier
        self.stealth_modifier = 2

    def describe_elf_moodifiers(self):
        """Print statement describing elven race modifiers"""
        print(f"The elf, {self.name}, has a +{self.stealth_modifier} stealth modifier")

# Create elf object
elf1 = RaceElf("Legolas")
# Print description of elf1 modifiers
print(elf1.describe_elf_moodifiers())
