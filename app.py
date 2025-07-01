from flask import Flask, render_template, request, jsonify
from model import detect_emotion, get_krishna_response, load_dataset

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form.get('message')
    language = request.form.get('language', 'en')  # Default is English

    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    detected_emotion = detect_emotion(user_input)
    print(f"[DEBUG] Emotion: {detected_emotion} | Lang: {language}")

    dataset = load_dataset()
    matching_verse = next((item for item in dataset if item['emotion'].lower() == detected_emotion.lower()), None)

    if not matching_verse:
        return jsonify({'error': 'No matching verse found'}), 404

    response = get_krishna_response(detected_emotion, language)

    return jsonify({
        "emotion": detected_emotion,
        "verse_id": matching_verse.get("verse_id"),
        "sanskrit": matching_verse.get("sanskrit"),
        "translation": matching_verse.get("translation"),
        "response": response
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
