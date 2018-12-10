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

The API is simple, with more functionality on the way as time permits.

```
/submit?song=<urlencoded song link> <-  submit a song to the queue
/stat                               <-  the length of the queue
/queue                              <-	 the queue
/clear                              <-  in case of emergencies
/next                               <-  used by player (and assholes)
```

Getting Started
---------------

This project is intended to be run with docker-compose. Depending on
what operating system you are using, you may want to grab it from your
package manager, or directly from upstream.

for the `api` and `player` containers, you should be able to simply
change into their directories, and run:

``` docker build -t <name> . ```

the `nginx` container has two extra steps to build:

generate a dhparams file with the following command

``` openssl dhparam -out dhparam.pem 4096 ```

It's going to take a little bit.

After it's done create a self-signed certificate and private key:

``` openssl req -newkey rsa:4096 -keyout cert.key -x509 -days 365 -out cert.pem -nodes ```

Once you have these three things, the cert.key, cert.pem, and dhparams.pem, make a
`keys` directory and move put that into the `nginx` directory:

``` mkdir keys/; mv cert.key cert.pem dhparams.pem keys/; mv keys/ nginx/ ```

Now the `nginx` container is good to be built in the same fashion as the other two.

after you've build all of the containers you can start them all
up with:

``` docker-compose up -d```

(You can leave off the `-d` if you want it to run in the tty.)

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

[Semantic Versioning](https://www.semver.org/) will be used to version this project.
Please consult the [releases](https://github.com/AHEAD-MSP/dashboard/releases)
page for a complete list of available versions.

Authors
-------

* [Patrick Delaney](https://github.com/ptdel)

License
-------

`soon`

Acknowledgements
----------------
[verboten](https://www.github.com/d3d1rty/verboten) the IRC bot currently
serving as the DJ for the live version running among friends. Written by
[d3d1rty](https://www.github.com/d3d1rty)
