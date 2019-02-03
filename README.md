## Inspiration

After attending the Docker workshop run by David, we were determined to build a solution which would solve his guests' arcade machine accessibility problem. So we built a mobile friendly, playable, cloud-powered, event-driven, TLS secure, serverless application to allow users to easily play arcade games.

## What it does

The application allows the user to launch retro arcade games inside the MAME arcade game emulator from their phone, without having to worry about any configuration details. The user simply visits the website, taps a game, and plays to their heart's content.

## How we built it

### Architecture

![The Archicecture](https://i.imgur.com/hdqF3fZ.png)

The applicaiton is divided into three primary components.

1. Web-app mobile frontend (Hosted on GCP Compute Engine)
    * Presents user with mobile-friendly UI for selecting which title to play
2. Python3 arcade machine listener
    * Listens for commands to play and change games
3. Google Cloud Platform Serverless Function
    * Links web-app frontend and python3 listener via GCP Storage

### Backend

The Backend is built entirely on Google Cloud Platform.

Typical control-flow looks like this:

1. The user taps their favorite game on the webapp, triggering the serverless function to update the GCP Storage object.
2. The arcade machine listener polls the GCP Storage object every 4 seconds.
    1. If the title has changed, or if the server has just started, the listener kills the current game process and runs the newly selected game.

### Frontend

* Frontend is built on HTML5, CSS (Bootstrap) and JavaScipt (JQuery).
* Bootstrap was used for the Carousel with the game titles and for the Game Menu. 
* We used jQuery for on click function to send request to start game process on the game icon click.

## Challenges we ran into

SO. MUCH. SALT.

1. GCP Serverless Functions have less than optimal logging capabilities. (Can't write directly to log?!?!)
2. GCP Serverless Functions are not syntactically consistent.
```python
blob.cache_control = "no-cache" # Set piece of metadata as field
blob.upload_from_filename(source_file_name, content_type="text/html") # Set piece of metadata as function argument
blob.make_public() # Set metadata by calling function on blob
# W. T. F.
```
3. Apparently there is a difference between http arguments and http parameters. Firefox and Postman seem to disagree on the precise definitions of both of those terms.
4. Didn't have previous experience with Bootstrap nor with jQuery, had to figure out how to use both of them to get the front end working.

## Accomplishments that we're proud of

* Actually wrote a 'functioning' GCP serverless function!
* Met every requirement in the NotBinary challenge!

## What we learned

* Python can be pain 
* Python on GCP is worse
* Python on GCP *serverless* is hell

* It is possible to make a decent enough MVP in a 24 hours

## What's next for Quick and Dirty Arcade System

* Hopefully some modifications by David, making it better (websockets?) and getting it to run on the actual arcade box (which we understand runs Windows.)

## Acknowledgements

* Frontend menu carousel referenced from W3School, https://www.w3schools.com/bootstrap4/bootstrap_carousel.asp

* Thanks to Sam Machin for his help in debugging our GCP Serverless function.
