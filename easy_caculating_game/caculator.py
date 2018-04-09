def addition_generator(num1,num2):
  number1=str(num1)
  number2=str(num2)
  if num1<0 and num2>=0 :
    question="("+number1+")+"+number2+"=?"
  elif num1>=0 and num2>=0 :
    question=number1+"+"+number2+"=?"
  elif num1>=0 and num2<0:
    question=number1+"+("+number2+")=?"
  else:
    question="("+number1+")"+"+("+number2+")=?"
  return question

def addition_check(num1,num2):
  return float(num1)+float(num2)

def substraction_generator(num1,num2):
  number1=str(num1)
  number2=str(num2)
  if num1<0 and num2>=0 :
    question="("+number1+")-"+number2+"=?"
  elif num1>=0 and num2>=0 :
    question=number1+"-"+number2+"=?"
  elif num1>=0 and num2<0:
    question=number1+"-("+number2+")=?"
  else:
    question="("+number1+")"+"-("+number2+")=?"
  return question

def substraction_check(num1,num2):
  return float(num1)-float(num2)



def multiplication_generator(num1,num2):
  number1=str(num1)
  number2=str(num2)
  if num1<0 and num2>=0 :
    question="("+number1+")*"+number2+"=?"
  elif num1>=0 and num2>=0 :
    question=number1+"*"+number2+"=?"
  elif num1>=0 and num2<0:
    question=number1+"*("+number2+")=?"
  else:
    question="("+number1+")"+"*("+number2+")=?"
  return question

def multiplication_check(num1,num2):
  return float(num1)*float(num2)


def division_generator(num1,num2):
    number1=str(num1)
    number2=str(num2)
    if num1<0 and num2>=0 :
        question="("+number1+")/"+number2+"=?"
    elif num1>=0 and num2>=0 :
        question=number1+"/"+number2+"=?"
    elif num1>=0 and num2<0:
        question=number1+"/("+number2+")=?"
    else:
        question="("+number1+")"+"/("+number2+")=?"
    return question