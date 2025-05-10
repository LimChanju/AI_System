import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

import gemini.config

load_dotenv()
gemini_key = os.getenv('GEMINI_KEY')
GeminiClient = genai.Client(api_key=gemini_key)

class gemini_judgment:
    def __init__(self):
        pass

    def malicious_reviews(self,review_data):
        gemini_config = gemini.config

        Gemini_model_name = gemini_config.Gemini_model_name
        system_instruction= gemini_config.system_instruction
        safety_settings = gemini_config.safety_settings

        review_data_string = json.dumps(review_data, ensure_ascii=False)

        response = GeminiClient.models.generate_content(
            model=Gemini_model_name,
            contents=review_data_string,
            config=types.GenerateContentConfig(
                candidate_count=1,temperature=0.75,
                system_instruction=system_instruction,
                safety_settings=safety_settings,))
        # csv파일 입력, json으로 출력, csv로 변환

        start_index = response.text.find('[')
        end_index = response.text.rfind(']')
        
        if start_index != -1 and end_index != -1 and start_index <= end_index:
            output_response = json.loads(response.text[start_index : end_index + 1])
        else:
            output_response = json.loads(response.text)

        return output_response