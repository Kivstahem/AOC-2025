import time
starttime = time.time()
total_joltage = 0;
BATTERY_BANK_SIZE = 12;

global output
global output_index

def push_down(output, output_index, index, limit, new_nmbr, new_nmbr_index):
    # check if we are not past the end:
    if index >= limit:
        return; # We are finished
    old_nmbr       = output[index];
    old_nmbr_index = output_index[index];
    if old_nmbr <= new_nmbr:
        # The new number is bigger or just as big, so let's replace it and push the current number down the stack
        if old_nmbr_index > new_nmbr_index:
            #The index should be LARGER as the new number is further left in the data stream
            output[index]       = new_nmbr;
            output_index[index] = new_nmbr_index;
            push_down(output, output_index, index+1, limit, old_nmbr, old_nmbr_index);
        else:
            return # done

with open("input.txt") as file:
    for line in file:
        str_number   = line.strip();
        output_index = [];
        output = list(line.strip()[-BATTERY_BANK_SIZE:]);
        start = len(str_number) - BATTERY_BANK_SIZE;
        output_index = list(range(start,start+BATTERY_BANK_SIZE));
        index          = output_index[0];
        for x in reversed(range(0, index)):
            push_down(output,output_index,0,BATTERY_BANK_SIZE,str_number[x],x)
        total_joltage = total_joltage + int("".join(output)); 

endtime = time.time()
print("The final joltage is: ", total_joltage);
print("Program took: ", endtime-starttime, " seconds");