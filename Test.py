'''
    Project name: Assignment 2
    File name: Test.py
    Author: Patrick D
    DTG created: 16 2224(Z-4) July 2020
    DTG last modification: 16 2230(Z-4) July 2020
    Python Version: 3.7.4
    Description: Test cases and unit tests for CharacterCreator.py
    Classes:
'''
# Importing all the required packages
import requests
apicall = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(apicall)
rDict = r.json()
numRepos = rDict["total_count"]
print(numRepos)