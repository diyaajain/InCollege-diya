import pytest
import io
from io import StringIO
import sys
from main import *
from unittest.mock import patch

@pytest.fixture(scope="module")
def mock_stdout():
    mock_output = StringIO()
    yield mock_output
    mock_output.close()

@pytest.fixture(scope="module")
def monkeypatch():
    from _pytest.monkeypatch import MonkeyPatch
    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.undo()

@pytest.fixture(scope="module")
def setup_accounts():
    accounts = []
    test_account = Account()
    test_account.create("TestUser", "Test123!", "Test", "User", "test.user@gmail.com", "1234567890", "Target", "English")
    accounts.append(test_account)
    yield accounts
    accounts.remove(test_account)

def test_check_username_and_password():
    accounts.append(Account())
    accounts[-1].create(
        "TestUser", "Test123!", "Test", "User",
        "test.user@gmail.com", "1234567890", "Target", "English"
    )

    assert check_username("TestUser") == True
    assert check_password("TestUser", "Test123!") == True
    assert check_username("NonExistentUser") == False
    assert check_password("TestUser", "WrongPassword") == False

def test_get_account():
    accounts.append(Account())
    accounts[-1].create("TestUser", "Test123!", "Test", "User", "test.user@gmail.com", "1234567890", "Target", "English")

    assert get_account("TestUser") >= 0
    assert get_account("NonExistentUser") == -1

def test_login_success(capsys, monkeypatch):
    input_values = ["TestUser", "Test123!"]
    
    def mock_input(prompt):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)

    login()

    captured = capsys.readouterr()

    assert "You have successfully logged in." in captured.out

def test_login_failure(capsys, monkeypatch):
    input_values = ["TestUser", "WrongPassword", "Exit"]
    
    def mock_input(prompt):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)

    login()

    captured = capsys.readouterr()

    assert "Incorrect username / password, please try again." in captured.out

def test_valid_password():
    assert check_valid_password("Test123$") == False

def test_invalid_length():
    assert check_valid_password("Test1") == True
    assert check_valid_password("TooLongPassword") == True

def test_no_capital():
    assert check_valid_password("test123$") == True

def test_no_digit():
    assert check_valid_password("TestPassword$") == True

def test_play_video(capsys, monkeypatch):
    def mock_input(prompt):
        return ""
    
    monkeypatch.setattr('builtins.input', mock_input)

    play_video()

    out, err = capsys.readouterr()

    assert "Video is now playing." in out
    assert "Press 'enter' to continue." in out

def test_play_video_input(capsys, monkeypatch):
    def mock_input(prompt):
        return "x"
    
    monkeypatch.setattr('builtins.input', mock_input)

    play_video()

    out, err = capsys.readouterr()

    assert "Video is now playing." in out
    assert "Press 'enter' to continue." in out

def test_create_job_max_jobs_per_user(monkeypatch):
    jobs = []

    inputs = ["Software Engineer", "Design software", "Google", "Mountain View", "120,000"]
    def mock_input(prompt):
        return inputs.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)

    test_account = Account()
    test_account.create("TestUser", "Test123!", "Test", "User", "test.user@gmail.com", "1234567890", "Target", "English")

    for _ in range(5):
        test_account.increment_jobs_posted()

    create_job()

    assert len(jobs) == 0

def test_display_jobs(capsys):
    display_jobs()
    
    out, err = capsys.readouterr()
    
    assert out == "Under construction!\n"

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

def test_privacy_policy(capsys):
    # Mock user input to simulate "R" for returning to the previous menu
    input_values = ["R"]

    with patch('builtins.input', side_effect=input_values):
        # Call the privacy_policy function
        privacy_policy()

        # Capture the printed output
        captured = capsys.readouterr()

        # Check if the expected content is present in the output
        assert "You entrust us with your information" in captured.out
        assert "this is a huge responsibility." in captured.out

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

def test_languages(capsys):

    current_account = None
    
    languages()
    
    captured = capsys.readouterr()
    
    print("Captured output:")
    print(captured.out)
    
    assert "Language Preferences: Info" in captured.out
    assert "Kindly login to your account to set your language preferences." in captured.out        
    assert "Language Preferences Menu" in captured.out
    assert "1. English" in captured.out 
    assert "(R)eturn to Previous Menu" in captured.out
