# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Dennis", image="dennis")
define m = Character("Maya", image="maya")

image dennis happy = "dennis_happy.png"
image dennis sad = "dennis_sad.png"

image maya sad = "dennis_sad.png"

image bg room = "bedroom_img.jpg"
image bg outside = "outdoors_img.jpg"

default talked = False
default been_outside = False

default science_knowledge = 0
default chemistry_topics = ["Protons","Stochiometry","SN2 Elimination"]
                            # 0          1              2

# The game starts here.

label start:

    scene bg room
    show dennis happy
    "Your science knowledge is [science_knowledge]."

    if talked == False:
        d "I'm so excited for my fulfilling life as a junior at Super Competitive High School!"
        "..."
        d sad "Oh wait that doesn't exist." with dissolve
        d "I guess I should figure out what to do today."
        $ talked = True

    menu:
        "What are you going to do today?"

        "Go outside!" if been_outside == False:
            jump outside
        "Study chemistry :(" if science_knowledge < len(chemistry_topics):
            $ local_chemistry_topic = chemistry_topics[science_knowledge]
            "You studied really hard and learned more about [local_chemistry_topic]."
            $ science_knowledge += 1
            "Good job! Your science knowledge is [science_knowledge]."
            "You had a very not fulfilling day, time to go bed."
            jump start
    return

label outside:
    $ been_outside = True
    scene bg outside
    "You are outside."
    "You get bored, and go back inside."
    jump start

label switch_sides:
    show dennis happy at left
    d "I'm really happy!"
    show maya sad at right
    m "I'm really sad."