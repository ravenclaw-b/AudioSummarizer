
from openai import OpenAI
import dotenv
import os
import whisper

# Define the path for the input file
path = input("audio file path: ")

#load transcribe the file
model = whisper.load_model("base")
transcript = model.transcribe(path)
print("file transcribed")

# Load the API key from environment variables
dotenv.load_dotenv()
KEY = os.getenv("KEY")

# Create an instance of the OpenAI client
client = OpenAI(api_key=KEY)

# Write the transcript to a file
with open("transcript.txt", "w+") as f:
   f.write(transcript["text"])

# Define a function to summarize the transcript
def summarize(transcript):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": """Your name is AUSUM. You are an audio summerizing program. You will take a transcrpt of a lesson and return a highly detailed summery of what happened. Keep in mind that the transcript is made automatically and may be incorrect,
                so please disregard nonesense in the transcript. You are designed to be used in school, and may make flashcard, quizzes, and tests based on the material given. You may answer questions based on the material given. """
            },
            {
                "role": "user",
                "content": transcript
            }
        ]
    )
    return response.choices[0].message.content

# Write the summarized text to a file
with open("summary.txt", "w") as f:
    f.write(summarize(transcript["text"]))
print("summery outputted in summery.txt")