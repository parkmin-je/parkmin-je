"""
Claude AI brain — multi-turn conversation manager for JARVIS.

Uses claude-haiku-4-5 by default for low-latency voice responses.
"""

import os
import anthropic

SYSTEM_PROMPT = """당신은 JARVIS입니다 — 아이언맨의 AI 어시스턴트처럼 행동하세요.

규칙:
- 한국어로 간결하게 대답하세요 (2-3문장 이내).
- 항상 자신감 있고 전문적인 어조를 유지하세요.
- 날씨, 시간, 계산, 웹 검색, 시스템 제어 등의 임무를 수행합니다.
- 임무를 받으면 "즉시 수행하겠습니다, 보스." 또는 유사한 표현으로 시작하세요.
- 불가능한 요청은 간단히 이유를 설명하고 대안을 제시하세요.
"""


class AIBrain:
    def __init__(self, model: str | None = None):
        self.client = anthropic.Anthropic(
            api_key=os.environ.get("ANTHROPIC_API_KEY")
        )
        self.model = model or os.environ.get("CLAUDE_MODEL", "claude-haiku-4-5")
        self.history: list[dict] = []

    def think(self, user_text: str) -> str:
        self.history.append({"role": "user", "content": user_text})

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            system=SYSTEM_PROMPT,
            messages=self.history,
        )

        answer = response.content[0].text
        self.history.append({"role": "assistant", "content": answer})

        # Keep history bounded to last 10 turns
        if len(self.history) > 20:
            self.history = self.history[-20:]

        return answer

    def reset(self):
        self.history.clear()
