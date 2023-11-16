import pytest
import os
from main import *

## HOW TO MAKE TEST CASES ##

# 1. If your test case needs to access the database for any reason, call the 'setup_and_teardown' fixture
#    as an argument, This should no longer be needed as the databases should be seperate.  
#
# 2. If you need a string to test, and the criteria for the string may change in the future;
#    then make a new VALUE fixture in the section "VALUES FOR TESTING" if said string doesn't
#    already exist.
#
# 3. If your test case requires the need for user input, call the 'mock_inputs' fixture and one of
#    the USER INPUT fixtures from the section "USER INPUTS" as an argument, Try to avoid doing this. 
#
# 4. If you need a new USER INPUT fixture, create one by calling the 'inputs' fixture as an argument, and any
#    of the VALUES fixtures you need. Then call 'inputs.append(VALUES or string)' In the EXACT ORDER that a user 
#    would input the value normally. DO NOT USE MORE INPUTS THEN NEEDED FOR THE TEST.
#
# 5. If making a test case that utilizes a working account, call the 'prefab_account' fixture as an argument. 
#    The username of the account is 'good_username' password is 'good_pass' firstname is 'firstname' and lastname 
#    is 'lastname'.
#
# 6. If you need to be logged into an account, call the 'prefab_accounts' fixture as an argument. 
#    Call the set_current_account(accounts[0]) function from the main script as the first line of code.
#
# 5. If making a test case that utilizes multiple working accounts, call the 'fill_accounts' fixture as an argument. 
#    The username of the first account is 'good_username0' password is 'good_pass' firstname is 'firstname0' and lastname 
#    is 'lastname0', the number increments each account.
#
# 6. If you need to be logged into one of the multiple accounts, call the 'fill_accounts' fixture as 
#    an argument. Call the set_current_account(accounts[ID OF ACCOUNT]) function from the main script as the first line of code.
#
# 7. Jobs work similarly to accounts; 'prefab_account' -> 'prefab_job' , 'fill_accounts' -> 'fill_jobs' .
#    all jobs use the VALUES 'job_title', 'job_desc', 'job_employer', 'job_location', 'job_salary' .
#
#    Finally: Feel free to make any new USEFUL FIXTURES to help youself with test cases.



## VALUES FOR TESTING ##

@pytest.fixture
def good_username():
    return "TestUser"

@pytest.fixture
def bad_username():
    return "username"

@pytest.fixture
def firstname():
    return "Tester"

@pytest.fixture
def lastname():
    return "McTestson"

@pytest.fixture
def good_pass():
    return "Test123!"

@pytest.fixture
def small_pass():
    return "Tes7."

@pytest.fixture
def long_pass():
    return "TooL0ngPassword!"

@pytest.fixture
def no_cap_pass():
    return "test123!"

@pytest.fixture
def no_dig_pass():
    return "Testers!"

@pytest.fixture
def no_sym_pass():
    return "test123s"

@pytest.fixture
def job_title():
    return "Code Tester"

@pytest.fixture
def job_desc():
    return "You Test Code!"

@pytest.fixture
def job_employer():
    return "TestLabs"

@pytest.fixture
def job_location():
    return "Test Location"

@pytest.fixture
def job_salary():
    return "73,575"

@pytest.fixture
def exit_key():
    return "Exit"

@pytest.fixture
def return_key():
    return "R"

######## USER INPUTS ###########

@pytest.fixture
def inputs():
    return []

@pytest.fixture
def user_input_login_on_second_attempt(inputs, bad_username, good_pass, good_username):
    inputs.append(bad_username)
    inputs.append(good_pass)
    inputs.append(good_username)
    inputs.append(good_pass)

@pytest.fixture
def user_input_return(inputs, return_key):
    inputs.append(return_key)

############## USEFUL FIXTURES ########################
    
## Run this when you work with the database!
@pytest.fixture
def setup_and_teardown():
    ## Set up a clean environment before each test

    # Changes the main database, so it won't be written over.
    try:
        os.rename("accounts.db", "accounts-main.db")
    except FileNotFoundError:
        pass

    #loads the database
    db.load()

    load_accounts()
    load_jobs()

    #waits for test to end
    yield

    # Deletes the testing database
    try:
        os.remove("accounts.db")
    except OSError:
        pass

    # Changes the main database back.
    try:
        os.rename("accounts-main.db", "accounts.db")
    except FileNotFoundError:
        pass
    ## Clear accounts when done
    accounts.clear()
    jobs.clear()

# This creates a prefab account
@pytest.fixture
def prefab_account(good_username, good_pass, firstname, lastname):
    accounts.append(Account())
    accounts[-1].create(good_username, good_pass, firstname, lastname)

    yield
    ## Clear accounts when done
    accounts.clear()
    unset_current_account()

