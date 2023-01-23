import math
from datetime import datetime

now = datetime.now()
date = datetime(2022, 3, 1, 1, 41, 0)
bb = abs(date - now)
sums = bb.days * 24 * 3600 + bb.seconds
print(bb)
print(sums)