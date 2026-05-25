import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt

# Get api
load_dotenv()
api_key = os.environ.get("GEM_API_KEY")
if (api_key==None):
    raise RuntimeError("Bad api key")
client = genai.Client(api_key=api_key)

# Read user prompt
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("-v", "--verbose", action="store_true", help="Show verbose output")
args = parser.parse_args()

messages: list[types.Content] = [
    types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
]

# Get response
res = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

if args.verbose:    
    print(
      f"User prompt: {args.user_prompt}\n" \
      f"Prompt tokens: {res.usage_metadata.prompt_token_count}\n" \
      f"Response tokens: {res.usage_metadata.candidates_token_count}\n" \
      f"Response: {res.text}"
    )
else:
    print(res.text)
    