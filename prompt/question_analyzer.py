class QuestionAnalyzer:
    def __init__(self, subject):
        self.prompt = \
r'''
당신은 {subject} 과외 수업에서 선생님의 발화를 분석하여, 각 문장이 질문인지 아닌지 구별해야합니다.
각 문장의 주변 문맥을 파악하고, 충분히 생각한 다음, 해당 문장이 질문일 경우 idx를 반환하세요.

## 출력 형식
```json
[
    {{
        "idx": [List]
    }}
]
'''
        self.prompt = self.prompt.replace("{subject}", subject)