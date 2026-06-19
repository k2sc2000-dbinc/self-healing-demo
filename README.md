# self-healing-demo

Claude Managed Agents 자가복구(self-healing) 에이전트 데모용 저장소입니다.

`calculator.py` 에는 일부러 두 개의 버그가 심어져 있고, `test_calculator.py` 의 테스트가 실패합니다.

- `subtract()` : 빼기인데 더하기로 구현됨
- `divide()` : 0으로 나누는 경우를 처리하지 않음

## 테스트 실행

```bash
pip install -r requirements.txt
pytest
```

에이전트가 할 일: 테스트를 실행 → 실패 원인 분석 → `calculator.py` 수정 → 테스트가 모두 통과할 때까지 반복 → PR 생성.
