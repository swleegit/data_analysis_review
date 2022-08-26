#모듈: 어떠한 기능이 있는 함수, 클래스 꾸러미
#확장자는 .py
#작업디렉토리 또는 anaconda라면 아나콘다 폴더에 모듈파일(.py)가 있어야 부를 수 있다.

import theater_module
#자주쓰는 같은 특성의 함수들은 모듈화시켜서 꺼내쓰면 편리하다.

theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv

mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
#from a import b :a 언급한 것은 더이상 안해도 ok
#(*) 전부를 의미함

from theater_module import price, price_morning
#두가지 함수만 수입했기 때문에 price_soldier은 사용불가

from theater_module import price_soldier as price
#price = price_soldier
