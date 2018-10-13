Assignment: We needed to make a compiler for a Top-Down parsing method with a simple grammar 
rule. We needed to take the input file (one was provided for an example), and we needed to 
provide the corresponding SIC/XE code.

What I did: Since it was all math equations and assigning values, I decided that doing a 
postfix method would be the best since that is how computers handle math equations. We had the 
freedom of doing any language we wanted, so I went with Python since it is what I am most comfortable 
with.

Improvements: Due to time constraints, I made a new temp variable for every time I needed one. 
This is inefficient for memory and time especially if the input was scaled much higher. Instead, I 
should reuse the current ones needed and determined either the maximum I would need for an equation, 
or figure out a way to dynamically calculate that as I go. Looking back it wouldn't be that hard, but 
I was in a time crunch.

Additionally, I should have made the postfix and printLineCode methods into their own files to clean 
up the file and just import and call them as needed.
