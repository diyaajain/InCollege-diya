########################################################################
##                         InCollege                                  ##
########################################################################
##                                                                    ##
##  An application for connecting with your fellow college students.  ##
##      As a means to collaberate, learn skills, and find jobs.       ##
##                                                                    ##
########################################################################
########################################################################
## Contributers:    Homatas, Kayla                                    ##
##                  Humphries, Tyler                                  ##
##                  Jain, Diya                                        ##
##                  Joshi, Varennyam Rajkumar                         ##
##                  Kapoor, Vatsal                                    ##
########################################################################
########################################################################
from math import ceil, floor
import sqlite3



accounts = []  ## Lists of all accounts
jobs = []      ## Lists of all job postings
current_account = None ## The currently active account

MAX_ACC = 5  ## Maximum number of accounts supported
MAX_JOB = 5  ## Maximun number of Jobs that can be posted.


class Account:
    """ 
    A class to store the information of each account.

    Attributes
    ----------
    __username : str (private)
        The username of the account.
    __password : str (private)
        The password of the account.
    __firstname : str (private)
        The first name of the account user.
    __lastname : str (private)
        The last name of the account user.
    __jobs_posted : int (private)
        The number of jobs posted by the user.

    Methods
    -------
    create(self, usrn, pswd, first, last):
        Populates the account with the supplied account details.

    get_username():
        Returns the username of the account.

    get_password():
        Returns the password of the account.

    get_firstname():
        Returns the first name of the account user.

    get_lastname():
        Returns the last name of the account user.

    increment_jobs_posted():
        Increments the count of jobs posted by the user.
    """

    def __init__(self):
        """Constructs the account class."""

        self.__username = None
        self.__password = None
        self.__firstname = None
        self.__lastname = None
        self.__jobs_posted = 0
        self.__email_ad='1'
        self.__sms_ad='1'
        self.__target_ad='1'
        self.__language='English'
    
    def create(self, usrn, pswd, first, last, email, sms, target,language):
        """
        Populates the account with the supplied account details.

        Parameters
        ----------
        usrn : str
            Username of account.

        pswd : str
            Password of account.

        first : str
            First name of account user.

        last : str
            Last name of account user.
        """

        self.__username = usrn
        self.__password = pswd
        self.__firstname = first
        self.__lastname = last
        self.__email_ad = email
        self.__sms_ad = sms
        self.__target_ad = target
        self.__language= language

    def get_username(self):
        """
        Returns the username of the account.

        Returns
        -------
        __username : str
            The username of the account.
        """

        return self.__username

    def get_password(self):
        """
        Returns the password of the account.

        Returns
        -------
        __password : str
            The password of the account.
        """

        return self.__password

    def get_firstname(self):
        """
        Returns the first name of the account.

        Returns
        -------
        __firstname : str
            The first name of the account.
        """

        return self.__firstname

    def get_lastname(self):
        """
        Returns the last name of the account.

        Returns
        -------
        __lastname : str
            The last name of the account.
        """

        return self.__lastname

    def increment_jobs_posted(self):
        """Increments the count of jobs posted by the user."""
        self.__jobs_posted += 1


    def get_jobs_posted(self):
        """
        Gets the number of jobs the user has posted and returns it.

        Returns
        -------
        __jobs_posted : str
            THe number of jobs the user has posted.
        """
        return self.__jobs_posted
    def get_emailAd(self):
        return self.__email_ad
    def get_smsAd(self):
        return self.__sms_ad
    def get_targetAd(self):
        return self.__target_ad
    def get_language(self):
        return self.__language
    def preferences(self):
        print("\nYour advertising preferences are:\n")
        emailVal="Yes" if self.__email_ad=='1' else "No"
        smsVal="Yes" if self.__sms_ad=='1' else "No"
        targetVal="Yes" if self.__target_ad=='1' else "No"
        print("\nEmail ads: ",emailVal," SMS ads: ",smsVal," Target ads: ",targetVal)
    def update_ad(self,email=True,sms=True,target=True):
        conn = sqlite3.connect('accounts.db')
        cursor = conn.cursor()
        if email==False:
            self.__email_ad=False
        elif sms==False:
            self.__sms_ad=False
        elif target==False:
            self.__target_ad=False
        # SQL statement to update emailAd, smsAd, and targetAD columns based on username
        update_query = "UPDATE accounts SET emailAd = ?, smsAd = ?, targetAD = ? WHERE username = ?"

        # Execute the update query with the new values and username
        cursor.execute(update_query, (self.__email_ad, self.__sms_ad, self.__target_ad, self.__username))

        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()
    def show_language(self):
        print("\nYour current language preference is: ",self.__language,"\n")
    def update_language(self,english=True,spanish=False):
        conn = sqlite3.connect('accounts.db')
        cursor = conn.cursor()
        if spanish==True:
            self.__language='Spanish'
        elif english==True:
            self.__language='English'
        update_query="UPDATE accounts SET language = ? WHERE username = ?"
        cursor.execute(update_query,(self.__language,self.__username))
        conn.commit()
        conn.close()


