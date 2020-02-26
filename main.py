# 모듈 import
# import 패키지.모듈
import models.account.bill
models.account.bill.charge(1, 50)

# 모듈안의 모든 함수 import
# from 패키지명 import 모듈명
from models.account import bill
bill.charge(2, 100)

# 특정 함수만 import
# from 패키지명.모듈명 import 함수명
from models.account.bill import charge
charge(3, 150)