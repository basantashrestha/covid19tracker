# Corona Patient Tracker by basanta.shrestha@gmail.com
A Covid 19 patient tracker in Python using mockup data.  
### This is for simple manual Run. Please refer to other readme files for docker-compose and kubernetes. 
**Steps to Run:**     

1. After doing git clone https://gitlab.com/libresoftitsolutions/corona-patient-tracker.git  
2. cd corona-patient-tracker  
3. covidnepal.py and covidnepal.csv are available in current folder   


**A.For Simple Run (No need to go to sections B)**   
a. Now Run streamlit run covidnepal.py and access it at http://localhost:8501 or IP:8501    



**B.For Docker Run ( Do not run section A if you want to run on docker )**   
a. docker image build -t covidtracker .   
b. docker container run -p 8501:8501 -d --name covid1 covidtracker  OR simply run run.sh    
c. Access it at http://localhost:8501 or IP:8501    