class Job:
    """ 
    A class to store the information of each job posting.

    ...

	    Attributes
	    ----------
	    title : str 
            The job title.
        description : str 
            A description of the job.
        employer : str 
            The name of the employer.
        location : str 
            The location of the job.
        salary : str 
            The expected salary of the job.

        __firstname : str (private)
            The first name of the user who posed the job.
        __lastname : str (private)
            The last name of the user who posed the job.

	
	Methods
	------
	    create(usrn, pswd):
            Populates the job posting with the supplied information.

        get_firstname():
        	Returns the password of the account.

        get_lastname():
        	Returns the password of the account.
        
        set_poster():
            Gets the first and last name of the poster and sets it to this job.

	"""

    def __init__(self):
        """Constructs the account class."""

        self.title = None
        self.description = None
        self.employer = None
        self.location = None
        self.salary = None

        self.__firstname = None
        self.__lastname = None
    
    def create(self, title, desc, employ, locat, salary):
        """
        Populates the job posting with the supplied information.

        Parameters
        ----------
        title : str
            The job title.

        desc : str
            A description of the job.

        employ : str
            The name of the employer.

        locat : str
            The location of the job.

        salary : str
            The expected salary of the job.
        """

        self.title = title
        self.description = desc
        self.employer = employ
        self.location = locat
        self.salary = salary


    def get_firstname(self):
        """
        Returns the first name of the poster.

        Returns
        -------
        __firstname : str
            The first name of the poster.
        """

        return self.__firstname

    def get_lastname(self):
        """
        Returns the last name of the poster.

        Returns
        -------
        __lastname : str
            The last name of the poster.
        """

        return self.__lastname

    def set_poster(self, fname, lname):
        """ 
        Sets the first and last name of the poster who listed the job. 

        Parameters
        ----------
        fname : str
            The first name of the poster.

        lname : str
            the last name of the poster.
        """

        self.__firstname = fname
        self.__lastname = lname



def check_name(firstname, lastname):
    """
    Checks if the first and last name alread exists in the database.
    Parameters
    ----------
    firstname : str
        A string representing the first name we are searching for.
    
    lastename : str
        A string representing the last name we are searching for.

    Returns
    -------
    str
        returns the username of the account if the first and last name matches an existing account,
        or "EXIT" if it doesn't.
    """

    firstname = firstname.upper()
    lastname = lastname.upper()

    for acc in accounts: ## iterates through all current account
        if acc:          ## checks if account exists
            if (acc.get_firstname()).upper() == firstname and (acc.get_lastname()).upper() == lastname:   
                return acc.get_username()
    return "EXIT"     


def check_password(usrn, pswd):
    """
    Checks if the username alread exists in the database.
    and if the password matches the password of the existing account.

    Parameters
    ----------
    usrn : str
        A string representing the username of a account.
    
    pswd : str
        A string representing the password of a account.

    Returns
    -------
    bool
        returns True if the username and password matches an existing account,
        or False if it doesn't.
    """
    for acc in accounts: ## iterates through all current account
        if acc:          ## checks if account exists
            if acc.get_username() == usrn and acc.get_password() == pswd:   
                return True                                                
    return False



def check_username(usrn):
    """
    Checks if the username alread exists in the database.

    Parameters
    ----------
    usrn : str
        A string representing the username of a account.

    Returns
    -------
    bool
        returns True if the username already exist,
        or False if it doesn't.
    """
    for acc in accounts: ## iterates through all current accounts
        if acc:          ## checks if account exists
            if acc.get_username() == usrn:            
                return True                 
            
    return False



def check_valid_password(pswd):
    """ 
    Checks if the supplied password matches all the criteria for a valid password.

    Parameters
    ----------
    pswd : str
        A string representing the password of a account.

    Returns
    -------
    bool
        returns True if it isn't a valid password,
        or False if it is a valid password.
    """
    is_capital = False
    is_digit = False
    is_symbol = False

    if not (8 <= len(pswd) <= 12):
        print("")
        print("The password must be be 8-12 characters long!")
        return True

    if not pswd.isprintable():
        print("")
        print("The password contains an invalid character!")
        return True

    for char in pswd:  ## iterates through each character to see if the correct criteria are met.
        if char.isupper():
            is_capital = True
        elif char.isdigit():
            is_digit = True
        elif char.isascii() and not char.isalnum():
            is_symbol = True
    
    if is_capital and is_digit and is_symbol:
        print("")
        print("Password set!")
        return False
    
    print("")
    if not is_capital:
        print("Password is missing a capital letter!")
    if not is_digit:
        print("Password is missing atleast one number!")
    if not is_symbol:
        print("Password is missing a symbol!")
    return True



