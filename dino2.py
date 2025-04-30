def store(filename): #store function creation with variable filename
    file=open(filename,'r'); #opening the file in read form
    text=file.readline() #reading the content of the text file
    comma=text.find(",") #using . find to find the position of the fist comma
    comma2=text.find(",",comma+1,len(text)); #finding the positon of the second comma
    list1=[]; #intialisng list
    list1.append(text[0:comma]); #appending the list with the first part of the text
    list1.append(text[comma+1:comma2]); #appending the list with the seconf part of the text
    list1.append(text[comma2+1:len(text)]); #appending the list with the third part of the text
    return list1; #returning the list with the elements of the text file separated

def decrypt(raw_dna): 
    sequence='' #initialisng the string to display the dna sequence
    for letter in raw_dna: #running a for loop through all the letters of raw data
        if letter=='A' or letter=='C' or letter=='G' or letter=='T': #conditonal statment to check whether the data is A,C,G or T.
            sequence += letter; #appending the string variable with the letters
    return sequence;

def process(valid_data):
    counta=0; #intialsing the counters
    countc=0;
    countg=0;
    countt=0;
    list2=[] #initialisng the list
    for i in valid_data: #for loop that runs through the  elements of the decrypted DNA sequence
        if i =='A': # conditonal statment that checks what the elements in the decrypted DNA Sequence are
            counta+= 1; #updating the counters accordingly
        elif i =='C':
            countc+= 1;
        elif i =='G':
            countg+= 1;
        elif i == 'T':
            countt+=1;
    list2=[counta,countc,countg,countt]; # adding the elements to the lists
    return list2;
        
def main():
    filename=input("Enter filename: ");
    info = store(filename);
    height = info[0];
    growth_rate = info[1];
    raw_dna = info[2];
    print(f"HEIGHT: {height} GROWTH RATE: {growth_rate}\nRAW DNA: {raw_dna[:30]}...");
    
    #part2
    print() ; # for space between parts 1 and 2 
    valid_dna = decrypt(raw_dna);
    count = process(valid_dna);
    print(f"DNA: {valid_dna}\nACGT-COUNT: {count}") ;  
    
main();