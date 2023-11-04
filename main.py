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
import string

import database

_testing_ = True

accounts = []  ## Lists of all accounts
jobs = []      ## Lists of all job postings
friends = []   ## List of all friends
friend_requests = []   ## List of all friend requests
current_account = None ## The currently active account

MAX_ACC = 10  ## Maximum number of accounts supported
MAX_JOB = 10  ## Maximun number of Jobs that can be posted.

job_id = 0

db = database.Database(database.default_db)



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

    self.friends = []
    self.friend_requests = []

    """
    


    def __init__(self):
        """Constructs the account class."""

        self.__username = None
        self.__password = None
        self.__firstname = None
        self.__lastname = None
        self.__email_ad = 1
        self.__sms_ad = 1
        self.__target_ad = 1
        self.__language = 'English'
        self.friends = ""
        self.friend_requests = ""
        self.active_requests = ""

        self.has_profile = 0

        self.__title = ""
        self.__major = ""
        self.__uni = ""
        self.__info = ""
        self.__exp = ""
        self.__edu = ""

        self.postings = ""
        self.applied = ""
        self.saved = ""


    
    def create(self, usrn, pswd, first, last):
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

    def save_initial_data(self):
        """ Saves the default information of the account"""
        if not _testing_:
            db.update("accounts", self.__username, ["password", "firstname", "lastname", "emailAd", "smsAd", "targetAd", "language"], 
                  [self.__password, self.__firstname, self.__lastname, self.__email_ad, self.__sms_ad, self.__target_ad, self.__language])
    
    def save_profile(self):
        """ Saves the profile information of the account"""

        if not _testing_:
            db.update("accounts", self.__username, ["has_profile", "title", "major", "university", "info", "experience", "education"], 
                  [self.has_profile, self.__title, self.__major, self.__uni, self.__info, self.__exp, self.__edu])
        
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

    def get_title(self):
        """
        Returns the title of the user.

        Returns
        -------
        __title : str
            The title of the user.
        """

        return self.__title

    def get_major(self):
        """
        Returns the major of the user.

        Returns
        -------
        __major : str
            The major of the user.
        """

        return self.__major

    def get_uni(self):
        """
        Returns the university of the user.

        Returns
        -------
        __uni : str
            The university of the user.
        """

        return self.__uni

    def get_info(self):
        """
        Returns the infomation about the user.

        Returns
        -------
        __info : str
            The infomation about the user.
        """

        return self.__info

    def get_exp(self):
        """
        Returns the experience of the user.

        Returns
        -------
        __exp : str
            The experience of the user.
        """

        return self.__exp

    def get_edu(self):
        """
        Returns the education of the user.

        Returns
        -------
        __edu : str
            The education of the user.
        """

        return self.__edu

    def get_saved(self):
        return self.saved
    
    def get_applied(self):
        return self.applied
    
    def get_posted(self):
        return self.postings


    def set_title(self, title):
        """
        Sets the title of the user.

        Parameters
        -------
        title : str
            The title of the user.
        """

        self.__title = title

    def set_major(self, major):
        """
        Sets the major of the user.

        Parameters
        -------
        major : str
            The major of the user.
        """

        self.__major = major

    def set_uni(self, uni):
        """
        Sets the university of the user.

        Parameters
        -------
        uni : str
            The university of the user.
        """

        self.__uni = uni

    def set_info(self, info):
        """
        Sets the infomation about the user.

        Parameters
        -------
        info : str
            The infomation about the user.
        """

        self.__info = info

    def set_exp(self, exp):
        """
        Sets the experience of the user.

        Parameters
        -------
        exp : str
            The experience of the user.
        """

        self.__exp = exp

    def set_edu(self, edu):
        """
        Sets the education of the user.

        Parameters
        -------
        edu : str
            The education of the user.
        """

        self.__edu = edu



    def get_emailAd(self):
        return self.__email_ad
    def get_smsAd(self):
        return self.__sms_ad
    def get_targetAd(self):
        return self.__target_ad
    def get_language(self):
        return self.__language
    def get_friend_requests(self):
        return self.friend_requests
    def get_friends(self):
        return self.friends
    
    def set_emailAd(self, emailAd):
        self.__email_ad = emailAd
    def set_smsAd(self, smsAd):
        self.__sms_ad = smsAd
    def set_targetAd(self, targetAd):
        self.__target_ad = targetAd
    def set_friend_requests(self, freq):
        self.friend_requests = freq
    def set_friends(self, friends):
        self.friends = friends




    def preferences(self):
        print("\nYour advertising preferences are:\n")
        emailVal="Yes" if self.__email_ad==1 else "No"
        smsVal="Yes" if self.__sms_ad==1 else "No"
        targetVal="Yes" if self.__target_ad==1 else "No"
        print("\nEmail ads: ",emailVal," SMS ads: ",smsVal," Target ads: ",targetVal)


    def update_ad(self,email=True,sms=True,target=True):

        if email==False:
            self.__email_ad=0
        elif sms==False:
            self.__sms_ad=0
        elif target==False:
            self.__target_ad=0

        # update emailAd, smsAd, and targetAD columns based on username
        if not _testing_:
            db.update("accounts", self.__username, ["emailAd", "smsAd", "targetAd"], [self.__email_ad, self.__sms_ad, self.__target_ad])

        
    def show_language(self):
        print("\nYour current language preference is: ",self.__language,"\n")

    def set_language(self,lang):

        if lang in ["English", "Spanish"]:
            self.__language = lang

        else:
            print("Not a valid Language!")

        if not _testing_:
            db.update("accounts", self.__username, "language", self.__language)

    def send_friend_request(self, other_user):
        accounts[get_account(other_user)].receive_friend_request(self.__username)


    def receive_friend_request(self, friend_request):
        if not self.friend_requests:
            self.friend_requests=friend_request
        else:
            self.friend_requests=self.friend_requests+','+friend_request

        # Update the friend_requests column with the updated data
        if not _testing_:
            db.update("accounts", self.__username, "friend_requests", self.friend_requests)

    def accept_friend_request(self, friend_request):
        new_friend = accounts[get_account(friend_request)]
        new_friend_username = new_friend.get_username()

        # Append new friend to the current user's friends string
        if not self.friends:
            self.friends = new_friend_username
        else:
            self.friends += ',' + new_friend_username

        # Append current user to the new friend's friends string
        if not new_friend.friends:
            new_friend.friends = self.__username
        else:
            new_friend.friends += ',' + self.__username

        # Remove friend request from pending friend requests
        reqs = self.friend_requests.split(',')
        reqs.pop(0)
        self.friend_requests = ','.join(reqs)

        if not _testing_:
            new_friend = accounts[get_account(friend_request)]
            new_friend_username = new_friend.get_username()

            # Update the friend_requests and friends column with the updated data
            db.update("accounts", self.__username, ["friend_requests", "friends"] , [self.friend_requests, self.friends])

            # Update friends for new friend
            db.update("accounts", new_friend.get_username(), ["friends", "active_requests"], [new_friend.friends, new_friend.active_requests])


    def reject_friend_request(self, friend_request):

        non_friend = accounts[get_account(friend_request)]
        non_friend_username = non_friend.get_username()

        act = non_friend.active_requests.split(",")
        
        if self.__username in act:
            act.remove(self.__username)
        non_friend.active_requests = ','.join(act)

        reqs=self.friend_requests.split(',')
        reqs.pop(0)
        self.friend_requests=','.join(reqs)

        if not _testing_:
            non_friend = accounts[get_account(friend_request)]
            non_friend_username = non_friend.get_username()
            
            # Update the friend_requests column with the updated data
            db.update("accounts", self.__username, "friend_requests", self.friend_requests)

            # Update the friend_requests column with the updated data
            db.update("accounts", non_friend_username, "active_requests", non_friend.active_requests)
            
    

    def remove_friend(self, friend):
        new_friends=(self.friends.split(','))
        new_friends.remove(friend)
        self.friends=','.join(new_friends)
        old_friend = accounts[get_account(friend)]
        old_friend_friendList=old_friend.friends.split(',')
        old_friend_friendList.remove(self.__username)
        old_friend.friends=','.join(old_friend_friendList)

        if not _testing_:
            # Update friends for current user
            db.update("accounts", self.__username, "friends", self.friends)

            # Update friends for new friend
            db.update("accounts", old_friend.get_username(), "friends", old_friend.friends)


    def show_friend_requests(self):
        if not self.friend_requests:
            return []
        pending_requests = self.friend_requests.split(',')
        if '' in pending_requests:
            pending_requests.remove("")
        return pending_requests

    def save_active_requests(self):
        if not _testing_:
            db.update("accounts", self.__username, "active_requests", self.active_requests)

    def add_posting(self, id):
        if self.postings == "":
            self.postings = str(id)
        else:
            self.postings = self.postings + "," + str(id)

        if not _testing_:
            db.update("accounts", self.__username, "postings", self.postings)

    def save_post(self, post):
        if self.saved == "":
            self.saved = str(post.id)
        else:
            self.saved = self.saved + "," + str(post.id)

        if not _testing_:
            db.update("accounts", self.__username, "saved", self.saved)

    def unsave_post(self, id):

        saved = []
        if self.saved:
            saved = self.saved.split(",")
        
        if str(id) in saved:
            saved.remove(str(id))
            self.saved = ",".join(saved)

        if not _testing_:
            db.update("accounts", self.__username, "saved", self.saved)

    def apply_for_job(self, job, grad_date, start_date, info):

        if str(job.id) in self.postings.split(","):
            print("You cannot apply for your own job posting!")
        
        if self.applied == "":
            self.applied = job.title
        else:
            self.applied = self.applied + "," + job.title

        self.unsave_post(job.id)

        job.add_application(current_account.get_username(), grad_date, start_date, info)

        print("\nApplication submitted successfully!\n")

        if not _testing_:
            db.update("accounts", self.__username, "applied", self.applied)

    def unapply_for_job(self, title):
        """ Removes the job from the user's list of applied jobs """
        applied = []
        if self.applied:
            applied = self.applied.split(",")
        
        if str(title) in applied:
            applied.remove(str(title))
            self.applied = ",".join(applied)

        if not _testing_:
            db.update("accounts", self.__username, "applied", self.applied)






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

        self.id = -1
        self.title = None
        self.description = None
        self.employer = None
        self.location = None
        self.salary = None

        self.__firstname = None
        self.__lastname = None

        self.applications = ""
    
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

    def save(self):
        if not _testing_:
            db.update("jobs", self.id, ["title", "desc", "employer", "location", "salary", "firstname", "lastname"], 
                  [self.title, self.description, self.employer, self.location, self.salary, self.__firstname, self.__lastname])




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

    def add_application(self,username, grad_date, start_date, info):

        if self.applications == "":
            self.applications = username+"::"+grad_date+"::"+start_date+"::"+info
        else:
            self.applications = self.applications + "," + username+"::"+grad_date+"::"+start_date+"::"+info

        if not _testing_:
            db.update("jobs", self.id, "applications", self.applications)



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

