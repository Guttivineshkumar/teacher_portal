# Teachers Portal
### Setting Up Django with Sqlite3 :
    - Create any one folder.
    - Open the terminal (Ctlr+R) press enter.
    - Go to the Created folder path in terminal.

### 1. Create Virtual Environment
    - Run the command to create virtual environment.

    -- python -m venv venv

### 2. Activate Virtual Environment
    - After creating the Virtual Environment need to activate it. 

    -- venv/scripts/activate

### 3. pull the code from GIT Hub
    - follow the steps to get the code fromgit hub repository.

   -- git init
   -- git remote add origin https://github.com/Guttivineshkumar/teacher_portal.git
   -- git pull origin main

### 4. Install Dependencies
    - After pull the code from the git hub repository need to run the belo command to install packages.

   -- pip install -r requirements.txt

### 5. Run the migrate command
    - After install the required packeges run the below command to migrate models.

    -- python manage.py migrate

### 6. Create superuser command
    - after complete the migrate command run the below command to create superuser for login teachers portal.

    -- python manage.py createsuperuser

    - when you run the above command in terminal it asking 
        Username: enter your username press enter
        Email address: enter your email address press enter
        password: make sure please enter your password carefully  # Note: while entering the password please note it. It is not displaying.
        Password(again): Please enter the same password again 

        Superuser created successfully.

### 7.Run the Server command
    - Run the server.

   -- python manage.py runserver

### 8. Go to web browser 
    - Enter the Url 

    -- http://127.0.0.1:8000/

### 9. teachers portal Application working process follow the steps:
    - After enter the above URL you will get Login page. 
    - Enter the valid username and password.
    - If username and password is valid you will redirect to the students listing page.
    - After entering to the the students listing page we can add new stundets by click Add button.
    - If we click the Add button will get the popup in that we have 3 Input fields are there Name, Subject, Marks.
# Note: we can give subject name from the given subjects list to the subject input field.
    subjects : 'telugu', 'english', 'hindi', 'maths', 'science', 'social'
    - Provide the required fields data and click Add new student will be created added in the list table and we get the message "New student added successfully".
    - We can edit/delete the students data by clicking the down arrow in Actions column.
    - If you click the Edit option we can able to edit the data and click save button to save.
    - the data will updated and we get message "student data updated successfully".
    - If you click the delete option the record will delete and get the message "Student deleted successfully".
    - If click the logout button it will logout and redirect to login page.

# Note:
    - While creating new studen if studen already exist with same name and same subject the marks will be updated if student not exist new student object will created.