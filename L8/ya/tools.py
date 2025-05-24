def calculate_bmi(height:int,weight:int)->float:
   return weight / (height /100)**2

def get_state(bmi: float)->str:
   if bmi < 18.5:
      return "過輕"
   elif bmi < 24:
      return"正常"
   elif bmi < 27:
      return "過重"
   elif bmi < 30:
      return "輕度肥胖"
   else:
      return "重度肥胖"