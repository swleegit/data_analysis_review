class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일]")

#클래스 선언시 반드시 def __init__ 있어야하는 것은 아님
#해당 detail함수는 ThailandPackage로 객체를 만든다음
#self.detail()함수를 사용할 수 있음 

#모듈파일을 직접실행하는가 아니면 외부에서 모듈을 사용하는가를 구분하는 코드

if __name__ == "__main__":
    print("thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
    
else:
    print("thailand 외부에서 모듈 호출")
    
