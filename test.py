import pytest
import os
from main import *

## HOW TO MAKE TEST CASES ##

# 1. If your test case needs to access the database for any reason, call the 'setup_and_teardown' fixture
#    as an argument.  
#
# 2. If you need a string to test, and the criteria for the string may change in the future;
#    then make a new VALUE fixture in the section "VALUES FOR TESTING" if said string doesn't
#    already exist.
#
# 3. If your test case requires the need for user input, call the 'mock_inputs' fixture and one of
#    the USER INPUT fixtures from the section "USER INPUTS" as an argument. 
#
# 4. If you need a new USER INPUT fixture, create one by calling the 'inputs' fixture as an argument, and any
#    of the VALUES fixtures you need. Then call 'inputs.append(VALUES or string)' In the EXACT ORDER that a user 
#    would input the value normally. DO NOT USE MORE INPUTS THEN NEEDED FOR THE TEST.
#
# 5. If making a test case that utilizes a working account, call the 'prefab_account' fixture as an argument. 
#    The username of the account is 'good_username' password is 'good_pass' firstname is 'firstname' and lastname 
#    is 'lastname'.
#
# 6. If you need to be logged into an account, call the 'prefab_account' and 'mock-inputs' fixture as an argument.
#    Make sure your USER INPUT starts with 'good_username' and 'good_pass' as the inputs. and call the Login()
#    function from the main script as the first line of code. (This should be simplified later, but works for now)
#
# 5. If making a test case that utilizes multiple working accounts, call the 'fill_accounts' fixture as an argument. 
#    The username of the first account is 'good_username0' password is 'good_pass' firstname is 'firstname0' and lastname 
#    is 'lastname0', the number increments each account.
#
# 6. If you need to be logged into one of the multiple accounts, call the 'fill_accounts' and 'mock-inputs' fixture as 
#    an argument. Make sure your USER INPUT starts with 'good_username+(id of account)' and 'good_pass' as the inputs. 
#    and call the Login() function from the main script as the first line of code.
#
#    Note: Login() requires the USER INPUT 'return_key' to log out.
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
def user_input_account(inputs, good_username, good_pass, firstname, lastname):
    inputs.append(good_username)
    inputs.append(good_pass)
    inputs.append(firstname)
    inputs.append(lastname)

@pytest.fixture
def user_input_account_bad(inputs, good_username, exit_key):
    inputs.append(good_username)
    inputs.append(exit_key)

@pytest.fixture
def user_input_login_good(inputs, good_username, good_pass):
    inputs.append(good_username)
    inputs.append(good_pass)

@pytest.fixture
def user_input_login_bad(inputs, bad_username, good_pass, exit_key):
    inputs.append(bad_username)
    inputs.append(good_pass)
    inputs.append(exit_key)

@pytest.fixture
def user_input_login_on_second_attempt(inputs, bad_username, good_pass, good_username):
    inputs.append(bad_username)
    inputs.append(good_pass)
    inputs.append(good_username)
    inputs.append(good_pass)

@pytest.fixture
def user_input_job(inputs, job_title, job_desc, job_employer, job_location, job_salary, good_username, good_pass):
    inputs.append(good_username)
    inputs.append(good_pass)
    inputs.append(job_title)
    inputs.append(job_desc)
    inputs.append(job_employer)
    inputs.append(job_location)
    inputs.append(job_salary)

@pytest.fixture
def user_input_job_bad(inputs, job_title, job_desc, job_employer, job_location, job_salary, good_username, good_pass):
    inputs.append(job_title)
    inputs.append(job_desc)
    inputs.append(job_employer)
    inputs.append(job_location)
    inputs.append(job_salary)

@pytest.fixture
def user_input_guest_controls(inputs, good_username, good_pass, return_key):
    inputs.append(good_username)
    inputs.append(good_pass)
    inputs.append("1")
    inputs.append("3")
    inputs.append("2")
    inputs.append(return_key)

@pytest.fixture
def user_input_languages(inputs, good_username, good_pass, return_key):
    inputs.append(good_username)
    inputs.append(good_pass)
    inputs.append("2")
    inputs.append("1")
    inputs.append(return_key)