def create_account_base():
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
        username = input(":: ")
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

    create_account(username, password, first_name, last_name)
    if not _testing_:
        db.create("accounts", username)
    accounts[-1].save_initial_data()

def incr_jobs():
    global job_id
    job_id += 1

def set_num_jobs(num):
    global job_id
    job_id = num

def create_account(username, password, first_name, last_name):

    if len(accounts) >= MAX_ACC:
        print("All permitted accounts have been created, please come back later.")
        return

    accounts.append(Account())
    accounts[-1].create(username, password, first_name, last_name)
    print("")
    print("Account successfully created!")

def create_job_base():
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

    if current_account:
        create_job(job_id, job_title, job_desc, job_employer, job_location, job_salary)
        incr_jobs()
    else:
        print("")
        print("You must be logged in to post a job!")

    
def create_job(id, title, desc, employ, loct, salary):

    if len(jobs) >= MAX_JOB:
        print("All permitted job postings have been created, please come back later.")
        return

    jobs.append(Job())
    jobs[-1].create(title, desc, employ, loct, salary)
    jobs[-1].id = id
    first_name = current_account.get_firstname()
    last_name = current_account.get_lastname()
    jobs[-1].set_poster(first_name, last_name)

    current_account.add_posting(id)

    print("")
    print("Job successfully posted!")

    if not _testing_:
        db.create("jobs", id)

    jobs[-1].save()


    

