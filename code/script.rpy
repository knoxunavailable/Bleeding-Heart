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
h "But worry not, my sweet child, and don't lose hope. A cursed half-breed such as yourself may just find the purity nestled within."
h "All you need to do is obey."

label day_one:

scene bgdungeon with fade

"If she could describe the cell with one word, it would be this: suffocating." 
"For one, the enchantments, whispered by shaky lips, which weaved themselves into every crack and crevice of the cement, flowed over rusty iron bars, and seeped into compact cuffs, were cloyingly sweet."
"Secondly, the space itself was so small that her captor's more imposing figure could hardly pace around without hitting the wall."
"With each step, the sound reverberated throughout in a steady rhythm not unlike the ticking of a clock."
"What it was counting down to was anybody's guess."
"It just kept marching on. Seconds, hours, and days bled into one another until all that was left was a monotonous haze."
"To make it worse, the tiny enclosure was all the more halved by the thick iron bars which boxed her in, a structural decision which felt excessive considering she was already restrained."
"As if to mock her, the rest of the room was decidedly more comfortable, offering a table and chair to lounge in should any visitor desire."
"Shifting her limbs, the sharp sting of the silver against her wrists and legs made her grit her teeth and swallow on air. The pain was a reminder."
"Nothing moved in this place without permission."
"Not her, and not even the stoic guard who loomed over her." 
"Everything had a set time and schedule, a routine that encouraged complacency." 
"There was no need to think when everything was already decided for you."
"But if she knew anything at all about survival, it was that allowing them to force you into such rigidity would spell your untimely demise."
"If you wanted to live, it'd have to be as the thorn in their side, the wrench in their plans. Find a distinction, or go against the grain yourself."
"Her ears perk up as the warden speaks for the first time today, voice gruff, unyielding, and with a simple message."

show astrid idle at kbitright
show junyue idle at kbitleft 
y "Here." 

"Thrown haphazardly between the bars, a small, mangy rat twitched and squirmed on the floor. Like her, it was fighting to survive, legs frantically scurrying in the air in an attempt to prop itself upright." 

y "Your meal for the day. Eat up."

"Unlike her, it was pathetic."

"She scrunched her nose in distaste."

j "This-- this is no meal! This barely counts as a {i}morsel!{/i} I am {i}not{/i} going to eat that."

y "Whether you eat it or not is not my prerogative, {i}monster.{/i} You asked for something living. I have given you something living."

j "...I have a name."

y "I am aware. You've made it very memorable over our first few encounters."  

j "And you'd better not forget it. That's Jun Yue, {i}rightful heir{/i} of the Yue bloodline to you."

"The warden's eyes narrow, before the beast slams her hands into the bars, gripping them with an abrupt fury." 

"Her fingers flex around the metal, and a part of Jun wonders what she's really envisioning grasping onto with those hands of hers."

"Her throat, perhaps?"

y "Don't {i}speak{/i} as if there is any glory held by your clan, {i}monster.{/i}"

y "Your 'bloodline' consists of the blasphemous and the undesired. Tens of our people had their souls rendered stained by you and the rest of your accursed family."

"Her hold on the iron tightens, each word spoken dripping with pure disgust."

j "Your kind kill to survive too, mutt. Besides, your humans worship the gods. It's not like I'm sending them to an {i}eternity of darkness.{/i}" 

j "They're always arranging afterlifes and whatnot for loyal followers."

y "Call me a 'mutt' again, and I'll make it incapable for you to speak, {i}monster.{/i}"

"Jun rolls her eyes, leaning back against the wall and scoffing."

j "I tell it like it is. Would you prefer {i}wolfkin?{/i}" 

"To her delight, her captor bristles."

y "{i}Hold your tongue, wench, or I'll do it for you.{/i}"

j "Do you blame birds for eating worms? Everything alive is part of the food chain. The strong live on in a world where the weak are doomed to die. In exchange, their victims get peace."

j "We're only 'unforgivable' because we have the guts to go after creatures who think of themselves as invincible."

"Chuckling, she bares her fangs in a snide grin, her tone dripping with condescension."

j "I have to hand it to you, {i}puppy.{/i} You made my little night time escapades {i}far{/i} more {i}interesting{/i}."

j "It was rather thrilling seeing you try to make me the hunted while waxing all this poetic about {i}cleansing the world of my wickedness.{/i}" 

j "You {i}do{/i} know it's not uncommon for you wolves to be in my position, right?"

j "Not to say you're anywhere near my level.."

"Jun inches forward, straining against the chains securely fastened around her ankles."

j "In fact, treating a noble like myself this way would've gotten you {i}kill-{/i}"

"The warden's hand pulls away from the bars to grasp at Jun's collar, dragging her to meet her captor face to face." 

