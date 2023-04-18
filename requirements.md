## Functional Requirements
1. Register (Tyler)
2. Login (Tyler)
3. Compose Email (Tyler)
4. Delete Email (Liza)
5. Search Emails (Liza)
6. Edit User Profile (Liza)
7. todo list (Phillip)
8. start chat (Phillip)
9. delete chat (Phillip)
10. flag email (Taehun)
11. Forgot password (Taehun)
12. Read email (Taehun)

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
- **Alternate Sequence:**
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
- **Alternate Sequence:**
2. Username incorrect
a. System prompts user that “username or password incorrect”
- **Alternate Sequence:**
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
- **Alternate Sequence:**
2. User enters an invalid email address
a. System display recipient is not found
- **Alternate Sequence:**
3. User forgets to enter subject
a. System displays no subject
- **Alternate Sequence:**
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

### Use Case 7: Create To-Do List
- **Pre-condition:** user already signed in
- **Trigger:** User selects "create todo list" button
- **Primary Sequence:**
1. User will select “create todo list”
2. System prompt user to enter todo list item
3. User will enter todo list item
4. System prompts user to save todo item
- **Primary Postconditions:** User will be able to see their created todo list
6. System will order items based on sequential order
7. User checks off item when done
- **Alternate Sequence:**
8. User doesn’t save todo item
9. Prompt user todo item has not been saved
- **Alternate Sequence:**
10. User wants to add todo lists on to existing list
11. Prompt user with edit list button
- **Alternate Sequence:**
13. User wants more than one todo list
14. User is able to create a new list by hitting the "create todo list" again

### Use Case 8: Start chat
- **Pre-condition:** user already signed in
- **Trigger:** hover over chat and click on it
- **Primary Sequence:**
1. User will select a chat to create
2. system prompts the user to enter the recipient's name
3. system prompts the user a chat interface
- **Primary Postconditions:** User is able to interact with a chat window
1. User can see each person they are chatting to
- **Alternate Sequence:**
1. User does not have any contacts to start chatting with
2. Prompt user chat cannot be created

### Use Case 9: Delete Chat
- **Pre-condition:** user has a chat created
- **Trigger:** hover over chat and click on it
- **Primary Sequence:**
1. User is able to delete a chat 
2. system prompts user if they want to delete the chat
3. system prompts the user with a confirmation
- **Primary Postconditions:** User is able to delete the chat window
1. User can see the deleted chat
- **Alternate Sequence:**
1. User does not have any contacts to start chatting with
2. Prompt user chat cannot be deleted

### Use Case 10: Flag email
- **Pre-condition:** User aleady signed in and have at least one email in inbox
- **Trigger:** Click flag icon
- **Primary Sequence:**
1. User will select an email to flag
2. User will click on flag icon
3. System will then light up the flag icon
4. System will put the flagged email to the very top of inbox
- **Primary Postconditions:** User is able to mark particular emails
- **Alternate Sequence:**
1. User misclicks flag icon.
2. System would open the email that was clicked

### Use Case 11: Forgot password
- **Pre-condition:** User aleady signed up and have an existing account in the system
- **Trigger:** Clicks forgot password button
- **Primary Sequence:**
1. User will select "forgot password" in the log-in page.
2. System prompt user to enter username
3. System will search dictionary of usernames for match
4. A match will have user change password
5. User will enter a new passowrd and re-enter the new password to confirm
6. System will update the account with the new password
- **Primary Postconditions:** User is able to update the account with a new password
- **Alternate Sequence:**
1. User enters an incorrect username 
2. System prompts user that the incorrect username is not found

### Use Case 12: Read email
- **Pre-condition:** User aleady signed up and have at least one email in inbox
- **Trigger:** Clicks an unread email with bold letter
- **Primary Sequence:**
1. User selects an unread email to read in inbox
2. User clicks on the title of the unread email
3. System will open the email and show the message of the selceted email 
- **Primary Postconditions:** System will display the message of email and change the title of the email from bold letter to normal letter
- **Alternate Sequence:**
1. User misclicks on a flag icon
2. System will light up the flag icon
3. System will display the flagged email to the very top of email list


