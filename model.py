import json
import random
import re

# Load Krishna dataset
def load_dataset(path='krishna_dataset.json'):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Advanced emotion detection using weighted keyword matching
def detect_emotion(user_input):
    input_lower = user_input.lower()
    emotion_scores = {}

    keywords = {
        "grief": ["death", "died", "dead", "dying", "grieve", "grieving", "sad", "cry", "crying", "tears", "mourning", "sorrow", "miss", "missing", "heartbroken"],
        "loss": ["loss", "lost", "gone", "leaving", "left me", "no more", "end", "goodbye", "departed", "taken away"],
        "failure": ["fail", "failed", "failing", "failure", "not working", "didn't", "error", "messed up", "can't succeed", "can't do it", "blunder"],
        "hope": ["hope", "believe", "faith", "maybe", "possible", "miracle", "trust", "still a chance", "can happen", "light", "believing", "not over"],
        "confusion": ["confused", "confusing", "why", "how", "unclear", "don't get", "no idea", "unsure", "doubt", "mixed up", "uncertain"],
        "karma": ["work", "working", "duty", "duties", "action", "actions", "deed", "responsibility", "task", "job", "obligation", "what should I do"],
        "desire": ["want", "wants", "wanted", "desire", "desires", "wish", "wishes", "need", "needs", "craving", "longing", "yearning"],
        "detachment": ["detached", "let go", "leave behind", "move on", "move forward", "release", "disconnected", "free from", "not attached", "unclinging"],
        "surrender": ["give up", "giving up", "gave up", "can't", "cannot", "help me", "surrender", "I quit", "I can't anymore", "I'm done", "too tired", "breakdown", "helpless", "overwhelmed", "defeated"],
        "inner strength": ["strong", "stronger", "strength", "resilience", "power", "powerful", "inner power", "stand again", "endure", "bounce back", "keep going"],
        "provision": ["provide", "provided", "protect", "protects", "help", "support", "care", "give", "sustain", "guardian", "watching over"],
        "intimacy": ["close", "near", "heart", "love", "guiding", "with me", "never alone", "by my side", "personal bond", "holding me"],
        "devotion": ["devotion", "bhakti", "faithful", "worship", "pray", "offering", "serve", "serving", "chant", "praise", "ritual"],
        "awe": ["destroyer", "end of time", "fearful", "all powerful", "great destroyer", "overwhelming", "terrifying", "majestic", "supreme force"],
        "self-discipline": ["control", "discipline", "master", "conquer", "self-control", "tame", "restrain", "hold back", "curb", "rule over"],
        "equality": ["equal", "all same", "no difference", "see equally", "equal vision", "non-judgmental", "everyone same", "unity of all", "non-discriminatory"],
        "social order": ["brahmin", "caste", "duty by nature", "varna", "class system", "natural role", "assigned duty", "kshatriya", "shudra", "vaishya"],
        "compassion": ["kind", "compassion", "friendly", "loving", "gentle", "forgiving", "merciful", "empathetic", "soft-hearted", "caring"],
        "divinity": ["divine", "spark", "god inside", "eternal part", "fragment of god", "higher self", "divine soul", "light within"],
        "freedom": ["freedom", "free", "liberated", "unbound", "release from sin", "peaceful", "unshackled", "deliverance", "released"],
        "equanimity": ["neutral", "calm", "no reaction", "balanced", "fair", "equal minded", "serene", "stable reaction", "non-reactive"],
        "calmness": ["peaceful", "calm", "no stress", "no fear", "undisturbed", "quiet mind", "still", "at ease", "relaxed", "tranquil"],
        "ignorance": ["don't know", "ignorant", "unaware", "no idea", "misunderstand", "illusion", "confused by maya", "false belief", "wrong thinking"],
        "steadiness": ["steady", "balanced", "composed", "stable", "not disturbed", "strong mind", "firm", "determined", "unshaken"]
    }

    for emotion, word_list in keywords.items():
        score = 0
        for word in word_list:
            # Match exact word or phrase with word boundary (avoid false partial matches)
            if re.search(r'\b' + re.escape(word) + r'\b', input_lower):
                score += 2 if ' ' in word else 1  # Give higher weight to phrases
        if score > 0:
            emotion_scores[emotion] = score

    if not emotion_scores:
        return "confusion"

    sorted_scores = sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores[0][0]  # Return emotion with highest score

# Get Krishna's quote and explanation based on emotion and preferred language
def get_krishna_response(emotion, language="en", dataset_path='krishna_dataset.json'):
    dataset = load_dataset(dataset_path)
    matching_verses = [entry for entry in dataset if entry["emotion"].lower() == emotion.lower()]
    
    if not matching_verses:
        return "I am here, but I sense confusion. Ask, and I shall guide you."

    selected = random.choice(matching_verses)

    if language == "hi":
        return selected.get("response_hindi", selected["response"])
    elif language == "bn":
        return selected.get("response_bengali", selected["response"])
    else:
        return selected["response"]
