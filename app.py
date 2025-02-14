from fastapi import FastAPI
from num2words import num2words
from mangum import Mangum

app = FastAPI()

@app.get("/convert/{number}")
def convert_number(number: int):
    try:
        text_representation = num2words(number, lang='pt')
        return {"number": number, "text": text_representation}
    except Exception as e:
        return {"error": str(e)}

handler = Mangum(app)  # Adaptador para AWS Lambda
