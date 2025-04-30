def pass_len(password): #Function that checks if the password is correct length, returns True if criteria met
    if len(password)>=8:
        return True
    
def lower_case(password): #Function that checks if the password has lower_case letter, returns True if criteria met
    lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #lists that stores all lower_case letters
    for letter in password: #loop going through every character of the password
        if letter in lower: #conditional statment that checks if there is a lowercase letter present in the password
            return True
        
def upper_case(password): #Function that checks if the password has Upper_case letter, returns True if criteria met
    upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #lists that stores all Upper_case letters
    for letter in upper: #loop going through every character of the password
        if letter in upper: #conditional statment that checks if there is an upper case letter present in the password
            return True
        
def numeric_case(password):     #Function that checks if the password has numeric characters, returns True if criteria met
    numeric=['1','2','3','4','5','6','7','8','9','0']   #lists that stores all numeric characters
    for letter in password:     #loop going through every character of the password
        if letter in numeric:   #conditional statment that checks if there is a number present in the password
            return True
        
def special_case(password): #Function that checks if the password has special characters, returns True if criteria met
    special=['!','@','#','%','?','$','^','&','*'] #lists that stores all numeric characters
    for letter in password: #loop going through every character of the password
        if letter in special: #conditional statment that checks if there is a special character present in the password
            return True
        
def space(password): #Function that checks if the password does not have spaces, returns True if criteria met
    if ' ' not in password: #conditional statment that checks the password
        return True
    
def invalid(password): #Function that checks if any invalid characters are present, returns a list of all the invalid characters
    e_list="7elL2GJVkrv0dQ%Eb?N6uw*#t!@hYAop&O^a3FWCyKUT4PR5zBjDH8XgZnf9qMm1cSIsi$x " #all the valid characters in a string, includes space so as not to clash with the space function
    invalid_letter=[] #intialising list that stores any invlaid characters found
    for letter in password: #loop going through every character of the password
        if letter not in e_list: # checks if password character is present in string that contains all valid characters
            invalid_letter.append(letter) #Appends the list with any invalid characters
    return invalid_letter

def encrypt(password,shift): #function encrypts that encrypts the password, by shifting it as per the shift key
    password2='' #intialising the new encrypted password
    ENCRYPTION_SOURCE = r"7elL2GJVkrv0dQ%Eb?N6uw*#t!@hYAop&O^a3FWCyKUT4PR5zBjDH8XgZnf9qMm1cSIsi$x " #Encryption source
    for letter in password: #loop going through every character of the password
        if letter in ENCRYPTION_SOURCE: #checks if the character is in the encryprion source
            index= ENCRYPTION_SOURCE.index(letter) #using .index to locate the index number of the character in the encryption source
            password2=password2+ENCRYPTION_SOURCE[index-shift] #creates encrypted password by adding new encrypted letter based on necryption source and shift value
    return password2

def main(): 
    file=open("saved_passwords.txt","w") #open the file in write mode
    shift=int(input("Enter the Encryption Key: ")) #prompting user to enter shift value in integer
    file.write(str(shift)+'\n') # using .write to store in text file
    website= input("\nEnter website: ")
    website=website.lower().strip()   #converting website to lower case and stripping trailing spaces
   
    valid_password=False
    while valid_password==False:  #while loop that controls when the program ends
        password=input("Enter password: ") #prompting user to enter password
        invalid_letter=invalid(password) #calls invalid function to check for any invalid characters in the password
        if pass_len(password) and lower_case(password)and upper_case(password)and numeric_case(password) and special_case(password)and space(password) and len(invalid_letter)==0: #conditonal statment that checks if all criteria of password is met
            new_password=encrypt(password,shift) #calls the encrypt function to encrypt website and password
            new_web=encrypt(website,shift)
            file.write(new_web+'\n') #writes encrypted website and password to text file
            file.write(new_password+'\n')
            print(f"\nPassword for {website} has been encrypted and stored successfully") #prints success message
            another=input("Add another password? (y/n): ") #prompts user to continue adding
            if another =='y': 
                website= input("\nEnter website: ") #asks user to enter website if they wish to continue
                website=website.lower().strip()                
                valid_password = False
            else: 
                valid_password = True #ends program if user enters 'n'
                print("Goodbye!")
        else:
            indent=(" "*8) #declaring indent size for print
            print("\nIssues:")
            if pass_len(password)!=True: #conditonal statments printing what is wrong with provided password by calling respective functions
                print(f"{indent}Password should be at least 8 characters")
            if space(password) != True:
                print(f"{indent}Password cannot have spaces")
            if upper_case(password) != True:
                print(f"{indent}Missing a uppercase letter in the password")
            if lower_case(password) != True:
                print(f"{indent}Missing a lowercase letter in the password")
            if special_case(password) != True:
                print(f"{indent}Missing a special character in the password")            
            if numeric_case(password) != True:
                print(f"{indent}Missing a digit in the password")           
            if len(invalid_letter) !=0:
                invalid_letter2=[]
                for value in invalid_letter: #loop through the list of invalid charachters
                    if value not in invalid_letter2: #checks if values already exsists in the list to avoid repeated printing
                        invalid_letter2.append(value)
                print(f"{' '*8}{', '.join(invalid_letter2)} are not allowed in the password")
            print("\nPlease enter a strong valid password")
    file.close() #closing file
main()
    