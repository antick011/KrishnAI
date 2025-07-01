# utils.py
from model import load_dataset
import random

dataset = load_dataset()

def get_krishna_quote(emotion):
    matching_quotes = [item for item in dataset if item["emotion"] == emotion]
    if matching_quotes:
        return random.choice(matching_quotes)
    return {
        "sanskrit": "🙏 कृष्ण ध्यानस्थ हैं...",
        "translation": "Krishna is meditating. Please try again later.",
        "response": "🙏 KrishnaAI is meditating... Please try again later."
    }