# This creates the maximun number of prefab accounts
@pytest.fixture
def fill_accounts(good_username, good_pass, firstname, lastname):
    for i in range(MAX_ACC):
        accounts.append(Account())
        accounts[-1].create(good_username+str(i), good_pass, firstname+str(i), lastname+str(i))

    yield
    ## Clear accounts when done
    accounts.clear()
    unset_current_account()


# This creates a prefab job
@pytest.fixture
def prefab_job(job_title, job_desc, job_employer, job_location, job_salary, firstname, lastname):

    ## set account 0 as the current account
    try:
        set_current_account(accounts[0])
        account = get_current_account()
    except IndexError:
        raise RuntimeError("Must call prefab_account or fill_accounts as an argument first before prefab_job!")
    
    create_job(0, job_title, job_desc, job_employer, job_location, job_salary)

    yield
    ## Clear jobs when done
    jobs.clear()

# This creates the maximun number of prefab jobs
@pytest.fixture
def fill_jobs(job_title, job_desc, job_employer, job_location, job_salary, firstname, lastname):

    ## set account 0 as the current account
    try:
        set_current_account(accounts[0])
        account = get_current_account()
    except IndexError:
        raise RuntimeError("Must call prefab_account or fill_accounts as an argument first before fill_jobs!")

    for i in range(MAX_JOB):
        create_job(i, job_title+str(i), job_desc, job_employer, job_location, job_salary)

    yield
    ## Clear jobs when done
    jobs.clear()

#This changes the input module so it takes a set input, call this with one of the user inputs above!
@pytest.fixture
def mock_inputs(monkeypatch, inputs):
    # Provide user input for username and password
    input_values = inputs

    # Monkeypatch the input function to simulate user input
    def mock_input(prompt=None):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    

############## TESTS ##################################

# Test getting an account by username
def test_get_account(prefab_account, good_username, bad_username):

    # Get the account by username
    assert get_account(good_username) >= 0
    assert get_account(bad_username) == -1


def test_create_account(capsys, good_username, good_pass, firstname, lastname):

    check1 = check_username(good_username)

    check2 = check_valid_password(good_pass)

    assert check1 == False
    assert check2 == False
    
    # Run the create account function
    create_account(good_username, good_pass, firstname, lastname)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "Account successfully created!" in captured.out

def test_create_account_already_exist(prefab_account, good_username):
    
    # Run the username checker function
    check = check_username(good_username)

    # Check if the username already exists
    assert check == True

def test_create_account_when_max(capsys, fill_accounts, good_username, good_pass, firstname, lastname):
    
    # Run the create account function
    create_account(good_username, good_pass, firstname, lastname)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "All permitted accounts have been created, please come back later." in captured.out


def test_create_job(capsys, prefab_account, job_title, job_desc, job_employer, job_location, job_salary):
    # login to a account
    set_current_account(accounts[0])

    # Run the create account function
    create_job(0, job_title, job_desc, job_employer, job_location, job_salary)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "Job successfully posted!" in captured.out

    jobs.clear()


def test_create_job_when_max(capsys, prefab_account, fill_jobs, job_title, job_desc, job_employer, job_location, job_salary):

    # login to a account
    set_current_account(accounts[0])

    # Run the create account function
    create_job(MAX_JOB, job_title, job_desc, job_employer, job_location, job_salary)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "All permitted job postings have been created, please come back later." in captured.out

    jobs.clear()


# Test with valid password
def test_valid_password(good_pass):
    assert check_valid_password(good_pass) == False

# Test with invalid length 
def test_invalid_length(small_pass, long_pass):
    assert check_valid_password(small_pass) == True
    assert check_valid_password(long_pass) == True

# Test without capital letter
def test_no_capital(no_cap_pass):
    assert check_valid_password(no_cap_pass) == True

# Test without digit  
def test_no_digit(no_dig_pass):
    assert check_valid_password(no_dig_pass) == True

# Test without symbol
def test_no_symbol(no_sym_pass):
    assert check_valid_password(no_sym_pass) == True


# Test the login function
def test_login_success(capsys, prefab_account, good_username, good_pass):

    # Run the login function
    login(good_username, good_pass)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "You have successfully logged in." in captured.out

def test_login_failure(capsys, prefab_account, bad_username, good_pass):

    # Run the login function
    login(bad_username, good_pass)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "Incorrect username / password, please try again." in captured.out

def test_login_on_next_attempt(prefab_account, mock_inputs, capsys, user_input_login_on_second_attempt):

    # Run the login function
    login_base()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "You have successfully logged in." in captured.out

def test_play_video_input(capsys, mock_inputs, user_input_return):

    # Call play_video function
    play_video()
    
    # Capture stdout
    captured = capsys.readouterr()
    
    # Check output
    assert "Video is now playing." in captured.out
    assert "Press 'enter' to continue." in captured.out

