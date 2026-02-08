from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    text: str

@app.post("/analyze-code")
def analyze_code(data: InputData):

    prompt = f"""
    Analyze the following code for SECURITY vulnerabilities only.
    Provide vulnerabilities and fixes.

    Code:
    {data.text}
    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    try:
        output_text = response.text
    except:
        output_text = response.candidates[0].content.parts[0].text

    return {"result": output_text}


@app.post("/analyze-specs")
def analyze_specs(data: InputData):

    prompt = f"""
    Given this GenAI system specification:

    {data.text}

    Identify potential vulnerabilities mapped to:
    - OWASP Top 10 for LLM Apps
    - ATLAS Perspective

    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    try:
        output_text = response.text
    except:
        output_text = response.candidates[0].content.parts[0].text

    return {"result": output_text}