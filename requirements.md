## Functional Requirements
1. Register
2. Login
3. Compose Email
4. Delete Email
5. Search Emails
6. Edit User Profile
7. todo list
8. start chat 
9. delete chat
10. requirement
11. requirement
12. requirement

## Non-functional Requirements
1. response time within (x seconds)
2. works on any browser
3. different languages
4. nice UI

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

### Use Case 4: Delete Email
- **Pre-condition:** User must have the email to delete
- **Trigger:** Select the email, click delete
- **Primary Sequence:**
1. User will select email
2. User will then select the delete button
3. System prompt user warning deleting of email
4. User confirms
- **Primary Postconditions:** User would be able to delete an email
- **Alternate Sequence:**
1. User clicks away before confirming to delete the email
2. System would reset and the email remains in inbox

### Use Case 5: Search Emails
- **Pre-condition:** User must be logged in
- **Trigger:** Select "Search" button
- **Primary Sequence:**
1. User will select search email
2. System prompts user to enter keywords
3. System will search through the user's inbox for a match
4. System will display all matches for the keywords
- **Primary Postconditions:** User would be able to find an email with the keywords entered 
- **Alternate Sequence:**
1. User does not enter keywords that are in email
2. System prompts the user that keyword has not been found
- **Alternate Sequence:**
1. User enters a search that is too long
2. System prompts the user that the search is experiencing heavy loading times

### Use Case 6: Edit Profile
- **Pre-condition:** User must be logged in
- **Trigger:** Select "Edit Profile" button
- **Primary Sequence:**
1. User will select edit profile 
2. User is able to change the name, password, profile picture
3. User selects to save changes
- **Primary Postconditions:** User would be able to see the changes to their profile
- **Alternate Sequence:**
1. User does not commit any changes and presses cancel
2. System prompts the user to confirm to cancel
3. User confirms
- **Alternate Sequence:**
1. User changes some information, but does not save and exit to another page
2. System cancels the changes and goes back to the original profile
