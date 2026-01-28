from google import genai

# genai.configure(api_key="YOUR_API_KEY_HERE")

client = genai.Client(api_key="YOUR_API_KEY_HERE")

model = genai.GenerativeModel("gemini-1.5-flash")


def ask_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Sorry, something went wrong with Gemini API."
    