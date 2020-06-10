# get_data.py

import requests
import json

prod_path = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"

prod = requests.get(prod_path)
prod_data=json.loads(prod.text)

#with open(prod_path, "r") as json_file:
#    file_contents = json_file.read()

#products = json.loans(file_contents)

#print(type(prod_data))
#print(prod_data)

print("REQUESTING SOME DATA FROM THE INTERNET...")

print(prod_data['name'])



#--------------------------------------------


prod2_path = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"

prod2 = requests.get(prod2_path)
prod2_data = json.loads(prod2.text)

print(prod2_data)
print(type(prod2_data))

for x in prod2_data:
    print(f"{x['name']} (Product ID: {x['id']}")



#-----------------------------------------------------

gb_path = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"

gb = requests.get(gb_path)
gb_data = json.loads(gb.text)

#print(gb_data)
#print(gb_data.keys())

grades = [x['finalGrade'] for x in gb_data['students']]
#print(test)
#print(type(test))

min_grade = min(grades)
max_grade = max(grades)
avg_grade = sum(grades) / len(grades)

print(f"Min Grade: {min_grade}, Max Grade: {max_grade}, and Average Grade: {avg_grade:.2f}")