def create_account():
    """ 
    Menu loop for creating as new account,
    prompts the user to input a username and password.
    If vaild, a new account is created.

    Returns
    -------
    None
        returns back to main menu after completion or on return command.
    """

    if len(accounts) >= MAX_ACC:
        print("All permitted accounts have been created, please come back later.")
        return

  # rest of create account code

    is_incorrect = True
    while is_incorrect:
        print("")
        print("######################################")
        print("##       Please enter a username.   ##")
        print("##      Or Type 'Exit' to return.   ##")
        print("######################################")
        print("")
        username = input(":: " )
        is_incorrect = check_username(username)

        if username.upper() == "EXIT":
            return

        print("")
        if is_incorrect:
            print("Username invalid! Username already exists!")
        else:
            print(username, "is a valid username.")

    is_incorrect = True
    while is_incorrect:
        print("")
        print("######################################")
        print("##   Please enter a valid password. ##")
        print("## The password must be 8-12 chars, ##")
        print("##  Have 1 capital letter, 1 digit, ##")
        print("##        and one symbol.           ##")
        print("######################################")
        print("")
        password = input(":: " )
        is_incorrect = check_valid_password(password)

    print("")
    print("######################################")
    print("##   Please enter your first name.  ##")
    print("######################################")
    print("")
    first_name = input(":: " )

    print("")
    print("######################################")
    print("##   Please enter your last name.   ##")
    print("######################################")
    print("")
    last_name = input(":: " )

    accounts.append(Account())
    accounts[-1].create(username, password, first_name, last_name, email='1', sms='1', target='1', language='English')
    save_accounts()

    print("")
    print("Account successfully created!")



def create_job():
    """ 
    Menu loop for creating a new job posting,
    prompts the user to input a title, description, employer,
    location, and salary. If valid, a new job is posted.

    Returns
    -------
    None
        returns back to the user menu after completion or on return command.
    """

    if len(jobs) >= MAX_JOB:
        print("All permitted job postings have been created, please come back later.")
        return

    # Check if the user has posted more than five jobs
    if current_account and current_account.get_jobs_posted() >= 5:
        print("You have already posted the maximum allowed number of jobs (5).")
        return

    print("")
    print("######################################")
    print("##      Please enter a job title.   ##")
    print("##      Or type 'Exit' to return.   ##")
    print("######################################")
    print("")
    job_title = input(":: ")

    if job_title.upper() == "EXIT":
        return

    print("")
    print("######################################")
    print("## Please enter a short description ##")
    print("##       describing the job.        ##")
    print("######################################")
    print("")
    job_desc = input(":: ")

    print("")
    print("######################################")
    print("##     Please enter the name of     ##")
    print("##           the employer.          ##")
    print("######################################")
    print("")
    job_employer = input(":: ")

    print("")
    print("######################################")
    print("##     Please enter the location    ##")
    print("##           of the job.            ##")
    print("######################################")
    print("")
    job_location = input(":: ")

    print("")
    print("######################################")
    print("##     Please enter the expected    ##")
    print("##        salary of the job.        ##")
    print("######################################")
    print("")
    job_salary = input(":: ")

    jobs.append(Job())
    jobs[-1].create(job_title, job_desc, job_employer, job_location, job_salary)

    if current_account:
        first_name = current_account.get_firstname()
        last_name = current_account.get_lastname()
        jobs[-1].set_poster(first_name, last_name)
        # Increment the number of jobs posted by the current user
        current_account.increment_jobs_posted()
    else:
        print("")
        print("You must be logged in to post a job!")

    save_jobs()

    print("")
    print("Job successfully posted!")



def display_jobs():
    """
    Todo.

    Returns
    -------
    None
        returns back to jobs menu after completion.
    """
    print("Under construction!")




def find_person():
    """
    Asks the user for the first and last name of a person
    they know and searches accounts of InCollege for the username of 
    that person

    Returns
    -------
    None
        returns back to user menu after completion.
    """
    print("")
    print("######################################")
    print("##  Please enter the first name of  ##")
    print("##      of the person you know.     ##")
    print("######################################")   
    print("")

    first_name = input(":: ")

    print("")
    print("######################################")
    print("##   Please enter the last name of  ##")
    print("##      of the person you know.     ##")
    print("######################################")    
    print("")

    last_name = input(":: ")

    is_user = True
    username = check_name(first_name, last_name)
    if username == "EXIT":
        is_user = False

    if is_user:
        print("")
        print("#############################################")
        print(f"  The username of {first_name} {last_name} is: {username}")
        print("       Press 'enter' to continue.  ")
        print("#############################################")    
        print("")

    else:
        print("")
        print("####################################")
        print("## This person is not a member of ##")
        print("##            InCollege!          ##")
        print("##    Press 'enter' to continue.  ##")
        print("####################################")    
        print("")

    input(">> ")



