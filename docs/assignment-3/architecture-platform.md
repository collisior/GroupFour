## Architecture

The architecture that we are using for our Web application is MVC with Microservices. We will use client-to-microservice communication architecture because when the User uses web application Controller, where Model (Backend) will make requests directly to Spotify and Azure microservices only when User needs them. View will be updated once the service is done. 


## Platform decision


We are using Python Flask to call the APIs for a more secure access for the user by holding the sensitive data on the backend like tokens. Since we are using Spotify API, there a great Python library created for developers that is called Spotipy that eases the use of Spotify Web API (compared to Node.JS, Perl, Java or .NET). Moreover, Flask provides us a powerful tool called “template”, which takes care of the general page structure for the playlists that we need to generate. This really would save us a lot of time as we probably would have thousands of playlists with similar layout.

Although Node.js is also a programming language, which is known for providing a basic functionality for web developing. The syntax of the language is harder to get familiar with. Moreover, compared with Python, Node.js is still a young language, and its library is not as mature and stable as Python’s. Therefore, we chose to use Flask rather than Node.JS considering that we can gain more support from the community if we encounter any problem. In addition, given Spotipy already in there to take care our access to Spotify API.
