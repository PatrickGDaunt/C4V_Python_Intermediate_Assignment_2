'''
    Project name: Assignment 2
    File name: Test.py
    Author: Patrick D
    DTG created: 16 2224 (Z-4) July 2020
    DTG last modification: 16 2230 (Z-4) July 2020
    Python Version: 3.7.4
    Description: Test cases and unit tests for CharacterCreator.py
    Classes:
'''
# Importing all the required packages
import requests
import unittest

def make_api_call(api_call):
    """Request repos from Github sorted by stars, and return total repo count"""
    # Declare API variables
    # API call to github
    response = requests.get(api_call)
    response_dict = response.json()
    # Set attack strength to total count of number of repositories
    return response_dict['total_count']

class unitTest(unittest.TestCase):
    """Creating the unit test class"""
    # Defining a test function and passing self
    def test_api_call(self):
        api_call = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        # Create variable to hold output
        output = make_api_call(api_call)
        self.assertEqual(output, 5387258)

def main():
    print(make_api_call("https://api.github.com/search/repositories?q=language:python&sort=stars"))


main()







