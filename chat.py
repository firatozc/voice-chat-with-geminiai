import google.generativeai as genai
from voice import text_to_speech
import API
import re

genai.configure(api_key=API.api)

generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  safety_settings=safety_settings,
)


chat_session = model.start_chat(
    history=[]
)


print("Gemini: Hello, how can I help you?")
print()
# text_to_speech("Hello, How can I help you", API.eleven_labs_api)

while True:

    user_input = input("You: ")
    print()

    response = chat_session.send_message(user_input)

    model_response = response.text
    model_response = re.sub(r"\*", "", model_response)

    print(f'Gemini: {model_response}')
    print()
    # text_to_speech(model_response, API.eleven_labs_api)