def get_account(usrn):
    """
    Checks if the account exists based on the supplied username.

    Parameters
    ----------
    usrn : str
        A string representing the username of a account.

    Returns
    -------
    int
        returns account number if account exists,
        or -1 if it doesn't.
    """
    i = 0
    for i in range(len(accounts)): ## iterates through all accounts
        if accounts[i]:            ## checks if account exists
            if accounts[i].get_username() == usrn:          
                return i                              
    return -1



def get_empty_slot():
    """ 
    Checks if an empty slot is available in the acccount list.
    DEPR: Not compatible with current account system!
          Kept for reference.

    Returns
    -------
    int
        The account number of the first empty slot,
        or -1 if there are no empty slots.
    """

    if len(accounts) >= MAX_ACC:
            return -1
  
  # existing code to find empty slot

    try:
        return accounts.index(None)
    except ValueError:
        return -1



def initialize_database():
    """Initalizes the database, must be run at start-up."""
    connection = sqlite3.connect("accounts.db")  # Connect to a SQLite database (creates it if it doesn't exist)
    cursor = connection.cursor()

    # Create a table to store account information
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        username TEXT PRIMARY KEY,
        password TEXT,
        firstname TEXT,
        lastname TEXT,
        emailAd TEXT,
        smsAd TEXT,
        targetAD TEXT,
        language TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        title TEXT PRIMARY KEY,
        desc TEXT,
        employer TEXT,
        location TEXT,
        salary TEXT,
        firstname TEXT,
        lastname TEXT
    )
    """)

    connection.commit()
    connection.close()



def learn_skill():
    """ 
    Menu Loop for asking a user what skills they want to learn.

    Returns
    -------
    None
        returns back to user menu after completion or on return command.
    """
    while True:
        print("")
        print("######################################")
        print("##   Learn (S)oftware Engineering   ##")
        print("##        Learn (W)eb Design        ##")
        print("##        Learn (N)etworking        ##")
        print("##  Learn (I)nternet Communication  ##")
        print("##         Learn (A)lgorithms       ##")
        print("##      or (R)eturn to last page.   ##")                    
        print("######################################")
        print("")

        main_input = input(":: ")
        main_input = main_input[0].upper()

        print("")

        if main_input == "S":
            print("Under construction!")
            print("")

        elif main_input == "W":
            print("Under construction!")
            print("")

        elif main_input == "N":
            print("Under construction!")
            print("")
        
        elif main_input == "I":
            print("Under construction!")
            print("")

        elif main_input == "A":
            print("Under construction!")
            print("")

        elif main_input == "R":
            return

        else:
            print ("That is not a valid command!")



def load_accounts():
    """Loads all the currently existing accounts from the SQLite database on start-up."""
    connection = sqlite3.connect("accounts.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM accounts")

    rows = cursor.fetchall()

    for acc_data in rows:
        load_account_data(acc_data)
  
    connection.close()



def load_account_data(data):
    """ 
    For a single line of data in the account table,
    create a new account class and populate it with the data.

    Parameters
    ----------
    data : tuple
        A tuple containing (username, password, firstname, lastname) data.
    """
    if data:
        accounts.append(Account())  # Append a new Account instance
        accounts[-1].create(data[0], data[1], data[2], data[3],data[4],data[5],data[6],data[7])  # Provide the 'username', 'password', 'firstname', 'lastname' arguments



def load_jobs():
    """Loads all the currently existing job postings from the SQLite database on start-up."""
    connection = sqlite3.connect("accounts.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM jobs")

    rows = cursor.fetchall()

    for job_data in rows:
        load_job_data(job_data)
  
    connection.close()



def load_job_data(data):
    """ 
    For a single line of data in the jobs table,
    create a new job class and populate it with the data.

    Parameters
    ----------
    data : tuple
        A tuple containing (title, description, employer, location, salary) data.
    """
    if data:
        jobs.append(Job())  # Append a new Account instance
        jobs[-1].create(data[0], data[1], data[2], data[3], data[4])  # Provide the 'title', 'description', 'employer', 'location', 'salary' arguments
        jobs[-1].set_poster(data[5], data[6])   # Provide the 'firstname' and 'lastname' arguments


        
def login():
    """ 
    Menu loop for logging in,
    prompts the user to input a username and password.
    If vaild, the account logs in.

    Returns
    -------
    None
        returns back to main menu after completion or on return command.
    """

    global current_account

    is_correct = False
    while not is_correct:
        print("")
        print("######################################")
        print("##    Please enter your username.   ##")
        print("##     Or Type 'Exit' to return.    ##")        
        print("######################################")
        print("")
        username = input(":: " )

        
        if username.upper() == "EXIT":
            return
        
        print("")
        print("######################################")
        print("##    Please enter your password.   ##")
        print("######################################")
        print("")
        password = input(":: " )
        is_password = check_password(username, password)

        print("")
        if is_password:
            is_correct = True
            current_account = accounts[get_account(username)]
            print("You have successfully logged in.")
        else:
            print("Incorrect username / password, please try again.")
    return



def menu_message():
    """Displays a message on the main menu."""

    print("BREAKING NEWS: COLLEGE STUDENT USES INCOLLEGE TO GET A JOB!")
    print("John Smith, a student at the University of South Florida, ")
    print("recently landed a job at Twitter after using the InCollege ")
    print("platform. The student noted that the use of InCollege and ")
    print("its many features allowed them to search for a job and learn")
    print("new skills that helped them land the job!")

    print("\nIf you would you like to watch a video about why you should")
    print(" join InCollege, please enter (V). \n")       



def play_video():
    """Plays a video."""
    print("")
    print("####################################")
    print("##      Video is now playing.     ##")
    print("##   Press 'enter' to continue.   ##")
    print("####################################")
    print("")   

    input(">> ")
            
def save_accounts():
    """Saves all currently existing accounts to the SQLite database."""
    connection = sqlite3.connect("accounts.db")
    cursor = connection.cursor()

    # Clear the existing data in the 'accounts' table
    cursor.execute("DELETE FROM accounts")

    for acc in accounts:
        if acc:
            cursor.execute("INSERT INTO accounts (username, password, firstname, lastname,emailAd, smsAd, targetAd, language) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                                (acc.get_username(), acc.get_password(), acc.get_firstname(), acc.get_lastname(),acc.get_emailAd(),acc.get_smsAd(),acc.get_targetAd(), acc.get_language()))

    connection.commit()
    connection.close()



def save_jobs():
    """Saves all currently existing jobs to the SQLite database."""
    connection = sqlite3.connect("accounts.db")
    cursor = connection.cursor()

    # Clear the existing data in the 'jobs' table
    cursor.execute("DELETE FROM jobs")

    for job in jobs:
        if job:
            cursor.execute("INSERT INTO jobs (title, desc, employer, location, salary, firstname, lastname) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                                (job.title, job.description, job.employer, job.location, job.salary, job.get_firstname(), job.get_lastname()))

    connection.commit()
    connection.close()



def search_job():
    """
    Todo.

    Returns
    -------
    None
        returns back to user menu after completion.
    """
    while True:
        print("")
        print("####################################")
        print("#  Would you like to (P)ost a job  #")
        print("#   (L)ook at the job postings,    #")
        print("#  or (R)eturn to the last page?   #")
        print("####################################")    
        print("")
        
        main_input = input(":: ")
        main_input = main_input[0].upper()
        print("")

        if main_input == "P":
            create_job()

        elif main_input == "L":
            display_jobs()
            
        elif main_input == "R":
            return

        else:
            print ("That is not a valid command!")
            print("")  



def search_user():
    """
    Asks the user for the first and last name of 
        a person and checks if that person is an InCollege member

    Returns
    -------
    None
        returns back to main menu after completion or on return command.
    """

    print("")
    print("######################################")
    print("##  Please enter the first name of  ##")
    print("##      of the person you want      ##")
    print("##         to search for.           ##")
    print("######################################")    
    print("")

    first_name = input(":: ")

    print("")
    print("######################################")
    print("##  Please enter the last name of   ##")
    print("##      of the person you want      ##")
    print("##         to search for.           ##")
    print("######################################")    
    print("")

    last_name = input(":: ")

    is_user = True
    username = check_name(first_name, last_name)
    if username == "EXIT":
        is_user = False                                             
    
    if is_user:
        print("")
        print("######################################")
        print("##      They are a part of the      ##")
        print("##        InCollege system.         ##")
        print("##    Press 'enter' to continue.    ##")
        print("######################################")
        print("")

    else: # person isnt a member of InCollege
        print("")
        print("####################################")
        print("##    They are not yet a part     ##")
        print("##    of the InCollege system!    ##")
        print("##   Press 'enter' to continue.   ##")
        print("####################################")
        print("")

    input(">> ")



def useful_links():

    '''
    Provides the user with a list of useful links and travels to a link based on the user input.

    Parameters: None

    Returns: None
    '''

    while True: 

        print("")
        print("######################################")
        print("##          Useful Links:           ##")
        print("##         1. General               ##")
        print("##         2. Browse InCollege      ##")
        print("##         3. Business Solutions    ##")
        print("##         4. Directories           ##")
        print("##                                  ##")
        print("##        (E)xit to Main Menu       ##")
        print("######################################")
        print("")

        user_input = input(":: ")

        if user_input == "1":
            general()

        elif user_input == "2":
            browse_incollege()

        elif user_input == "3":
            business_solutions()

        elif user_input == "4":
            directories()

        elif user_input.upper() == "E":
            return
        
        else:
            print("That is not a valid command!")



def important_links():

    '''
    Provides the user with a list of important links and travels to one selected by the user.
    
    Parameters: None

    Returns: None
    '''

    while True:
        
        print("")
        print("######################################")
        print("##     InCollege Important Links    ##")
        print("##        1. Copyright Notice       ##")
        print("##        2. About                  ##")
        print("##        3. Accessibility          ##")
        print("##        4. User Agreement         ##")
        print("##        5. Privacy Policy         ##")
        print("##        6. Cookie Policy          ##")
        print("##        7. Copyright Policy       ##")
        print("##        8. Brand Policy           ##")
        print("##        9. Guest Controls         ##")
        print("##       10. Languages              ##")
        print("##                                  ##")
        print("##       (E)xit to Main Menu        ##")
        print("######################################")
        print("")

        user_input = input(":: ")

        if user_input == "1":
            copyright_notice()

        elif user_input == "2":
            about()

        elif user_input == "3":
            accessibility()

        elif user_input == "4":
            user_agreement()

        elif user_input == "5":
            privacy_policy()

        elif user_input == "6":
            cookie_policy()

        elif user_input == "7":
            copyright_policy()
        
        elif user_input == "8":
            brand_policy()

        elif user_input == "9":
            guest_controls()

        elif user_input == "10":
            languages()

        elif user_input.upper() == "E":
            return
        
        else:
            print("That is not a valid command!")



def general():

    '''
    Provides the user with a list of general links and travels to a link based on the user input.

    Parameters: None

    Returns: None
    '''

    while True:

        if current_account == None: # if user is not signed in, provide them with option to sign in
            print("")
            print("###################################")
            print("##           (S)ign Up           ##")
            print("##         (H)elp Center         ##")
            print("##            (A)bout            ##")
            print("##            (P)ress            ##")
            print("##            (B)log             ##")
            print("##           (C)areers           ##")
            print("##         (D)evelopers          ##")
            print("##                               ##")
            print("##    (R)eturn to Useful Links   ##")
            print("###################################")
            print("")
        
        else: # user is already signed in
            print("")
            print("###################################")
            print("##         (H)elp Center         ##")
            print("##            (A)bout            ##")
            print("##            (P)ress            ##")
            print("##            (B)log             ##")
            print("##           (C)areers           ##")
            print("##         (D)evelopers          ##")
            print("##                               ##")
            print("##    (R)eturn to Useful Links   ##")
            print("###################################")
            print("")

        user_input = input(":: ")
        user_input = user_input.upper()

        if user_input == "S" and current_account == None:
            create_account()
        
        elif user_input == "H":
            help_center()

        elif user_input == "A":
            about()

        elif user_input == "P":
            press()

        elif user_input == "B":
            blog()

        elif user_input == "C":
            careers()

        elif user_input == "D":
            developers()

        elif user_input == "R":
            return

        else:
            print("That is not a valid command!")



def help_center():
    
    '''
    Provides the user with a message for the help center.

    Parameters: None

    Returns: None
    '''

    while True:

        print("")
        print("###################################")
        print("##       We're here to help      ##")
        print("##                               ##")
        print("##           (R)eturn            ##")
        print("###################################")
        print("")

        user_input = input(":: ")

        if user_input.upper() == "R":
            return
        else:
            print("That is not a valid command!")



def about():

    '''
    Provides the user with a message about InCollege.

    Parameters: None

    Returns: None
    '''

    while True:

        print("")
        print("###################################")
        print("##       InCollege: Welcome      ##")
        print("##   to InCollege, the world's   ##")
        print("##    largest college student    ##")
        print("##  network with many users in   ##")
        print("##       many countries and      ##")
        print("##     territories worldwide     ##")
        print("##                               ##")
        print("##           (R)eturn            ##")
        print("###################################")
        print("")

        user_input = input(":: ")

        if user_input.upper() == "R":
            return
        else:
            print("That is not a valid command!")



def press():

    '''
    Provides the user with a message about the InCollege Pressroom.

    Parameters: None

    Returns: None
    '''

    while True:

        print("")
        print("###################################")
        print("##      InCollege Pressroom:     ##")
        print("##   Stay on top of the latest   ##")
        print("##   news, updates, and reports  ##")
        print("##                               ##")
        print("##           (R)eturn            ##")
        print("###################################")
        print("")

        user_input = input(":: ")

        if user_input.upper() == "R":
            return
        else:
            print("That is not a valid command!")



def blog():

    '''
    Under Construction

    Parameters: None

    Returns: None
    '''

    while True:

        print("")
        print("###################################")
        print("##       Under Construction      ##")
        print("##                               ##")
        print("##           (R)eturn            ##")
        print("###################################")
        print("")

        user_input = input(":: ")

        if user_input.upper() == "R":
            return
        else:
            print("That is not a valid command!")



def careers():

    '''
    Under Construction

    Parameters: None

    Returns: None
    '''

    while True:

        print("")
        print("###################################")
        print("##       Under Construction      ##")
        print("##                               ##")
        print("##           (R)eturn            ##")
        print("###################################")
        print("")

        user_input = input(":: ")

        if user_input.upper() == "R":
            return
        else:
            print("That is not a valid command!")



def developers():

    '''
    Under Construction

    Parameters: None

    Returns: None
    '''

    while True:

        print("")
        print("###################################")
        print("##       Under Construction      ##")
        print("##                               ##")
        print("##           (R)eturn            ##")
        print("###################################")
        print("")

        user_input = input(":: ")

        if user_input.upper() == "R":
            return
        else:
            print("That is not a valid command!")



def browse_incollege():

    '''
    Under Construction

    Parameters: None

    Returns: None
    '''

    while True:

        print("")
        print("###################################")
        print("##       Under Construction      ##")
        print("##                               ##")
        print("##           (R)eturn            ##")
        print("###################################")
        print("")

        user_input = input(":: ")

        if user_input.upper() == "R":
            return
        else:
            print("That is not a valid command!")



def business_solutions():

    '''
    Under Construction

    Parameters: None

    Returns: None
    '''

    while True:

        print("")
        print("###################################")
        print("##       Under Construction      ##")
        print("##                               ##")
        print("##           (R)eturn            ##")
        print("###################################")
        print("")

        user_input = input(":: ")

        if user_input.upper() == "R":
            return
        else:
            print("That is not a valid command!")



def directories():

    '''
    Under Construction

    Parameters: None

    Returns: None
    '''

    while True:

        print("")
        print("###################################")
        print("##       Under Construction      ##")
        print("##                               ##")
        print("##           (R)eturn            ##")
        print("###################################")
        print("")

        user_input = input(":: ")

        if user_input.upper() == "R":
            return
        else:
            print("That is not a valid command!")



'''
Important Link Functions:
'''

def copyright_notice():
    return """