def create_profile():
    """
    Allows a user to create their user profile.

    Returns
    -------
    None
        returns back to user menu after completion.
    """
    print("")
    if not current_account.get_title():
        print("######################################")
        print("##     Please enter your title      ##")
        print("##  type 'Skip' to go to next part  ##")
        print("##     or type 'Exit' to leave.     ##")
        print("######################################") 
    else:
        print("######################################")
        print("##      Would you like to edit      ##")
        print("##           your title?            ##")
        print("##  type 'Skip' to go to next part  ##")
        print("##     or type 'Exit' to leave.     ##")
        print("######################################") 
    
    print("")
    user_title = input(":: ")

    if user_title.upper() == "EXIT":
        return

    elif not user_title.upper() == "SKIP":
        current_account.set_title(user_title)

    current_account.has_profile = 1

    print("")
    if not current_account.get_major():
        print("######################################")
        print("##     Please enter your major      ##")
        print("##  type 'Skip' to go to next part  ##")
        print("##     or type 'Exit' to leave.     ##")
        print("######################################")
    else:
        print("######################################")
        print("##      Would you like to edit      ##")
        print("##           your major?            ##")
        print("##  type 'Skip' to go to next part  ##")
        print("##     or type 'Exit' to leave.     ##")
        print("######################################")

    print("")
    user_major = input(":: ")

    if user_major.upper() == "EXIT":
        return

    elif not user_major.upper() == "SKIP":
        current_account.set_major(string.capwords(user_major))

    print("")
    if not current_account.get_uni():
        print("######################################")
        print("##   Please enter your university   ##")
        print("##  type 'Skip' to go to next part  ##")
        print("##     or type 'Exit' to leave.     ##")
        print("######################################")
    else:
        print("######################################")
        print("##      Would you like to change    ##")
        print("##         your university?         ##")
        print("##  type 'Skip' to go to next part  ##")
        print("##     or type 'Exit' to leave.     ##")
        print("######################################")

    print("")
    user_uni = input(":: ")

    if user_uni.upper() == "EXIT":
        return

    elif not user_uni.upper() == "SKIP":
        current_account.set_uni(string.capwords(user_uni))

    print("")
    if not current_account.get_info():
        print("######################################")
        print("##  Write some info about yourself  ##")
        print("##  type 'Skip' to go to next part  ##")
        print("##     or type 'Exit' to leave.     ##")
        print("######################################")
    else:
        print("######################################")
        print("##      Would you like to change    ##")
        print("##            your info?            ##")
        print("##  type 'Skip' to go to next part  ##")
        print("##     or type 'Exit' to leave.     ##")
        print("######################################")

    print("")
    user_info = input(":: ")

    if user_info.upper() == "EXIT":
        return

    elif not user_info.upper() == "SKIP":
        current_account.set_info(user_info)

    print("")
    print("######################################")
    print("##    Would you like to add some    ##")
    print("##        job experience?           ##")
    print("## type 'Remove' to delete previous ##")
    print("##              entry               ##")
    print("##     or type 'Exit' to leave.     ##")
    print("######################################") 

    exp = current_account.get_exp()
    topics = ["Add job? (Y/N) ", "Job Title: ", "Employer: ", "Date-started: ", "Date-ended: ", "Location: ", "Description: "]
    is_add = True

    while is_add:

        for topic in topics:
            print("")
            user_exp = input(":: "+topic)

            if topic == "Add job? (Y/N) " and user_exp.upper() == "N":
                is_add = False
                break

            elif topic == "Add job? (Y/N) " and user_exp.upper() == "REMOVE" and not exp:
                print("No previous line to remove!")

            elif topic == "Add job? (Y/N) " and user_exp.upper() == "REMOVE":
                remove_line(exp)

            elif user_exp.upper() == "EXIT":
                current_account.set_exp(exp)
                return

            elif topic == "Add job? (Y/N) " and user_exp.upper() == "Y":
                continue

            #elif topic == "Add job? (Y/N) ":
            #    "Not a correct input!"

            elif user_exp.upper() == "REMOVE":
                print("You must finish editing a job before removing it!")

            elif not topic == "Add job? (Y/N) " and user_exp.upper() != "SKIP":
                exp = exp+topic+user_exp+" "

        exp = exp+"\n "

    current_account.set_exp(exp)

    print("")
    print("######################################")
    print("##    Would you like to add your    ##")
    print("##       amount of education?       ##")
    print("## type 'Remove' to delete previous ##")
    print("##              entry               ##")
    print("##     or type 'Exit' to leave.     ##")
    print("######################################") 

    edu = current_account.get_edu()
    topics = ["Add Edu? (Y/N) ", "School Name: ", "Degree: ", "Years-Attended: "]
    is_add = True

    while is_add:

        for topic in topics:
            print("")
            user_edu = input(":: "+topic)

            if topic == "Add Edu? (Y/N) " and user_edu.upper() == "N":
                is_add = False
                break

            elif topic == "Add Edu? (Y/N) " and user_edu.upper() == "REMOVE" and not edu:
                print("No previous line to remove!")

            elif topic == "Add Edu? (Y/N) " and user_edu.upper() == "REMOVE":
                remove_line(edu)

            elif user_edu.upper() == "EXIT":
                current_account.set_edu(edu)
                return

            elif topic == "Add Edu? (Y/N) " and user_edu.upper() == "Y":
                continue

            #elif topic == "Add Edu? (Y/N) ":
            #    print("Not a correct input!")

            elif user_edu.upper() == "REMOVE":
                print("You must finish editing a job before removing it!")

            elif not topic == "Add Edu? (Y/N) " and user_edu.upper() != "SKIP":
                edu = edu+topic+user_edu+" "

        edu = edu+"\n "
    
    current_account.set_edu(edu)

    current_account.save_profile()


