#!/usr/bin/env python3
"""
JARVIS — Voice-Activated AI Assistant
======================================
박수 두 번 → 깨어남 → 음성 명령 인식 → Claude AI 응답 → TTS 재생

사용법:
    cp ../.env.example ../.env   # API 키 설정
    pip install -r requirements.txt
    python main.py
"""

import os
import sys
import time
import threading

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

from clap_detector import ClapDetector
from voice_listener import VoiceListener
from ai_brain import AIBrain
from speaker import Speaker
from tasks import quick_respond

# ── 상태 ──────────────────────────────────────────────────────────────────────
class State:
    IDLE = "idle"
    LISTENING = "listening"
    THINKING = "thinking"
    SPEAKING = "speaking"


_state = State.IDLE
_state_lock = threading.Lock()


def set_state(s: str):
    global _state
    with _state_lock:
        _state = s


def get_state() -> str:
    with _state_lock:
        return _state


# ── 컴포넌트 초기화 ────────────────────────────────────────────────────────────
threshold = int(os.environ.get("CLAP_THRESHOLD", 2500))
language = os.environ.get("LANGUAGE", "ko-KR")

speaker = Speaker()
listener = VoiceListener(language=language)
brain = AIBrain()


# ── 핵심 루프 ──────────────────────────────────────────────────────────────────
def on_double_clap():
    if get_state() != State.IDLE:
        return

    set_state(State.LISTENING)
    _wake()

    text = listener.listen()

    if not text:
        _say("잘 못 들었습니다, 보스.")
        set_state(State.IDLE)
        return

    print(f"\n👂 인식: {text}")
    _process(text)


def _wake():
    print("\n⚡ JARVIS 활성화")
    _say("무엇을 도와드릴까요, 보스?")


def _process(text: str):
    # 종료 명령
    if any(k in text for k in ("종료", "꺼", "잠들어", "슬립")):
        _say("잠들겠습니다, 보스. 필요하시면 박수 두 번 치세요.")
        set_state(State.IDLE)
        return

    set_state(State.THINKING)

    # 즉시 처리 가능한 명령 먼저 시도
    quick = quick_respond(text)
    if quick:
        _say(quick)
        set_state(State.IDLE)
        return

    # Claude에게 전달
    try:
        answer = brain.think(text)
        print(f"🤖 JARVIS: {answer}")
        _say(answer)
    except Exception as e:
        print(f"[오류] Claude 호출 실패: {e}")
        _say("죄송합니다, 보스. 처리 중 오류가 발생했습니다.")

    set_state(State.IDLE)


def _say(text: str):
    set_state(State.SPEAKING)
    speaker.speak(text)
    # state is reset by the caller after _say returns


# ── 메인 ───────────────────────────────────────────────────────────────────────
def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("❌ ANTHROPIC_API_KEY가 설정되지 않았습니다.")
        print("   .env 파일에 키를 입력하거나 환경변수를 설정하세요.")
        sys.exit(1)

    print("=" * 50)
    print("  ⚙️  JARVIS AI 어시스턴트 시작")
    print("=" * 50)
    print("  👏 박수 두 번 → 활성화")
    print("  🎤 명령어 말씀 → AI 처리")
    print("  🔊 음성 응답")
    print("  [Ctrl+C] 종료")
    print("=" * 50)

    detector = ClapDetector(threshold=threshold, on_double_clap=on_double_clap)
    detector.start()

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n\n👋 JARVIS 종료합니다.")
    finally:
        detector.stop()


if __name__ == "__main__":
    main()
