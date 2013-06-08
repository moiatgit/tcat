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

    Most of the code in util/ should be revised if anyone wants to
    perform some automated scoring. I'd suggest to use the ods file to
    test further combinations instead.

I've got a program that, given a file/url, generates a report on layout
performance: score_text.py

Now, the ToDo list include:

#. since corpora and layout numbers are growing fast, it will be
   interesting to create some kind of make utility to compute scores
   for each file/layout that has changed.

#. develop a new program that given a symbol, it shows the distance
   with the rest of the symbols. It will help to try a new version of
   tcat that could beat v03 on Spanish and v01 on English

#. define further improvings:

   - collapse ñç in one key
   - programming symbols accessibility () {} []

#. program that, given a layout, generates xkb files

#. deb pack that installs the new layout on a debian box

#. training series (at least for typeme)

#. publicity