def delete_job(job):

    ## delete the job from the job list
    jobs.remove(job)

    ## remove posting from account
    postings = current_account.postings.split(",")

    if str(job.id) in postings:
        postings.remove(str(job.id))
    
    current_account.postings = ",".join(postings)

    print("\nJob deleted successfully!\n")
    
    if not _testing_:
        ## update the database
        db.update("accounts", current_account.get_username(), "postings", current_account.postings)


def remove_line(text):
    """
    Removes a line of text from a given paragraph.

    Parameters
    -------
    text : str
        The paragraph to modify.

    Returns
    -------
    result : str
        The original paragraph with one less line of text.
    """
    lines = text.split("\n")
    lines = lines[0:-2]
    result = ""
    for line in lines:
        result += line
        result += "\n"
    return result


def show_post(post):
    """
    Todo.

    Returns
    -------
    None
        returns back to jobs menu after completion.
    """

    applied = []
    if current_account.applied:
        applied = current_account.applied.split(",")

    saved = []
    if current_account.saved:
        saved = current_account.saved.split(",")


    is_users_post = False
    if post.get_firstname() == current_account.get_firstname() and post.get_lastname() == current_account.get_lastname():
        is_users_post = True

    display_post(post)
    
    if is_users_post:
        while True:
            main_input = input("\nWould you like to (D)elete this post, or (R)eturn?\n\n:: ")
            main_input = main_input[0].upper()
            if main_input == "D":
                ## delete the job from the database
                if not _testing_:
                    db.delete("jobs", post.id)
                delete_job(post)
                return True
            elif main_input == "R":
                return
            else:
                print("\nThat is not a valid input!\n")
    else:
        while True:
            if post.title in applied:
                input("\nPress enter to return...\n ")
                return

            elif str(post.id) in saved:
                main_input = input("\nWould you like to (A)pply for this job, (U)nsave this job, or (R)eturn?\n\n:: ")
                main_input = main_input[0].upper()
                if main_input == "A":
                    add_application(post)
                    return
                elif main_input == "U":
                    current_account.unsave_post(post.id)
                    return
                elif main_input == "R":
                    return
                else:
                    print("\nThat is not a valid input!\n")
            else:
                main_input = input("\nWould you like to (A)pply for this job, (S)ave this job for later, or (R)eturn?\n\n:: ")
                main_input = main_input[0].upper()
                if main_input == "A":
                    add_application(post)
                    return
                elif main_input == "S":
                    current_account.save_post(post)
                    return
                elif main_input == "R":
                    return
                else:
                    print("\nThat is not a valid input!\n")