"The bars limited any further aggressions, but Jun could nonetheless feel her intent."

y "Do not delude yourself. {i}monster.{/i} It matters not how much you dress your crimes in the finest of cloth, or how much gold and silver you have in your treasuries." 

y "you will be nothing more than a blot left uncleaned, eager to further stain the perfect world {i}She{/i} has made." 

y "{cps=30}{i}YOU.{cps=2} {cps=30}ARE.{cps=2} {cps=30}{b}S C U M.{/b}{/i}{/cps}"

"She shoves Jun back down, letting her land against the cold, stone floors of her cell. As the guard looms over her, blanketing her in darkness, her eyes gleam with hatred."

"She {i}almost{/i} looks frightening."

y "...The barbarity you dress up as valor is what led to your inevitable capture. Soon enough, your brethren shall join you in your fate. I cannot wait to see them in the same cell you sit in."

y "You should consider yourself blessed to be chosen by the Highmother for such a high honor. Your death is the least you could give to the world after decades of chaos and bloodshed."

"Careful not to betray any weakness, Jun quips back."

j "What else did I expect? You clearly don't have any manners. You haven't even introduced yourself after putting me through that whole goose chase."

j "I always make it a point to let my prey know just who they're dying for before I dig in~ What's your excuse?"

"The warden glares at her pointedly before turning her back on Jun to take a seat at the table."

a "And why exactly does it matter who {i}I{/i} am. I am merely the hand of the Highmother. If you wish to curse a name, Her is there to utter." 

a "In fact, I {i}call{/i} upon it. A curse uttered from your mouth is an equivalent to a blessing from the gods above." 

"She lifts a Battleaxe from the table, running through the familiar motions of checking for imperfections. Finally, she takes the cloth hanging on the wall and dips it in a small container before beginning to polish the blade."

"Jun's eyes rake over it. That is new, a disruption to the mind-numbing sameness of her current existence. Greedily, she takes it in."

"Shining steel with the barest hint of blood crusting over the tips, soon to be wiped away by a rag that the warden held with uncharacteristic softness. Her other hand clutched the wooden handle to keep the weapon in place. "

"Just when she thought she'd memorized it, and one more cursory glance would all but cement it in her mind, she found yet another novelty."

"An engraving on the wood, tiny and simplistic enough that it would be missed at the first once over, but remained stark and solid in your vision if you knew where to look."

"An engraving that answered a question that had been evading her ever since their first encounter."

j "...{i}Astrid.{/i}"

"She delighted in how the werewolf stiffened as the syllables rolled off her tongue, in breaking through limitations set by people who doubted she could truly cross them." 

"Now, when Astrid looked at her, it wouldn't be with dismissal."

a "...You're a {i}perceptive{/i} one, aren't you."

"..In fact, it might even carry some degree of respect."

"Astrid's hand moved to cover the handle, foolishly thinking that pushing it to the shadows would make her forget."

j "That, and you're just not very bright. Vampires can read, you know."

a "You seem awfully proud of yourself. I suppose it makes sense to celebrate the small victories when your defeat is practically assured."

a "I hope the knowledge of my name is comforting to you, Jun Yue. Consider it one of the few you can have."

j "I think I have more than you. Considering how anti-'monster' this town is, I doubt you get a free pass. Even {i}I{/i} can smell the {i}beast{/i} off of you."

"Astrid bristles, quickly looking back to the weapon she had been brandishing like giving Jun her gaze would give credence to her remarks."

j "Come to think of it, have they ever really talked to you for the whole time you've been looking after me? You usually thank them and they shut the door in your face."

j "With the physical strength you have, you should be making them cower and beg for mercy. It's pathetic seeing you let them reduce you to a lapdog."

a "As I've said before, that barbaric thought was what led you to your capture. Besides, I do not think you can speak of camaraderie yourself."

a "You speak so highly of your bloodline, and yet, I haven't seen any attempt from them to help you escape."

j "I don't need them."

"Jun snaps, uncharacteristically brusque." 

j "And if we're running with that argument, what about your pack?"

"This time, Astrid has no smart-aleck response or preachy spiel. She just clasps her Battleaxe hard enough that her claws start to tear at the rope on its haft."

j "Come to think of it.. wolves only go solo when their group kicks them out." 

"All that can be heard is the squeak of the blade as Astrid's hand quickens its pace. She scowls, eyebrows furrowed, and holds that expression until she finishes her handiwork."

"Before Jun can get another word in, she's out the door, taking all of Jun's remaining energy with her."

"Her stomach churns, the final push that prompts her to even begin considering the measly rodent below her."

"She reaches down and starts with its head."


jump dream_one

label day_two:

    # This ends the game.

return
