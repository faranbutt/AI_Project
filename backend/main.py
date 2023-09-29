from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def faran():
    return {"message":"Hello World"}