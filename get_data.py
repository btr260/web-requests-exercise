# get_data.py

import json

prod_path = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"

with open(prod_path, "r") as json_file:
    file_contents = json_file.read()

products = json.loans(file_contents)

print(type(products))
print(products)



print("REQUESTING SOME DATA FROM THE INTERNET...")
