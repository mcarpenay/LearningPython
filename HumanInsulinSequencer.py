import re 

sum = 0
with open('preproinsulin_seq.txt','r') as rf:
    with open('preproinsulin_seq_clean.txt','a') as wf:
        for line in rf:
#replace every 1st argument in the sub() method with the second argument if found in the line
            line_Content = line
            line_Content = re.sub(" ","",line_Content)
            line_Content = re.sub("61","",line_Content)
            line_Content = re.sub("1","",line_Content)
            line_Content = re.sub("//","",line_Content)
            line_Content = re.sub("\n","",line_Content)
            line_Content = re.sub("\t","",line_Content)
            line_Content = re.sub("ORIGIN","",line_Content)
            line_Content = line_Content.lower()

            sum = sum + len(line_Content)

            print(line_Content, end="")
            wf.write(line_Content)
            print(sum)

#Save amino acids 1-24 as lsinsulin_seq_clean.txt. Verify that your file has 24 characters.
with open('preproinsulin_seq_clean.txt','r') as rf:
    with open('lsinsulin_seq_clean.txt','a') as wf:
        rf.seek(1) 
        sizeToRead = 24
    # read the next 10 characters in from the point set by the seek function
        f_content = rf.read(sizeToRead) 
        print(f_content)
        wf.write(f_content)
        wf.close()

#Save amino acids 25-54 as binsulin_seq_clean.txt. Verify that your file has 30 characters
   
    with open('binsulin_seq_clean.txt','a') as wf:
        rf.seek(25) 
        sizeToRead = 30
    # read the next 10 characters in from the point set by the seek function
        f_content = rf.read(sizeToRead) 
        print(f_content)
        wf.write(f_content)
        wf.close()
#Save amino acids 55-89 as cinsulin_seq_clean.txt. Verify that your file has 35 characters
    
    with open('cinsulin_seq_clean.txt','a') as wf:
        rf.seek(55) 
        sizeToRead = 35
    # read the next 10 characters in from the point set by the seek function
        f_content = rf.read(sizeToRead) 
        print(f_content)
        wf.write(f_content)
        wf.close()
#Save amino acids 90-110 as ainsulin_seq_clean.txt. Verify that your file has 21 characters.
    
    with open('ainsulin_seq_clean.txt','a') as wf:
        rf.seek(90) 
        sizeToRead = 21
    # read the next 10 characters in from the point set by the seek function
        f_content = rf.read(sizeToRead) 
        print(f_content)
        wf.write(f_content)
        wf.close()
