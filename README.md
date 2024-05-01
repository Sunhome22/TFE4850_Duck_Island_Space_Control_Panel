# TFE4850_Duck_Island_Space_Control_Panel
Python script for the Raspberry Pi 4B HAT control panel module.
Designed to run with our modified Magic-Sand software. Check this [repository](https://github.com/MartinHeim/TFE4850_Duck_Island_Space). 

## Set-up

Ensure that you have Python3 and Pip installed.
Create a .env file named .dev.env This file needs two variables HOST and PORT, containing whatever host and port you are using.
The modified Magic-Sand software runs on port 11999. 

The file should look something like this:

''
HOST="192.168.x.x"
PORT=11999
''

Then install the required dotenv package by running:

```console
foo@bar:~/TFE4850_Duck_Island_Space_Control_Panel/$ pip install python-dotenv
```


Then you should be all set!
Start the script by running:

```console
foo@bar:~/TFE4850_Duck_Island_Space_Control_Panel/$ python3 control_panel.py
```
