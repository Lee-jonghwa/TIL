
import my_math
# from my_math import add


print(my_math.add(1, 2))
# print(add(1, 2))


# package는 두 번 들어가야하므로 import만 쓰긴 어려움

from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add(1, 2)) # 3
print(tools.mod(1, 2)) # 1

