#예외처리
#try : 시도해라, 예외가 발생하면 except 구문으로 넘어감
#try와 except는 짝꿍 어느 하나만 사용하면 안됨

try:
    print("나누기 전용 계산기입니다.")
    nums = [] 
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    nums.append(nums[0] / nums[1])
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError: #에러중 ValueError인 경우 이 구문을 타게된다.
    print("값을 잘못 입력하셨습니다.")
    
except ZeroDivisionError as err: #ZeroDivisionError을 err에 할당함 
    print("0으로 나누지 마세요")
    print(err)
    
except Exception:
    print("알 수 없는 오류입니다.") #위의 두가지 에러를 제외한 나머지 에러 

#except:
    #print("알 수 없는 오류입니다.") 위에 Exception구문과 같은 결과임 
    
#사용자 정의 에러
#python에서 정의한 에러말고 사용자가 직접 에러를 정의하고 예외처리할 수 있음 

#그냥 raise 사용하기 

num1 = int(input("첫번째 숫자를 입력하세요"))
num2 = int(input("두번째 숫자를 입력하세요"))

if num1 >= 10 or num2 >= 10: #if와 raise의 조합, 해당조건을 만족하면 구문 오류를 내고
                             #코드가 종료됨
    raise
    #또는 에러 정의
    raise ValueError
    #또는 메시지 출력
    raise Exception("한자리 숫자만 입력하세요 ")

    #이처럼 raise는 try , except 구문이 아니더라도 사용가능함.
    
#try,except,raise

try:
    num1 = int(input("첫번째 숫자를 입력하세요"))
    num2 = int(input("두번째 숫자를 입력하세요"))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    
except ValueError:
    print("값을 잘못입력했습니다.")
    
#숫자가 아닌 다른 값을 입력하면 python에서 자체적으로 ValueError을 발생시키고
#ValueError이 발생했을 때 어떻게 해야하는지 나타내는 except 구문을 실행
#뿐만아니라, 사용자가 지정한 상황에도 raise ValueError
#즉 사용자가 지정한 상황에 ValueError을 발생시키라는 것으로
#ValueError이 발생했을 때 어떻게 해야하는지 나타내는 except 구문을 실행

#class를 활용한 사용자 에러 처리 

class BigNumberError(Exception): #Exception을 상속받는다. 
    def __init__(self,msg):
        self.msg = msg
    def __str__(self): #init함수 다음에 str함수도 자동적으로 호출된다.
        return self.msg

try:
    num1 = int(input("첫번째 숫자를 입력하세요"))
    num2 = int(input("두번째 숫자를 입력하세요"))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1,num2))
        #if조건문에 맞으면 BigNumberError 라는 오류를 발생시키라는 의미
        #해당 오류는 사용자가 클래스로 임의지정함.
        #raise를 만나면 해당오류에 해당하는 except구문으로 내려간다.
        #이 위치에서 BigNumberError을 실행하지 않음. 
    
except BigNumberError as err: # __str__함수의 리턴값이 err에 대입됨
    print("값을 잘못입력했습니다.")
    print(err)

finally:
    print("계산기를 이용해주셔서 감사합니다.")
    
#try든 except구문이든 마지막에 무조건적으로 실행됨. 