def test_copyright_notice():
    result = copyright_notice()
    assert "Copyright Notice" in result
    assert "All content provided on inCollege" in result

def test_accessibility():
    result = accessibility()
    assert "Accessibility" in result
    assert "inCollege is committed to providing an" in result

def test_user_agreement():
    result = user_agreement()
    assert "User Agreement" in result
    assert "By using inCollege, you agree to comply" in result

def test_privacy_policy(capsys, mock_inputs, user_input_return):

    privacy_policy()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the expected content is present in the output
    assert "You entrust us with your information" in captured.out
    assert "this is a huge responsibility." in captured.out

def test_privacy_policy_logged_in(capsys, prefab_account, mock_inputs, user_input_return):

    set_current_account(accounts[0])

    privacy_policy()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the expected content is present in the output
    assert "You entrust us with your information" in captured.out
    assert "this is a huge responsibility." in captured.out
    assert "(G)uest Controls" in captured.out

def test_cookie_policy():
    result = cookie_policy()
    assert "Cookie Policy" in result
    assert "inCollege uses cookies to enhance user" in result

def test_copyright_policy():
    result = copyright_policy()
    assert "Copyright Policy" in result
    assert "inCollege respects the intellectual" in result

def test_brand_policy():
    result = brand_policy()
    assert "Brand Policy" in result
    assert "Our Brand Policy outlines the guidelines" in result

def test_guest_controls(capsys, mock_inputs, user_input_return):
    guest_controls()

    # Capture the printed output
    captured = capsys.readouterr()

    assert "Guest Controls: Information" in captured.out
    assert "Kindly login to use" in captured.out

def test_languages(capsys, mock_inputs, user_input_return):

    languages()

    # Capture the printed output
    captured = capsys.readouterr()

    assert "Language Preferences: Info" in captured.out
    assert "Kindly login to your account to set your" in captured.out


def test_languages_logged_in(prefab_account):
    
    # Set the current account and retrieve it
    set_current_account(accounts[0])
    account = get_current_account()

    #Set Language to spanish first
    account.set_language("Spanish")

    assert account.get_language() == "Spanish"

    #Next Language to english next
    account.set_language("English")

    assert account.get_language() == "English"


def test_guest_controls_logged_in(prefab_account):

    # Run the login function
    set_current_account(accounts[0])
    account = get_current_account()

    #Run the guest controls menu
    update_ad_setting("1")
    update_ad_setting("2")
    update_ad_setting("3")

    assert account.get_emailAd() == 0
    assert account.get_smsAd() == 0
    assert account.get_targetAd() == 0

def test_search_user(capsys, prefab_account, firstname, lastname):

    ## Search for a user using a existing firstname and lastname
    search_user(firstname, lastname)

    # Capture the printed output
    captured = capsys.readouterr()

    assert "They are a part of the" in captured.out

def test_search_user_bad(capsys, prefab_account, bad_username, lastname):

    ## Search for a user using a nonexisting firstname or lastname
    search_user(bad_username, lastname)

    # Capture the printed output
    captured = capsys.readouterr()

    assert "They are not yet a part" in captured.out

def test_find_person(capsys, prefab_account, firstname, lastname, good_username):

    # Set the current account
    set_current_account(accounts[0])

    ## Search for a user using a existing firstname and lastname
    find_person(firstname, lastname)

    # Capture the printed output
    captured = capsys.readouterr()

    assert "The username of "+firstname+" "+lastname+" is: "+good_username in captured.out

def test_find_person_bad(capsys, prefab_account, bad_username, lastname):

    # Set the current account
    set_current_account(accounts[0])

    ## Search for a user using a nonexisting firstname or lastname
    find_person(bad_username, lastname)

    # Capture the printed output
    captured = capsys.readouterr()

    assert "This person is not a member of" in captured.out


def test_send_friend_request(capsys, fill_accounts, good_username):

    set_current_account(accounts[0])

    send_request(good_username+"1")

    # Capture the printed output
    captured = capsys.readouterr()

    assert "Sent friend request to  "+good_username+"1" in captured.out


def test_accept_friend_request(capsys, fill_accounts, good_username):

    ## set account 1 as the current account
    set_current_account(accounts[1])

    ## send friend request to account 0
    send_request(good_username+"0")

    ## set account 0 as current account
    set_current_account(accounts[0])

    ## Accept friend request from account 1
    accept_request(True, good_username+"1")

    # Capture the printed output
    captured = capsys.readouterr()

    assert "Accepted "+good_username+"1"+"'s request!" in captured.out

