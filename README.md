# Deluge-Directory-Search

This is a python script solves an issue many might not run into.
I HIGHLY recommend you do not run this in your files if you don't have any current issues with missing files in
your SONGS, SYNTHS, or KITS.

PLEASE BACKUP YOUR SONGS, SYNTHS, and KITS .XML files.
This script worked for me but I will not be held resposible for any changes to files that lead to
unintended results. If this does happen please add a bug or issue to my github at:
https://github.com/Blazaca/Deluge-Directory-Search
Your SAMPLES folder will be completely untouched and is only used as reference for the python script.

(At this very moment the program WILL search for files in all of the directories in SAMPLES and grab the FIRST
match it finds. Whether it's the correct file or not it will modify the synth preset or kit preset to that
sample. For good file structure and general directory cleanliness I recommend always importing files into
any type of DAW or hardware unit with UNIQUE names that can but not always include note, source of audio,
short description, etc... This helps with not only identifying a single .wav file from potentially 50+ files
but when searching for files computers can more easily give you specific results. 
"moog_one_poly_sqr_C3.wav", "chocolate_hitting_floor.wav", "dusty_piano_slam.wav", or "linndrum_kick.wav"...
A good tip for when you get a new sample pack is to find and replace on all files in a new drum folder
and add "linndrum" before every word. Also if you have more than 3 nested folders like:
SAMPLES/synths/dx7/preset_2/recent_edits/noisey_boy.wav
C'mon. Really. This can be refactored easily by putting some of this in the name or just put a 2 by it.)

TL:DR
Script will grab first file it sees in decending order and assign it to matching sample name for preset without exception
example: Synth Preset 1 w/ sample "chocolate_hitting_floor.wav" will grab the first "chocolate_hitting_floor.wav"
Also script will not read past 4 folders. I made this go a little past my own use case for others.
example: SAMPLES/synths/dx7/preset_2/chocolate_square_2.wav
Samples/ then synths/ then dx7/ then preset_2/ finally chocolate_sqaure_2.wav
Anything past that will be ignored. If there is more of a demand for deeper folder searching,
I will work on it in my spare time.

After a preset is made in either SYNTH or KIT mode when the preset is loaded
'FILE' will flash promptly which gives the first hint that your preset sample directory is wrong.
After trying to play the synth or kit if nothing plays this is the biggest flag.
If there is a case where only 1-5 of your presets are missing that may of been a minor mistake and
I highly recommend just remaking the synth unless you are dying to try the tool.
Again BACKUP YOUR DATA except for SAMPLES.

Anyways. If you'd like to take a stab at potentially fixing your files here are the things you will need...

Python 3.9
(When installing python you'll need to make sure the add to bash box is checked)

This version of python from my knowledge has:
Regular Expressions
Pathlib
OS

All important libraries needed to edit the files.
If you get 3.9 don't worry they will be included.

(You may want to make these edits in a copy of the folder on your desktop and move the files to your deluge...
It will help with speed I promise...)

Download and place file_fixer.py into the ROOT folder of your Deluge's sd card.
(last time I'll remind you please backup your files incase this doesn't work that way you can revert and
still use the deluge)

THIS WILL GO THROUGH YOUR FOLDERS FOR:
SYNTHS
KITS
SONGS
IF YOU ONLY NEED 1 FIXED DELETE THE TWO OTHER AT THE BOTTOM OF THE PYTHON FILE.
THEY LOOK LIKE THIS:
preset_search('SONGS')
preset_search('DRUMS')
preset_search('SYNTHS')

Depending on which operating system you use terminal to navigate the computers directories to access the sd card.
For windows it usually ends up being...


C:\Users\'your name here'> cd desktop
C:\Users\'your name here'\Desktop> cd delugefolder
C:\Users\'your name here'\Desktop\delugefolder> 

from here you'll type:

C:\Users\'your name here'\Desktop\delugefolder> python file_fixer.py

There you go!
At this point it should work.
It will output plenty of data showing you that it is working.
If it looks like python is not doing anything please let give it time to work its magic. It'll continue I promise.
If at all the program just seems to completely stop for more than a few minutes or gives you an error please file
a report onto github stating the error and we can go from there if you really need this tool.

At the end it should give you an all good that it worked its magic with a nice list showing you which files it
couldn't find. Don't be worried this just means python couldn't match a preset to its correct sample because
it's either missing or the name was changed to something else. In this case there is nothing more the script can do
and it will be up to you to either remake the patch or find .wav somewhere on your computer and put it back into the
samples folder.

Hope this helped! If you have any questions go ahead and shoot me a message on discord!
GIGAHAXX #0754

If this helped at all I'd love to hear about it. I'm happy to get someone back up and running as much because it was
super satisfying even getting it fixed for myself.
(also its 12:30am where I'm at so if there are any typos or things don't make sense its late, sorry not sorry.)


