# dialog

__Command line dialogs made easy.__

## Installation

From github:

```
git clone https://github.com/nicr9/dialog.git
cd dialog
sudo python2.7 setup.py install
```

## Examples

First things first, import `Dialog`:

```
from dialog import Dialog
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
