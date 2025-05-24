import tools


def main():
   height:int=int(input("身高(cm):"))
   weight:int=int(input("體重(kg):"))
   
   bmi=tools.calculate_bmi(height, weight)
   
   print(bmi)
   
   print(tools.get_state(bmi))   

if __name__ == '__main__':
   main()
