## Functional Requirements
1. Register
2. Login
3. Compose Email
4. requirement
5. requirement
6. requirement
7. requirement
8. requirement
9. requirement
10. requirement
11. requirement
12. requirement

## Non-functional Requirements
1. non-functional
2. non-functional
3. non-functional
4. non-functional

## Use Cases
### Use Case 1: Register
- **Pre-condition:** Assumed on website home page
- **Trigger:** Select register account button
- **Primary Sequence:**
1. User will select “create account”
2. System prompt user to enter username and password
3. User will enter desired username and password
4. User will confirm password
5. User will enter “create account”
- **Primary Postconditions:** User has created an account and has access to email
- **Alternate Sequence:**
1. User enters a username but not a password
a. Prompt user to enter password
2. User passwords don’t match
a. Prompt user that passwords don’t match

### Use Case 2: Login
- **Pre-condition:** Assumed User has an account already
- **Trigger:** Clicking login button
- **Primary Sequence:**
1. User selects “Login” button
2. System prompts user to enter username and password
3. User enters username and password
4. User press “Sign in” button
5. System logs in user to appropriate account page
- **Primary Postconditions:** User is logged into their email page
- **Alternate Sequence:**
1. User doesn’t have account
a. System prompts user that account not found and to make account
2. Username incorrect
a. System prompts user that “username or password incorrect”
3. Password incorrect
a. System prompts user that “username or password incorrect”

### Use Case 3: Compose Email
- **Pre-condition:** User must have an email account.
- **Trigger:** Select “Compose” button
- **Primary Sequence:**
1. User will select “compose email”
2. System prompt user with text box to enter message to send to recipient
3. User will enter recipient email
4. User will enter subject
5. User will select “send email”
- **Primary Postconditions:** User would be able to write and send an email
- **Alternate Sequence:** 
1. User doesn’t enter recipient email
a. System display no recipient is entered
2. User enters an invalid email address
a. System display recipient is not found
3. User forgets to enter subject
a. System displays no subject
4. User doesn’t enter contents of email
a. System displays that email is empty

### Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description> Lorem ipsum dolor sit
amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore
magna aliqua.
- **Trigger:** <can be a list or short description> Ut enim ad minim veniam, quis
nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea
commodi consequatur.
- **Primary Sequence:**
1. Ut enim ad minim veniam, quis nostrum e
2. Et sequi incidunt
3. Quis aute iure reprehenderit
4. ...
5. ...
6. ...
7. ...
8. ...
9. ...
10. <Try to stick to a max of 10 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to
describe multiple issues that may arise>
1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence
to describe multiple issues that may arise>
1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...
2. Use Case Name (Should match functional requirement name)
