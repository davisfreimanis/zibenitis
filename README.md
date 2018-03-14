# Wiki

The page covers development and operational info for _Zibenitis_ web page project.

### Git

Add your SSH public key to Github

<pre>
~/.ssh/id_rsa.pub
</pre>

Set your name and email before committing any code

<pre>
git config --global user.name "Your Name"
git config --global user.email "your.email@example.net"
</pre>

Clone git repos, you shall have all rights to pull/push

<pre>
git clone git@github.com:davisfreimanis/zibenitis.git
</pre>

### Production

http://zibenitis.se/

#### Set up
* Install python3
* Install pip3 `sudo apt-get install python3-pip`
* Install pip modules `sudo pip3 install -r requirements.txt"`
* Install node with nvm
* Install yarn
* Install yarn dependencies

* Run migrations `python3 manage.py makemigrations` and `python3 manage.py migrate`
* Generate stylesheets `scss static-loc/scss/style.scss static-loc/style.css`

* Add latvian locale to be able to sort names `sudo locale-gen "lv_LV.utf8"`

* Create a local superuser to use adminpanel `python3 manage.py creatsuperuser`

##### Add SECRET_KEY file
Create a new file called `secret_key` in the same folder as settings.py and add the secret key. Ask Davis

## Dev (development)

### Languages/Frameworks

* Python 3+ (python-pip3)
* Django 1.9 (Back-end)
* HTML 5
* SCSS
* Bootstrap 3 (Front-end)

### Some useful tools

* PyCharm (IDE for Python and Django)
* Sublime text (Text editor)
* SourceTree (GUI for git)
* DB Browser for SQLite (SQLite browser)

### Useful links

* Python documentation - https://docs.python.org/3/
* Python tutorial - https://docs.python.org/3/tutorial/index.html
* Django documentation - https://docs.djangoproject.com/en/1.7/
* Django tutorial - https://docs.djangoproject.com/en/1.7/intro/tutorial01/
* Git for total beginners - https://try.github.io/levels/1/challenges/1
* Git more advanced - http://git-scm.com/book/en/v2
* Interactive programming tutorials - http://www.codecademy.com/learn
