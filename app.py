from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware

# Permitir CORS
origins = ["*"]

app = FastAPI(title="Pokémon Legendary Prediction")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Cargar el modelo entrenado
model = load(pathlib.Path("model/All_Pokemon-v1.joblib"))

# Definición de los datos de entrada (todas las columnas numéricas del CSV)
class InputData(BaseModel):
    HP: int
    Attack: int
    Defense: int
    Sp_Atk: int
    Sp_Def: int
    Speed: int
    BST: int
    Mean: float
    Standard_Deviation: float
    Generation: int
    Experience_to_level_100: int
    Final_Evolution: int
    Catch_Rate: int
    Mega_Evolution: int
    Alolan_Form: int
    Galarian_Form: int
    Against_Normal: float
    Against_Fire: float
    Against_Water: float
    Against_Electric: float
    Against_Grass: float
    Against_Ice: float
    Against_Fighting: float
    Against_Poison: float
    Against_Ground: float
    Against_Flying: float
    Against_Psychic: float
    Against_Bug: float
    Against_Rock: float
    Against_Ghost: float
    Against_Dragon: float
    Against_Dark: float
    Against_Steel: float
    Against_Fairy: float
    Height: float
    Weight: float
    BMI: float

# Respuesta de salida
class OutputData(BaseModel):
    score: float

@app.post("/score", response_model=OutputData)
def score(data: InputData):
    input_dict = data.dict()

    # Mantener el mismo orden de columnas que en entrenamiento
    ordered_values = [
        input_dict["HP"],
        input_dict["Attack"],
        input_dict["Defense"],
        input_dict["Sp_Atk"],
        input_dict["Sp_Def"],
        input_dict["Speed"],
        input_dict["BST"],
        input_dict["Mean"],
        input_dict["Standard_Deviation"],
        input_dict["Generation"],
        input_dict["Experience_to_level_100"],
        input_dict["Final_Evolution"],
        input_dict["Catch_Rate"],
        input_dict["Mega_Evolution"],
        input_dict["Alolan_Form"],
        input_dict["Galarian_Form"],
        input_dict["Against_Normal"],
        input_dict["Against_Fire"],
        input_dict["Against_Water"],
        input_dict["Against_Electric"],
        input_dict["Against_Grass"],
        input_dict["Against_Ice"],
        input_dict["Against_Fighting"],
        input_dict["Against_Poison"],
        input_dict["Against_Ground"],
        input_dict["Against_Flying"],
        input_dict["Against_Psychic"],
        input_dict["Against_Bug"],
        input_dict["Against_Rock"],
        input_dict["Against_Ghost"],
        input_dict["Against_Dragon"],
        input_dict["Against_Dark"],
        input_dict["Against_Steel"],
        input_dict["Against_Fairy"],
        input_dict["Height"],
        input_dict["Weight"],
        input_dict["BMI"],
    ]

    model_input = np.array(ordered_values).reshape(1, -1)

    # Predecir probabilidad de ser legendario
    result = model.predict_proba(model_input)[:, -1][0]

    return {"score": float(result)}
