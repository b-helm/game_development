"Amnesia" by "Ben Helm"

maximum score is 100.

The roof is a room.  "[if roof is not visited][italic type]You wake up lying on your back on the roof of a building.  There are no visible doors but there is a fire escape down from you.

[roman type]You stand up, dizzy, trying to remember any events that might have transpired leaving you in this dire predicament.  Nothing comes to mind.[otherwise]You stand as a solitary figure on the empty rooftop.  The fire escape is below you."

A scrap of paper is here.   "A crumpled scrap of paper lies on the ground."  The description is "On the paper is scrawled in red script are the words [italic type] not again [roman type]";

after examining the paper:
award 10 points.



The fire escape is a room.  It is down from the roof. "[if fire escape is not visited]You hang from the edge of the building and drop down 10 feet onto the fire escape, landing precariously and barely keeping your balance above a dizzying drop.   A rickety set of metal stairs leads down to the ground.[otherwise]You stand somewhat uncomfortably on the fire escape with the rickety stairs below you and the roof a short but frightening climb above you."

A bottle is here.  It is a thing. It is edible.  "Lying next to your foot is a bottle with a single pill in it."  The description is "[if we have not examined the bottle]In bright letters it says 'Radiation Medication.'  There appears to be some fine print below it. [otherwise]The fine print states that Radiation poisoning is a serious condition and that any human will die quickly without medication, but that if the medication is used on a non-human subject there can be harmful side effects.[end if]"

Understand "medication" as bottle;
Understand "pill" as bottle;

After eating bottle:
say "Your head starts to spin and you fall to your knees, vomiting uncontrollably through the grate of the fire escape for several minutes";
award 10 points.





The alley is a room.  It is down from the fire escape.  "[if the alley is not visited]After an arduous descent down the rusting stairs, you find yourself in a dimly lit alley.  To the west you can see the street.  East the alley appears to go deeper, and gets darker as it goes.[otherwise]You stand in the dim alley, with the street to the west and the alley extending to the east."

The cat is a female animal in the alley.  "Nearby you lurks a mangy looking alley cat.  Perhaps it is safe to take with you as a companion."  The description is "It is clearly very diseased, and is looking at you as if you were a meal."

Instead of taking cat:
say "The rabid beast leaps onto your face and claws you until you collapse into an unconscious heap to be devoured.";
end the game saying "You died bravely in the process being food for a rabid alley cat."





The deep alley is a room.  It is east of the alley.  "It is darker here.  Your eyes adjust slowly."

Vagabond is a woman in the deep alley.  "You can see the outline of a woman standing nearby."  The description of Vagabond is "What did your parents tell you about talking to strangers?  Then again... she might know what happened."

understand "woman" as vagabond

after asking vagabond about "what happened":
say "The woman's eyes go wide and she says 'You mean the epidemic? How could you not know?";
award 10 points.



The street is a room.  It is west of the alley.  "Blinking in the bright sun you find yourself standing in the middle of a busy street.  People hurry by each other without making eye contact.  To the south is the sidewalk at the other side of the street.  Directly in front of you is an ornate revolving door."

Bradley is a man.  He is in the street.  "Next to the door is a man leaning against the wall wearing a tuxedo.  He is tall and lean, and is smoking a cigarette." The description of Bradley is "Sticking out of his pocket is a flask with the name [italic type] Bradley [roman type] engraved on it.  He appears to be someone who might know about the building."

understand "man" as Bradley

after examining Bradley:
award 10 points.

After asking Bradley about "building":
say "He says in an incredulous tone: 'What do you mean?!?  That is where we used to work!";
award 10 points.

After asking Bradley about "the building":
say "He says in an incredulous tone: 'What do you mean?!?  That is where we used to work!";
award 10 points.

A door called the revolving door is south of the lobby and north of the street.  It is scenery.  The description is "There is caution tape blocking it off, but you can remove it easily.  The lock seems to have been forcibly broken recently."




