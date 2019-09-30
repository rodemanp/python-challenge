#Import nessary dependancies for os.path.join()
import os
import csv

#Path to read and collect data (input)
election_data=os.path.join('election_data.csv')
#Path to write output data via text (output)
output_data=os.path.join('election_output.txt')
#Create empty list for csv file
polls=[]
#Create empty dictionary to record candidate names
dict_polls={}
#Create empty dictionaty to summarize the total number votes 
dict_summary={}

#https://docs.python.org/3/library/csv.html
#Read in the CSV file;  If csvfile is a file object, it should be opened with newline=''
with open(election_data, newline='') as csvfile:
    #Read and split the data on commas and put into string variable poll_reader
    poll_reader=csv.reader(csvfile,delimiter=',')
    #Skip header row - dont need first row (header labels)
    next(poll_reader)

    #Create text file and open to start with election results and print; "w" means write
    text_file=open(output_data,"w")
    #Output to text file
    text_file.write("Election Results")
    #Output to environment
    print("Election Results")
    #Output to text file; \n means new line
    text_file.write("\n-------------------------")
    #Output to py environment
    print("-------------------------") 
    
    #Convert poll_reader string to list 
    for line in poll_reader:
        #Add single element to a list at the end
        polls.append(line)
    #Output to text file; \n means new line; len means length
    text_file.write("\nTotal Votes: "+str(len(polls)))
    #Output to py enviroment
    print("Total Votes: "+str(len(polls)))
    #Output to text file
    text_file.write("\n-------------------------")
    #Output to py environment
    print("-------------------------")
    
    #Convert list, poll, into dictionary for counting; and to group candidate names
    #Create loop to count and group by candidate name
    for line in polls:
        candidate=line[2]
        if candidate not in dict_polls:
           #Insert candidate into dictionary; and initialize to 0
            dict_polls[candidate]=0
        #Count the candidate inside dictionary
        dict_polls[candidate]+=1
    
    #Compute the percentages of each candidate of dict_polls and insert into new dict_summary; lens is length
    total_polls=len(polls)

    #Create loop to find percentage of each candidate
    for name in dict_polls:
        dict_summary[name]=round((dict_polls[name]/total_polls)*100)
        #Output to text file
        text_file.write("\n"+str(name)+": "+str(dict_summary[name])+"% "+"("+str(dict_polls[name])+")")
        #Output to py environment
        print(str(name)+": "+str(dict_summary[name])+"% "+"("+str(dict_polls[name])+")")
        
    #Initialize the highest value to compare
    highest=0

    #Find larget value of the key/value pair inside dictionary and place the key name inside winner
    #Create loop to find largest value within candidate summary of votes; from earlier
    for name in dict_summary:
        if highest < dict_summary[name]:
            highest=dict_summary[name]
            winner=name

    #Output to text file; \n is new line
    text_file.write("\n-------------------------")
    #Output to py environment
    print("-------------------------")
    #Output to text file; \n is new line
    text_file.write("\nWinner: "+winner)
    #Output to py environment
    print("Winner: "+winner)
    #Output to text file
    text_file.write("\n-------------------------")
    #Output to py enviornment
    print("-------------------------")
    
#Close text file
text_file.close()

