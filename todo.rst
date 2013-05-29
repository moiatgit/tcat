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

   Currently score_text.py is generating the following ranking

$ python score_text.py http://ca.wikipedia.org/wiki/Base_de_dades http://es.wikipedia.org/wiki/Base_de_datos http://en.wikipedia.org/wiki/Database http://de.wikipedia.org/wiki/Datenbank#Datenbankmanagementsystem http://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es
http://ca.wikipedia.org/wiki/Base_de_dades [tcat_v04]: 190
http://ca.wikipedia.org/wiki/Base_de_dades [tcat_v01]: 191
http://ca.wikipedia.org/wiki/Base_de_dades [tcat_v02]: 206
http://ca.wikipedia.org/wiki/Base_de_dades [tcat_v03]: 211
http://ca.wikipedia.org/wiki/Base_de_dades [dvorak_es]: 250
http://ca.wikipedia.org/wiki/Base_de_dades [qwerty]: 289
http://es.wikipedia.org/wiki/Base_de_datos [tcat_v04]: 189
http://es.wikipedia.org/wiki/Base_de_datos [tcat_v01]: 190
http://es.wikipedia.org/wiki/Base_de_datos [tcat_v02]: 205
http://es.wikipedia.org/wiki/Base_de_datos [tcat_v03]: 210
http://es.wikipedia.org/wiki/Base_de_datos [dvorak_es]: 248
http://es.wikipedia.org/wiki/Base_de_datos [qwerty]: 288
http://en.wikipedia.org/wiki/Database [tcat_v01]: 188
http://en.wikipedia.org/wiki/Database [tcat_v04]: 189
http://en.wikipedia.org/wiki/Database [tcat_v02]: 203
http://en.wikipedia.org/wiki/Database [tcat_v03]: 209
http://en.wikipedia.org/wiki/Database [dvorak_es]: 246
http://en.wikipedia.org/wiki/Database [qwerty]: 283
http://de.wikipedia.org/wiki/Datenbank#Datenbankmanagementsystem [tcat_v04]: 190
http://de.wikipedia.org/wiki/Datenbank#Datenbankmanagementsystem [tcat_v01]: 192
http://de.wikipedia.org/wiki/Datenbank#Datenbankmanagementsystem [tcat_v02]: 210
http://de.wikipedia.org/wiki/Datenbank#Datenbankmanagementsystem [tcat_v03]: 212
http://de.wikipedia.org/wiki/Datenbank#Datenbankmanagementsystem [dvorak_es]: 249
http://de.wikipedia.org/wiki/Datenbank#Datenbankmanagementsystem [qwerty]: 283
http://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es [tcat_v04]: 192
http://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es [tcat_v01]: 193
http://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es [tcat_v02]: 209
http://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es [tcat_v03]: 213
http://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es [dvorak_es]: 253
http://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es [qwerty]: 292

That is, if there's no further errors, I've got a layout (v04) that is
improving performance over the rest of layouts for Catalan, Spanish,
English, German and French!

Of course, this is more than expected. I'd like to perform some
further testing so I can dectect any bug that could throw away these,
by now, impressive results.


Now, the ToDo list include:

#. perform a controlled test (with manual counting) in order to check
   whether score_text.py is right

#. define further improvings:

   - collapse ñç in one key
   - programming symbols accessibility () {} []

#. program that, given a layout, generates xkb files

#. deb pack that installs the new layout on a debian box

#. training series (at least for typeme)

#. publicity
