time = '1h 45m,360s,25m,30m 120s,2h 60s'
time = time.split(',')
count_m = 0 
for i in range(0,len(time)):
    time1 = time[i].split(' ')
    for part in time1:
            if 'h' in part:
                part = part.replace('h','')                  
                count_m += int(part)*60
            elif 'm' in part:
                 part = part.replace('m','')
                 count_m += int(part)
            elif 's' in part:
                 part = part.replace('s','')
                 count_m += int(part)/60           
        
print(int(count_m))
#