def read_file(filename): #Fucntion that opens the text file, and decrypts the content
    file=open(filename,'r') #usng open in read mode
    text=file.readlines() #reading everyline of the text file
    ENCRYPTION_SOURCE = r"7elL2GJVkrv0dQ%Eb?N6uw*#t!@hYAop&O^a3FWCyKUT4PR5zBjDH8XgZnf9qMm1cSIsi$x "
    words=[] #intialising list that stores the words in the text
    decrypt_list=[] #list that will store the decrypted text 
    web_pass={} #intialising dictionary that stores the password
    for lines in text: #loop runs through the lines of the text
        lines=lines.strip() #strips of any whitespaces
        words.append(lines) #appends the stripped words to the word list
    shift=int(words[0]) #declares that the first line is the shift key
    for i in range(1,len(words)): #loops through the text except for the shift key
        decrypt='' #Intialisng the decrypted text
        for letter in words[i]: #loop through every character of the words
            index=ENCRYPTION_SOURCE.index(letter) #finds the position of the letter on the encryption source
            new_index = shift+index #finds the position of the decrypted letter on the encryption source
            if new_index > len(ENCRYPTION_SOURCE): #checks if the new index is larger than the length of the encryption source so as not to make the index go out of bounds
                new_index = new_index-len(ENCRYPTION_SOURCE) #substracts the new index with the length of the encryption source to find the postion of the decrypted letter
            decrypt=decrypt+ENCRYPTION_SOURCE[new_index] #add the letters to form the decrypted word
        decrypt_list.append(decrypt) #append the list with the decrypted word
    for i in range(0,len(decrypt_list),2): #loop that goes through the decrypted list and skips by step of 2
        key=decrypt_list[i] #defines the key value
        value=decrypt_list[i+1] #defines the value
        web_pass[key]=value #updates the dictionary
    return web_pass        
                
def main():
    file=input("Enter filename: ") #propmt to enter file name
    dictionary=read_file(file) #calls the read_file function
    valid=False
    while valid==False: #while loop to control how many times it will loop
        website=input("\nEnter a website: ") #prompt user to enter website
        website=website.lower().strip() #transforms website to lowercase and strips whitespaces
        if website in dictionary.keys(): #loop that runs through the keys of the dictionary
            print(f"Password for {website} is '{dictionary[website]}.") #print message
            cont=input("\nGet another password? (y/n):")#prompts user to continue or not
            if cont =='y': #keeps running while loop if user says 'y'
                valid=False
            elif cont=='n': #ends while loop if user says 'n'
                valid=True
                print("Goodbye!")
        else:
            print("The website doesn't exist") #message printed if website doesnt exist
            valid=False
    
        
main()