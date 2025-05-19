Here’s your updated `README.md` with the contributors section filled in:

---

# 🗣️ English to Italian Voice Translator

This project is a speech-to-speech translator that takes English audio input, converts it to text, translates it into Italian, and plays the translated Italian audio using text-to-speech.

## 🔄 Workflow

1. 🎤 **Speech Recognition** – Converts spoken English into text using `SpeechRecognition`.
2. 🌍 **Translation** – Translates English text to Italian using `googletrans`.
3. 🔊 **Text-to-Speech** – Converts translated Italian text into speech using `gTTS`.

## 🚀 How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/english-to-italian-voice-translator.git
   cd english-to-italian-voice-translator
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   > If you face issues with `pyaudio`, install it using:

   ```bash
   pip install pipwin
   pipwin install pyaudio
   ```

3. **Run the app**

   ```bash
   python app.py
   ```

4. **Use the Gradio interface** to speak in English or upload an audio file and get Italian voice output.

## 🛠️ Tech Stack

* Python
* Gradio
* SpeechRecognition
* Googletrans
* gTTS (Google Text-to-Speech)

## 📄 Example

Speak: "Hello, how are you?"
→ Translated: "Ciao, come stai?"
→ Output: Italian audio playback

## 👥 Contributors

* Joel Ebenezer P
* Koushik Balaji P
* Roshaun Infant R
* Sharvesh K

## 📌 Use Cases

* Real-time voice translation
* Language learning
* Communication assistant for travelers

## 📃 License

This project is licensed under the MIT License.
