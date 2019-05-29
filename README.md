#JustifyText

```
Takes  a  string  and  inserts
spaces  between  words,  until
line is  desired  width,  like
you see here.
```

### Importing the module and using the function:
*Option 1:
```
from justify_text import justify
justify(text, width)

```
*Option 2:
```
import justify
justify_text.justify(text, width)
```

### Module Requirements/Dependencies:
* Python code tab = 4 spaces
* Requires textwrap module


### Module Assumptions:
* Line has at least one space  between  words  (at  least in this version).
* Relies on break_on_long words equalling true in textwrapper. (You could make the change to the textwrapper function call in this module, but at a small enough width you would just get back lines with single words and nothing but spaces on the ends of them, i.e not justified.) 


### Required positional arguments:
* text == string to be formatted as list of strings exactly n characters long (You'll have to handle quotes and special characters of course.) 
* width == desired width of the resulting line 

### Optional and default arguments: 

```
justify_last_line = False
```
This is the default for handling the final line of the string. Convention is to NOT stretch a few words across the span of the formatted block, but I've included a way to undo that - if that's your kind of thing.  For example: 

```
	text = "The end of this bit of text will be these three words." 
	
	justify(text, 35) 
```
will return a list that can iterate over to display: 
```
	The end of this bit of text will be
	these three words.
```
whereas 
```
	justify(text, 35, justify_last_line = True) 
```
will return a iterable list that will display: 
```
	The end of this bit of text will be
	these         three          words.
```
### Module Flow: 

1.	Accepts a string (Module seems to ignore \n, not sure why yet --  I'm very tired.  Probably has something to do with textwrap behavior. To preserve a special character, escape it, i.e.  '\\n').  Otherwise normal string manipulation rules apply, you'll need to handle quotation marks and special characters accordingly.  One of the earliest steps in this module puts text through textwrapper, so if your input doesn't raise a textwrapper error there, you should be all right. (Probably). 

2. 	Break into lines no longer than n using textwrap and TextWrapper.     See discussion at end of 1. above. 

3. 	Loop, starting from the last space (actually, the word before the   last space), and walk backward, adding a space between words (on the theory that readers will be less likely to notice extra spaces when reading from left-to-right and encountering them at the end of a line. 

4. 	If a line is still short after adding a space between all words in a line, module will start again at the last space (IOW, it enters a second or third or eighth space - beginning at the end - to reach desired width). 

5. 	Once all lines are exactly n width, return list of lines.  Module *could* just print them into a nice block, but I prefer to hand the reformatted text back to you, so you can do with it what you like.  To display the reformatted text a simple iterable will do. 
	e.g.: 
```
	for i in returnText:
	print(i)
```
# Sample Usage

Raw text: 

```
	text = "Now did the Lord say, \"First thou pullest the Holy Pin. Then thou must count to three.
	Three shall be the number of the counting and the number of the counting shall be three. Four
	shalt thou not count, neither shalt thou count two, excepting that thou then proceedeth to three.
	Five is right out. Once the number three, being the number of the counting, be reached, then lobbest
	thou the Holy Hand Grenade in the direction of thine foe, who, being naughty in my sight, shall snuff it." 
```
Call: 
```
x = justify(text, 30) 
```

Returns: 
```
x = ['Now did the Lord say, "First', 'thou pullest the Holy Pin.', 'Then thou must count to three.',
'Three shall be the number of', 'the counting and the number of', 'the counting shall be three.', 
'Four shalt thou not count,', 'neither shalt thou count two,', 'excepting that thou then', 'proceedeth
to three.  Five is', 'right out.  Once the number', 'three, being the number of the', 'counting, be
reached, then', 'lobbest thou the Holy Hand', 'Grenade in the direction of', 'thine foe, who, being 
naughty', 'in my sight, shall snuff it.'] 
```
Process list for justified display: 

```
	for i in x: 
	print(i) 
```

Sample output: 

```
	Now did the Lord  say,  "First
	thou  pullest  the  Holy  Pin.
	Then thou must count to three.
	Three shall be the  number  of
	the counting and the number of
	the counting shall  be  three.
	Four  shalt  thou  not  count,
	neither shalt thou count  two,
	excepting   that   thou   then
	proceedeth to three.  Five  is
	right  out.  Once  the  number
	three, being the number of the
	counting,  be  reached,   then
	lobbest  thou  the  Holy  Hand
	Grenade in  the  direction  of
	thine foe, who, being  naughty
	in my sight, shall snuff it.
```

### Other/Misc.: 
This package was prepared per the advice at: https://packaging.python.org 

Found bugs? Let me know! 
mailto: cjtx.code@gmail.com
 
-cjtx / May 27, 2019
