## Functional Requirements
1. Register (Tyler)
2. Login (Tyler)
3. Compose Email (Tyler)
4. Delete & Flag Email (Liza)
5. Search Emails (Liza)
6. Edit User Profile (Liza)
7. Create todo list (Phillip)
8. Start chat (Phillip)
9. Notes (Phillip)
10. Forgot password (Taehun)
11. Delete todo item/list (Taehun)
12. Contact Form (Taehun)

## Non-functional Requirements
1. response time within (5 seconds)
2. works on any browser
3. read email
4. different fonts

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

### Use Case 4: Delete & Flag Email
- **Pre-condition:** User must have the email in inbox
- **Trigger:** Select the email, click delete or flag
- **Primary Sequence:**
1. User will select email from email
2. User will then select the delete or flag button
3. If deleting email, the system prompts the user warning deleting of email
4. User confirms to delete email
5. If flagging email, system will display highlighted flag on email
6. System puts flagged email at the top of the inbox
- **Primary Postconditions:** User would be able to delete or flag an email
- **Alternate Sequence:**
7. User clicks away before confirming to delete the email
8. System would reset and the email remains in inbox
- **Alternate Sequence:**
9. User misclicks flag icon.
10. System would open the email that was clicked

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
2. System prompts user with fields to change to their profile such as name, username, password, or profile picture
3. User fills in all of the fields they want to change on their account
4. System prompts user to save changes to profile
5. User selects to save changes
- **Primary Postconditions:** User would be able to see the changes to their profile
- **Alternate Sequence:**
6. User does not commit any changes and presses cancel
7. System prompts the user to confirm to cancel
8. User confirms
- **Alternate Sequence:**
9. User changes some information, but does not save and exit to another page
10. System cancels the changes and goes back to the original profile

### Use Case 7: Create To-Do List
- **Pre-condition:** user already signed in
- **Trigger:** User selects "create todo list" button
- **Primary Sequence:**
1. User will select “todo list”
2. System prompts user to name list
3. User will enter todo list name
4. System prompt user to enter todo list item
5. User will enter todo list item
6. System prompts user to save todo item
- **Primary Postconditions:** User will be able to see their created todo list
8. User can click on delete to remove finished task
- **Alternate Sequence:**
9. User doesn’t save todo item
- **Alternate Sequence:**
11. User wants to add todo lists on to existing list
12. Prompt user with add button

### Use Case 8: Start chat
- **Pre-condition:** user already signed in
- **Trigger:** select "start chat" button
- **Primary Sequence:**
1. User will select "chat"
2. system prompts the user to enter the recipient's name
3. User enters recipient name
4. System prompts user to enter short message to other user
5. user enters short message
6. System prompts user with send button
7. User clicks send to send chat message
- **Primary Postconditions:** User chat message is sent to other user
- **Alternate Sequence:**
8. User does not enter any chat message
9 Prompt user chat box is empty

### Use Case 9: Notes
- **Pre-condition:** user is already signed in
- **Trigger:** click on note button for notes application
- **Primary Sequence:**
1. User clicks on note in nav bar
2. User clicks onto an empty field.
3. User can input the subject of the note and the note itself
4. User confirms by clicking on enter
- **Primary Postconditions:** creates the notes
1. User can click on delete note to delete it
- **Alternate Sequence:**
1. Text field is empty
2. prompts user to enter all required info
- **Alternate Sequence:**
3. User doesn't confirm by hitting enter
4. prompts user note is not saved

### Use Case 10: Forgot password
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

### Use Case 11: Delete Todo List
- **Pre-condition:** User aleady signed up and have an existing account in the system
- **Trigger:** Clicks "delete todo list/item"
- **Primary Sequence:**
1. User will select "delete todo list/item".
2. System prompt user select item or todo list to delete
3. User press list or item they want to delete
4. System prompt user to confirm change
5. User will confirm change
- **Primary Postconditions:** User is able to see todo list/item delted
- **Alternate Sequence:**
6. User doesn't save change
7. System prompts user that change has not been saved

### Use Case 12: Contact Form
- **Pre-condition:** User aleady signed up and have an existing account in the system
- **Trigger:** Clicks "Contact Us"
- **Primary Sequence:**
1. User will select "Contact Us"
2. System prompt user to enter information.
3. User inputs information
4. System will propmt user with message of confirmation
5. User will confirm delete contact
- **Primary Postconditions:** Contact form is sent
- **Alternate Sequence:**
6. User doesn't confirm sending contact form
7. System prompts user that contact form has not been sent
- **Alternate Sequence:**
8. User doesn't enter all required info
9. System prompts user to enter all required info




