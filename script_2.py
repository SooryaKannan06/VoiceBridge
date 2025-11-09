
# Create FREE translation_service.py using only free libraries
free_translation_service = '''"""
FREE Translation Service for Voice Bridge
Uses completely free libraries - NO Google Cloud required!
"""

import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import io
import os

class FreeTranslationService:
    """
    Completely FREE translation service using:
    - SpeechRecognition (Google Speech Recognition API - Free tier)
    - googletrans (Free Google Translate)
    - gTTS (Free Google Text-to-Speech)
    
    NO API KEYS OR PAYMENT REQUIRED!
    """
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
    
    def speech_to_text(self, audio_file_path, language='en'):
        """
        Convert speech to text using SpeechRecognition (FREE)
        
        Args:
            audio_file_path: Path to audio file (WAV format recommended)
            language: Language code (e.g., 'en', 'es', 'hi', 'fr')
        
        Returns:
            Transcribed text string
        """
        try:
            with sr.AudioFile(audio_file_path) as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio_data = self.recognizer.record(source)
                
                # Use Google's free speech recognition
                text = self.recognizer.recognize_google(audio_data, language=language)
                return text
        except sr.UnknownValueError:
            return "[Could not understand audio]"
        except sr.RequestError as e:
            return f"[Error: {e}]"
    
    def translate_text(self, text, dest_language='en', src_language='auto'):
        """
        Translate text using googletrans (FREE)
        
        Args:
            text: Text to translate
            dest_language: Target language code (e.g., 'en', 'es', 'hi', 'fr')
            src_language: Source language (auto-detect by default)
        
        Returns:
            Translated text string
        """
        if not text or text.startswith('['):
            return text
        
        try:
            result = self.translator.translate(text, dest=dest_language, src=src_language)
            return result.text
        except Exception as e:
            print(f"Translation error: {e}")
            return text
    
    def text_to_speech(self, text, language='en', output_file=None):
        """
        Convert text to speech using gTTS (FREE)
        
        Args:
            text: Text to synthesize
            language: Language code for voice (e.g., 'en', 'es', 'hi', 'fr')
            output_file: Optional file path to save audio
        
        Returns:
            Audio data as bytes
        """
        if not text or text.startswith('['):
            return b''
        
        try:
            # Create TTS object
            tts = gTTS(text=text, lang=language, slow=False)
            
            # Save to memory
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            audio_data = audio_fp.read()
            
            # Optionally save to file
            if output_file:
                with open(output_file, 'wb') as f:
                    f.write(audio_data)
            
            return audio_data
        except Exception as e:
            print(f"TTS error: {e}")
            return b''
    
    def full_translation_pipeline(self, audio_file_path, source_lang, target_lang):
        """
        Complete FREE translation pipeline:
        Speech -> Text -> Translation -> Speech
        
        Args:
            audio_file_path: Input audio file path
            source_lang: Source language code (e.g., 'en', 'es', 'hi')
            target_lang: Target language code (e.g., 'en', 'es', 'hi')
        
        Returns:
            Dictionary with transcript, translation, and audio bytes
        """
        print(f"Processing audio: {source_lang} -> {target_lang}")
        
        # Step 1: Speech to Text
        transcript = self.speech_to_text(audio_file_path, language=source_lang)
        print(f"Transcript: {transcript}")
        
        # Step 2: Translate
        translation = self.translate_text(transcript, dest_language=target_lang, src_language=source_lang)
        print(f"Translation: {translation}")
        
        # Step 3: Text to Speech
        audio_output = self.text_to_speech(translation, language=target_lang)
        print(f"Generated audio: {len(audio_output)} bytes")
        
        return {
            'transcript': transcript,
            'translation': translation,
            'audio': audio_output
        }


# Language code mappings for the UI
LANGUAGE_CODES = {
    'en-US': 'en',
    'es-ES': 'es',
    'fr-FR': 'fr',
    'de-DE': 'de',
    'hi-IN': 'hi',
    'zh-CN': 'zh-CN',
    'ja-JP': 'ja',
    'ar-SA': 'ar',
    'pt-BR': 'pt',
    'ru-RU': 'ru',
    'it-IT': 'it',
    'ko-KR': 'ko',
    'nl-NL': 'nl',
    'pl-PL': 'pl',
    'tr-TR': 'tr',
}

def convert_language_code(full_code):
    """Convert full language code to short code"""
    return LANGUAGE_CODES.get(full_code, full_code.split('-')[0])


# Test function
if __name__ == '__main__':
    print("Testing FREE Translation Service...")
    print("No API keys needed!")
    print("\\nSupported operations:")
    print("1. Speech Recognition (via Google - Free)")
    print("2. Text Translation (via googletrans - Free)")
    print("3. Text-to-Speech (via gTTS - Free)")
'''

with open(f"{base_dir}/translation_service.py", 'w') as f:
    f.write(free_translation_service)

print("✅ Created FREE translation_service.py (NO Google Cloud needed!)")
