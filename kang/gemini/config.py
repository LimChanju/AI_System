from google.genai import types

#gemini-2.0-flash
#gemini-2.5-flash-preview-04-17
Gemini_model_name = 'gemini-2.0-flash'
system_instruction="<Required> **Write in JSON format**"\
                    "1. Predict the \'score\'(star rating) of each review"\
                    "2. The more dishonesty a review is, the higher its \'score\'. Here's an example"\
                    "2-1. Ad-formatted reviews"\
                    "2-2. Viral ads (unidentified)"\
                    "2-3. review bomb"\
                    "2-4. undermining(sabotage) review"\
                    "2-5. (Malicious) review attack"\
                    "3. The \'score\' is a maximum of 10 points, a minimum of 1 point, and a float up to 1 digit"\
                    "4. The type of key: order, review score, dishonesty score"\
                    "4-1. Don't put review in key"
safety_settings = [
    types.SafetySetting(
        category="HARM_CATEGORY_HATE_SPEECH",
        threshold="BLOCK_MEDIUM_AND_ABOVE"
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_HARASSMENT",
        threshold="BLOCK_MEDIUM_AND_ABOVE"
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_DANGEROUS_CONTENT",
        threshold="BLOCK_MEDIUM_AND_ABOVE"
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
        threshold="BLOCK_MEDIUM_AND_ABOVE"
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_CIVIC_INTEGRITY",
        threshold="BLOCK_MEDIUM_AND_ABOVE"
    )
]