# Discover Movies!
### *A web-app to discover 10 most popular movies by year & genre.*


## Usage
* Goto to [http://35.243.142.43](http://35.243.142.43).
* Use the sidebar form to select genre & enter year.
* Press *Arrow* icon to submit.
* A list of 10 most popular movies appears on the page. Each listing contains:
  - The title
  - Poster image
  - An overview of the plot
  - And, a link to the imdb page of the movie (opens in a new tab)


## Implementation
The app has been deployed on a public cloud server accessible through the web. Details:

* A VM instance running *Debian Linux* was created using *Google Cloud Compute Engine* service.
* [*Bottle*](https://bottlepy.org/docs/dev/tutorial.html), a lightweight WSGI micro web-framework for Python was used along with *apache* webserver using *wsgi* integration. At a high-level, following steps were carried out:
  - install packages (use: *sudo apt install <pkg-name>*): apache2, libapache2-mod-wsgi-py3, libapache2-mod-wsgi
  - install python packages (use: *pip install <pkg-name>* & *pip3 install <pkg-name>*): bottle, requests
  - Create new directory under /var/www: *mkdir /var/www/myapp*
  - Create new *VirtualHost* entry in apache conf (*make a new .conf file in "sites-enabled" conf directory and paste below content*):
```
<VirtualHost *>
    WSGIDaemonProcess myapp user=<replace_your_username_here> group=www-data processes=1 threads=5
    WSGIScriptAlias / /var/www/myapp/app.wsgi
    <Directory /var/www/myapp>
        WSGIProcessGroup myapp
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>
```
 - Restart apache server
 - Now, *Bottle* app can be deployed used *wsgi* integration with *apache*, see [link](https://bottlepy.org/docs/dev/deployment.html#apache-mod-wsgi)

* A free API service hosted by [themoviedb.org](https://www.themoviedb.org/documentation/api) (requires key-based authentication) was used to fetch list of movies based on user input.

## Bugs / Issues:
* User input is not sanitised / validated.
* The API service is rate-limited, which leads to error in case of frequent user requests.
