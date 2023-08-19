import numpy as np
temp=np.array([
               [
                  [[6,23],[14,20],[6,27],[14,22],[8,22],[6,32],[14,29]],
                  [[7,27],[12,29],[11,29],[-13,23],[15,28],[15,20],[8,32]],
                  [[5,21],[12,18],[-1,12],[12,20],[25,29],[17,22],[12,19]],
                  [[-2,15],[0,12],[2,18],[13,24],[10,16],[12,18],[0,17]]
               ],
               [
                  [[8,23],[14,20],[6,27],[14,22],[8,22],[6,32],[14,29]],
                  [[7,27],[12,29],[11,29],[-15,23],[15,31],[15,30],[8,30]],
                  [[5,21],[12,18],[-12,12],[12,20],[25,27],[17,28],[12,19]],
                  [[-2,15],[0,12],[2,18],[13,24],[10,20],[12,24],[0,17]]
               ],
               [
                  [[9,23],[14,20],[6,27],[14,22],[8,22],[6,32],[14,29]],
                  [[7,27],[12,29],[11,29],[15,23],[-13,31],[15,30],[8,30]],
                  [[5,21],[12,18],[-1,12],[12,20],[25,27],[17,28],[12,19]],
                  [[-2,15],[0,12],[2,18],[13,24],[10,20],[12,24],[0,17]]
               ],
               [
                  [[6,23],[14,20],[6,27],[14,22],[8,22],[6,32],[14,29]],
                  [[7,27],[12,29],[11,29],[-13,23],[15,31],[15,30],[8,30]],
                  [[5,21],[12,18],[-1,12],[12,20],[25,27],[17,28],[12,19]],
                  [[-2,15],[0,12],[2,18],[13,24],[10,20],[12,24],[0,17]]]
           ])

month=['November','December','January','February']
day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

print(temp)

# 2
print('Dimension: ' ,temp.ndim)
print('Shape:',temp.shape)


# 3
print('daily temperatures for the first week of eaxh month \n',temp[:,0,:])


# Print the temperatures for Tuesday of each month.
print('daily temeratures for tuesday of each month \n',temp[:,:,1])


#Print only the maximum temperature for all the weekdays of Dec and Feb.
print('Only the max temperature for all the weekdays of dec and feb\n ' ,temp[1:4:2,:,:,1])


# Print all the days along with the week number in November when the minimum temperature was less than 8 degrees.
print('all the days along with the week number in november when the minimum temperature was less than 8 degrees \n',np.argwhere(temp[0,:,:,0]<8))

# Print all the weeks in Dec and Jan where the maximum temperature has crossed a threshold of 20 degrees.
print('Above 20 Degrees in Dec & Jan')

for i in [1,2]: 
    
     for j in range(4): 
            
            if np.any(temp[i,j]>20): 
                print(f'{month[i]} Week-{j+1}')
#Check if there are any absurd values present in the dataset(like some temp which should not be present in the data)
valid_min_temp = -50
valid_max_temp = 50

# Check for absurd values in the dataset
absurd_values = []

for month_idx in range(4):
    for week_idx in range(4):
        for day_idx in range(7):
            min_temp = data[month_idx, week_idx, day_idx, 0]
            max_temp = data[month_idx, week_idx, day_idx, 1]
            
            if min_temp < valid_min_temp or min_temp > valid_max_temp:
                absurd_values.append(f"Month: {month_idx + 1}, Week: {week_idx + 1}, Day: {day_idx + 1}, Min Temp: {min_temp}")
                
            if max_temp < valid_min_temp or max_temp > valid_max_temp:
                absurd_values.append(f"Month: {month_idx + 1}, Week: {week_idx + 1}, Day: {day_idx + 1}, Max Temp: {max_temp}")

if absurd_values:
    print("Absurd temperature values found:")
    for value in absurd_values:
        print(value)
else:
    print("No absurd temperature values found.")



# Find and print the indexes of all the outlier(unusual) values present in the above dataset.
valid_min_temp = -50
valid_max_temp = 50


outlier_indexes = []

for month_idx in range(4):
    for week_idx in range(4):
        for day_idx in range(7):
            min_temp = data[month_idx, week_idx, day_idx, 0]
            max_temp = data[month_idx, week_idx, day_idx, 1]
            
            if min_temp < valid_min_temp or min_temp > valid_max_temp:
                outlier_indexes.append((month_idx, week_idx, day_idx, 0))
                
            if max_temp < valid_min_temp or max_temp > valid_max_temp:
                outlier_indexes.append((month_idx, week_idx, day_idx, 1))


