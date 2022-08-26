# import travel.thailand
# #import travel.thailand.ThailandPackage
# #from 없이 import를 사용할 때 패키지.모듈까지는 가능하나, 클래스, 함수를 바로 수입은 안됨

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail() #객체를 만든다음 self.detail함수사용함

# #똑같은 기능 
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

#travel 패키지 안에 있는 모든 모듈 가져오기
from travel import * #vietnam과 thailand 모듈 가져오기 (__init__.py)에서 공개범위를 지정함

#모듈,패키지가 저장되어 있는 위치를 확인하는 방법
import inspect
import random

print(inspect.getfile(random))
print(inspect.getfile(thailand))