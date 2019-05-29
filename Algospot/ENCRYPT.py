# 문자열의 개수만큼 딕셔너리를 생성하고 짝수는 짝수끼리 저장하고 홀수는 홀수끼리 저장하여 출력해준다.

#딕셔너리 변수 
a = {}
#문자열을 리스트로 변환해 담을 변수 호출
b = []
#입력한 문자열의 개수를 인식할 변수
count2=0
#짝수의 해당하는 문자들을 저장할 변수
output1 = ''
#홀수의 해당하는 문자들을 저장할 변수
output2 = ''

#입력할 횟수를 받아온다
count = int(input())


while count>0:
#count2를 0으로 초기화 시킨다 ( 반복문이 돌 때마다 초기화 시켜야함 )
    count2=0
    #암호화시킬 문자를 받아온다
    num = input()
    #문자를 리스트로 변환한다
    num=list(num)
  
  #암호화 과정
    while num != []:
        
        #b의 변수에 리스트로 변환한 num을 추가후 이를 e에 문자열로 교환시켜 넣는다.
        b.append(num[0])
        e=''.join(b)

        #새로운 문자열이 들어오는것을 대비해 미리 num의 값을 제거해준다
        del num[0]
        
        #문자열마다 딕셔너리를 생성해줌
        a[count2] = e
        
        #count2를 2로 나누어 나머지가 0 이면 짝수이므로 이는 output1에 추가하고 나머지가 0이 아니면 홀수이므로 이는 output2에 추가해준다.
        if count2%2 == 0:
            output1+=a[count2]
        elif count2%2 != 0:
            output2+=a[count2]
        
        count2+=1
        #반복문이 끝나면 초기화시켜 다음 문자열을 받을 준비를 한다.
        b=[]
        e=''
    
    count-=1
    #출력부분과 마찬가지로 output1,2를 초기화시켜준다.
    print(output1+output2)
    output1=''
    output2=''
