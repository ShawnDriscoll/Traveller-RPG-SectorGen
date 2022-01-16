**Traveller RPG SectorGen**
===========================

**Traveller RPG SectorGen** is a Windows program for generating sectors.

.. figure:: images/app_screen.png


Notes
-----

**Traveller RPG SectorGen** is being developed using Python 3.9.7 and PyQt5.
There are a few Python programs included.

``SectorGen.py`` will generate a sector at origin 0,0. The sector density can be selected. It
will create both raw CSV and JSON data files, and a Traveller 5 format sector file as well.

(Optional) ``CSV_to_GEnie_converter.py`` will create a GEnie format file from the raw sector data generated.

(Optional) ``PyMapGen.py`` will read the Traveller 5 format sector file and display it graphically using PyGame.




Requirements
------------

* **Windows 10**

   It might not work in OSX or Linux.

* **Python 3.9.7**
   
   This code was written using the C implementation of Python
   version 3.9.7. Also known as CPython.

* **colorama 0.4.4**

   Because CMD may have some colored text messages for debugging invalid die rolls.
   
* **PyQt5 5.15.4**

   PyQt5 is the framework used for displaying the Window GUI and buttons, etc.

* (Optional) **pyttsx3 2.90**

   PyMapGen speaks in Zira's voice (her voice comes with Windows). Can be changed to a different voice in the source.

* (Optional) **pygame 2.1.0**

   PyGame is used to draw the maps. It's basically a Python wrapper for SDL 2.0.16, which PyGame includes.


Warning
-------

This code will not work with **Python 2.7-**.


Not Using Python?
-----------------

You can always run the .EXE versions for Windows 10 if you don't have the Python language installed.


The Traveller game in all forms is owned by Far Future Enterprises. Copyright 1977 - 2022 Far Future Enterprises. Traveller is a registered trademark of Far Future Enterprises.


Contact
-------
Questions? Please contact shawndriscoll@hotmail.com
