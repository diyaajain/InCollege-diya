import pytest
import io
from io import StringIO
import sys
from main import *
from unittest.mock import patch

class Job:
    def __init__(self, title, description, employer, location, salary):
        self.title = title
        self.description = description
        self.employer = employer
        self.location = location
        self.salary = salary

jobs = []
# Test checking username and password
def test_check_username_and_password():
    # Create a test account
    accounts.append(Account())
    accounts[-1].create("TestUser", "Test123!", "Test", "User", )

    # Check if the username and password are correct
    assert check_username("TestUser") == True
    assert check_password("TestUser", "Test123!") == True

    # Check if incorrect username and password are detected
    assert check_username("NonExistentUser") == False
    assert check_password("TestUser", "WrongPassword") == False

# Test getting an account by username
def test_get_account():
    # Create a test account
    accounts.append(Account())
    accounts[-1].create("TestUser", "Test123!", "Test", "User")

    # Get the account by username
    assert get_account("TestUser") >= 0
    assert get_account("NonExistentUser") == -1

# Create a test account
test_account = {"username": "TestUser", "password": "Test123!"}
accounts.append(test_account)

# Test the login function
def test_login_success(capsys, monkeypatch):
    # Provide user input for username and password
    input_values = ["TestUser", "Test123!"]
    
    # Monkeypatch the input function to simulate user input
    def mock_input(prompt):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)

    # Run the login function
    login()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login was successful
    assert "You have successfully logged in." in captured.out

def test_login_failure(capsys, monkeypatch):
    # Provide incorrect user input for username and password
    input_values = ["TestUser", "WrongPassword", "Exit"]
    
    # Monkeypatch the input function to simulate user input
    def mock_input(prompt):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)

    # Run the login function
    login()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the login failed
    assert "Incorrect username / password, please try again." in captured.out

# Clean up the test account after testing
accounts.remove(test_account)

def mock_print(*args, **kwargs):
    captured_output.append(" ".join(map(str, args)))

# Test the learn_skill function
def test_learn_skill_return_to_menu(capsys):
    global captured_output

    # Initialize a list to capture the printed output
    captured_output = []

    # Simulate user input for each option, including "R"
    input_values = ["S", "W", "N", "I", "A", "R"]

    with patch('builtins.input', side_effect=input_values):
        # Replace the built-in print function with the mock_print function
        patch('builtins.print', side_effect=mock_print)

        # Run the menu function and check if it returns when "R" is selected
        result = menu_message()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the function returns None (returns to the main menu) when "R" is selected
    assert result is None

    # Check if "Under construction!" is not present in the captured output
    assert "Under construction!" not in captured_output

# Test with valid password
def test_valid_password():
    assert check_valid_password("Test123$") == False

# Test with invalid length 
def test_invalid_length():
    assert check_valid_password("Test1") == True
    assert check_valid_password("TooLongPassword") == True

# Test without capital letter
def test_no_capital():
    assert check_valid_password("test123$") == True

# Test without digit  
def test_no_digit():
    assert check_valid_password("TestPassword$") == True

# Test without symbol
def test_no_symbol():
    assert check_valid_password("Test123Password") == True

def test_play_video(capsys, monkeypatch):

    # Mock input to return empty string
    def mock_input(prompt):
        return ""
    
    monkeypatch.setattr('builtins.input', mock_input)

    # Call play_video function
    play_video()
    
    # Capture stdout
    out, err = capsys.readouterr()
    
    # Check output
    assert "Video is now playing." in out
    assert "Press 'enter' to continue." in out

def test_play_video_input(capsys, monkeypatch):

    # Mock input to return "x"
    def mock_input(prompt):
        return "x"
    
    monkeypatch.setattr('builtins.input', mock_input)

    # Call play_video function
    play_video()
    
    # Capture stdout
    out, err = capsys.readouterr()
    
    # Check output
    assert "Video is now playing." in out
    assert "Press 'enter' to continue." in out

# Test to ensure that no more than five jobs can be posted by a user
def test_create_job_max_jobs_per_user(monkeypatch):
    # Ensure the jobs list is empty at the beginning of the test
    jobs.clear()

    # Mock input values
    inputs = ["Software Engineer", "Design software", "Google", "Mountain View", "120,000"]
    def mock_input(prompt):
        return inputs.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)

    # Create a test account
    test_account = Account()
    test_account.create("TestUser", "Test123!", "Test", "User")

    # Set the number of jobs posted by the user to the maximum limit (5)
    for _ in range(5):
        test_account.increment_jobs_posted()

    # Call create_job function
    create_job()

    # Check that no job was added to the list
    assert len(jobs) == 0

    # Debugging output to see the jobs list after the test
    print(jobs)

def test_display_jobs(capsys):

    display_jobs()
    
    out, err = capsys.readouterr()
    
    assert out == "Under construction!\n"
    
if __name__ == "__main__":
    pytest.main()
