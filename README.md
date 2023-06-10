# Insider Threat Project Data Generator
This is to generate simulated logs for insider threat project - school project

#### How to run

```python
python main.py
```

The following datasets will be generated
1. Employee Data
2. PC Login/logoff logs
3. Office Building access logs
4. Web access proxy logs

Every suspect case is highlighted in the data generated. The following are suspect cases. Every suspect employee is marked as '1' in employee table.
#### Case 1 - after hour login
* There are 3 employee profiles. Any PC login/out outside of these usual hours for each employee profile is marked as suspect case '1' in pc access logs
- profile 1 --> 9am - 6pm Mon-Fri, 
- profile 2 --> 9am - 6pm any day 
- profile 3 --> 12 hour shift any day (8am-8pm or 8pm-8am)

#### Case 2 - potential account sharing (no building access, but pc logs)
* Potential account sharing - similar to impossible traveller, however no corresponding building access log by the same employee in another geographical location. May potentially mean that employee account is compromised. Marked as suspect case '2' in pc access logs

#### Case 3 - terminated employee login
* Marked as suspect case '3' in pc access logs

#### Case 4 - failed attempt to enter building / potential tailgating
* Marked as suspect case '4' in building access logs

#### Case 5 - impossible traveller
* Impossible traveller - employee pc access log is found to be in 2 geographical locations within a short span of time. Marked as suspect case '5' in pc access logs and building access logs. Potential case of account compromise and malicous actor impersonating as employee

#### Case 6 - potential data exfiltration
* Unusually large amount of data upload/download 
* Marked as suspect case '6' in proxy logs




