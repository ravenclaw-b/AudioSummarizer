
# %%
from openai import OpenAI
import dotenv
import os
import whisper
# %%

#load transcribe the file
model = whisper.load_model("base")
transcript = model.transcribe("pyCut.mp3")

# %%
# Load the API key from environment variables
dotenv.load_dotenv()
KEY = os.getenv("KEY")
# %%

# Create an instance of the OpenAI client
client = OpenAI(api_key=KEY)

# Define the path for the output file
path = "pyCut.mp3"

# Write the transcript to a file
with open("transcript.txt", "w+") as f:
   f.write(transcript["text"])
# %%
   
# Define a function to summarize the transcript
def summarize(transcript):
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": """You are a highly skilled AI trained in language comprehension and 
                summarization. I would like you to read the following text and summarize it into a 
                concise abstract paragraph. Aim to retain the most important points, providing a 
                coherent and readable summary that could help a person understand the main points 
                of the discussion without needing to read the entire text. Please avoid unnecessary 
                details or tangential points."""
            },
            {
                "role": "user",
                "content": transcript
            }
        ]
    )
    return response.choices[0].message.content

# Write the summarized text to a file
with open("summary2.txt", "w") as f:
    f.write(summarize(transcript["text"]))