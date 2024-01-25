# Password validation in Python
# using naive method

# Function to validate the password
def password_check(passwd):
	
	SpecialSym =['$', '@', '#']
	val = True
	
	if len(passwd) < 5 :
		#print('length should be at least 6')
		val = False
		
	if len(passwd) > 12 :
		#print('length should be not be greater than 8')
		val = False
		
	if not any(char.isdigit() for char in passwd):
		#print('Password should have at least one numeral')
		val = False
		
	if not any(char.isupper() for char in passwd):
		#print('Password should have at least one uppercase letter')
		val = False
		
	if not any(char.islower() for char in passwd):
		#print('Password should have at least one lowercase letter')
		val = False
		
	if not any(char in SpecialSym for char in passwd):
		#print('Password should have at least one of the symbols $@#')
		val = False
	if val:
		return val

# Main method
def main():
        input_password = 'asqwr1234@1,aF145#,2w3E*,2We3345'
        data = input_password.split(',')
        for passwd in data:
            if (password_check(passwd)):
                #print("Password is valid")
                print(passwd)
            else:
                #print("Invalid Password !!")
             print('')
		
# Driver Code	 
if __name__ == '__main__':
	main()












