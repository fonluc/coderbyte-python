import requests

def age_counting():
    result = requests.get('<https://coderbyte.com/api/challenges/json/age-counting>')
    response = result.json()["data"].split(",")
    count = 0
    for res in response:
        data = res.split("=")
        if data[0].strip() == 'age' and int(data[1]) >= 50:
            count += 1
    return count