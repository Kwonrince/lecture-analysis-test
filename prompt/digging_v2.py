class Digging:
    def __init__(self, subject):
        self.prompt = \
r'''당신은 {subject} 과외 수업에서 선생님의 질문을 분석하여, 다음 작업을 진행합니다.
주어진 선생님의 질문이 메타인지형 질문인지 이해점검형 질문인지 아래 정의에 따라 판단하세요.
주어진 질문(question)에 대해 문맥(context)을 고려하여, 충분히 생각한 다음 출력 형식에 따라 결과를 반환하세요.
문맥(context)에서는 해당 질문 근처의 선생님과 학생의 대화를 시간 정보와 함께 제공합니다.

## 메타인지형 질문이란?
- 왜 그렇게 생각하는지, 왜 틀렸다고 생각하는지, 왜 그렇게 풀었는지 등 학생의 생각을 묻는 질문
- 어디를 알고 어디를 모르는지 학생 스스로 생각하고 답변해야하는 질문
- **질문에 구체성이 있어야 함**
-> 왜 1번이 답이라고 생각했어?
-> 개념이해가 부족한 것 같아? 아님 문제 풀이 방식을 잘 모르겠어?

## 이해점검형 질문이란?
- 학생이 배워가는 과정에서 지식을 확실하게 기억하게 하기 위한 의도로 이루어지는 이해도 체크나, 배운 것을 설명해보도록 하는 참여형 질문
- 단순히 확인을 위한 질문, **"네"/"아니오"로 대답할 수 있는 질문**
-> (선생님 A 개념 설명 후) 그럼 A-1일 때는 어떻게 해야 하지?
-> (소수 개념 설명 후) 13은 소수일까?
-> (단어 및 문장 구조 설명해주고) 그럼 이 문장은 어떻게 해석해야 할까?
-> (개념 설명 후) 아까 미시 세계의 특징은 뭐라고 했지?
-> 마름모의 성질은 뭐라고 했지?
-> 혹시 19번, 20번은 손을 못 댔어요? 아니면 풀다가 중간에 막혔어요?

## 출력 형식
```json
{{
      "idx": INT,
      "result": "메타인지형 질문"/"이해점검형 질문",
      "reason": "판단 이유"
}}
'''
        self.prompt = self.prompt.replace("{subject}", subject)