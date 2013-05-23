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

    Following computations at frequencies.ods:

    -   dvorak.es improves qwerty by 5,63%
    -   tcat.v01 improves qwerty by 17,74%
    -   tcat.v01 improves dvorak.es by 12,83%

    There's a test version that improves tcat.v01 by placing most
    frequent symbol (dot) at home row. But pair scores are still
    bellow dvorak.

    Most of the code in util/ should be revised if anyone wants to
    perform some automated scoring. I'd suggest to use the ods file to
    test further combinations instead.

Now, the ToDo list include:

#. review
   https://help.ubuntu.com/community/Howto%3A%20Custom%20keyboard%20layout%20definitions
   to learn which are the customization possibilities

#. define further checks that allow discriminate layouts

   - pair frequencies
     get at least dvorak score

   - programming symbols accessibility () {} []

#. program that, given a layout, generates xkb files

#. deb pack that installs the new layout on a debian box
