# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# we imported the datetime module 
import datetime
today = datetime.date.today()
print(f"today is : {today}")


# also we can do this like
# now we are importing date method from datetime module 
from datetime import date
today2 = date.today()
print(f"today is : {today2}")