##############################################
##             Copyright Notice               ##
##                                            ##
## All content provided on inCollege,         ##
## including but not limited to text,         ##
## graphics, logos, images, and software,     ##
## is the property of inCollege or its        ##
## content suppliers and is protected by      ##
## international copyright laws. The use,     ##
## reproduction, and distribution of such     ##
## content without permission is prohibited.  ##
##############################################
"""

def accessibility():
    return """
##############################################
##             Accessibility                  ##
##                                            ##
## inCollege is committed to providing an     ##
## accessible and inclusive platform for all  ##
## users. We strive to ensure that our        ##
## services are accessible to individuals     ##
## with disabilities. If you encounter any    ##
## accessibility issues, please contact our   ##
## support team to assist you.                 ##
##############################################
"""

def user_agreement():
    return """
##############################################
##           User Agreement                   ##
##                                            ##
## By using inCollege, you agree to comply    ##
## with our User Agreement. This agreement    ##
## outlines the terms and conditions for      ##
## using our platform, including user         ##
## conduct, privacy, and content guidelines.  ##
## Please read the User Agreement carefully   ##
## before using our services.                 ##
##############################################
"""

def privacy_policy():
    print("\n##############################################")
    print("## You entrust us with your information when ##")
    print("## you use our services. We make a lot of    ##")
    print("## effort to safeguard your information and  ##")
    print("## give you control since we realize that    ##")
    print("## this is a huge responsibility.             ##")
    print("##############################################\n")
    
    while True:
        if current_account == None:
            print("##############################################")
            print("##                  Main Menu                ##")
            print("##           (R)eturn to Previous Menu        ##")
            print("##############################################")
            inp = input()
            if inp == 'R':
                return
        else:
            print("##############################################")
            print("##                  Main Menu                ##")
            print("##           (R)eturn to Previous Menu        ##")
            print("##           (G)uest Controls                ##")
            print("##############################################")
            inp = input()
            if inp == 'R':
                return
            elif inp == 'G':
                guest_controls()

def cookie_policy():
    return """
