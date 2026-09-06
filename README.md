# Python-Log-Analyser


I created a Python log analyser to investigate authentication (login) activity and identify suspicious behaviour

The tool reads logs from a .txt file which contains whether it was successful or failed, its IP address and the timestamp of the log.

This project improves my understanding of Cybersecurity and allows me to apply it to a real word scenario.


### Objective

The project focused on:

- Tracking failed and successful login attempts by IP.
- Track IPs with repeated failed login attempts.
- Detect suspicious logins during out of work hours.
- For potential brute force attacks, assign high severity alert.
- Output a security report containing key data.


## Technologies Used 
-  Python was used to create the tool.
-  Dictionaries were used to store failed and successful IPs.
-  Lists stored suspicious log in events.
-  Loops and conditional statements were used to process each log and to identify brute force activity. 


## How the Analyser Works

1. The code opens up the log.txt file and reads the logs so they can be analysed.
2. Each log is split using .split() and the login status, IP and timestamp are extracted.
3. To store successful and failed logins dictionaries were used.
4. If the IP exceeded more than 5 failed attempts the code flags it as potential brute force activity with a HIGH severity.
5. The hour of the login is also checked and any login before 6:00 is considered suspicious activity and flagged.
6. After a full analysis a security report is created containing the total number of IP addresses analysed, failed and successful login attempts, HIGH severity alerts and suspicious login events.

## Security Features

# Brute Force Detection 

To detect a brute force attack, dictionaries for loops and if statements were used to count failed login attempts for each IP. The max amount of login attempts was 5, if this threshold was exceed the code flags the IP in question as potential brute force activity and gives it a high severity.

# Suspicious Login Detection 

The code takes the hour from each timestamp using split and int. An if statement is used to check if the login was before 6:00. Suspicious events are stored in a list which uses append(), this allows the program to keep track of the IP in question.

# Security Report 

Using len() and sum() the program calculates the key data for the report.

These include:
- Total IP addresses analysed
- Total failed login attempts
- Total successful login attempts
- Number of HIGH severity alerts
- Number of suspicious login events

The output is then displayed using f-strings. 


# Testing 

The log analyser was tested using authentication log entries containing both normal and potentially suspicious/brute force activity.

Multiple failed login attempts were created for the the same IP address to test whether the analyser could identify potential brute-force activity. The IP 192.168.1.19 had 6 failed login attempts. The program flagged the IP as potential brute force activity and assigned it a severity of HIGH as it exceeded the threshold of five failures.






















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


