from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List,Optional
import pandas as pd
from model import recommend,output_recommended_recipes


dataset=pd.read_csv('../Data/dataset.csv',compression='gzip')

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class params(BaseModel):
    n_neighbors:int=5
    return_distance:bool=False

class PredictionIn(BaseModel):
    nutrition_input: List[float]
    ingredients: List[str] = []
    params: Optional[dict] = None


class Recipe(BaseModel):
    Name: str
    CookTime: float  # Changed from str to float
    PrepTime: float  # Changed from str to float
    TotalTime: float  # Changed from str to float
    RecipeIngredientParts: List[str]
    Calories: float
    FatContent: float
    SaturatedFatContent: float
    CholesterolContent: float
    SodiumContent: float
    CarbohydrateContent: float
    FiberContent: float
    SugarContent: float
    ProteinContent: float
    RecipeInstructions: List[str]

class PredictionOut(BaseModel):
    output: Optional[List[Recipe]] = None


@app.get("/")
def home():
    return {"health_check": "OK"}


@app.post("/predict/",response_model=PredictionOut)
def update_item(prediction_input:PredictionIn):
    # Handle params - use default if None
    if prediction_input.params is None:
        params_dict = {'n_neighbors': 5, 'return_distance': False}
    else:
        params_dict = prediction_input.params

    recommendation_dataframe=recommend(dataset,prediction_input.nutrition_input,prediction_input.ingredients,params_dict)
    output=output_recommended_recipes(recommendation_dataframe)
    if output is None:
        return {"output":None}
    else:
        return {"output":output}

