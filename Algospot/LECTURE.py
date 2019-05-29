#입력할 횟수를 받아옴
T=int(input())
#입력한 횟수만큼 반복하는 반복문을 생성
while T>0:
#소팅할 문자열을 입력
    a=input()
    #입력한 문자열을 리스트로 변환
    b=list(a)
    #리스트의 개수를 센다
    c=len(b)
    #리스트를 2개씩 빼서 저장할 변수 d를 초기화
    d=[]
    #2로 나누는 이유는 리스트를 2개씩 빼기 때문임
    c=c/2
    #리스트 소팅 과정
    while c>0:
    #b의 첫번째와 두번째 리스트를 result로 집어넣는다
        result=b[0]+b[1]
        #리버스로 뒤집어주고
        b.reverse()
        #두번의 pop를 통해 집어넣은 리스트를 제거해줌
        b.pop()
        b.pop()
        #다시 리버스로 뒤집어주어 원래대로 만듬
        b.reverse()
        #초기화한 변수 d 에 result 값을 추가 ( result 는 따로 초기화할 필요가 없음 ) 
        d.append(result)
        
        c-=1
    #d에 추가한 리스트들을 sort로 소팅해줌
    d.sort()
    #출력하는 부분 for문과 end를 통해 끝까지 출력하게 하고 그 다음의 프린트 문을 통해서 띄어쓰기를 해줌
    for output in d:
            print(output,end='')
    print('')
    T-=1
