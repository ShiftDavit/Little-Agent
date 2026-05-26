import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt
from functions.declarations import functions

def main():
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
    generate_content(client, messages, args.verbose)
    

def generate_content(
    client: genai.Client, messages: list[types.Content], verbose: bool
) -> None:
    content_config=types.GenerateContentConfig(
        tools=[functions],
        system_instruction=system_prompt
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=content_config,
    )
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        print("Response:")
        print(response.text)
        return

    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")

if __name__ == "__main__":
    main()