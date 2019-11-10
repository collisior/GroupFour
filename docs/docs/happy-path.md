# Happy path - everything goes right - Spotify login

1. From web application homepage User presses button 'Get Started'
2. From web application backend {client_id, response_type, redirect_uri, state=None, scope} send to Spotify Accounts Service. 
3. Web application directs user to login using Spotify Account Service. User inputs 'username' and 'password'.
4. After successful login: prompt User to a webpage where he/she can choose to grant you access to their data.
5. User authorizes access to the data sets defined in scopes.
6. After the User grants permission, the Spotify Accounts Service redirects the User back to redirect_uri. The Spotify Accounts Service response includes {access_token, token_type, expires_in, state}.
6. After the authorization code has been received, the URL will contain hash fragment with following data encoded {access_token, token_type, scope, expires_in, state}
7. The access_token will allow web application to make requests to the Spotify Web API


Defintions:
  client_id     : as a registered Spotify Accounts Services developer we get unique Client ID  
  response_type : code  
  redirect_uri  : if user successfully grants permission we redirect to our 'Upload/Take photo' page (where User will be able to take or upload photo for further analysis)  
  scope         : playlist-modify-public, user-library-read  
  grant_type    : authorization_code  
  response_type : "token"  
  expires_in    : time period for which the access token is valid  
  state	        : the value of the state parameter supplied in the request  
  
  
