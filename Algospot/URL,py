# 상당히 어려웠습니다 많은 시행착오가 있었습니다

####### 틀린코드 
'''

# 딕셔너리 a 선언
a = { ' ' : '%20',
      '!' : '%21',
      '$' : '%24',
      '%' : '%25',
      '(' : '%28',
      ')' : '%29',
      '*' : '%2a' }

#반복할 횟수 받아오기
T = int(input())
#반복문을 탈출하기 위한 조건 설정을 위해 Null 변수 선언
Null = 0
#반복
for b in range(T):
#문자열을 입력받으며
    N = input()
    #반복문에 진입
    while True:
        
        #해당되는 문자열을 찾는다 
        tz = N.find(a[' '])
        # if 문 find 함수의 경우 문자열을 못 찾을 경우 -1을 반환함 즉 -1이 아니라면 if 문을 들어가게된다. 슬라이싱을 적절히 활용해서 문자를 바꾸어줌.
        if tz !=-1:
            N = N[:tz] + ' ' + N[tz+3:]
        #else의 경우는 문자열을 못 찾을 경우
        else:
            Null +=1
            
        tzo = N.find(a['!'])
         
        if tzo !=-1:
            N = N[:tzo] + '!' + N[tzo+3:]
        else:
            Null +=1


        tzf = N.find(a['$'])

        if tzf !=-1:
            N = N[:tzf] + '$' + N[tzf+3:]
        else:
            Null +=1

        
        tzfi = N.find(a['%'])

        if tzfi !=-1:
            N = N[:tzfi] + '%' + N[tzfi+3:]
        else:
            Null +=1

        
        tze = N.find(a['('])

        if tze !=-1:
            N = N[:tze] + '(' +N[tze+3:]
        else:
            Null +=1

        
        tzn = N.find(a[')'])

        if tzn !=-1:
            N = N[:tzn] + ')' + N[tzn+3:]
        else:
            Null +=1
 
        
        tza = N.find(a['*'])

        if tza !=-1:
            N = N[:tza] + '*' + N[tza+3:]
        else:
            Null +=1
        # 
        # Null 이 7보다 커지면 탈출
        if Null > 7:
            break

    print(N)
'''

'''문제점**
  위 코드에서의 문제점은 %2520을 입력하면 %20이 나와야 하지만 %20 도 계산되어서 ' ' 이 나온다 
  이러한 문제가 있었고 코드 자체들의 구성을 다시 생각했어야 했는데 이 부분을 해결하지 못해서 문제가 생김
  하지만 이 것도 방법에 따라서 새로운 정답이 될 수도 있다고 생각함.
  '''
  
  ### 코드 자체를 새로 뜯어 고친 결과의 답.
  #딕셔너리 선언
a = { '%20' : ' ',
      '%21' : '!',
      '%24' : '$',
      '%25' : '%',
      '%28' : '(',
      '%29' : ')',
      '%2a' : '*' }

#반복할 횟수를 입력받고
T=int(input())
for i in range(T):
#문자열을 입력받음
    N = input()
    #x 선언 
    x=0
    #N의 문자열 개수만큼 range 함수를 통해 반복
    for i in range(len(N)):
    #만일 N[x] 가 "%" 라면
        if N[x] == "%":
        #딕셔너리에 맞는 문자를 비교해서 출력
            print(a[N[x:x+3]],end='')
            x+=3
            
        else :
        #그렇지 않을 경우는 그냥 출력후 넘어감
            print(N[x],end='')
            x+=1
        # 만일 x가 N의 개수와 같아지면 반복문을 탈출함 ( 그렇지 않을경우 문자열의 개수만큼 루프를 돌기 때문에 오류가 발생 )  
        if x==len(N):
            break
    #반복문을 탈출할 때마다 구분을 지어주기 위해 엔터 효과 
    print('')
    
### 처음의 방식대로 푼 답안
'''
N = int(input())
#반복
for i in range(N):
#문자열을 입력받고
    T = input()
    #입력받은 문자열의 수를 count 변수에 저장
    count = len(T)
    #결과값이 저장될 Null 변수 선언
    Null = ""
    #문자열의 위치를 구분할 x 변수 선언
    x = 0
    #만일 x가 count(문자열의 개수)보다 적다면 반복 
    while x < count:
        #만일 T[x:x+2] 의 범위가 %2 라면 아래의 조건문을 통해서 그 뒤의 문자를
        #인식 후에 문자에 따른 문자를 Null 에 집어넣어서 계속적으로 집어넣어준다.
        if T[x:x+2] == '%2':
            if T[x+2] == '0':
                Null += " "
                x = x+3
            elif T[x+2] == '1':
                Null += "!"
                x = x+3
            elif T[x+2] == '4':
                Null += "$"
                x = x+3
            elif T[x+2] == '5':
                Null += "%"
                x = x+3
            elif T[x+2] == '8':
                Null += "("
                x = x+3
            elif T[x+2] == '9':
                Null += ")"
                x = x+3
            elif T[x+2] == 'a':
                Null += "*"
                x = x+3
        #공백일 경우 혹은 문자열이 맞지 않을 경우엔 그 문자를 그대로 넣어준다
        else:
            Null += T[x]
            x = x+1
    #출력 부분
    print(Null)
'''
    
