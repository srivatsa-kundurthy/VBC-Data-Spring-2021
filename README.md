# VBC Data - Spring 2021     
## About
We're back for Spring!   
This business simulation involves shortlisting resumes to hire employees
for jobs in a bike factory. Hiring the best employees, as well as paying
them enough and keeping them happy will increase the final score.  
  
Having a program to parse all resumes and eliminate those that 
are inadequate is very helpful in doing what would take a human
an unreasonable amount of time to accomplish.   
  
A huge thanks to the "english-words" repository at https://github.com/dwyl/english-words for providing
the basis file of over 460000 words in [dictionary.txt](dictionary.txt).  

This repo will be updated over the duration of the challenge.
## Code
```scraper.py``` parses through the resumes and appends all the information to a CSV file.  
```shortlister.py``` reads the generated CSV file, checking for the existence of references,
as well as spelling mistakes. Those with references and without spelling mistakes are added to a new CSV file.  
```reference_checker.py``` parses the references for the remaining candidates, making sure that key blacklisted words
are not present. At this stage, the remaining applicants are the best candidates, and are
appended to the final CSV file. 

Team No Chance: Jeremy Bao, Srivatsa Kundurthy, Moses Yang