def add_application(post):
    grad_date = input("\nWhat date are you graduating (mm/dd/yy)?\n\n:: ")
    start_date = input("\nWhat date can you start(mm/dd/yy)?\n\n:: ")
    info = input("\nWhy do you think you will be a good fit for this job?\n\n:: ")
    current_account.apply_for_job(post, grad_date, start_date, info)

def display_post(post):
    print("")
    print("##################################################")
    print("##")
    print("##  Title:", post.title)
    print("##")
    print("##  Description:", post.description)
    print("##")
    print("##  Employer:", post.employer)
    print("##  Location:", post.location)
    print("##  Salary:", post.salary)
    print("##")     
    print("##################################################")
    print("")


def display_jobs(posts, is_owned=False):
    """
    Displays all the jobs that the user requested.

    Returns
    -------
    None
        returns back to jobs menu after completion.
    """
    if posts:

        while True:

            print("")
            if is_owned:
                print("These are the jobs that you own: ")
            else:
                print("These are the jobs that are available: ")
            print("")

            display_job_list(posts)

            print("")
            user_input = input("Enter the number of the job you want to view or enter '0' to return.\n\n:: ")
            print("")

            try:
                user_input=int(user_input)-1
            except ValueError:
                print("not a valid input!")
                print("")
                continue

            if not (-1 <= user_input < len(posts)):
                print("not a valid input!")
                print("")
                continue

            if user_input == -1:
                return
        
            else:
                was_deleted = show_post(posts[user_input])
                if was_deleted:
                    return


    else:
        print("There are no jobs/internships available!")

        print("")
        user_input = input("Press enter to continue...")
        print("")

    
def display_job_list(posts):
    postings = []
    saved = []
    applied = []

    if current_account.postings:
        postings = current_account.postings.split(",")
    if current_account.saved:
        saved = current_account.saved.split(",")
    if current_account.applied:
        applied = current_account.applied.split(",")


    i = 0
    for post in posts:
        if str(post.id) in postings:
            label = " (OWNED)"
        elif post.title in applied:
            label = " (APPLIED)"
        elif str(post.id) in saved:
            label = " (SAVED)"
        else:
            label = ""
        print(str(i+1)+". "+post.title+label)
        i+=1

def display_jobs_menu():
    """
    Todo.

    Returns
    -------
    None
        returns back to jobs menu after completion.
    """
    print("")
    print("######################################")
    print("## This is where you can view jobs. ##")
    print("##    You can view (A)ll postings,  ##")
    print("##         (S)aved postings,        ##")
    print("##  (P)ostings already applied for, ##")
    print("##   or postings (N)ot applied for. ##")
    print("##      You can also (R)eturn.      ##")
    print("######################################")
    print("")

    user_input = None

    while user_input not in ["A", "S", "P", "N", "R"]:

        if user_input:
            print("Not a valid input!")

        user_input = input(":: ")

        if user_input:
            user_input = user_input[0].upper()

        print("")

    

    

    if user_input == "R":
        return

    elif user_input == "A":
        posting = get_all_postings()

    elif user_input == "S":
        posting = get_saved_postings()

    elif user_input == "P":
        posting = get_applied_postings()

    elif user_input == "N":
        posting = get_applied_postings(switch=True)
        
    display_jobs(posting)


def get_all_postings():
    return jobs

def get_saved_postings():

    saved = []

    if current_account.saved:
        saved = current_account.saved.split(",")
        saved = [int(x) for x in saved]

    postings = []

    for job in jobs:
        if job.id in saved:
            postings.append(job)

    return postings

def get_applied_postings(switch = False):

    applied = []

    if current_account.applied:
        applied = current_account.applied.split(",")

    postings = []

    for job in jobs:
        if job.title in applied and not switch:
            postings.append(job)
        elif job.title not in applied and switch:
            postings.append(job)

    return postings

def get_posted_postings():

    posts = []

    if current_account.postings:
        posts = current_account.postings.split(",")
        posts = [int(x) for x in posts]

    postings = []

    for job in jobs:
        if job.id in posts:
            postings.append(job)

    return postings



def find_person_base():
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

    username = find_person(first_name, last_name)

    if username != "EXIT":
        print("   Press S to send request and R to return  ")
        inp=input(":: ")
        
        if inp:
            inp = inp[0].upper()

        while inp!='R' and inp!='S':
            print("Incorrect input.")
            inp=input(":: ")
        
        if inp=='R':
        
            return
        
        elif inp=='S':
            send_request(username)
            return
    
    input("\nPress enter to continue... ")


def find_person(first_name, last_name):

    is_user = True
    username = check_name(first_name, last_name)
    if username == "EXIT":
        is_user = False

    if is_user:
        print("")
        print("#############################################")
        print(f"  The username of {first_name} {last_name} is: {username}")
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

    return username


