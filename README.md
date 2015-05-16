# pydialog

__Command line dialogs made easy.__

## Installation

From github:

```
git clone https://github.com/nicr9/pydialog.git
cd pydialog
sudo python2.7 setup.py install
```

## Examples

First things first, import `Dialog`:

```
from pydialog import Dialog
```

This is used to make a variety of different dialogs for collecting user input.

For example, asking user for a string:

```
d = Dialog("What's your name?")
d.input() # This blocks until user answers

print "Hello %s" % d.result
```

You can also ask the user to choose from a selection:

```
d = Dialog("Which do you prefer?")
d.choose(['cake', 'chocolate'])

print "I like %s too!" % d.result
```

Or maybe you just want the answer to a yes/no question?:

```
d = Dialog("Do you want to quit?")
d.yesno()

if d.result:
    quit()
```

Finally, you can also ask users for passwords. This is like the `Dialog.input()`
method shown above but it doesn't display what the user is typing:

```
d = Dialog("Please enter your password")
d.secret()

sign_in(username, d.result)
```

## Author

Name: Nic Roland<br>
Twitter: [@nicr9_](https://twitter.com/nicr9_)<br>
email: nicroland9@gmail.com
