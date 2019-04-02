I recommend using `pip` alongside [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io) to manage the install process.

To create a new virtual enviornment, then, you can use:
`mkvirtualenv -a [SRC_DIRECTORY] -r requirements.txt aohg_site`


The following environment variables are used to configure local versus product installs:

 - `PROJECT_HOME`
 - `DATABASE_NAME`
 - `DATABASE_USER`
 - `DATABASE_PASSWORD`
 - `SECRET_KEY`
 - `STATIC_ROOT`