def send_request(username):
    current_account.send_friend_request(username)
    print("Sent friend request to ", username,"!\n")
    current_account.active_requests += username+","
    current_account.save_active_requests()

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
    rows = db.fetch_all("accounts")

    for acc_data in rows:
        load_account_data(acc_data)
  

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
        accounts[-1].create(data[0], # username
                            data[1], # password
                            data[2], # firstname
                            data[3]) # lastname
        accounts[-1].set_emailAd(int(data[4])), # emailAD
        accounts[-1].set_smsAd(int(data[5])), # smsAD
        accounts[-1].set_targetAd(int(data[6])), # targetAD
        accounts[-1].set_language(data[7]), # language
        accounts[-1].set_friend_requests(data[8]), # friend_requests
        accounts[-1].active_requests = data[9]   # active_requests
        accounts[-1].set_friends(data[10]) # friends
        accounts[-1].has_profile = int(data[11])   # has_profile
        accounts[-1].set_title(data[12]) # title
        accounts[-1].set_major(data[13]) # major
        accounts[-1].set_uni(data[14])   # university
        accounts[-1].set_info(data[15])  # info
        accounts[-1].set_exp(data[16])   # experience
        accounts[-1].set_edu(data[17])   # education
        accounts[-1].postings = data[18]   # job postings
        accounts[-1].applied = data[19]   # postings applied
        accounts[-1].saved = data[20]   # postings saved


def load_jobs():
    """Loads all the currently existing job postings from the SQLite database on start-up."""
    global job_id

    rows = db.fetch_all("jobs")

    for job_data in rows:
        load_job_data(job_data)

    if jobs:
        job_id = jobs[-1].id + 1 ## sets the job id to 1 + the current highest id

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
        jobs[-1].id = int(data[0])    # id
        jobs[-1].create(data[1], # title
                        data[2], # description
                        data[3], # employer
                        data[4], # location
                        data[5]) # salary
        jobs[-1].set_poster(data[6],  # firstname
                            data[7])  # lastname
        jobs[-1].applications = data[8] #applications


def set_current_account(account):
    global current_account

    current_account = account

def get_current_account():
    return current_account

def set_testing(state):
    global _testing_

    _testing_ = state


def login_base():
    """ 
    Menu loop for logging in,
    prompts the user to input a username and password.
    If vaild, the account logs in.

    Returns
    -------
    None
        returns back to main menu after completion or on return command.
    """

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
        print("")

        is_correct = login(username, password)

        
    return

def login(username, password):

    is_password = check_password(username, password)
    
    if is_password:
        set_current_account(accounts[get_account(username)])
        print("You have successfully logged in.")
        return True
    else:
        print("Incorrect username / password, please try again.")
        return False


def check_requests():
    reqs=current_account.show_friend_requests()
    for i in reqs:
        print("You have a new friend request: ",i,"\n")
        print("Press 'A' to accept, or 'R' to reject.\n")
        inp=input(":: ")
        if inp:
            inp = inp[0].upper()
            
        while inp!='R' and inp!='A':
            print("Incorrect input.")
            inp=input(":: ")

        if inp=='A':
            accept_request(True, i)
        else:
            accept_request(False, i)

def accept_request(is_accept, user):
    if is_accept:
        current_account.accept_friend_request(user)
        print("Accepted "+user+"'s request!\n")
    else:
        current_account.reject_friend_request(user)
        print("Rejected "+user+"'s request!\n")



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
        

def notify_if_deleted():

    ############## Notify if job deleted ################
    saved = []
    applied = []

    ## Get the accounts saved by user
    if current_account.saved:
        saved = current_account.saved.split(",")

    ## Get the accounts applied by user
    if current_account.applied:
        applied = current_account.applied.split(",")
    

    for job in jobs:
        # if the saved job still exists, delete it from list
        if str(job.id) in saved:
            saved.remove(str(job.id))
            applied.remove(job.title)


    ## Unsave the jobs still remaining in the list (The jobs that were deleted)
    for unsave in saved:
        current_account.unsave_post(unsave)

    ## Unapply and notify the user if the jobs still remaining in the list (The jobs that were deleted)
    for unapply in applied:
        current_account.unapply_for_job(unapply)
        print("\nThe job you applied for has been deleted! -> "+unapply+"\n")
    ####################################################



def search_job():
    """
    Todo.

    Returns
    -------
    None
        returns back to user menu after completion.
    """

    
    notify_if_deleted()


    while True:
        print("")
        print("######################################")
        print("##  Would you like to (P)ost a job  ##")
        print("##   (L)ook at the job postings,    ##")
        print("##   (V)iew your own job postings,  ##")
        print("##  or (R)eturn to the last page?   ##")
        print("######################################")  
        print("")
        
        main_input = input(":: ")
        main_input = main_input[0].upper()
        print("")

        if main_input == "P":
            create_job_base()

        elif main_input == "L":
            display_jobs_menu()
        
        elif main_input == "V":
            post = get_posted_postings()
            display_jobs(post, is_owned=True)
            
        elif main_input == "R":
            return

        else:
            print ("That is not a valid command!")
            print("")  

def search_user_base():
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

    search_user(first_name, last_name)

    input("\nPress enter to continue... ")


