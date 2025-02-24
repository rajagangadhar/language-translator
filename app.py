from flask import Flask, request, jsonify, render_template
from deep_translator import GoogleTranslator

# Initialize Flask app
app = Flask(__name__)

# LANGUAGES dictionary
LANGUAGES = {
    'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'as': 'assamese',
    'ay': 'aymara', 'az': 'azerbaijani', 'bm': 'bambara', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali',
    'bho': 'bhojpuri', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa',
    'zh-CN': 'chinese (simplified)', 'zh-TW': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian',
    'cs': 'czech', 'da': 'danish', 'dv': 'dhivehi', 'doi': 'dogri', 'nl': 'dutch', 'en': 'english',
    'eo': 'esperanto', 'et': 'estonian', 'ee': 'ewe', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french',
    'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gn': 'guarani',
    'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi',
    'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'ilo': 'ilocano', 'id': 'indonesian',
    'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh',
    'km': 'khmer', 'rw': 'kinyarwanda', 'gom': 'konkani', 'ko': 'korean', 'kri': 'krio', 'ku': 'kurdish (kurmanji)',
    'ckb': 'kurdish (sorani)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'ln': 'lingala',
    'lt': 'lithuanian', 'lg': 'luganda', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mai': 'maithili',
    'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi',
    'mni-Mtei': 'meiteilon (manipuri)', 'lus': 'mizo', 'mn': 'mongolian', 'my': 'myanmar', 'ne': 'nepali',
    'no': 'norwegian', 'or': 'odia (oriya)', 'om': 'oromo', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish',
    'pt': 'portuguese', 'pa': 'punjabi', 'qu': 'quechua', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan',
    'sa': 'sanskrit', 'gd': 'scots gaelic', 'nso': 'sepedi', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona',
    'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish',
    'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'tt': 'tatar',
    'te': 'telugu', 'th': 'thai', 'ti': 'tigrinya', 'ts': 'tsonga', 'tr': 'turkish', 'tk': 'turkmen',
    'ak': 'twi', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese',
    'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu',
}

# Function to translate text
def translate_text(text, target_language='fr'):
    translated = GoogleTranslator(source='auto', target=target_language).translate(text)
    return translated

# Route to serve the translation page
@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

# Route to handle the translation
@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    target_language = request.form['target_language']

    if not text:
        return jsonify({"error": "No text provided"}), 400

    translated_text = translate_text(text, target_language)
    return jsonify({"original_text": text, "translated_text": translated_text})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)  # Enable debug mode for better error messages