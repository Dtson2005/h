import math
try:
    value =int(input("nhap so x:"))
    y =10/value
except ValueError:
 print ("bi loi")
except ZeroDivisionError as loi:
 print ("loi chia")
except:
 print ("loi ko xac dinh")
finally:
 print ('result', y)