def search_user(first_name, last_name):

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
        print("##        (R)eturn to Main Menu     ##")
        print("######################################")
        print("")

        user_input = input(":: ")

        if user_input[0] == "1":
            general()

        elif user_input[0] == "2":
            browse_incollege()

        elif user_input[0] == "3":
            business_solutions()

        elif user_input[0] == "4":
            directories()

        elif user_input[0].upper() == "R":
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
        print("##       (R)eturn to Main Menu      ##")
        print("######################################")
        print("")

        user_input = input(":: ")

        if user_input == "1":
            print(copyright_notice())

        elif user_input == "2":
            about()

        elif user_input == "3":
            print(accessibility())

        elif user_input == "4":
            print(user_agreement())

        elif user_input == "5":
            privacy_policy()

        elif user_input == "6":
            print(cookie_policy())

        elif user_input == "7":
            print(copyright_policy())
        
        elif user_input == "8":
            print(brand_policy())

        elif user_input == "9":
            guest_controls()

        elif user_input == "10":
            languages()    

        elif user_input[0].upper() == "R":
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
        user_input = user_input[0].upper()

        if user_input == "S" and current_account == None:
            create_account_base()
        
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

        if user_input[0].upper() == "R":
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

        if user_input[0].upper() == "R":
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

        if user_input[0].upper() == "R":
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

        if user_input[0].upper() == "R":
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

        if user_input[0].upper() == "R":
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

        if user_input[0].upper() == "R":
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

        if user_input[0].upper() == "R":
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

        if user_input[0].upper() == "R":
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
################################################
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
################################################
"""

def accessibility():
    return """
################################################
##             Accessibility                  ##
##                                            ##
## inCollege is committed to providing an     ##
## accessible and inclusive platform for all  ##
## users. We strive to ensure that our        ##
## services are accessible to individuals     ##
## with disabilities. If you encounter any    ##
## accessibility issues, please contact our   ##
## support team to assist you.                ##
################################################
"""

def user_agreement():
    return """
################################################
##           User Agreement                   ##
##                                            ##
## By using inCollege, you agree to comply    ##
## with our User Agreement. This agreement    ##
## outlines the terms and conditions for      ##
## using our platform, including user         ##
## conduct, privacy, and content guidelines.  ##
## Please read the User Agreement carefully   ##
## before using our services.                 ##
################################################
"""

def privacy_policy():
    print("\n###############################################")
    print("## You entrust us with your information when ##")
    print("## you use our services. We make a lot of    ##")
    print("## effort to safeguard your information and  ##")
    print("## give you control since we realize that    ##")
    print("## this is a huge responsibility.            ##")
    print("###############################################\n")
    
    while True:
        if current_account == None:
            print("##############################################")
            print("##                  Main Menu               ##")
            print("##           (R)eturn to Previous Menu      ##")
            print("##############################################")
            print("")
            inp = input(":: " )
            if inp[0].upper() == 'R':
                return
        else:
            print("##############################################")
            print("##                  Main Menu               ##")
            print("##           (R)eturn to Previous Menu      ##")
            print("##           (G)uest Controls               ##")
            print("##############################################")
            print("")
            inp = input(":: " )
            if inp[0].upper() == 'R':
                return
            elif inp[0].upper() == 'G':
                guest_controls()

def cookie_policy():
    return """
################################################
##           Cookie Policy                    ##
##                                            ##
## inCollege uses cookies to enhance user     ##
## experience and provide personalized        ##
## content and ads. By using our platform,    ##
##  you consent to the use of cookies in      ##
## accordance with our Cookie Policy. To      ##
## learn more, please review our Cookie       ##
## Policy on our website.                     ##
################################################
"""
    
def copyright_policy():
    return """
################################################
##         Copyright Policy                   ##
##                                            ##
## inCollege respects the intellectual        ##
## property rights of others. If you believe  ##
## that your copyrighted work has been used   ##
## in a way that constitutes copyright        ##
## infringement, please contact us with       ##
## relevant details. We will investigate and  ##
## take appropriate action.                   ##
################################################
"""

def brand_policy():
    return """
