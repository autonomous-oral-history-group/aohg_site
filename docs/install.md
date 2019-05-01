# Installing Python
If you're on a mac, I recommend using [homebrew](http://brew.sh) to install `python2.7` and `ffmpeg`

`brew install python2.7 ffmpeg`

# Installing dependencies

I recommend using `pip` alongside [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io) to manage the install process.

To create a new virtual enviornment, then, you can use:
`mkvirtualenv -a [SRC_DIRECTORY] -r requirements.txt -p [POINT TO YOUR PYTHON2.7] aohg_site`

One trick is to use `which` to find your installed version of Python
`mkvirtualenv -a [SRC_DIRECTORY] -r requirements.txt -p $(which python2.7) aohg_site`

The following environment variables are used to configure installs. I recommend putting them in the settings module.

 - `DJANGO_SECRET`
 - `DATABASE_NAME`
 - `DATABASE_USER`
 - `DATABASE_PASSWORD`

`DJANGO_SETTINGS_MODULE` should equal `django_project.settings.local` on a local install, and `django_project.settings.production` on production. Easy!

If you want to use [django-admin](https://docs.djangoproject.com/en/1.11/ref/django-admin/), you need to add the first `django_project` directory to your Python path. If using `virtualenvwrapper`, you can do that with the [`add2virtualenv` command](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html#add2virtualenv). Not required.

# Install django-audiofield

[django-audiofield](https://github.com/areski/django-audiofield) is installed as a git [submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules), it seems like the annoying thing will be [cloning](https://git-scm.com/book/en/v2/Git-Tools-Submodules#_cloning_submodules) with this approach. Sorry! Might refactor if it's a pain. As of writing, I'll be trying to install [version 0.9.2](https://github.com/areski/django-audiofield/releases/tag/v0.9.2).

on init: 
`git submodule update --init --recursive`

`git pull --recurse-submodules`
'git submodule update --recursive --remote` is used to update

According to django-audiofield, it depends on:
 - `libsox-fmt-mp3` : (which I'm hoping is just [SoX](https://arielvb.readthedocs.io/en/latest/docs/commandline/sox.html)
 - `libsox-fmt-all` : same
 - `mpg321` : trying `brew install mpg321`
 - `dir2ogg` : trying `brew install dir2ogg` didn't work, here's the [github](https://github.com/julian-klode/dir2ogg)
 - `libav-tools` : `brew install libav`


In order to get `django-audiofield` playing nice with `django-storages`, I commented out a couple methods in the `django-audiofield` install, as [mentioned in a comment here](https://github.com/areski/django-audiofield/issues/21).


# Production installs

Using the [DigitalOcean one click install](https://www.digitalocean.com/products/one-click-apps/django/), environment variables should be set using [systemd Environment directives](https://coreos.com/os/docs/latest/using-environment-variables-in-systemd-units.html)

## Setting environment variables
There are a few more environment variables that need to be defined in Production to [django-storages](https://django-storages.readthedocs.io/en/latest/backends/digital-ocean-spaces.html) to play nicely with [Digital Ocean Spaces](https://www.digitalocean.com/docs/spaces/) (their equivalend of Amazon S3, which S3 also supports):

```
Environment=DJANGO_SECRET_KEY=SECRET_KEY
Environment=DATABASE_NAME=DB_NAME
Environment=DATABASE_USER=DB_USER
Environment=DATABASE_PASSWORD=DATABASE_PASS
Environment=DJANGO_SETTINGS_MODULE=django_project.settings.production 
Environment=AWS_ACCESS_KEY_ID='ACCESS_ID_HERE'
Environment=AWS_SECRET_ACCESS_KEY='SECRET_KEY_HERE'
Environment=AWS_STORAGE_BUCKET_NAME=XXX
Environment=AWS_S3_REGION_NAME=sfo2
Environment=AWS_S3_ENDPOINT_URL=https://sfo2.digitaloceanspaces.com
Environment=AWS_S3_CUSTOM_DOMAIN=XXX.sfo2.digitaloceanspaces.com
```

These should be set in `/etc/systemd/system/gunicorn.service`.

Once you change these, enter the command:
`systemctl daemon-reload && systemctl restart gunicorn`

In retrospect, a Docker image would've been a little easier to spin up.
