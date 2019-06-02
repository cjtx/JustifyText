"""Returns list of strings *exactly* n width (using monospaced fonts)

Takes  a  string  and  inserts
spaces  between  words,  until
line is  desired  width,  like
you see here.



__author__ = "cjtx (cjtx.code@gmail.com)"""


#================================= CODE =================================#

import textwrap
	
def justify(text, width, sep = ' ', justify_last_line = False):
	
	#Initial wrap with Textwrapper - this will
	#chunk/approximate our lines, but return will
	#have ragged right side...like this comment does
	wrapper = textwrap.TextWrapper(width = width)
	newText = wrapper.wrap(text)
	
	#Handle optional justify_last_line argument
	if justify_last_line == False:
		ourRange = len(newText)-1				#	1 is subtracted from len of the range so that the final line is not justified (as is the convention)
	if justify_last_line == True:
		ourRange = len(newText)					#	This will justify the final line, no matter how short it may be.
	
	#Algorithm for actual justifying
	for i in range(ourRange):   			
		#Break the current textwrapped line further down into words only.
		#(!== ASSUMES WORDS HAVE ' ' BETWEEN THEM ==!)
		line = newText[i].split(' ')
		
		#This counter helps us start at the second to the last word; IOW, the word before the last space.
		#We will use it to walk backward through the line, adding a space between words until our line
		#is exactly n characters long
		counter = -2
		
		#Test whether line is exactly n characters long
		while len(newText[i]) < width:
			
			#Test/handle for one word line.
			if len(line) < 2:
				newText[i] += sep
				continue
			
			#If it's short...
			try:
				
				#...add our seperator character to the end of the word before the last space...
				line[counter] += sep
				
				#..then increase counter by one to walk back to the next previous word...
				counter += -1
				
				#...put the line back together to be evaluated by while statement above.  
				#Joining on the sep ensures there's at least a single space between the words.
				#we just borrowed it above b/c it was there.  ;D
				newText[i] = sep.join(line)
			
				
			except IndexError:
				#Resets counter to start at word before final space, if we've stepped through the list once
				counter = -2		
					
	return newText