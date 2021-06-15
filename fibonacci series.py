elements = int(input("PLEASE ENTER THE NUMBER OF TERMS? "))

a= 0
b=1
terms = 0

if elements <= 0:
   print("Please enter a positive integer")

else:
   print("Fibonacci series is:")
   while terms< elements:
       print(a)
       total = a + b
       
       a = b
       b = total
       terms+= 1 
