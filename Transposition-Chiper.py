text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING UNIVERSITY OF RAJSHAHI BANGLADESH";
width = 5;
print("Plain Text: " + text);
chiper = "";
j = 0;
k = 0;
for i in range(len(text)):   #Encryption
    char = text[i];
    if(j+width*k < len(text)):
        chiper = chiper + text[j+width*k];
        k = k + 1;
    else:
        j = j + 1;
        k = 0;
        chiper = chiper + text[j+width*k];
        k = k + 1;
print("Chiper Text: " + chiper);

plain = "";
j = 0;
k = 0;
l = 1;
r = int(len(chiper)/width);
for i in range(len(chiper)):   #Decryption
    char = chiper[i];
    if(j+r*k < len(chiper)):
        plain = plain + chiper[j+r*k];
        k = k + 1;
    else:
        j = j + 1;
        k = 0;
        l = 1;
        plain = plain + chiper[j+r*k];
        k = k + 1;
    print(k)
    print(j)
    print(l)
print("Decrypted Text: " + plain);
