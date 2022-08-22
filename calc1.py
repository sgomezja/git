#Calculadora
#This program will create a basic calculator

#Step1- Define the functions to be called later

def addition (a,b):
	return a + b

def subctraction(a,b):
	return a - b 

def multiply ( a ,b):
	return a * b
 
def divide (a,b):
	return a / b 


print("Thank you for using the calculator script")
print("")
print("Please choose your option")
print("1-Add")
print("2-Substraction")
print("3-Multiply")
print("4-Divide")
print("")


while True:
#takes the input from user
	choice = input ("Enter your choice between 1-4: ")

	#This will check depending of user input between 1-4
	if choice in ("1", "2", "3", "4"):
		n1= float (input("Enter the 1st number: "))
		n2= float (input("Enter the 2nd number"))

		if choice == "1":
			print (n1, "+", n2, "=" , addition(n1, n2))

		elif choice == "2":
				print (n1, "-", n2, "=", subctraction(n1,n2))
		elif choice == "3":
				print (n1, "*", n2, "=", multiply(n1,n2))
		elif choice == "4":
				print (n1, "/", n2, "=", divide(n1,n2))

		break

	else:
		print("Invalid option")



