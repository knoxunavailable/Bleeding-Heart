# Characters
define h = Character("THE HIGHMOTHER")
define j = Character("JUN YUE", color='#b43a38', image='junyue')
define y = Character("??????", color='#B1A3C0', image= 'astrid')
define a = Character("ASTRID", color='#B1A3C0', image='astrid')
define g = Character("GUARD", color='#000000')

# Positions
define cright = Position(xanchor=0.5, yanchor=1.0, xalign=0.7, yalign=0.75)
define cleft = Position(xanchor=0.5, yanchor=1.0, xalign=0.2, yalign=0.75)
define ccenter = Position(xanchor=0.5, yanchor=1.0, xalign=0.5, yalign=0.75)

# Video Transitions
image prolog_day1 = Movie(play="images/transitions/prologue-day1.webm", size=(1440,1080), loop=False, xalign=0.5, yalign=0.5)
image day1_day2 = Movie(play="images/transitions/day1-day2.webm", size=(1440,1080), loop=False, xalign=0.5, yalign=0.5)
image day2_day3 = Movie(play="images/transitions/day2-day3.webm", size=(1440,1080), loop=False, xalign=0.5, yalign=0.5)

# Images
## Astrid
image astrid idle neutral = "astrid/astrid_idle_neutral.png"
image astrid idle talk = "astrid/astrid_idle_talk.png"
image astrid idle explain = "astrid/astrid_idle_explain.png"
image astrid idle fluster = "astrid/astrid_idle_fluster.png"
image astrid idle frown = "astrid/astrid_idle_frown.png"
image astrid idle frown talk = "astrid/astrid_idle_frown_talk.png"
image astrid idle lookdown = "astrid/astrid_idle_lookdown.png"
image astrid idle outis = "astrid/astrid_idle_outis.png"
image astrid idle smile = "astrid/astrid_idle_smile.png"
image astrid idle smileclosed = "astrid/astrid_idle_smileclosed.png"
image astrid idle yell = "astrid/astrid_idle_yell.png"
image astrid idle curious = "astrid/astrid_idle_curious.png"
image astrid freakout lookup = "astrid/astrid_freakout_lookup.png"
image astrid freakout lookdown = "astrid/astrid_freakout_lookdown.png"
image astrid bars shock = "astrid/astrid_bars_shock.png"
image astrid bars yell = "astrid/astrid_bars_yell.png"
image astrid bars angry = "astrid/astrid_bars_angry.png"
image astrid bars angry talk = "astrid/astrid_bars_angry_talk.png"
image astrid ashamed talk = "astrid/astrid_ashamed_talk.png"
image astrid ashamed neutral = "astrid/astrid_ashamed_neutral.png"
image astrid ashamed lookside = "astrid/astrid_ashamed_lookside.png"
image astrid ashamed fluster = "astrid/astrid_ashamed_fluster.png"
image astrid ashamed fluster talk = "astrid/astrid_ashamed_fluster_talk.png"
image astrid shocked = "astrid/astrid_shocked.png"

## Jun Yue
image jun idle neutral = "jun/jun_idle_neutral.png"
image jun idle talk = "jun/jun_idle_talk.png"
image jun idle discomfort = "jun/jun_idle_discomfort.png"
image jun idle discomfort talk = "jun/jun_idle_discomfort_talk.png"
image jun idle doxxing = "jun/jun_idle_doxxing.png"
image jun idle endeared = "jun/jun_idle_endeared.png"
image jun idle fluster talk1 = "jun/jun_idle_fluster_talk1.png"
image jun idle fluster talk2 = "jun/jun_idle_fluster_talk2.png"
image jun idle fluster yell = "jun/jun_idle_fluster_yell.png"
image jun idle yell = "jun/jun_idle_yell.png"
image jun idle wtf = "jun/jun_idle_wtf.png"
image jun idle laugh = "jun/jun_idle_laugh.png"
image jun idle question = "jun/jun_idle_question.png"
image jun idle shiteating1 = "jun/jun_idle_shiteating1.png"
image jun idle shiteating2 = "jun/jun_idle_shiteating2.png"
image jun idle shiteating3 = "jun/jun_idle_shiteating3.png"
image jun idle smug = "jun/jun_idle_smug.png"
image jun idle2 curious = "jun/jun_idle2_curious.png"
image jun idle2 disgust neutral = "jun/jun_idle2_disgust_neutral.png"
image jun idle2 disgust talk = "jun/jun_idle2_disgust_talk.png"
image jun idle2 horrified = "jun/jun_idle2_horrified.png"
image jun idle2 mansplaining = "jun/jun_idle2_mansplaining.png"
image jun idle2 shocked = "jun/jun_idle2_shocked.png"
image jun idle2 tease closedeyes = "jun/jun_idle2_tease_closedeyes.png"
image jun idle2 tease openeyes = "jun/jun_idle2_tease_openeyes.png"
image jun idle2 smug = "jun/jun_idle2_smug.png"
image jun idle2 idgaf = "jun/jun_idle2_idgaf.png"
image jun idle2 poise = "jun/jun_idle2_poise.png"
image jun expressive arrogant = "jun/jun_expressive_arrogant.png"
image jun expressive evil = "jun/jun_expressive_evil.png"
image jun idle bruh = "jun/jun_idle_donewithyoshit.png"
image jun idle2 curious nomouth = "jun/jun_idle2_curious_nomouth.png"
image jun idle fluster fuck = "jun/jun_idle_fluster_fuck.png"

## The Evil Scenes
image astrid evil neutral = "astrid/astrid_evil_neutral.png"
image astrid evil talk = "astrid/astrid_evil_talk.png"
image astrid evil scream = "astrid/astrid_evil_scream.png"
image astrid evil bars yell = "astrid/astrid_evil_bars_yell.png"
image jun evil neutral = "jun/jun_evil_neutral.png"
image jun evil talk = "jun/jun_evil_talk.png"
image jun evil quiver = "jun/jun_evil_quiver.png"

# Epilogue booleans
define persistent.epilogue = False
define epilogue_origin = False