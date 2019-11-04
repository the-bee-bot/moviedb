MMDB-MyMovieDatabase
====================
A simple python commandline application to generate web page to show favorite movies from available Movie objects list.
This can also be used as an command line to add their own favorite movies to the list.

Requirements:
-------------
*   Python3 executable needs to be in the PATH.

How To run:
-----------
*   python movie_db.py [-option]
*   Both options and args are optional.
    If the script is run without any arguments it will simply create a html file and will open that in a browser.

Commandline options:
---------------------
    -sw :  to switch database option. Database needs to be enabled before adding additional movies to list.
    -a  :  option to add movies to the database in interactive mode.
    -d  :  option to delete one or more movies from the database.
