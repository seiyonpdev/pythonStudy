#파이썬 패키지
#패키지 작성 및 사용법
#파이썬은 패키지로 분할 된 개별적인 모듈로 구성
#__init__.py : Python 3.3부터는 없어도 패키지로 인식 → 단 하위호환을 위해 작성 추천
#상대경로 : ..(부모 디렉토리), .(현재 디렉토리)  → 모듈 내부에서만 사용

#예제 1
import sub.sub1.module1
import sub.sub2.module2

#사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()

#예제 2
from sub.sub1 import module1
from sub.sub2 import module2 as m2

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

#예제 3
from sub. sub1 import *
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()

#예제 4
from sub.sub3 import chapter06_02 as oper

print(oper.add(1, 2))
print(oper.sub(5, 4))