import requests

body = {
    "Number": 19,
    "HP": 30,
    "Att": 56,
    "Def": 35,
    "Spa": 25,
    "Spd": 35,
    "Spe": 72,
    "BST": 253,
    "Mean": 42.2,
    "Standard_Deviation": 15.3,
    "Generation": 1,
    "Experience_to_level_100": 1000000,
    "Final_Evolution": 0,
    "Catch_Rate": 255,
    "Mega_Evolution": 0,
    "Alolan_Form": 1,
    "Galarian_Form": 0,
    "Against_Normal": 1.0,
    "Against_Fire": 1.0,
    "Against_Water": 1.0,
    "Against_Electric": 1.0,
    "Against_Grass": 1.0,
    "Against_Ice": 1.0,
    "Against_Fighting": 2.0,
    "Against_Poison": 1.0,
    "Against_Ground": 1.0,
    "Against_Flying": 1.0,
    "Against_Psychic": 1.0,
    "Against_Bug": 1.0,
    "Against_Rock": 1.0,
    "Against_Ghost": 0.0,
    "Against_Dragon": 1.0,
    "Against_Dark": 1.0,
    "Against_Steel": 1.0,
    "Against_Fairy": 1.0,
    "Height": 0.3,
    "Weight": 3.5,
    "BMI": 38.9
}

response = requests.post("http://127.0.0.1:8000/score", json=body)

print("Status code:", response.status_code)
try:
    print("Response:", response.json())
except Exception:
    print("Raw response:", response.text)
