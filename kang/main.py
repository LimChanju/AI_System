import gemini.judgment as judgment
import os
import json

def main():
    review_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"review.json")
    with open(review_path, 'r') as f:
        review_data = json.load(f).copy()

    output_response = judgment.gemini_judgment().malicious_reviews(review_data)

    review_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"output.json")
    with open(review_path, 'w') as f:
        review_data = json.dump(output_response,f)

if __name__ == '__main__':
    main()