# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("THE HIGHMOTHER")
define j = Character("JUN YUE", color='b43a38', image='junyue')
define y = Character("??????", color='#B1A3C0', image= 'astrid')
define a = Character("ASTRID", color='#B1A3C0', image='astrid')

#Positions
define baseright = Position(yanchor=1.0, xalign=0.95, ypos=1.0)
define bitright = Position (yanchor=1.0, xalign=0.75, ypos=1.0)
define basecenter = Position(yanchor=1.0, xalign=0.5, ypos=1.0)
define bitleft = Position(yanchor=1.0, xalign=0.25, ypos=1.0)
define baseleft = Position(yanchor=1.0, xalign=0.05, ypos=1.0)
define kleft = Position(yanchor=1.0, xalign=-0.25, ypos=1.0)
define kbitleft = Position(yanchor=1.0, xalign=0.0, ypos=1.0)
define kright = Position(yanchor=1.0, xalign=1.20, ypos=1.0)
define kbitright = Position(yanchor=1.0, xalign=1.0, ypos=1.0)

# The game starts here.

label start:

label prologue:
"Want to know something about the gods, (REDACTED)?" 
"They made everything." 
"From lush green forests, to tumultuous waters, to tranquil breezes.."
"And us, too, of course."
"Each pore of your skin and hair on your head… all of it was made with a purpose."
"With an intention."
"Like a well-oiled machine, like a piece of a jigsaw puzzle."
"Working as one living, breathing world."
"All with an understanding that, should they falter or fall out of line, this delicate balance which informs the entire universe will split clean in half, taking all our happily ever afters with it."
"It's a good thing, then, that the gods run a tight ship."
"..Now, what if I told you the gods could make mistakes?"
"Ah, not many, mind you, because the process has been finely tuned for eons." 
"Long before you, or even I, were on this earth." 
"But it happens."
"Sometimes an error will slip through the cracks and begin its descent to our lands." 
"These instances are few and far between, but like a tumor, they spread, infecting the rest of creation with their sinful nature." 
"Doomed to be wicked for eternity."
h "But worry not, my sweet child, and don’t lose hope. A cursed half-breed such as yourself may just find the purity nestled within."
h "All you need to do is obey."

label day_one:

show astrid idle at kbitright 
y "this is a test."

show astrid idle at kbitright 
a "my name is--"

show junyue idle at kbitleft 
j "shut up faggot"


    # This ends the game.

return
