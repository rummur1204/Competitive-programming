def is_leap(year):
    leap = False
    if (year%4==0): 
         if (year%100==0 and year%400==0):
              return True
    # Write your logic here
         else:
             return False
    return leap

year = int(input())
