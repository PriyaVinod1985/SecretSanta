# ![Icon](Assets/Images/SecretSanta_icon.png) SecretSanta   
![Icon](Assets/Images/About_icon.jpg) **About Secret Santa**
This is a user-friendly desktop application that lets you generate employee and child pairs while avoiding duplicates. 

![Icon](Assets/Images/Requirements_icon.png) **Requirements**

The application uses two input files: 

  a. Current year employee list given as a.csv file  
  b. Previous year employee and child list given as a.csv file 
  ** Please ensure that both the files are in .csv formats 

The application also uses two image files: 

  a. Label_img – An image used in the application heading.  
  b. Secret_santa icon – This is an application logo.  
  ** Please ensure that the image is in the same folder as the application 
  
![Icon](Assets/Images/Constraints_icon.png) **Features**

1. Randomized assignment - Each employee is randomly paired with another employee.
   
2. Self-assignments are avoided.

3. Last year's pairings are compared to avoid same assignments in the current year.

4. Appropriate error handling has been done so users are notified why the application has failed.

![Icon](Assets/Images/File_formats_icon.png) **File Formats**

**Input file** – Emp_Current[For current year employees] 

Employee_Name,Employee_EmailID  
Hamish Murray,hamish.murray@acme.com 

**Output file** – Emp_prev_yr[For previous year] 

Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID  
Hamish Murray,hamish.murray@acme.com,Benjamin Collins,benjamin.collins@acme.com 

**All entries need to be comma separated values with the header fields same as given above 

![Icon](Assets/Images/Installation_icon.png) **Installation** 

To run the application, follow steps below: 

1.Download the .exe file from github 

2.Before running the application, please ensure that the image files are in the same folder as the .exe 

3.Run the application by double-clicking on the exe.
   
4.If there is a **Windows Security Prompt**, click **“More info”** → **“Run anyway”**. 

![Icon](Assets/Images/Technology_icon.png) **Technologies Used** 

The application has been developed using Python3.13 with pip and auto-py-to-exe.  

The application files are available in the main branch of the github repository along with the testing files and images used. 

![Icon](Assets/Images/Screenshot.png) **Application Screenshots** 

1. Load the current year's employee list by clicking on "Load Participants CSV".

   ![Icon](Assets/Images/App_SS_1.png)

2. A message box with number of participants loaded appears as shown below upon successful loading.

   ![Icon](Assets/Images/App_SS_2.png)
  
3. If there is any error in loading, the equivalent error message is shown in the message box.

4. Load the last year santa-child pairings by clicking on "Load Last Year's Pairs". A success message appears upon successful loading.

   ![Icon](Assets/Images/App_SS_3.png) 
   
5. For generating new pairs, click on "Generate Pairs".

   ![Icon](Assets/Images/App_SS_4.png) 

6. For writing the pairs into a new .csv file, click on "Save Pairs to CSV". You will be prompted to choose the output folder and file name. A success message is displayed upon successful upload.

   ![Icon](Assets/Images/App_SS_5.png)

![Icon](Assets/Images/Acknowledgements_icon.png) **Acknowledgements**

Image attributes - https://www.freepik.com/ 
