"""
Text-to-speech engine with pyttsx3 (offline, fast) and gTTS fallback.
"""

import os
import threading


class Speaker:
    def __init__(self, engine: str | None = None):
        self.engine_name = engine or os.environ.get("TTS_ENGINE", "pyttsx3")
        self._lock = threading.Lock()
        self._engine = None

        if self.engine_name == "pyttsx3":
            self._init_pyttsx3()

    def _init_pyttsx3(self):
        try:
            import pyttsx3
            self._engine = pyttsx3.init()
            self._engine.setProperty("rate", 165)
            # Try to set a Korean-compatible voice if available
            voices = self._engine.getProperty("voices")
            for v in voices:
                if "korean" in v.name.lower() or "ko" in v.id.lower():
                    self._engine.setProperty("voice", v.id)
                    break
        except Exception:
            self._engine = None

    def speak(self, text: str):
        with self._lock:
            if self.engine_name == "pyttsx3" and self._engine:
                self._speak_pyttsx3(text)
            else:
                self._speak_gtts(text)

    def _speak_pyttsx3(self, text: str):
        try:
            self._engine.say(text)
            self._engine.runAndWait()
        except Exception:
            self._speak_gtts(text)

    def _speak_gtts(self, text: str):
        try:
            from gtts import gTTS
            import tempfile
            import subprocess

            lang = os.environ.get("LANGUAGE", "ko-KR").split("-")[0]
            tts = gTTS(text=text, lang=lang, slow=False)
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
                tmp = f.name
            tts.save(tmp)

            # Play with system player
            for cmd in (["mpg123", "-q", tmp], ["ffplay", "-nodisp", "-autoexit", tmp],
                        ["aplay", tmp], ["afplay", tmp]):
                try:
                    subprocess.run(cmd, check=True,
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    break
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            os.unlink(tmp)
        except Exception as e:
            print(f"[Speaker] TTS 오류: {e}")
