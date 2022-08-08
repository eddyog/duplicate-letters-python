
string = "Hello I am looking for an internship."

print("The duplicate letters are the following ")
for a in range(0, len(string)):
    count = 1; 
    for b in range(a+1, len(string)):
        if(string[a] == string[b] and string[a] != ' '):
            count = count + 1
            string = string[:b] + '0' + string[b+1:]

    if (count > 1 and string[a] != '0'):
        print [string[a], "- ", count]