the far sidewalk is a room.  it is south of the street. "You stand on the south side of the street on a nondescript sidewalk.  The building is on the north side."

The stranger is a man.  He is in the far sidewalk.  "Nearby is a stranger sitting on the steps of a brick building."  The description is "You notice that he is wearing a gold watch, and it reminds you that your own watch is missing from you wrist.  Maybe this man could tell you the time."

after asking stranger about "time":
say "He replies 'it is 4:25pm on December 29, 2015.";
award 10 points.

after asking stranger about "the time":
say "He replies 'it is 4:25pm on December 29, 2015'.";
award 10 points.



The lobby is a room.  It is north of the revolving door.  "You are standing in the center of the lobby of a modern looking building.  In addition to the revolving door, there is a glass door that appears to lead outside to the west and a metal door to the north.  In the center of the room is a fountain, and around the rim is a sign in tarnished bronze lettering." 

There is a fountain in the lobby.  It is scenery.  The description is "It is completely dry, and appears to have been that way for some time."

There is a sign in the lobby.   It is scenery. The description is "It reads [italic type]National Artificial Intelligence Agency[roman type]" 

after examining the sign:
award 10 points.

A door called the glass door is west of the lobby and east of the courtyard.  It is scenery.

A door called the metal door is north of the lobby and south of the operating room.  It is scenery.




the operating room is a room.  it is north of the metal door.  "You are in what appears to be an OR, with an operating table on the center and various machines around it. To the east is an entryway to a room with an ominous orange glow coming from it.  There is a gigantic hydraulic injection needle next to the table, with a computer attached to it."  

the needle is in the operating room.  it is scenery. 

the computer is in the operating room.  it is scenery. The description is "On the screen is green writing on a black background that says 'Test subject 0'.  Below it is a picture of your face."

the lab notes is in the operating room.  "Lying on the floor is a crumpled piece of paper with the phrase 'Lab Notes' written at the top."  The description is "It says 

'Subject experiences massive memory loss and erratic behavior.  Subject's radiation levels far exceed normal limits, and will cause severe radiation poisoning to anyone in the vicinity.  Subject seems to be immune to the radiation."   

after examining the computer:
award 10 points.

after examining the lab notes:
award 10 points.



the furnace room is a room. it is east of the operating room.  "In one wall of the room is a gigantic incinerator, big enough for a truck to pass through."

a door called the incinerator is east of the furnace room and west of heaven.  it is scenery.

the scientist is a woman in the furnace room.  "Standing next to the incinerator is a woman wearing a HAZMAT suit."  The description of the scientist is "She looks to be a scientist.  Maybe she knows you."

understand "woman" as scientist

after asking the scientist about [something]:
say "The woman turns around and her eyes go wide when she sees you.  In a solemn voice she says 'So you are back.  I didn't know how long you would be gone this time.  Each time you are gone for longer, and you infect more people.  This time was almost three months.  In the year since you were injected with the learning chip you have infected nearly 3 million people, but every time you return back here you can't remember it.  There is no way to stop you.  Unless....'  She slowly looks towards the incinerator.";
award 10 points.

heaven is a room.  it is east of the incinerator.  "You stand among the clouds in front of a massive golden gate."

a door called the gate is north of heaven and south of bliss.  it is scenery.

after going through the gate:
say "You sacrificed yourself to save humankind, proving that perhaps you weren't the monster that you thought....";
end the game in victory.


The courtyard is a room.  it is west of the glass door.  "You stand in a beautiful courtyard.  The glass door is behind you."

There is a newspaper in the courtyard.  It is a thing.  "Lying on a bench is a newspaper, with a picture of the lobby on the front page."  The description is "The date in the top corner is January 1, 2015.  The headline reads 'NAIA Shuts Down After Brain Implant Catasrophe." 

after examining newspaper:
award 10 points.


