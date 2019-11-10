## Architecture

The architecture that we are using for our Web application is MVC with Microservices. We will use client-to-microservice communication architecture because when the User uses web application Controller, where Model (Backend) will make requests directly to Spotify and Azure microservices only when User needs them. View will be updated once the service is done. 


## Platform decision


We are using Python Flask to call the APIs for a more secure access for the user by holding the sensitive data on the backend like tokens. Since we are using Spotify API, there a great Python library created for developers that is called Spotipy that eases the use of Spotify Web API (compared to Node.JS, Perl, Java or .NET). Moreover, Flask provides us a powerful tool called “template”, which takes care of the general page structure for the playlists that we need to generate. This really would save us a lot of time as we probably would have thousands of playlists with similar layout.
