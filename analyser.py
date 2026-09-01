failed_ips = {}

with open("logs.txt", "r") as file:  #read data from logs.txt file
     log_data = file.readlines()   


for log in log_data:
    log = log.split()

    if log[0] == "FAILED":
        if log[3] in failed_ips:
            failed_ips[log[3]] = failed_ips[log[3]] + 1
        else:
            failed_ips[log[3]] = 1

print("Failed login attempts by IP:")

for ip in failed_ips:
    print(f"{ip}: {failed_ips[ip]} failed attempts")