################################################
##           Brand Policy                     ##
##                                            ##
## Our Brand Policy outlines the guidelines   ##
## for using inCollege's brand assets,        ##
## including logos and trademarks. To         ##
## maintain the integrity of our brand,       ##
## please adhere to our brand guidelines      ##
## when using inCollege's branding elements.  ##
## For specific details, refer to our Brand   ##
## Policy available on our website.           ##
################################################
"""

def guest_controls():
    if current_account == None:
        print("\n################################################")
        print("##          Guest Controls: Information       ##")
        print("## Guest Controls helps our users turn off    ##")
        print("## advertising alerts. Kindly login to use    ##")
        print("## this feature.                              ##")
        print("################################################\n")
        return
    
    while True:
        current_account.preferences()
        print("##############################################")
        print("##            Guest Controls Menu           ##")
        print("##    1. Turn off email advertising.        ##")
        print("##    2. Turn off SMS advertising.          ##")
        print("##    3. Turn off targeted advertising.     ##")
        print("##    (R)eturn to Previous Menu             ##")
        print("##############################################\n")
        print("")
        inp = input(":: " )
        if inp[0].upper() == 'R':
            return
        
        if inp in ["1", "2", "3"]:
            update_ad_setting(inp)
        else:
            print("Invalid input")


def update_ad_setting(setting):
    if setting == '1':
        current_account.update_ad(email=False)
    if setting == '2':
        current_account.update_ad(sms=False)
    if setting == '3':
        current_account.update_ad(target=False)


def languages():
    if current_account == None:
        print("\n################################################")
        print("##         Language Preferences: Info         ##")
        print("## Kindly login to your account to set your   ##")
        print("## language preferences.                      ##")
        print("################################################\n")
        return
    
    while True:
        current_account.show_language()
        print("###############################################")
        print("##           Language Preferences Menu       ##")
        print("##  1. English                               ##")
        print("##  2. Spanish                               ##")
        print("##  (R)eturn to Previous Menu                ##")
        print("###############################################\n")
        print("")
        inp = input(">> ")
        if inp[0].upper() == 'R':
            return
        elif inp == '1':
            current_account.set_language("English")
        elif inp == '2':
            current_account.set_language("Spanish")
        else:
            print("Invalid input")

def show_my_network():
    while 1:
        print("")
        print("##############################################")
        print("")  
        print("Your connections:\n")
        friend_list=current_account.get_friends().split(',')
        if friend_list==[] or friend_list==['']:
            print("None.\n")
            return
        for i,v in enumerate(friend_list):
            print(i+1,'. ',v,'\n')

        print("")
        print("## Would you like to (V)iew their profiles  ##")
        print("##             (D)elete the friend          ##")
        print("##                or (R)eturn               ##")
        print("##############################################")  

        print("")
        user_input = input(":: ")
        user_input = user_input[0].upper()

        if user_input == "R":
            return
        elif user_input == "D":
            delete_friend(friend_list)
        elif user_input =="V":
            view_friend_profiles(current_account)
        else:
            print("Not a Valid input!")

def delete_friend(friend_list):
    print("Enter the number of the connection you want to remove or enter '0' to return.\n")
    inpStr=input(":: ")

    try:
        inp=int(inpStr)-1
    except ValueError:
        print("Not a valid input!")
        return
    
    if inp == -1:
        return
    
    if inp in range(len(friend_list)):
        current_account.remove_friend(friend_list[inp])
        print("Successfully removed ",friend_list[inp]," from your network!\n")
    else:
        print("Not a valid input!")


def view_friend_profiles(self):
    """
    Displays the profiles of friends.
    """
    if not self.friends:
        print("You don't have any friends yet.")
        return

    friend_list = self.friends.split(',')

    friend_choice = int(input("Enter the number of the friend to view their profile (or 0 to go back): "))
    print("")
    if 0 < friend_choice <= len(friend_list):
        friend = accounts[get_account(friend_list[friend_choice - 1])]
        if friend.has_profile:
            view_profile(friend)
        else:
            print("Profile not available.")
    elif friend_choice == 0:
        return
    else:
        print("Invalid choice.")

def pending_friend_requests():
    print("Here are your pending friend requests: \n")
    results = current_account.active_requests.split(",")[0:-1]
    for result in results:
        print("-> "+result+"\n")
    
    input("\npress enter to return...")

def unset_current_account():
    """ Unsets the current account"""
    global current_account
    current_account = None

def user_menu():

    """ 
    Menu Loop for user menu after login.

    Returns
    -------
    None
        returns back to main menu after completion or on return command.
    """

    check_requests()   ## Check for friend requests

    is_logged_in = True
    while is_logged_in:
        name = current_account.get_username()
        buffer1 = " "*ceil((36 - len(name))/2)          ## Makes sure the username is centered.
        buffer2 = " "*floor(((36 - len(name))/2)-1)
        print("")
        print("##################################################")
        print("##", buffer1,   "Hello", name + "!", buffer2,  "##")
        print("##    Would you like to (S)earch for a job,     ##")
        print("##  (F)ind someone you know, (L)earn a skill.   ##")
        print("## (E)dit your profile, or (V)iew your profile  ##") 
        print("##    You can also (R)eturn to the main menu.   ##")                
        print("##################################################")
        print("")

        print("")
        print("##################################################")
        print("##                  (U)seful Links              ##")
        print("##            (I)nCollege Important Links       ##")
        print("##                 Show my (N)etwork            ##")
        print("##             (P)ending friend requests        ##")
        print("##################################################")
        print("")   

        main_input = input(":: ")
        main_input = main_input[0].upper()

        print("")

        if main_input == "S":
            search_job()

        elif main_input == "F":
            find_person_base()

        elif main_input == "L":
            learn_skill()
        
        elif main_input == "R":
            unset_current_account()  ## log out of current_account
            return
        
        elif main_input == "U":
            useful_links()

        elif main_input == "I":
            important_links()

        elif main_input=="N":
            show_my_network()

        elif main_input=="P":
            pending_friend_requests()

        elif main_input=="E":
            create_profile()

        elif main_input=="V":
            view_profile(current_account)
        
        else:
            print ("That is not a valid command!") 



def view_profile(user):

    print("")
    print("##################################################")
    print("##", user.get_firstname(), user.get_lastname())
    print("##")
    print("##  Title:", user.get_title())
    print("##  Major:", user.get_major())
    print("##  University:", user.get_uni())
    print("##")
    print("##  Info:", user.get_info())
    print("##")
    print("##  Experience:\n", user.get_exp())             
    print("##")
    print("##  Education:\n", user.get_edu())
    print("##")     
    print("##################################################")
    print("")
    main_input = input("press enter to return... ")




def main():
    """Menu Loop for main menu."""

    ## Load Database
    db.load()

    ## Turn off testing mode, when program is run normally.
    set_testing(False)

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
            login_base()

        elif main_input == "C":
            create_account_base()

        elif main_input == "S":
            search_user_base()

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