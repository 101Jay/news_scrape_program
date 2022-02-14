# import theater_module as mv
# mv.price(2)

# from theater_module import price_morning as pm
# pm(2)#이렇게 함수를 임포트할 경우 .없이 바로 사용할 수 있다.


#패키지의 사용
# import travel.thailand #임포트 단독 구문에서는 모듈 단위까지만 가져올 수 있다.

from travel import *
import travel
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random

print(inspect.getfile(random))
print(inspect.getfile(thailand))
