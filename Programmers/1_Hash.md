[사이트 링크 : 코딩테스트 연습 - 완주하지 못한 선수 | 프로그래머스 https://programmers.co.kr/learn/courses/30/lessons/42576](solution.cpp 1 #include <string> 2 #include <vector> 3 ​ 4 using namespace std ; 5 ​ 6 string solution ( vector < string > participant , vector < string > completion ) { 7 string answer = "" ; 8 return answer ; 9 } 실행 결과 실행 결과가 여기에 표시됩니다. 문제 설명 구현해야 하는 내용에 대한 설명입니다. 잘 읽고 설명에 따라 코드를 작성하세요. 1 / 7 〈 이전...)

<br>

### 처음 풀이

<br>

```py
def solution(participant, completion):
    participant.sort(reverse=True)
    completion.sort(reverse=True)

    for i in range(len(participant)):
        if(participant[i]!=completion[i]):
            return participant[i]
```

<br>

틀린 문제.. remove도 이용해보고 별 방법을 다 사용하다.. 효율성의 벽에 맞혀 답을 보고 말았다.

<br>

```py
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```

이거 푼 사람 천재인듯...
