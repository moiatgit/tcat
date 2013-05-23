##############
List of TODO's
##############

Currently:

    I've found that a brute force approach is not suitable for this
    problem. It would require analysing up to 35! layouts (I won't
    live that much to see the results)

    Therefore I've decided to take another approach: start working
    from well known layouts and hand-modify tcat in order to improve
    it on different subjects.

    Current version v01 scores clearly better than qwerty and
    dvorak.es:

    Following computations at util/frequencies.ods:

    -   dvorak es improves qwerty by 5,63%
    -   tcat.v01 improves qwerty by 17,74%
    -   tcat.v01 improves dvorak es by 12,83%

    Most of the code in util/ should be revised if anyone wants to
    perform some automated scoring. I'd suggest to use the ods file to
    test further combinations instead.

Now, the ToDo list include:

#. correct *confort* as *comfort* everywhere!

#. review
   https://help.ubuntu.com/community/Howto%3A%20Custom%20keyboard%20layout%20definitions
   to learn which are the customization possibilities

#. include fixed keys possibility for numbers and so

#. define a class that allows mapping preferred fingers for key

#. define a class that allows mapping a comfort key

#. define a class that allows mapping a layout

#. develop a program that, given comfort key map, a key-frequency
   a pair of keys-frequency, and a layout, returns
   the comfort score of the layout

#. develop a program that, given comfort key map, a layout and a text
   returns the comfort score of the text

#. develop a program to test whether a given layout suits vi hjkl keys
   usage

#. develop a program that, given a comfort key map, a key-frequency
   and a pair of keys-frequency, generates the N better scored comfort
   layouts (ordered by better to worse)

#. develop a program that, given comfort key map, a list of layouts
   and a test, returns the comfort score of the text for each layout
   (ordered by better to worse)

#. develop a program that is able to calculate the comfort score the
   text from a given url for a given list of layouts.

#. program that, given a layout, generates xkb files

#. deb pack that installs the new layout on a debian box
