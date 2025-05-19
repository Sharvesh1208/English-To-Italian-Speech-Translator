import gradio as gr
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import tempfile
import os

# Initialize recognizer & translator
recognizer = sr.Recognizer()
translator = Translator()

# Function to perform speech-to-speech translation
def translate_and_speak(audio_filepath):
    try:
        # 1. Transcribe English speech to text
        with sr.AudioFile(audio_filepath) as source:
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.record(source)
            text_en = recognizer.recognize_google(audio_data, language="en-US")

        # 2. Translate to Italian
        translation = translator.translate(text_en, dest="it")
        text_it = translation.text

        # 3. Generate Italian speech as MP3
        tts = gTTS(text_it, lang="it")
        tmp_mp3 = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(tmp_mp3.name)

        # Return translated text and MP3 path
        return text_it, tmp_mp3.name
    except sr.UnknownValueError:
        return "Error: Could not understand audio", None
    except sr.RequestError:
        return "Error: Speech recognition service unavailable", None
    except Exception as e:
        return f"Error: {str(e)}", None

# Build Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## English → Italian Voice Translator")

    inp = gr.Audio(
        sources=["microphone", "upload"],  # Support both mic and file upload
        type="filepath",
        label="Speak in English or Upload Audio"
    )
    out_text = gr.Textbox(label="Translated Text (Italian)")
    out_audio = gr.Audio(
        label="Italian Audio Output",
        type="filepath",
        format="mp3",
        autoplay=True
    )

    gr.Button("Translate & Speak").click(
        fn=translate_and_speak,
        inputs=inp,
        outputs=[out_text, out_audio]
    )

demo.launch()