failed_ips = {}     #Create Dictionary  
succsessful_ips = {}  #Create Dictionary  
suspicious_logins = [] # make list  
  
  
  
Brute_Force_Max = 5 #Max amounts of fails before brute force attack is conisdered   

high_alerts = 0    #create counter to be used in final report 
  
  
with open("logs.txt", "r") as file:  #read data from logs.txt file  
     log_data = file.readlines()     


  
  
for log in log_data:    #Loop through Logs  
    log = log.split() 
    time = int(log[4].split(":")[0]) #split the time at the : and get the hour
    ip = log[3]

    if time < 6:
        suspicious_logins.append((ip, log[4]))

    


  
    if log[0] == "FAILED":  #Check for failed log  
        if log[3] in failed_ips:  
            failed_ips[log[3]] = failed_ips[log[3]] + 1  
        else:  
            failed_ips[log[3]] = 1  
  


  
  
    if log[0] == "SUCCESS":  
         if log[3] in succsessful_ips:  
              succsessful_ips[log[3]] = succsessful_ips[log[3]] +1  
         else:  
              succsessful_ips[log[3]] = 1  

  
  
  
ips = []    # make list   
  
for ip in failed_ips:  
     ips.append(ip) # add to list   
  
for ip in succsessful_ips:  
     if ip not in ips: # check if the ip is not in the list  
        ips.append(ip)  
 

 
 
for ip in ips: 
    if ip in failed_ips: 
        failed = failed_ips[ip] # find ip in failed ip dict and give me failed login count 
    else: 
        failed = 0 # if not in failed ip give value of 0 
    if ip in succsessful_ips: 
        successful = succsessful_ips[ip] 
    else: 
        successful = 0 




    if failed > Brute_Force_Max:
        severity = "HIGH"
        high_alerts = high_alerts +1
        print(f"{ip} - {failed} failed, {successful} successful - Potential brute-force activity - Severity: {severity}")



    elif any(suspicious_ip == ip for suspicious_ip, timestamp in suspicious_logins):
        for suspicious_ip, timestamp in suspicious_logins:
            if suspicious_ip == ip:
                print(f"{ip} - {failed} failed, {successful} successful - Suspicious login time: {timestamp}")
                break



    else:
        print(f"{ip} - {failed} failed, {successful} successful")


total_ips = len(ips)
total_failed = sum(failed_ips.values())
total_successful = sum(succsessful_ips.values()) # get totals for security report 
total_suspicious = len(suspicious_logins)

print("SECURITY REPORT")
print("-------------------------------")
print(f"Total IPs analysed: {total_ips}")
print(f"Total failed logins: {total_failed}")
print(f"Total successful logins: {total_successful}")
print(f"High severity alerts: {high_alerts}")
print(f"Suspicious login events: {total_suspicious}")