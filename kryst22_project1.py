# Krystalina Truong # TCSS 142 # PROJECT ONE # FEB 23RD, 2017


#PSEDUOCODE :
# Set a variable for an open file for the training set (train.csv);
# Initialize lists and counters for the healthy patients and the unhealthy patients;
# Understand that the deliminter is commas (csv file);
# Extract the 7th value (which in python is considered the 6th) to determine whether the patient has a disease;
# Append to accoridng list;
# Calculate the averages for each set - both healthy and unhealthy  (use a for loop);
# Print the averages out to the IDLE screen;
# Create a for loop to calculate, and print, the seperator values;
# Create a for loop to determine the accuracy of the program - print this to the IDLE screen;
# Create a for loop to determine the identifier numnbers and its' determination on whether or not they have a disease;
# Ask the user to enter a new test set (set1.csv);
# Ask the user to enter a csv file name to write results out to (results1.csv);
# CLOSE all open files to save work;



# Open the file inputs

openFile = input('Enter the name of the training set file: ')
fileInput = open(openFile, 'r')

# Initialize lists and counters for both healthy and ill patients

lHealthy = [0]*7;
cHealthy = 0;
aHealthy = [0]*7;
aHealthyCount = 0;

lIll = [0]*7;
cIll = 0;
aIll = [0]*7;
aIllCount = 0;

lHealthynIll = [];
meanList = [0]*7;


# For Loop used to declare what patient is healthy or ill;

for line in fileInput: # reads each line from fileInput above;
    idxCount = 0;
    idxCount2 = 0;
    tLine = line.split(',');
    if '?' in tLine[6]: # if there is a '?', replace it with 0
        tLine[6] = 0;
    cNum = float(tLine[6]);
    if cNum < 0.5: # declares healthy patients
        lHealthynIll.append(cNum);
        cHealthy += 1;
        for number in tLine:
            if number == '?':
                number = 0;
            lWrite = float(number) + lHealthy[idxCount]; # total for healthy patients
            lHealthy[idxCount] = lWrite;
            idxCount += 1;
    if cNum >= 0.5: # declares ill patients
        lHealthynIll.append(cNum);
        cIll += 1;
        for iNum in tLine:
            if iNum == '?':
                iNum = 0;
            lWrite2 = float(iNum) + lIll[idxCount2]; # total for ill patients
            lIll[idxCount2] = lWrite2;
            idxCount2 += 1;


# For loop for averages for healthy patient average values

for num in lHealthy:
    num = num / cHealthy;
    aHealthy[aHealthyCount] = num; # replaces old value with new value for num
    aHealthyCount += 1;
# Print to IDLE the averages for healthy patients
print("Healthy patients' averages: ");
print("{:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}".format(aHealthy[0], aHealthy[1], aHealthy[2], aHealthy[3], \
                                                        aHealthy[4], aHealthy[5], aHealthy[6]))
    


# For loop for averages for ill patient average values

for num in lIll:
    num = num/cIll;
    aIll[aIllCount] = num; # replaces old value with new value for num
    aIllCount += 1;
# Print to IDLE the averages for Ill patients
print("Ill patients' averages: ");
print("{:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}".format(aIll[0], aIll[1], aIll[2], aIll[3], \
                                                        aIll[4], aIll[5], aIll[6]))

# For loop to calculate seperator value

for num in range(0,7):
    meanList[num] = (aHealthy[num] + aIll[num]) / 2;
print("Separator values: ");
print("{:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f},".format(meanList[0], meanList[1], meanList[2], meanList[3], \
                                                        meanList[4], meanList[5], meanList[6]));



fileInput = open(openFile, 'r');

# Set up list and counter for test set

lIsIll = [];
cIsIll = 0;

isIll = len(meanList) / 2;

# For loop for accuracy

isAccurate = -1;
for line in fileInput:
    accIdx = 0;
    illTotal = 0;
    tLine = line.split(',');
    cNum = tLine[6];
    for num in tLine:
        if '?' in num: # changes '?' to 0 value
            num = 0;
        if float(num) > meanList[accIdx]:
            illTotal += 1;
        accIdx += 1;
    if cNum == 0.5 and illTotal <= isIll: # determines if analysis is the same as disease indicator value
        isAccurate += 1;
        
    else:
        isAccurate += 1;
            
print("Accuracy: {:.2f}".format(isAccurate/len(lHealthynIll))) # prints to IDLE accuracy

fileInputT = open(input("Enter the name of the test set: "), 'r')

# Initialize list and counter for the new test set

lPatient = [];
lRisk = [];
classIdx = 0;

# For loop to obtain identifier numbers

for line in fileInputT:
    cRisk = 0;
    lineIdx = 0;
    line = line.split(',');
    lPatient.append(line[0]);
    if float(line[0]) > 120: # value can't be age if above 120, file has identifier numbers    
        line = line[1:7];
    elif float(line[0]) < 120: # value potentially age, not identifier numbers
        line = line[0:6];
    for num in line:
        if '?' in num:
            num = 0;
        if float(num) > meanList[lineIdx]: # accumulates total number of values above average
            cRisk += 1;
        lineIdx += 1;
    lRisk.append(cRisk); # appends total values above average per line into list
    classIdx += 1;


# Ask user for the input of the testing file
# Ask the user for a name to write out for results to a csv file
# Write out to csv file
    
outFile = open(input('Enter the name of the output file: '),'w'); # opens new file to output to
outFile.write('ID,Disease?\n'); # writes header to file
for num in lPatient:
    if lRisk[cIsIll] > isIll: # finds patient identifier number
        outFile.write('{},yes\n'.format(lPatient[cIsIll])) # if >= 0.5, display ID and "yes"
    elif lRisk[cIsIll] < isIll: # finds patient identifier number
        outFile.write('{},no\n'.format(lPatient[cIsIll])) # if < 0.5, display ID and "no"
    cIsIll += 1;
    lIsIll.append(num);

# Print to IDLE screen "Done" to ensure that csv outFile is written to.

print("Done");

# CLOSE ALL OPEN FILES TO SAVE

fileInput.close();
outFile.close();



    
