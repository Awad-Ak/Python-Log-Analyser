# Python-Log-Analyser


I created a Python log analyser to investigate authentication (login) activity and identify suspicious behaviour

The tool reads logs from a .txt file which contains whether it was successful or failed, its IP address and the timestamp of the log.

This project improves my understanding of Cybersecurity and allows me to apply it to a real word scenario 


### Objective

The project focused on:

- Tracking failed and successful login attempts by IP
- Track IPs with repeated failed login attempts
- Detect suspicious logins during out of work hours
- For potential brute force attacks, assign high severity alert
- Output a security report containing key data


## Technologies Used 
-  Python was used to create the tool
-  Dictionaries were used to store failed and successful IPs
-  Lists stored suspicious log in events
-  Loops and conditional statements were used to process each log and to identify brute force activity. 





Reads login data from a .txt log file
Identifies failed login attempts
Extracts the IP address associated with each failed attempt
Counts the number of failed attempts from each IP address
Displays the results in a readable format


Example log:

FAILED login from 192.168.1.10
SUCCESS login from 192.168.1.20
FAILED login from 192.168.1.10
FAILED login from 192.168.1.15
FAILED login from 192.168.1.10

Output:

Failed login attempts by IP:
192.168.1.10: 3 failed attempts
192.168.1.15: 1 failed attempts


Skills Practised:
Python dictionaries
Loops
Conditional statements
File handling
String manipulation


