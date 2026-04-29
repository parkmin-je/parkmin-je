"""
Speech-to-text via Google Web Speech API.
Falls back to offline Sphinx if internet is unavailable.
"""

import speech_recognition as sr


class VoiceListener:
    def __init__(self, language: str = "ko-KR", timeout: int = 5, phrase_limit: int = 10):
        self.language = language
        self.timeout = timeout
        self.phrase_limit = phrase_limit
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True

    def listen(self) -> str | None:
        """
        Record one utterance from the microphone and return transcribed text.
        Returns None on failure.
        """
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.3)
            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=self.timeout,
                    phrase_time_limit=self.phrase_limit,
                )
            except sr.WaitTimeoutError:
                return None

        try:
            text = self.recognizer.recognize_google(audio, language=self.language)
            return text.strip()
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            # Network unavailable – try offline engine
            try:
                return self.recognizer.recognize_sphinx(audio).strip()
            except Exception:
                return None
