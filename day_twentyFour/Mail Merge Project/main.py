#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []

with open("./Input/Names/invited_names.txt") as name_list:
    for name in name_list:
        names.append(name.rstrip(name[-1]))
        # The .rstrip(name[-1]) is to remove the \n from the invited_names.txt file
        
with open("./Input/Letters/starting_letter.txt") as letter_text:
    body = letter_text.read()
    for name in names:
        print(body.replace("[name]", name))
        with open(f"./Output/ReadyToSend/{name}.txt", mode='w') as ReadyToSend:
            ReadyToSend.write(body.replace("[name]", name))

