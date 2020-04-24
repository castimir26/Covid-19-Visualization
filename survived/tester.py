
import pandas as pd
from datetime import date, datetime



d0 = date(2020, 1, 23)
d1 = datetime.today().date()
print(d1)
print(d0)
delta = d1 - d0
print(delta)
