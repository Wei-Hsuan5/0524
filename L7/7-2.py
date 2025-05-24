def calculate_bmi(h:int,w:int)->float:
   return w / (h /100)**2

def get_state(b: float)->str:
   if b < 18.5:
      return "過輕"
   elif b < 24:
      return"正常"
   elif b < 27:
      return "過重"
   elif b < 30:
      return "輕度肥胖"
   else:
      return "重度肥胖"


def main():
   height:int=int(input("身高(cm):"))
   weight:int=int(input("體重(kg):"))
   
   bmi=calculate_bmi(height, weight)
   
   print(bmi)
   
   print(get_state(bmi))

if __name__ == '__main__':
   main()
