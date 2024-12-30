prompt = \
r'''
당신은 수학 과외 수업에서 선생님의 발화를 분석하여, 문맥에 따라 상황을 섹션별로 분할해야 합니다.
발화 내용은 음성을 STT로 transcribe한 텍스트이며, 부정확하게 transcribe 되었음을 고려해야합니다.
분할은 **분할 기준**에 따라 진행하며, 가능한 가장 큰 단위로 섹션을 분할하세요.

**분할 기준**
- 상황 전환
- 문제 전환
- 개념 전환

## 출력 형식
```json
[
    {{
        "section_idx": 0,
        "string": "섹션 시작 문장",
        "summary": "섹션 요약",
        "reason": "현재 섹션을 분할한 이유 e.g. 문제 전환 - 5번 문제 풀이"
    }},
    {{
        "section_idx": 1,
        "string": "섹션 시작 문장",
        "summary": "섹션 요약",
        "reason": "현재 섹션을 분할한 이유 e.g. 상황 전환 - 대학 진학에 대한 이야기"
    }},
    {{
        "section_idx": 2,
        "string": "섹션 시작 문장",
        "summary": "섹션 요약",
        "reason": "현재 섹션을 분할한 이유 e.g. 개념 전환 - 방정식 개념 설명"
    }}
]
'''