# PAT8

	<h2>Server Setup</h2>

	<h3>python modules to install</h3>
	sudo apt-get install python-visual sudo apt-get install python-matplotlib
	<br>sudo apt-get install python-numpy
	<br> sudo apt-get install python-scipy
	<br>sudo apt-get install python-jinja2
	<br>sudo apt-get install python-pip
	<br>sudo pip install mpld3


	<h2>Library Versions</h2>
	Ubuntu 14.04 provides numpy version 1.8.2 and scipy version 0.13.3. Some optimization examples require at least scipy
	0.14. To upgrade: sudo apt-get install libatlas-base-dev gfortran python-pip sudo pip install --upgrade numpy sudo pip
	install --upgrade scipy


	<h3>Folder Configurations</h3>
	give www-data user write access
	<br>
	<br>
	<a href="http://askubuntu.com/questions/244406/how-do-i-give-www-data-user-to-a-folder-in-my-home-folder">http://askubuntu.com/questions/244406/how-do-i-give-www-data-user-to-a-folder-in-my-home-folder</a>
	<br>
	<br> usermod -a -G www-data (your username)
	<br>
	<br> chgrp www-data /home/myuser/folderA
	<br> chmod g+rwxs /home/myuser/folderA
	<br>
	<a href="http://stackoverflow.com/questions/29331872/ioerror-errno-13-permission-denied">http://stackoverflow.com/questions/29331872/ioerror-errno-13-permission-denied</a>
	<br> chmod 777 /var/www/path/to/file (may have to delete file if it already exists and belongs to a different
	user)
	<br>
	<br>
	<br>
	<br>
	<br> Using matplotlib on web server
	<br>
	<a href="http://matplotlib.org/faq/howto_faq.html#matplotlib-in-a-web-application-server">http://matplotlib.org/faq/howto_faq.html#matplotlib-in-a-web-application-server</a>
	<h2>Development</h2>
	If a Python application does not work, try to run it in a terminal. This will give you the detailed error messages.
	Sometimes, a library is not installed.




