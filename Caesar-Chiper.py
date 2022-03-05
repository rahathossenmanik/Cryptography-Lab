text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING UNIVERSITY OF RAJSHAHI BANGLADESH";
shift = 3;
print("Plain Text: " + text);
chiper = "";
for i in range(len(text)):   #Encryption
    char = text[i];
    if(char.isupper()):
        chiper = chiper + chr( (ord(char)+shift-65)%26 + 65);
    elif(char.islower()):
        chiper = chiper + chr( (ord(char)+shift-97)%26 + 97);
    else:
        chiper = chiper + char;
print("Chiper Text: " + chiper);

plain = "";
for i in range(len(chiper)):   #Decryption
    char = chiper[i];
    if(char.isupper()):
        plain = plain + chr( (ord(char)-shift-65)%26 + 65);
    elif(char.islower()):
        plain = plain + chr( (ord(char)-shift-97)%26 + 97);
    else:
        plain = plain + char;
print("Decrypted Text: " + plain);
