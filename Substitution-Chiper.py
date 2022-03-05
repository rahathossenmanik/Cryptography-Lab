text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING UNIVERSITY OF RAJSHAHI BANGLADESH";
key = "phqgiumeaylnofdxjkrcvstzwb";
print("Plain Text: " + text);
chiper = "";
for i in range(len(text)):   #Encryption
    char = text[i];
    if(char.isupper()):
        chiper = chiper + key[ord(char)-65].upper();
    elif(char.islower()):
        chiper = chiper + key[ord(char)-97];
    else:
        chiper = chiper + char;
print("Chiper Text: " + chiper);

plain = "";
for i in range(len(chiper)):   #Decryption
    char = chiper[i];
    if(char.isupper()):
        plain = plain + chr(key.find(chr(ord(char)-65+97))+65);
    elif(char.islower()):
        plain = plain + chr(key.find(char)+97);
    else:
        plain = plain + char;
print("Decrypted Text: " + plain);
