#open certificate in read mode
with open('sample.txt', 'r+') as f:   

#open input values in read mode to convert to list
    with open('sampleInput.txt','r') as file:   
        for line in file.readlines():
#append comma seperated names to a list
            fname = line.rstrip().split(',') 
    
#read file
    file_source = f.read()

#loop for iterating over the list
    for j in range(len(fname)): 
        for i in fname:
            #replace name given in sample format with name from the list
            replace_string = file_source.replace('Arunesh Kumar',i ) 
            st=".txt"
            #save certificate for each name in the list
            with open("certificate_%s.txt" %i,"w") as f1:
                f1.write(replace_string)

