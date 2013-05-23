##############
List of TODO's
##############


Consider the following list of ToDo's for this project


#. Last point:

   I was working on a simulation at Layout.py

   Target was to get ConfortKeys.scoreLayout() working but I've
   found a problem in defining the function. comfort keys are lower
   the best, but frequencies are higher the best.

   The target is to define a formula such as given a low comfort key
   index the higher the assigned symbol, the best should score (the
   lowest the best)

        comfort index       freq            score
        -------------       --------        ---------
        low                 low             high
        low                 high            low
        high                low             low
        high                high            high

   Then apply this formula to ConfortKeys.scoreLayout() and see what
   happens.

   Layout.main() should keep only a maximum of say 100 best scored layouts.

   It can be hard to compute them, having into account the enormous
   amount of permutations (35!) Some optimizations should be
   considered. For example, think about passing the 100th best score.
   Once the computations of the score of a layout surpass this 100th
   best score, the layout can be dismissed.

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
