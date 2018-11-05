Tasty Shapes With Friends
=========================

A tiny SaaS for sharing song links with your friends over a common stream.

About
-----

`tswf` is a api interface for interacting with a queue that serves as a
playlist for an rtmp streaming worker:

* `api` serves the flask routes for interacting with the queue
* `nginx` routes to the api, and serves the rtmp endpoint as well
* `player` plays song links submitted to the queue by calling the api

The API
-------

The API is simple.

```
/submit?song=<urlencoded song link>  <-  submit a song to the queue
/stat			      	     <-  the length of the queue
/queue				     <-	 the queue
/clear				     <-  in case of emergencies
/next				     <-  used by player (and assholes)
```

Getting Started
---------------

This project is intended to be run with docker-compose.

To build the containers, travel into their directory and type:

``` docker build -t <name> . ```

after you've build all of the containers you can start them all
up with:

``` docker-compose up ```

If things worked as intended, you should see the player attempt
to grab a song from the queue immediately.

Built With
----------

* [Flask](http://flask.pocoo.org/)
* [youtube-dl](http://rg3.github.io/youtube-dl/)
* [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)
* [nginx](www.nginx.com)
* [docker](www.docker.com)

Contributing
------------

 1. **Fork** the repository
 2. **Clone** the project from your forked repository to your macine
 3. **Commit** changes to your own branch
 4. **Push** your changes on your branch to your forked repository.
 5. Submit a **Pull request** back to our repository for review.

**NOTE**: always merge from latest upstream before submitting pull requests.

Versioning
----------

[Semantic Versioning](https://www.semver.org/) is used to version this project.
Please consult the [releases](https://github.com/AHEAD-MSP/dashboard/releases)
page for a complete list of available versions.

Authors
-------

* [Patrick Delaney](https://github.com/ptdel)

License
-------

`soon`