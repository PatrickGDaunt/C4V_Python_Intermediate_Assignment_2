"""
    Project name: Assignment 2
    File name: CharacterCreator.py
    Author: Patrick D
    DTG created: 14 1423(Z-4) July 2020
    DTG last modification: 16 2112(Z-4) July 2020
    Python Version: 3.7.4
    Description: Create a character for a video game
    Classes: Char, RaceElf(Char)
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
