Tasty Shapes With Friends
=========================

A tiny SaaS for sharing song links with your friends over a common stream.

About
-----

`tswf` is a api interface for interacting with a queue that serves as a
playlist for an rtmp streaming worker:

* `api` serves the flask routes for interacting with the queue
* `player` plays song links submitted to the queue by calling the api

The API
-------

The API is simple, with more functionality on the way as time permits.

```
/submit?song=<urlencoded song link> <-  submit a song to the queue
/stat                               <-  the length of the queue
/queue                              <-	the queue
/clear                              <-  in case of emergencies
/next                               <-  used by player (and assholes)
/current                            <-  currently playing URL
/skip?username=<username>           <-  Vote to skip song
```

Getting Started
---------------

This project is intended to be run with docker-compose. Depending on
what operating system you are using, you may want to grab it from your
package manager, or directly from upstream.

for the `api` and `player` containers, you should be able to simply
change into their directories, and run:

``` docker build -t <name> . ```

after you've build all of the containers you can start them all
up with:

``` docker-compose up -d```

(You can leave off the `-d` if you want it to run in the tty.)

## NGINX

It's assumed that the API and Player are sitting behind NGINX.
Included in this repository are example `api.conf` and `rtmp.conf`.
The `api.conf` should be included within the `http` block of your
`nginx.conf`, with `rtmp.conf` under it's own block.  An example
`nginx.conf` is provided below:

```
user  nginx;
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    ssl on;
    ssl_session_cache	shared:SSL:10m;
    ssl_session_timeout	10m;
    ssl_session_tickets	off;
    
    sendfile        on;
    keepalive_timeout  70;
    include /etc/nginx/conf.d/api.conf;
}

include /etc/nginx/conf.d/rtmp.conf;
```
NGINX needs to be built with the RTMP Module in order to serve
player content.  Compile NGINX with the following `./configure`
flag:
```--add-module=/path/to/nginx-rtmp-module```

If you are running NGINX on another host, you will need to modify
`api.conf` and `rtmp.conf` to point to the address of the NGINX
host, rather than localhost (127.0.0.1).

If things worked as intended, you should see the player attempt
to grab a song from the queue immediately.

Built With
----------

* [Flask](http://flask.pocoo.org/)
* [youtube-dl](http://rg3.github.io/youtube-dl/)
* [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)
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
* [Powtrak](https://github.com/powtrak)

License
-------

`soon`

Acknowledgements
----------------
[verboten](https://www.github.com/d3d1rty/verboten) the IRC bot currently
serving as the DJ for the live version running among friends. Written by
[d3d1rty](https://www.github.com/d3d1rty)
