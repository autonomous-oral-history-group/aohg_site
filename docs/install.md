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

`DJANGO_SETTINGS_MODULE` should probably equal `django_project.settings` if you want to use [django-admin](https://docs.djangoproject.com/en/1.11/ref/django-admin/). Not required.

# Install django-audiofield

[django-audiofield](https://github.com/areski/django-audiofield) is installed as a git [submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules), it seems like the annoying thing will be [cloning](https://git-scm.com/book/en/v2/Git-Tools-Submodules#_cloning_submodules) with this approach. Sorry! Might refactor if it's a pain. As of writing, I'll be trying to install [version 0.9.2](https://github.com/areski/django-audiofield/releases/tag/v0.9.2).


According to django-audiofield, it depends on:
 - `libsox-fmt-mp3` : (which I'm hoping is just [SoX](https://arielvb.readthedocs.io/en/latest/docs/commandline/sox.html)
 - `libsox-fmt-all` : same
 - `mpg321` : trying `brew install mpg321`
 - `dir2ogg` : trying `brew install dir2ogg` didn't work, here's the [github](https://github.com/julian-klode/dir2ogg)
 - `libav-tools` : `brew install libav`
