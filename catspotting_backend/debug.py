from pympler import muppy
from pympler import summary
from pympler import tracker
from pympler import asizeof
import types

# HTTP request times out when Heroku tries to load the app. Have also had memory leak on front end, wondering if related.  Pympler memory panels shows 500: internal server error.  Using muppy to try to find memory leak.

all_objects = muppy.get_objects()
print(len(all_objects))
# len = 32680

# my_types = muppy.filter(all_objects, Type=types.ClassType)
# print(len(my_types))

sum1 = summary.summarize(all_objects)
sum2 = summary.summarize(muppy.get_objects())
tr = tracker.SummaryTracker()
tr.print_diff()