@pytest.fixture
def user_input_search_user(inputs, firstname, lastname, return_key):
    inputs.append(firstname)
    inputs.append(lastname)
    inputs.append(return_key)

@pytest.fixture
def user_input_search_user_bad(inputs, good_username, bad_username, return_key):
    inputs.append(good_username)
    inputs.append(bad_username)
    inputs.append(return_key)

@pytest.fixture
def user_input_find_person(inputs, good_username, good_pass, firstname, lastname, return_key):
    inputs.append(good_username)
    inputs.append(good_pass)
    inputs.append(firstname)
    inputs.append(lastname)
    inputs.append(return_key)

@pytest.fixture
def user_input_find_person_bad(inputs, good_username, good_pass, bad_username, return_key):
    inputs.append(good_username)
    inputs.append(good_pass)
    inputs.append(good_username)
    inputs.append(bad_username)
    inputs.append(return_key)

@pytest.fixture
def user_input_privacy(inputs, good_username, good_pass, return_key):
    inputs.append(good_username)
    inputs.append(good_pass)
    inputs.append(return_key)

@pytest.fixture
def user_input_send_request(inputs, good_username, good_pass, firstname, lastname, return_key):
    inputs.append(good_username+"0")
    inputs.append(good_pass)
    inputs.append("F")
    inputs.append(firstname+"1")
    inputs.append(lastname+"1")
    inputs.append("S")
    inputs.append(return_key)

@pytest.fixture
def user_input_accept_request(inputs, good_username, good_pass, firstname, lastname, return_key):
    inputs.append(good_username+"1")
    inputs.append(good_pass)
    inputs.append("F")
    inputs.append(firstname+"0")
    inputs.append(lastname+"0")
    inputs.append("S")
    inputs.append(return_key)
    inputs.append(good_username+"0")
    inputs.append(good_pass)
    inputs.append("A")
    inputs.append(return_key)



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
    initialize_database()

    load_accounts()
    load_jobs()

    #waits for test to end
    yield

    ## Clean up after each test
    save_accounts()

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
    accounts[-1].create(good_username, good_pass, firstname, lastname, '1', '1', '1', "English", "", "")

    yield
    ## Clear accounts when done
    accounts.clear()
    unset_current_account()

# This creates the maximun number of prefab accounts
@pytest.fixture
def fill_accounts(good_username, good_pass, firstname, lastname):
    for i in range(MAX_ACC):
        accounts.append(Account())
        accounts[-1].create(good_username+str(i), good_pass, firstname+str(i), lastname+str(i), '1', '1', '1', "English", "", "")

    yield
    ## Clear accounts when done
    accounts.clear()
    unset_current_account()


# This creates a prefab job
@pytest.fixture
def prefab_job(job_title, job_desc, job_employer, job_location, job_salary, firstname, lastname):
    jobs.append(Job())
    jobs[-1].create(job_title, job_desc, job_employer, job_location, job_salary)
    jobs[-1].set_poster(firstname, lastname)

    yield
    ## Clear jobs when done
    jobs.clear()

# This creates the maximun number of prefab jobs
@pytest.fixture
def fill_jobs(job_title, job_desc, job_employer, job_location, job_salary, firstname, lastname):
    for i in range(MAX_JOB):
        jobs.append(Job())
        jobs[-1].create(job_title, job_desc, job_employer, job_location, job_salary)
        jobs[-1].set_poster(firstname, lastname)

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


def test_create_account(setup_and_teardown, mock_inputs, capsys, user_input_account):
    
    # Run the create account function
    create_account()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "Account successfully created!" in captured.out

def test_create_account_with_same_username(setup_and_teardown, prefab_account, mock_inputs, capsys, user_input_account_bad):
    
    # Run the create account function
    create_account()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "Username invalid! Username already exists!" in captured.out

def test_create_account_when_max(setup_and_teardown, fill_accounts, mock_inputs, capsys, user_input_account):
    
    # Run the create account function
    create_account()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "All permitted accounts have been created, please come back later." in captured.out


