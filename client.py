import requests

body = {
    "HP": 106,
    "Attack": 110,
    "Defense": 90,
    "Sp_Atk": 154,
    "Sp_Def": 90,
    "Speed": 130,
    "BST": 680,
    "Mean": 113.3,
    "Standard_Deviation": 25.4,
    "Generation": 1,
    "Experience_to_level_100": 1250000,
    "Final_Evolution": 1,
    "Catch_Rate": 3,
    "Mega_Evolution": 0,
    "Alolan_Form": 0,
    "Galarian_Form": 0,
    "Against_Normal": 1,
    "Against_Fire": 1,
    "Against_Water": 1,
    "Against_Electric": 1,
    "Against_Grass": 1,
    "Against_Ice": 1,
    "Against_Fighting": 2,
    "Against_Poison": 1,
    "Against_Ground": 1,
    "Against_Flying": 1,
    "Against_Psychic": 1,
    "Against_Bug": 1,
    "Against_Rock": 1,
    "Against_Ghost": 1,
    "Against_Dragon": 2,
    "Against_Dark": 2,
    "Against_Steel": 1,
    "Against_Fairy": 1,
    "Height": 2.0,
    "Weight": 122,
    "BMI": 30.5
}

url = "http://127.0.0.1:8000/score"

try:
    response = requests.post(url, json=body)

    print("Status code:", response.status_code)

    # Intentar parsear JSON
    try:
        print("JSON response:", response.json())
    except Exception:
        print("Raw response (not JSON):")
        print(response.text)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