def test_reject_friend_request(capsys, fill_accounts, good_username):

    ## set account 1 as the current account
    set_current_account(accounts[1])

    ## send friend request to account 0
    send_request(good_username+"0")

    ## set account 0 as current account
    set_current_account(accounts[0])

    ## Reject friend request from account 1
    accept_request(False, good_username+"1")

    # Capture the printed output
    captured = capsys.readouterr()

    assert "Rejected "+good_username+"1"+"'s request!" in captured.out

# Test job listing
def test_job_listing(capsys, prefab_account, fill_jobs, job_title):

    ## set account 0 as current account
    set_current_account(accounts[0])

    ## get all posts then disply them
    posts = get_all_postings()
    display_jobs(posts)

    captured = capsys.readouterr()
    assert job_title+"0" in captured.out

# Test job details display
def test_job_details_display(capsys, prefab_account, fill_jobs, job_title):

    posts = get_all_postings()

    post_info(posts[0])
    captured = capsys.readouterr()
    assert "Title: " + job_title+"0" in captured.out

# Test job application
def test_job_application(capsys, fill_accounts, fill_jobs):

    ## set account 1 as current account
    set_current_account(accounts[1])
    account = get_current_account()

    posts = get_all_postings()

    account.apply_for_job(posts[0], "12/01/2023", "01/01/2024", "I am a good fit for this job because...")
    captured = capsys.readouterr()

    assert "Application submitted successfully!" in captured.out

# Test job deletion by poster
def test_job_deletion_by_poster(capsys, prefab_account, fill_jobs):

    ## set account 0 as current account
    set_current_account(accounts[0])

    posts = get_all_postings()

    delete_job(posts[0])
    captured = capsys.readouterr()
    assert "Job deleted successfully!" in captured.out

# Test job deletion impact on applications
def test_job_deletion_impact_on_applications(capsys, fill_accounts, fill_jobs):
    
    ## set account 1 as current account
    set_current_account(accounts[1])
    account = get_current_account()

    posts = get_all_postings()

    account.apply_for_job(posts[0], "12/01/2023", "01/01/2024", "I am a good fit for this job because...")

    ## Get name of job to be deleted
    job_name = posts[0].title

    ## set account 0 as current account (Owner of jobs) and delete job
    set_current_account(accounts[0])
    delete_job(posts[0])

    ## set account 1 as current account and notify if job deleted
    set_current_account(accounts[1])
    
    notify_if_deleted()

    captured = capsys.readouterr()

    assert "The job you applied for has been deleted! -> "+job_name in captured.out

# Test job saving and unsaving
def test_job_saving_and_unsaving(fill_accounts, prefab_job):

    ## set account 1 as current account 
    set_current_account(accounts[1])
    account = get_current_account()

    posts = get_all_postings()
    account.save_post(posts[0])

    saved = account.get_saved().split(",")

    assert str(posts[0].id) in saved[0]

    account.unsave_post(posts[0].id)

    saved = account.get_saved().split(",")

    assert str(posts[0].id) not in saved


# Test applying for own job posting
def test_applying_for_own_job(capsys, prefab_account, fill_jobs):
    
    account = get_current_account()

    posts = get_all_postings()
    account.apply_for_job(posts[0], "12/01/2023", "01/01/2024", "I am a good fit for this job! ")

    captured = capsys.readouterr()
    assert "You cannot apply for your own job posting!" in captured.out

# Test viewing list of applied jobs
def test_viewing_applied_jobs(capsys, fill_accounts, fill_jobs, job_title):
    
    ## set account 1 as current account 
    set_current_account(accounts[1])
    account = get_current_account()

    posts = get_all_postings()

    account.apply_for_job(posts[1], "12/01/2023", "01/01/2024", "I am a good fit for this job! ")

    posts = get_applied_postings(True)
    
    display_jobs(posts)

    captured = capsys.readouterr()
    assert job_title+"1" in captured.out

# Test viewing list of jobs not applied for
def test_viewing_jobs_not_applied_for(capsys, fill_accounts, fill_jobs, job_title):
    
    ## set account 1 as current account 
    set_current_account(accounts[1])
    account = get_current_account()

    posts = get_all_postings()

    account.apply_for_job(posts[0], "12/01/2023", "01/01/2024", "I am a good fit for this job! ")

    posts = get_applied_postings(False)
    
    display_jobs(posts)

    captured = capsys.readouterr()
    assert job_title+"1" in captured.out

# Test retrieving list of saved jobs
def test_retrieving_saved_jobs(capsys, fill_accounts, fill_jobs, job_title):

    ## set account 1 as current account 
    set_current_account(accounts[1])
    account = get_current_account()

    posts = get_all_postings()
    account.save_post(posts[0])

    posts = get_saved_postings()

    display_jobs(posts)

    captured = capsys.readouterr()
    assert job_title+"0" in captured.out
