"""
    Project name: Assignment 2
    File name: CharacterCreator.py
    Author: Patrick D
    DTG created: 14 1423 (Z-4) July 2020
    DTG last modification: 22 1534 (Z-4) July 2020
    Python Version: 3.7.4
    Description: Create a character for a video game
    Classes: Char, RaceElf(Char)
"""
# Import requests package
import requests

# Declare global variables
api_call = "https://api.github.com/search/repositories?q=language:python&sort=stars"

# Create global functions
def make_api_call(api_call):
    """Request repos from Github sorted by stars, and return total repo count"""
    # Declare API variables
    # API call to github
    response = requests.get(api_call)
    response_dict = response.json()
    # Set attack strength to total count of number of repositories
    return response_dict['total_count']


def create_obj():
    """Instantiate objects from user input"""
    char_list = list()  # Create an empty list to store RaceElf objects
    # Set number of characters to create via user input
    n = int(input("Enter the number of characters to create>> "))
    # Iterate through range of number of characters and append to the list
    for i in range(n):
        name = input("Enter character name>> ")
        char_list.append(RaceElf(name))
    # Iterate through created list of character objects and print their description
    for char in char_list:
        RaceElf.describe_elf_modifiers(char)


# Declaring class name
class Char:
    """Create a new character"""
    # Class constructor
    # Parameters: self, character name
    def __init__(self, name):
        self.name = name
        self.a_s = make_api_call(api_call)


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

    # Create function to display the object's description
    def describe_elf_modifiers(self):
        """Print statement describing elven race modifiers"""
        print(f"The elf, {self.name}, has a +{self.stealth_modifier} stealth modifier, and an attack"
              f" strength of {self.a_s}")


# Create main function for program execution
def main():
    create_obj()


main()
