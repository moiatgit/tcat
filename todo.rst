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

Source (22436 sym): http://ca.wikipedia.org/wiki/Jos%C3%A9_Mar%C3%ADa_Aznar_L%C3%B3pez
	[tcat_v04]:	distance=    3468.0 (0.00%)	hands=3713 (3.00%)
	[tcat_v01]:	distance=    3630.0 (4.67%)	hands=3754 (4.00%)
	[tcat_v03]:	distance=    3751.0 (8.16%)	hands=3713 (3.00%)
	[dvorak_es]:	distance=    3762.0 (8.48%)	hands=3649 (1.00%)
	[tcat_v02]:	distance=    3858.0 (11.25%)	hands=3590 (0.00%)
	[qwerty]:	distance=    5382.0 (55.19%)	hands=7315 (103.00%)

Source (67142 sym): http://es.wikipedia.org/wiki/Jos%C3%A9_Mar%C3%ADa_Aznar
	[tcat_v03]:	distance=    9958.0 (0.00%)	hands=9875 (2.00%)
	[tcat_v02]:	distance=    9992.0 (0.34%)	hands=9627 (0.00%)
	[tcat_v04]:	distance=   10605.0 (6.50%)	hands=9875 (2.00%)
	[tcat_v01]:	distance=   10887.0 (9.33%)	hands=10062 (4.00%)
	[dvorak_es]:	distance=   10987.0 (10.33%)	hands=9986 (3.00%)
	[qwerty]:	distance=   19095.0 (91.76%)	hands=20623 (114.00%)

Source (46423 sym): http://en.wikipedia.org/wiki/Jos%C3%A9_Mar%C3%ADa_Aznar
	[tcat_v01]:	distance=    6994.0 (0.00%)	hands=9547 (10.00%)
	[dvorak_es]:	distance=    7255.0 (3.73%)	hands=8645 (0.00%)
	[tcat_v04]:	distance=    7399.0 (5.79%)	hands=9066 (4.00%)
	[tcat_v02]:	distance=    8135.0 (16.31%)	hands=8764 (1.00%)
	[tcat_v03]:	distance=    8477.0 (21.20%)	hands=9066 (4.00%)
	[qwerty]:	distance=   11979.0 (71.28%)	hands=14531 (68.00%)

Source (9762 sym): http://de.wikipedia.org/wiki/Jos%C3%A9_Mar%C3%ADa_Aznar
	[dvorak_es]:	distance=    1474.0 (0.00%)	hands=2123 (0.00%)
	[tcat_v01]:	distance=    1512.0 (2.58%)	hands=2270 (7.00%)
	[tcat_v02]:	distance=    1630.0 (10.58%)	hands=2110 (0.00%)
	[tcat_v04]:	distance=    1743.0 (18.25%)	hands=2177 (3.00%)
	[tcat_v03]:	distance=    1806.0 (22.52%)	hands=2177 (3.00%)
	[qwerty]:	distance=    2497.0 (69.40%)	hands=3246 (53.00%)

Source (19263 sym): http://fr.wikipedia.org/wiki/Jos%C3%A9_Mar%C3%ADa_Aznar
	[dvorak_es]:	distance=    2856.0 (0.00%)	hands=3603 (4.00%)
	[tcat_v04]:	distance=    2897.0 (1.44%)	hands=3558 (3.00%)
	[tcat_v01]:	distance=    2926.0 (2.45%)	hands=3586 (4.00%)
	[tcat_v02]:	distance=    3137.0 (9.84%)	hands=3438 (0.00%)
	[tcat_v03]:	distance=    3145.0 (10.12%)	hands=3558 (3.00%)
	[qwerty]:	distance=    4433.0 (55.22%)	hands=5718 (66.00%)


That is, if there's no further errors, I've got a layout (v04) that is
improving performance over the rest of layouts for Catalan when
considering key distance. Unfortunately on alternating hands, it is
worse than the rest of considered layouts (except, of course, for
qwerty) 

For Spanish, the second priority language, v04 is bellow v02 and v03,
but still over dvorak.

For English, the third priority language, v04 scores slightly worse than dvorak and both below v01.

While not a priority, it is interesting to appreciate that v04 is
still on competition for French but not for dvorak.


Now, the ToDo list include:

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