if outlier_indexes:
    print("Indexes of outlier values:")
    for index in outlier_indexes:
        print(f"Month: {index[0] + 1}, Week: {index[1] + 1}, Day: {index[2] + 1}, Value Type: {'Min Temp' if index[3] == 0 else 'Max Temp'}")
else:
    print("No outlier values found.")


# Find the average max temperature for the winter months in Jaipur
for i in range(1,4): 
   
    mean=[] 
    a=np.mean(temp[i],axis=1) 
    b=np.mean(a,axis=0) 
    mean.append(b[1]) 
print(f'Average max temperature for the winter month: {np.round(np.mean(mean),2)}',chr(176),'c')

#  Find the weekly min avg temp for the month of Dec in Jaipur
a=np.mean(temp[1:4],axis=1) # calculate mean weekly temp 
b=np.mean(a,axis=1)
c=np.mean(b,axis=0)
print(f'Average max temperature for the winter month: {np.round(c[1],2)}',chr(176),'c')

# Find the weekly min avg temp for the month of Dec in Jaipur 
a=np.mean(temp[1:4],axis=1) # calculate mean weekly temp 
b=np.mean(a,axis=1)
c=np.mean(b,axis=0)
print(f'Average max temperature for the winter month: {np.round(c[1],2)}',chr(176),'c')

 # Find the overall avg temp for the months Dec and Jan
print(f'Overall avg temp for the months Dec & Jan: {np.round(np.mean(temp[1:3]),2)}',chr(176),'C')
  
# Find the least temp experienced by the city in the month of Dec and Jan. Also print the exact date( Day/Week/Month) for the same.
for i in range(1,3): # iterate over Dec & Jan 
    print(f'Least temperature in {month[i]}- {np.min(temp[i])}',chr(176),'C')
    
    min_temp=np.min(temp[i]) # Finding min temp
    frmt=np.argwhere(temp[i] == min_temp) # indexing min temp
    
    print(f'{day[frmt[0,1]]}/Week-{frmt[0,0]+1}/{month[i]}') 
# Find the max temp in the month of Feb and return its date(Day/Week/Month)
print(f'Max temperature in Feb - {np.max(temp[3])}',chr(176),'C') #Feb is the fourth month

max_temp=np.max(temp[3]) # Finding max temp
frmt=np.argwhere(temp[3] == max_temp) # indexing max temp 

print(f'{day[frmt[0,1]]}/Week-{frmt[0,0]+1}/Feb') #frmt[week,day,temp]

# Find the days in the month of Nov where the max temp of the day dropped below the avg temp of the month. A      
loc=np.argwhere((temp[0,:,:,1])<(np.mean(temp[0])))
for i in range(loc.shape[0]):
    print(f'Week-{loc[i,0]+1} {day[loc[i,1]]}')

print(temp.reshape(4,56))

print(f'Temp data in Fahrenheit:\n{temp*(9/5)+32}')

# calculate the average min & max temp weekly in Dec
avg=np.mean(temp[1],axis=1)

# calculate  overall average weekly temp
avg2=np.mean(avg,axis=1) 

# sort and print the result in descending order
print(f'Dec month average weekly temp in descending order: {np.round(np.sort(avg2)[::-1],1)}')


#selecting the temp of the first three days of each month
temp_3days=temp[:,:,:3] 

x=np.mean(temp_3days,axis=2) # calculate 3 days avg weekly temp
y=np.mean(x,axis=1) # calculate each 3 days avg weekly temp
z=np.mean(y,axis=1) # calculate 3 days avg weekly temp for each month

ovral_mean=np.mean(temp[1:4]) # calculate overall avg temp of wintere
base=np.append(z,ovral_mean) # adding base value into array 

print(np.sort(base)[::-1]) # print in descending order

# store the difference between the temp
diff=(temp[:,:,:,1]-temp[:,:,:,0]).reshape(4,4,7,1) # reshape it as the same as base array
print('Difference Between Dilay temperatures: \n',diff)


wint_maxdiff=[]
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,6):
            x=temp[i,j,k+1,1]-temp[i,j,k,1]
            wint_maxdiff.append(x)
print(wint_maxdiff)



wint_mindiff=[]
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,6):
            x=temp[i,j,k+1,0]-temp[i,j,k,0]
            wint_mindiff.append(x)
print(wint_mindiff)

array=np.array((wint_maxdiff,wint_mindiff))
array