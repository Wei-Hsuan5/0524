# import ya
from ya.tools import calculate_bmi, get_state


def main():
   height:int=int(input("身高(cm):"))
   weight:int=int(input("體重(kg):"))
   
   bmi=calculate_bmi(height, weight)
   
   print(bmi)
   
   print(get_state(bmi))
      

if __name__ == '__main__':
   main()