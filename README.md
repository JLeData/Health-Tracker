# Health-Tracker

Version 1.0

## Description
Health Tracker is a Python-based application that allows users to log and monitor their weight data.

Current features include:
- Logging weight entries into a CSV file.
- Generating a visual line graph to see weight progress over time.

## Purpose
I developed this application as a personal project to practice Python programming and enhance my skills for career development. It also serves as a tool to motivate and track my own health and fitness journey, influenced by my family’s health experiences and my commitment to improving my overall well-being. Seeing progress and improvements over time inspires me to maintain a healthier lifestyle.

## Disclaimer
This health tracker is a personal project aimed at practicing programming and promoting a healthier lifestyle. You are welcome to use it, but please be aware of the following:

- **Not a Substitute for Professional Advice:** I am not a healthcare professional. This tool is intended for general informational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. For personalized health advice, please seek the guidance of a qualified healthcare provider.

- **Accuracy of Data:** The accuracy of any estimates provided by this tool depends entirely on the accuracy and completeness of the data entered by the user. Please ensure that all data inputs are correct and up-to-date to obtain accurate results.

- **Liability Disclaimer:** I am not liable for any outcomes or consequences resulting from the use of this tool, including but not limited to health-related issues, data inaccuracies, or any other incidents arising from its use.

# Installation
**Installation for Windows:** The following steps are tailored for setting up for Windows. While instructions should generally apply to other platforms, they are specifically tested and optimized for Windows.

**1) Download/Install Python**
- Go to [python.org](https://www.python.org/) in your web browser.
- Click download and choose the latest version for Windows. (Python version 3.12.4 as of creating this)

**2) Run the installer:**
- Once the download is complete, run the installer.
- **IMPORTANT NOTE:** Check the box that says "Add Python to PATH" in the installation window before installing. This will make it easier for Python to run from the command line.
- Select "Customize Installation" for better ease of use in future installations.
  
![image](https://github.com/user-attachments/assets/042390a8-37f5-489b-9b9f-01fa8704b2e8)

**3) Customize Installation:**
- On the Optional Features screen, make sure to check the following options:
  - pip (Package installer for Python)
  - tcl/tk and IDLE (GUI for Python)
  - Python test suite (For testing Python)
  - py launcher (For all users, recommended)
- Click "Next".

![image](https://github.com/user-attachments/assets/4e46d889-453c-4529-b953-02224fd6c1a5)

**4) Advanced Options:**
- Select the following options on the Advance Options screen:
  - "Install for all users"
  - "Associate files with Python (requires the 'py' launcher)
  - (optional) Create shortcuts for installed applications
  - "Precompile standard library"
- Click "Install".

![image](https://github.com/user-attachments/assets/1ba58e56-6933-485a-948a-677f0978ab6e)

**5) Complete Installation:**
- Once installation is complete, you can click "Close".

**6) Verify Python installation**
- Open command prompt by pressing "Windows + R" and type "cmd", then press enter to open the Command Prompt.
  
  ![image](https://github.com/user-attachments/assets/07553af0-2dbf-421c-906d-0728558d8876)

- Check Python version by typing the following command and pressing "Enter":
```
python --version
```
Output should display "Python (version number)"

- Check Pip version by typing the following command and pressing "Enter":
```
pip --version
```
Output should display "Pip (version number)"

**7) Install required Libraries:**
- Health Tracker requires some libraries to be installed to run and function properly.
    - **matplotlib**: for graph generation
    - **pandas**: for handling CVS files
- Within the Command Prompt, type the following commands to install these libraries:
  ```
  pip install matplotlib
  ```
  ```
  pip install pandas
  ```
  These commands will download the libraries and their dependencies.

# Using the Program
Follow these steps after succesfully downloading Python and libraries.
**1) Clone the Repository:**
- clone or fownload the Health Tracker repository from here.

**2) Navigating and changing the Directoryy**
- Open Command Prompt and navigate to where you downloaded the Health Tracker Repository.
- Copy the file location and paste it into Command Prompt preceded by "cd":
```
cd C:\Users\YourUsername\Projects\HealthTracker
```
Press Enter to change the directory.

**3) Verify Your Location:**
- Confirm you are in the correct folder by typing:
```
dir
```
The Health Tracker file should be listed if done correctly.

# Running the Program
- Type the following command to execute the program:
```
python health_tracker.py
```
Press Enter to run the application.

# Conclusion
Congratulations on setting up Health Tracker on your Windows system! As a data analyst exploring programming, this project is part of my journey to expand my skills and improve my health. Programming offers new perspectives and tools for tackling data challenges, which I find fascinating.

Health Tracker is a tool that's helping me stay on track with my fitness goals. I hope it proves useful for you too.

Your input is valuable! Whether you've got ideas to improve this tool, need assistance, or want to chat about data analysis and programming, let's connect. We can learn together and make this tool even better.

I appreciate you taking the time to check out my project. Best wishes for your health and learning journey!
  
