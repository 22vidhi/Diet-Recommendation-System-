import os
import sys
from functools import lru_cache
from pathlib import Path

import pandas as pd
import requests

BACKEND_DIR = Path(__file__).resolve().parents[1] / "FastAPI_Backend"
DATASET_PATH = Path(__file__).resolve().parents[1] / "Data" / "dataset.csv"
sys.path.insert(0, str(BACKEND_DIR))

from model import output_recommended_recipes, recommend


class _LocalResponse:
    def __init__(self, payload):
        self._payload = payload

    def json(self):
        return self._payload


@lru_cache(maxsize=1)
def _load_dataset():
    return pd.read_csv(DATASET_PATH, compression="gzip")

class Generator:
    def __init__(
        self,
        nutrition_input: list,
        ingredients: list = None,
        params: dict = None,
    ):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients or []
        self.params=params or {'n_neighbors':5,'return_distance':False}

    def set_request(self,nutrition_input:list,ingredients:list,params:dict):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients
        self.params=params

    def generate(self,):
        request={
            'nutrition_input':self.nutrition_input,
            'ingredients':self.ingredients,
            'params':self.params
        }
        backend_url = os.getenv("BACKEND_URL")
        if backend_url:
            response = requests.post(
                url=f"{backend_url.rstrip('/')}/predict/",
                json=request,
                timeout=60,
            )
            response.raise_for_status()
            return response

        recommendations = recommend(
            _load_dataset(),
            self.nutrition_input,
            self.ingredients,
            self.params,
        )
        return _LocalResponse(
            {"output": output_recommended_recipes(recommendations)}
        )
