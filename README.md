# erp_auto_login
Auto Login in ERP, IIT Kharagpur

## Requirements :
* Linux System
* Python 2.7 or higher 
* Selenium Package :
  * Install selenium by using the following command in terminal.
    > pip install selenium

## Fill Details : 
Edit 'details.txt' file with your own details. 

* Replace **Roll Number** with your roll number (Ex: **13XX23848**)
* Replace **Password** with your password (Ex: **XXXXXXXX**)
* Replace **Question-1**, **Question-2**, **Question-3** with your questions (Ex: **Your Favourite Sport**)
* Replace **Answer-1**, **Answer-2**, **Answer-3** with the respective answers to the above questions (Ex: **XXXXXXX** or **837379**)
* Replace **Title** with the webpage title that appears after logging into ERP (Ex: **Welcome XXXXXXXXXXX to ERP, IIT Kharagpur**)


## Usage :
* This is just one time installation
* Edit **details.txt** file with your details.  
* Keep both the **erp_login.py** and **details.txt** in the same folder.
* You can login into ERP using 2 ways :
  * Without Executable Script
  * With Executable Script

### Without Executable Script :
* Simply, open the terminal.
* Go to the directory in which **erp_login.py** and **details.txt** are stored.
* Run the **erp_login.py** just like you run any normal python script. 

### With Executable Script :
* Open the terminal. 
* Go to the directory in which **erp_login.py** and **details.txt** are stored.
* Run the following command for making erp_login.py an executable file.
  > chmod +x erp_login.py
* Now you can run this executable file by two ways.
  * Through Terminal
  * Through Double-Clicking

#### Through Terminal :
* Open the terminal. 
* Go to the directory in which **erp_login.py** and **details.txt** are stored.
* Run the following command for making erp_login.py an executable file.
  > ./erp_login.py

#### Through Double-Clicking :
* Open the folder in which **erp_login.py** and **details.txt** are located.
* Go to Edit->Preferences->Behaviour.
* Click **Ask Everytime** in What to do for executable files section and close it. 
* Now double click the **erp_login.py** and click **Run**. 

