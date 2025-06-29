from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return " hy i am fastapi that is my "