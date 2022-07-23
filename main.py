# import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from Similarity import *

app = FastAPI()

class inputs(BaseModel):
    sentence_1: str
    sentence_2: str

@app.post('/show_data')
def show_data(data: inputs):
    return ({"data": [data.sentence_1, data.sentence_2]})

@app.post('/similarity_score')
def similarity_score(data: inputs):
    return sentence_similarity(data.sentence_1,data.sentence_2)


# # create a FastAPI instance
# app = FastAPI()
#
#
# # create a path operation
# @app.get("/")
# # define the path operation function
# def root():
#     return {"message": "Hello World"}