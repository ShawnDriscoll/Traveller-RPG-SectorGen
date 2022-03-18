.. image:: https://img.shields.io/github/stars/ShawnDriscoll/Traveller-RPG-SectorGen.svg
	:target: https://github.com/ShawnDriscoll/Traveller-RPG-SectorGen/stargazers
	

**Traveller RPG SectorGen**
===========================

**Traveller RPG SectorGen** is a Windows program for generating sectors, based on rules from Mongoose Traveller 2nd Edition.

.. figure:: images/app_screen.png


Notes
-----

**Traveller RPG SectorGen** is being developed using Python 3.9.10 and PyQt5.
There are a few Python programs included.

``SectorGen.py`` will generate a sector at origin 0,0. The sector density can be selected. It
will create both raw CSV and JSON data files, and a Traveller 5 format sector file as well.

(Optional) ``CSV_to_GEnie_converter.py`` will create a GEnie format file from the raw sector data generated.

(Optional) ``PyMapGen.py`` will read the Traveller 5 format sector file and display it graphically using PyGame.

(Optional) ``CSV_to_WBS_converter.py`` will create an H&E WBS format file from the raw sector data generated.


Requirements
------------

* **Windows 10**

  It might not work in OSX or Linux.

* **Python 3.9.10**
   
  This code was written using the C implementation of Python version 3.9.10. Also known as CPython.

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


PyMapGen Usage
--------------

Click on a sector to center it.

Dragging a sector (or pressing the arrow keys) will scroll the map.

The ``mouse wheel`` will zoom the map in and out while pointing.

Pressing ``m`` will toggle the computer's voice on/off.

Pressing ``h`` will flip to a hex map(s) at different zoom levels.

Pressing ``r`` will flip to a rectangle map.

Pressing ``c`` will toggle solid/clear travel zones while zoomed in.

Pressing ``z`` will toggle circle/hex/rectangle travel zones while zoomed in.

Pressing ``t`` will toggle world UWP/TC while zoomed in.

Pressing ``l`` will toggle the world system locations on/off.

Pressing ``g`` will toggle the hex/rectangle grid on/off.

Pressing ``ESC`` will exit the program.


Not Using Python?
-----------------

You can always run the .EXE versions for Windows 10 if you don't have the Python language installed.

.. |ss| raw:: html

    <strike>

.. |se| raw:: html

    </strike>

Things To-Do
------------

| Add more world types.
| Add trade routes.
| Instruction manual.
| Add proper allegiance distribution across a sector.
| Cheat codes.
|ss|

| Put back "some" Traveller 5 stuff that was removed.
| Add number of worlds for each system (a T5 trait).
| Add option for Super-Earths (another T5 trait).
| Start on a To-Do.

|se|

**Known History**

* v0.3.1b

  Corrected values for starports.

* v0.3.0b

  A differentiation has now been made between barren and dieback worlds. New graphic will follow for PyMapGen.

* v0.2.3b

  Sector Density DM is now properly logged.

* v0.2.2b

  Now displays number of worlds generated. Helps with letting user know that sector generation has completed.

* v0.2.1b

  A CSV to WBS converter is included for creating H&E WBS formatted files.
  
  Chance of Super-Earths being generated. This Traveller 5 rule was previously removed, but then put back in as an option.
  
  Added number of worlds for each system.

* v0.2.0b

  Sectors are now generated in Traveller 5 format.
  
  A lot of the Traveller 5 world generation rules were removed, while keeping the Mongoose Traveller 2nd Edition rules. No more 3,000 trillion population sectors.

* v0.0.1b

  Initial release.


The Traveller game in all forms is owned by Far Future Enterprises. Copyright 1977 - 2022 Far Future Enterprises. Traveller is a registered trademark of Far Future Enterprises.


Contact
-------
Questions? Please contact shawndriscoll@hotmail.com
