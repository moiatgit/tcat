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

#. program that, given a file/url, generates a report on layout
   performance

   Winner should outperform any other known layout for all the test
   in Catalan. Whishfully with Castillian and English as bonus

   Currently score_text.py is generating the following ranking

    my ca : tcat_v01, tcat_v03, dvorak_es, tcat_v02, qwerty
    gen ca: tcat_v03, tcat_v02, tcat_v01, dvorak_es, qwerty
    es    : tcat_v03, dvorak_es, tcat_v01, tcat_v02, qwerty
    en    : dvorak_es, tcat_v01, tcat_v02, tcat_v03, qwerty

    It seems that I've done it! However, there're two issues:

    1st. why my ca (my own catalan writings) have worse results on v03
    than on v01?

    2nd. it is not possible to outperform dvorak_es on English too?
    Distance is not that bad (always considering old qwerty) but I
    doubt if really dot is so frequent after all.

#. define further improvings:

   - collapse ñç in one key
   - programming symbols accessibility () {} []

#. program that, given a layout, generates xkb files

#. deb pack that installs the new layout on a debian box

#. training series (at least for typeme)

#. publicity
