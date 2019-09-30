#Import nessary dependancies for os.path.join()
import os
import csv

#Path to read and collect data (input)
budget_data=os.path.join('budget_data.csv')
#Path to write output data via text (output)
output_data=os.path.join('budget_output.txt')

#Create empty list for CSV file
profit_loss=[]
#Create empty dictionary to record profit/loss summary
pl_summary={}

#https://docs.python.org/3/library/csv.html
#Read in the CSV file;  If csvfile is a file object, it should be opened with newline=''
with open(budget_data, newline='') as csvfile:
    #Read and split the data on commas and put into string variable budget_reader
    budget_reader=csv.reader(csvfile,delimiter=',')
    #Skip header row - dont need first row (header_labels)
    next(budget_reader)
    
    #Set values for total and total_month varaiables to setup our loop function 
    total=0
    total_months=0
    
    #Manipulate element by converting budget_reader string to create list profit_loss
    for line in budget_reader:
        #Add single element to a list at the end
        profit_loss.append(line)
        #Make The total net amount of "Profit/Losses" over the entire period an integer
        total+=int(line[1])
        #The total number of months included in the data set
        total_months+=1

    #Set values to help find increase and decrease profits for next loop   
    subtract_MoM=0
    tot_MoM=0
    Avg_Mom=0

    #Initialize max increase and max decrease values with new values
    max_decrease=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])
    max_increase=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])
    
    #Compute the change in "Profit/Losses" between months over the entire period; need to look at latest month and year to earliest
    for months in range(total_months,1,-1): 
        #Stops when Months change
        subtract_MoM=int(profit_loss[months-1][1])-int(profit_loss[months-2][1])
        #Setup up to find the Greatest Increase (max_increase) and Greatest Decrease (max_decrease)
        if subtract_MoM < max_decrease:
            min_month_yr=profit_loss[months-1][0]
            max_decrease=subtract_MoM
        elif subtract_MoM > max_increase:
            max_increase=subtract_MoM
            max_month_yr=profit_loss[months-1][0]
        #Total amount change in "Profit/Losses" between months over the entire period
        tot_MoM=tot_MoM+subtract_MoM
    #The average change in "Profit/Losses" between months over the entire period    
    Avg_MoM=tot_MoM/(total_months-1)



#Create text file and open; w means write
text_file=open(output_data,"w")
#Output to text file
text_file.write('Financial Analysis')
#Output to py environment
print('Financial Analysis')
#Output to text file; \n means new line
text_file.write('\n----------------------------')
#Output to py environment
print('----------------------------')
#Output to text file; \n means new line
text_file.write('\nTotal Months: '+str(total_months))
#Output to py environment
print('Total Months: '+str(total_months))
#Output to text file
text_file.write('\nTotal: $'+str(total))
#Output to py environment
print('Total: $'+str(total))
#Output to text file
text_file.write('\nAverage  Change: $'+str(round(Avg_MoM,2)))
#Output to py environment
print('Average  Change: $'+str(round(Avg_MoM,2)))
#Output to text file
text_file.write('\nGreatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
#Output to py environment
print('Greatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
#Output to text file
text_file.write('\nGreatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')
#Output to py environment
print('Greatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')
#Close text file
text_file.close()