##############################################
##           Cookie Policy                    ##
##                                            ##
## inCollege uses cookies to enhance user     ##
## experience and provide personalized        ##
## content and ads. By using our platform,    ##
## you consent to the use of cookies in      ##
## accordance with our Cookie Policy. To      ##
## learn more, please review our Cookie       ##
## Policy on our website.                     ##
##############################################
"""
    
def copyright_policy():
    return """
##############################################
##         Copyright Policy                   ##
##                                            ##
## inCollege respects the intellectual        ##
## property rights of others. If you believe  ##
## that your copyrighted work has been used   ##
## in a way that constitutes copyright       ##
## infringement, please contact us with       ##
## relevant details. We will investigate and  ##
## take appropriate action.                    ##
##############################################
"""

def brand_policy():
    return """
##############################################
##           Brand Policy                     ##
##                                            ##
## Our Brand Policy outlines the guidelines   ##
## for using inCollege's brand assets,        ##
## including logos and trademarks. To         ##
## maintain the integrity of our brand,      ##
## please adhere to our brand guidelines      ##
## when using inCollege's branding elements.  ##
## For specific details, refer to our Brand   ##
## Policy available on our website.           ##
##############################################
""" 

def guest_controls():
    if current_account == None:
        print("\n##############################################")
        print("##          Guest Controls: Information        ##")
        print("## Guest Controls helps our users turn off    ##")
        print("## advertising alerts. Kindly login to use    ##")
        print("## this feature.                              ##")
        print("##############################################\n")
        return
    
    while True:
        current_account.preferences()
        print("##############################################")
        print("##            Guest Controls Menu            ##")
        print("##    1. Turn off email advertising.          ##")
        print("##    2. Turn off SMS advertising.            ##")
        print("##    3. Turn off targeted advertising.      ##")
        print("##    (R)eturn to Previous Menu               ##")
        print("##############################################\n")
        
        inp = input()
        if inp.upper() == 'R':
            return
        elif inp == '1':
            current_account.update_ad(email=False)
        elif inp == '2':
            current_account.update_ad(sms=False)
        elif inp == '3':
            current_account.update_ad(target=False)
        else:
            print("Invalid input")

def languages():
    if current_account == None:
        print("\n##############################################")
        print("##         Language Preferences: Info         ##")
        print("## Kindly login to your account to set your   ##")
        print("## language preferences.                      ##")
        print("##############################################\n")
        return
    
    while True:
        current_account.show_language()
        print("##############################################")
        print("##           Language Preferences Menu        ##")
        print("##  1. English                               ##")
        print("##  2. Spanish                               ##")
        print("##  (R)eturn to Previous Menu                ##")
        print("##############################################\n")
        
        inp = input()
        if inp.upper() == 'R':
            return
        elif inp == '1':
            current_account.update_language(english=True)
        elif inp == '2':
            current_account.update_language(spanish=True)
        else:
            print("Invalid input")



def user_menu():

    global current_account

    """ 
    Menu Loop for user menu after login.

    Returns
    -------
    None
        returns back to main menu after completion or on return command.
    """
    is_logged_in = True
    while is_logged_in:
        name = current_account.get_username()
        buffer1 = " "*ceil((36 - len(name))/2)          ## Makes sure the username is centered.
        buffer2 = " "*floor(((36 - len(name))/2)-1)
        print("")
        print("##################################################")
        print("##", buffer1,   "Hello", name + "!", buffer2,  "##")
        print("##    Would you like to (S)earch for a job,     ##")
        print("## (F)ind someone you know, or (L)earn a skill. ##")
        print("##    You can also (R)eturn to the main menu.   ##")                
        print("##################################################")
        print("")

        print("")
        print("##################################################")
        print("##                  (U)seful Links              ##")
        print("##            (I)nCollege Important Links       ##")
        print("##################################################")
        print("")   

        main_input = input(":: ")
        main_input = main_input[0].upper()

        print("")

        if main_input == "S":
            search_job()

        elif main_input == "F":
            find_person()

        elif main_input == "L":
            learn_skill()
        
        elif main_input == "R":
            current_account = None  ## log out of current_account
            return
        
        elif main_input == "U":
            useful_links()

        elif main_input == "I":
            important_links()

        else:
            print ("That is not a valid command!") 



def main():
    """Menu Loop for main menu."""
    initialize_database()

    is_running = True
    load_accounts()
    load_jobs()

    while is_running:

        if current_account:
            user_menu()

        print("")
        print("######################################")
        print("## Hello, and welcome to InCollege! ##")
        print("##    Would you like to (L)ogin,    ##")
        print("##       (S)earch for a user,       ##")
        print("## (C)reate an account, or (E)xit?  ##")
        print("######################################")
        print("")

        print("")
        print("######################################")
        print("##           (U)seful Links         ##")
        print("##    (I)nCollege Important Links   ##")
        print("######################################")
        print("")


        menu_message()

        main_input = input(":: ")
        main_input = main_input[0].upper()

        if main_input == "L":
            login()

        elif main_input == "C":
            create_account()

        elif main_input == "S":
            search_user()

        elif main_input == "V":
            play_video()

        elif main_input == "U":
            useful_links()

        elif main_input == "I":
            important_links()

        elif main_input == "E":
            is_running = False

        else:
            print ("That is not a valid command!")



if __name__ == "__main__":
    main()
