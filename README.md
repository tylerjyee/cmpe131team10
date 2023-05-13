# CMPE 131 Team 10 
### Team Members
- Tyler Yee (@tylerjyee) - Team Lead
- Liza Podkamenna (@lizapodk)
- Taehun Lee (@taehunleee5)
- Phillip Gee (@phillipgeezus)

### Title: Email and Chat Website

### Ethical Implications
When creating a website that is available for the public to use, it poses challenges such as privacy and security of information. In today’s society, there is no hard line of what is private anymore since technology has evolved and retains information well. User’s privacy is extra important to us since we are building an email and chat website. Within the website, users would be able to interact with our site and possibly enter information that is sensitive which pertains specifically to each individual user. Some of this information can be as simple as a username or something more significant such as a password. Even the content inside emails and chat messages include private information. But to keep this information and the user safe, we are using an internal database that holds all of this information. For security reasons, the information is only able to be accessed by members who manage and build the website. If this website was built for use on a global scale, security efforts would be even greater. Usually they would employ multi-factor authentication or security questions to heighten the security level ensuring only the user has the ability to access their account. But with these features, comes a price to implement and maintain another system to handle this additional sensitive set of data. This usually comes at the price of having more servers to hold this information. But there also shouldn’t be a price on how valuable information is which is why servers have limited access to prevent security risks. Environmentally the more servers that are used, it also requires more space to place them. Besides power consumption, servers don’t require more maintenance as they can usually be maintained and monitored over the air. Although there are some challenges in place, these are usually pushed aside in order to prioritize the user experience and security. And though our website cannot do all of these things, professionally as a group we strive to be the best we possibly can be when it comes to lowering any risk in our website.

### Implementation
Communication is a big part of our world today since we normally work with other people. Our website allows a user to send and recieve emails within an internal system to other users. In order for a user to use our website, they would need to make an account and it would then give them access to our website. Besides sending snd recieving emails, the user is able to send chat messages and create a todo list.

For our webpage we used Python 3, Flask, Flask Forms, Flask Login, SQL Alchemy, and HTML

### Instructions
- First create an account or login
- Once you create an account you will be brought to our home page
- From the home page you can access features such as chat, email, contact us, todo list, delete account and logout via buttons on navigation bar
- Each of the different features will bring you there specific webpage considing of different forms and inputs
- Once you are done with using our webpage, you can logout of your account via the logout button
- Upon logging out, the login page will appear
- If you have account already and forgot your password, you can retreive your password by filling out the form in the login page

### Responsiblities
- Login, Logout, Create User(Register Account), Delete Account: Taehun
- Compose Email, Forgot password, Delete todo item/list, Contact Form: Tyler
- Delete & Flag Email, Search Emails, Edit User Profile: Liza
- Create todo list, Chat, Notes: Phillip
