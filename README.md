# Wiki

The page covers development and operational info for _Zibenitis_ web page project.

### Git

Send your SSH public (not private!) key to Kaspars (gmail)

<pre>
cat .ssh/id_rsa.pub
</pre>

Set your name and email before committing any code

<pre>
git config --global user.name "Your Name"
git config --global user.email "your.email@example.net"
</pre>

Clone git repos, you shall have all rights to pull/push

<pre>
git clone git@git.zibenitis.se:repos/zibenitis
</pre>

### Production

http://zibenitis.se/

#### Server requirements
sudo apt-get install ruby-full
sudo su -c "gem install sass"

## Dev (development)

### Languages/Frameworks

* Python 3+ (python-pip3). run "pip3 install -r requirements.txt"
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