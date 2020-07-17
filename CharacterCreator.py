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
# Import requests package
import requests

# API call to github
APICALL = "https://api.github.com/search/repositories?q=language:python&sort=stars"

# Declare API variables
response = requests.get(APICALL)
responseDict = response.json()

# Set attack strength to total count of number of repositories
attack_strength = responseDict['total_count']

# Declaring class name
class Char:
    """Create a new character"""

    # Class constructor
    # Parameters: self, character name
    def __init__(self, name):
        self.name = name
        response = requests.get(APICALL)
        self.a_s = attack_strength

# Declare child class to Char
class RaceElf(Char):
    """Class for general class actions"""
    # Class constructor
    # Parameters: self, name for parent class
    def __init__(self, name):
        # Call init method from parent class Char
        super().__init__(name)
        # Child class attribute stealth modifier
        self.stealth_modifier = 2

    def describe_elf_moodifiers(self):
        """Print statement describing elven race modifiers"""
        print(f"The elf, {self.name}, has a +{self.stealth_modifier} stealth modifier, and an attack"
              f" strength of {self.a_s}")

# Create elf object
elf1 = RaceElf("Legolas")
# Print description of elf1 modifiers
print(elf1.describe_elf_moodifiers())
