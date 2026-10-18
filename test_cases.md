# Test Cases – Simulated Device Monitoring and Alert System

**Tested by:** [Your Name]  
**Date:** October 18, 2026

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | Displays all five initial readings correctly. | Pass |
| TC02 | Choose 2, enter 33 | Reading added successfully | Displays "Reading added successfully." | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | Displays an invalid-input message, and the reading is not added. | Pass |
| TC04 | Choose 2, enter 3.5 | Rejected; list unchanged | Displays an invalid-input message, and the reading is not added. | Pass |
| TC05 | Choose 2, enter 101 | Rejected because the value exceeds 100 | Displays a range error, and the reading is not added. | Pass |
| TC06 | Choose 3 | Displays correct temperature classifications | Displays 28 as NORMAL, 31 and 35 as WARNING, and 37 as CRITICAL. | Pass |
| TC07 | Choose 4 before adding a reading | Displays 5 readings, total 160, average 32.00, minimum 28, and maximum 37 | Displays 5 readings, total 160, average 32.00 °C, minimum 28 °C, and maximum 37 °C. | Pass |
| TC08 | Generate the initial summary | Displays NORMAL: 2 (40.00%), WARNING: 2 (40.00%), CRITICAL: 1 (20.00%) | Displays NORMAL: 2 (40.00%), WARNING: 2 (40.00%), and CRITICAL: 1 (20.00%). Overall status is ATTENTION REQUIRED. | Pass |
| TC09 | Enter 9 at the menu | Displays an invalid-choice message and shows the menu again | Displays "Invalid choice. Please enter a number from 1 to 5." and returns to the menu. | Pass |
| TC10 | Choose 5 | Displays the exit message and ends the program | Displays the thank-you message and exits the program. | Pass |

## Bugs Found and Fixed

The hardest test on this was checking the temperature classification boundaries. I checked that readings below 30 are classified as NORMAL, readings from 30 to 35 are classified as WARNING, and readings above 35 are classified as CRITICAL.