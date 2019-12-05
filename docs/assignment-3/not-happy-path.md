# Fail path - Failed Spotify login

Spotify don't respond

1. From web application homepage User presses button 'Get Started'
2. From web application backend {client_id, response_type, redirect_uri, state=None, scope} send to Spotify Accounts Service.
3. Spotify Accounts Service do not respond, set back to homepage with message included 'Sorry, try later :("

User denies access

1. From web application homepage User presses button 'Get Started'
2. From web application backend {client_id, response_type, redirect_uri, state=None, scope} send to Spotify Accounts Service.
3. Web application directs user to login using Spotify Account Service. User inputs 'username' and 'password'.
4. After successful login: prompt User to a webpage where he/she can choose to grant you access to their data.
5. User authorizes access to the data sets defined in scopes.
6. After the User denies access to scopes included. The Spotify Accounts Service will get final URL containing following parameters {error, state}. Here, error = "access_denied".
7. Redirect User to web application homepage.



Defintions:  
client_id     : as a registered Spotify Accounts Services developer we get unique Client ID  
response_type : code  
redirect_uri  : if user successfully grants permission we redirect to our 'Upload/Take photo' page (where User will be able to take or upload photo for further analysis)  
scope         : playlist-modify-public, user-library-read  
grant_type    : authorization_code  
response_type : "token"  
state	        : the value of the state parameter supplied in the request  
  
  