def test_create_job(setup_and_teardown, mock_inputs, capsys, prefab_account, user_input_job):
    # login to a account
    login()

    # Run the create account function
    create_job()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "Job successfully posted!" in captured.out

def test_create_job_when_not_log_in(setup_and_teardown, mock_inputs, capsys, user_input_job_bad):

    # Run the create account function
    create_job()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "You must be logged in to post a job!" in captured.out

def test_create_job_when_max(setup_and_teardown, fill_jobs, prefab_account, mock_inputs, capsys, user_input_job):
    # login to a account
    login()

    # Run the create account function
    create_job()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "All permitted job postings have been created, please come back later." in captured.out


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
def test_login_success(prefab_account, mock_inputs, capsys, user_input_login_good):

    # Run the login function
    login()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "You have successfully logged in." in captured.out

def test_login_failure(prefab_account, mock_inputs, capsys, user_input_login_bad):

    # Run the login function
    login()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "Incorrect username / password, please try again." in captured.out

def test_login_on_next_attempt(prefab_account, mock_inputs, capsys, user_input_login_on_second_attempt):

    # Run the login function
    login()

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

def test_privacy_policy_logged_in(prefab_account, capsys, mock_inputs, user_input_privacy):

    login()

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

def test_guest_controls(mock_inputs, capsys, user_input_return):
    guest_controls()

    # Capture the printed output
    captured = capsys.readouterr()

    assert "Guest Controls: Information" in captured.out
    assert "Kindly login to use" in captured.out

def test_languages(mock_inputs, capsys, user_input_return):

    languages()

    # Capture the printed output
    captured = capsys.readouterr()

    assert "Language Preferences: Info" in captured.out
    assert "Kindly login to your account to set your" in captured.out


def test_languages_logged_in(setup_and_teardown, prefab_account, mock_inputs, capsys, user_input_languages):

    # Run the login function
    login()

    #Run the guest controls menu
    languages()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "Your current language preference is:  Spanish" in captured.out
    assert "Your current language preference is:  English " in captured.out


def test_guest_controls_logged_in(setup_and_teardown, prefab_account, mock_inputs, capsys, user_input_guest_controls):

    # Run the login function
    login()

    #Run the guest controls menu
    guest_controls()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "Email ads:  Yes  SMS ads:  Yes  Target ads:  Yes" in captured.out
    assert "Email ads:  No  SMS ads:  Yes  Target ads:  Yes" in captured.out
    assert "Email ads:  No  SMS ads:  Yes  Target ads:  No" in captured.out
    assert "Email ads:  No  SMS ads:  No  Target ads:  No" in captured.out

def test_search_user(prefab_account, mock_inputs, capsys, user_input_search_user):

    search_user()

    # Capture the printed output
    captured = capsys.readouterr()

    assert "They are a part of the" in captured.out

def test_search_user_bad(prefab_account, mock_inputs, capsys, user_input_search_user_bad):

    search_user()

    # Capture the printed output
    captured = capsys.readouterr()

    assert "They are not yet a part" in captured.out

def test_find_person(prefab_account, mock_inputs, capsys, user_input_find_person, firstname, lastname, good_username):

    login()

    find_person()

    # Capture the printed output
    captured = capsys.readouterr()

    assert "The username of "+firstname+" "+lastname+" is: "+good_username in captured.out

def test_find_person_bad(prefab_account, mock_inputs, capsys, user_input_find_person_bad):

    login()

    find_person()

    # Capture the printed output
    captured = capsys.readouterr()

    assert "This person is not a member of" in captured.out


def test_send_friend_request(setup_and_teardown, fill_accounts, mock_inputs, capsys, user_input_send_request, good_username):

    login()

    user_menu()

    # Capture the printed output
    captured = capsys.readouterr()

    assert "Sent friend request to  "+good_username+"1" in captured.out


def test_accept_friend_request(setup_and_teardown, fill_accounts, mock_inputs, capsys, user_input_accept_request, good_username):

    login()

    user_menu()

    login()

    # Capture the printed output
    captured = capsys.readouterr()

    assert "You have a new friend request:  "+good_username+"1" in captured.out