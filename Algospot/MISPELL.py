# 입력할 횟수를 입력
count=int(input())
#출력시 횟수를 구분할 변수
count2=1

# 입력한 횟수만큼 반복한다
for i in range(count):
# 문자열을 입력하고
    a = input()
    #공백을 기준으로 나눈다
    b = a.split()
    # b[0] 은 당연히 제거할 문자의 위치이므로 이를 정수로 반환해 c 변수에 선언해준다
    c = int(b[0])
    #b는 b[1]은 당연히 문자열이므로 다시 선언해 재활용해주자
    b=b[1]
    #문자열 제거 과정
    b=b[:c-1]+b[c:]
    #출력및 count2에 1을 더해 다음 문자열이 입력되는 것을 대비해준다.
    print(str(count2)+' '+b)
    count2+=1
