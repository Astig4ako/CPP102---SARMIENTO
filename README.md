Simulated Device Monitoring and Alert System

1. Student Name

Charles Kent R. Sarmiento

2. Student Number

260130

3. Section

1 CPE-B

4. Project Description

The Simulated Device Monitoring and Alert System is a Python program that monitors temperature readings and classifies them based on set limits. It can display readings, accept new readings, generate classifications, and calculate a summary of the data.

5. Features

Displays the current temperature readings.

Accepts new readings from 0 to 100.

Rejects invalid inputs.

Classifies readings as NORMAL, WARNING, or CRITICAL.

Calculates the total, average, minimum, and maximum.

Displays category counts, percentages, and overall system status.

Provides a menu for selecting program functions.

6. Requirements

Python 3

Visual Studio Code or another Python editor

A terminal or command prompt

7. How to Run the Program

Open the Week17 folder in Visual Studio Code.

Open the terminal.

Run the following command:

python device_monitor.py

Select a menu option from 1 to 5.

Follow the instructions displayed by the program.

8. Sample Output

DEVICE MONITORING AND ALERT SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 4

MONITORING SUMMARY
------------------
Number of readings   : 5
Total of readings    : 160
Average temperature  : 32.00 °C
Minimum temperature  : 28 °C
Maximum temperature  : 37 °C

NORMAL   : 2 (40.00%)
WARNING  : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED

9. Test Cases

The program is tested using valid and invalid inputs, temperature classifications, summary calculations, and menu options. The detailed test cases and results are documented in test_cases.md.

10. Known Limitations

The program uses simulated temperature readings and does not connect to an actual device or temperature sensor. The readings are stored in memory, so any newly added readings are lost when the program ends.

11. Reflection

Through this project, I learned how to organize a Python program using functions, loops, conditions, and input validation. I also learned how to calculate summaries and classify data using different conditions. This project helped me understand how a simple monitoring system can process readings and provide useful information to its users.