def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

loop=1
while loop==1:
 print("Please select operation -\n" \
    "1. Add\n"\
    "2. Subtract\n" \
    "3. Multiply\n"  \
    "4. Divide\n" \
    "5. Exit")

 try:
  select = int(input("Enter your choice:"))
  if(select==5):
      loop=0
  elif(select>5) :
      print("Invalid instructions!\n Do you want to try again?")      
  else:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number:"))
  
 #after selection 
  if (select == 1):
   print(number1, "+", number2, "=",add(number1, number2))

  elif (select == 2):
   print(number1, "-", number2, "=",subtract(number1, number2))

  elif (select == 3):
   print(number1, "*", number2, "=",multiply(number1, number2))

  elif (select == 4):

   if (number2 == 0):
       print("[Sorry, the answer is not defined ]\n")
   else:
       print(number1, "/", number2, "=",divide(number1, number2))
  
  
 except:
    print("[error, this is IMPOSSIBLE!\n Do you want to try again?]\n")
