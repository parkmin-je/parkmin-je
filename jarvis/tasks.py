"""
Task executor — intercepts known keywords before sending to Claude
so common tasks are handled instantly (time, date, open apps, etc.).
"""

import datetime
import subprocess
import sys
import webbrowser
from typing import Callable


def _open_app(name: str) -> str | None:
    apps = {
        "유튜브": "https://youtube.com",
        "구글": "https://google.com",
        "날씨": "https://weather.naver.com",
        "네이버": "https://naver.com",
        "카카오": "https://kakao.com",
        "깃허브": "https://github.com",
    }
    url = apps.get(name)
    if url:
        webbrowser.open(url)
        return f"{name} 열었습니다, 보스."
    return None


def _system_command(cmd: str) -> str | None:
    if "볼륨" in cmd or "음량" in cmd:
        if "올려" in cmd or "키워" in cmd:
            if sys.platform == "darwin":
                subprocess.run(["osascript", "-e", "set volume output volume (output volume of (get volume settings) + 10)"])
            return "볼륨을 올렸습니다."
        elif "내려" in cmd or "줄여" in cmd:
            if sys.platform == "darwin":
                subprocess.run(["osascript", "-e", "set volume output volume (output volume of (get volume settings) - 10)"])
            return "볼륨을 낮췄습니다."
    return None


def quick_respond(text: str) -> str | None:
    """
    Try to handle the request locally before calling Claude.
    Returns a response string if handled, None otherwise.
    """
    text_lower = text.lower()

    # Time / Date
    if any(k in text_lower for k in ("몇 시", "현재 시간", "지금 시간")):
        now = datetime.datetime.now()
        return f"현재 시각은 {now.strftime('%H시 %M분')}입니다, 보스."

    if any(k in text_lower for k in ("오늘 날짜", "몇 월", "무슨 날")):
        now = datetime.datetime.now()
        weekdays = ["월", "화", "수", "목", "금", "토", "일"]
        wd = weekdays[now.weekday()]
        return f"오늘은 {now.month}월 {now.day}일 {wd}요일입니다, 보스."

    # Open apps
    for app_name in ("유튜브", "구글", "날씨", "네이버", "카카오", "깃허브"):
        if app_name in text_lower and ("열어" in text_lower or "켜" in text_lower or "실행" in text_lower):
            result = _open_app(app_name)
            if result:
                return result

    # System commands
    sys_result = _system_command(text_lower)
    if sys_result:
        return sys_result

    return None
