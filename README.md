# NOTES
1. Been told to use any language & I preferred Python to automate the test case.
2. JBehave is my suitable choice for BDD
3. Pacakage.json has been modified to fix the local network issue
4. For MVP/Demo test, I choose Allure report which generate the results in HTML using below commands
   1. Command prompt and go to feature directory
      1. behave -f allure_behave.formatter:AllureFormatter -o reports ./feature
      2. allure serve reports/
      3. HTML report should generate in local. I have attached some screenshots.


## TO RUN THE AUTO TEST

1. Install PyCharm IDE professional edition (trial) as it support BDD
2. Clone the repo in local and export the project.
3. **[IMPORTANT]** Seems like API is not returning the correct results as per the 
 logic perhaps something to check at server end. Therefore I have stopped the test immediate after submit the answers.


Thank you
