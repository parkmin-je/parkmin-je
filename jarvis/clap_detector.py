"""
Double-clap detection via microphone energy analysis.

Listens continuously for two loud transients within 1 second.
"""

import time
import threading
import numpy as np
import pyaudio

CHUNK = 1024
RATE = 44100
CHANNELS = 1
FORMAT = pyaudio.paInt16

MAX_CLAP_GAP = 1.0   # seconds between first and second clap
MIN_CLAP_GAP = 0.1   # ignore claps that are too close (echo)


class ClapDetector:
    def __init__(self, threshold: int = 2500, on_double_clap=None):
        self.threshold = threshold
        self.on_double_clap = on_double_clap
        self._running = False
        self._thread = None
        self._last_clap_time = 0.0
        self._audio = pyaudio.PyAudio()

    def _rms(self, data: bytes) -> float:
        samples = np.frombuffer(data, dtype=np.int16).astype(np.float32)
        return float(np.sqrt(np.mean(samples ** 2))) if len(samples) else 0.0

    def _listen(self):
        stream = self._audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK,
        )
        try:
            while self._running:
                data = stream.read(CHUNK, exception_on_overflow=False)
                energy = self._rms(data)
                if energy > self.threshold:
                    now = time.time()
                    gap = now - self._last_clap_time
                    if gap > MIN_CLAP_GAP:
                        if gap <= MAX_CLAP_GAP and self._last_clap_time > 0:
                            self._last_clap_time = 0.0
                            if callable(self.on_double_clap):
                                threading.Thread(
                                    target=self.on_double_clap, daemon=True
                                ).start()
                        else:
                            self._last_clap_time = now
        finally:
            stream.stop_stream()
            stream.close()

    def start(self):
        self._running = True
        self._thread = threading.Thread(target=self._listen, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=2)
        self._audio.terminate()
