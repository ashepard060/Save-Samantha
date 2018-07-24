

print "Samantha is a young girl who was told at a young age that her mother died in an accident when she was a baby. She is now a teenager starts to over hear too much information that she can’t seem to piece together. She begins an adventure to find out the secrets that are being withheld from her."

raw_input ("type 'okay' to continue" )

print " "

print "it’s 7:30 a.m. and your alarm clock goes off. BRRRRIIIIIING! You think about how amazing it would be to stay in the bed and get just a couple more minutes of sleep, but you know a couple might lead to more. Do you get up now or risk sleeping a little longer?"


A1 = raw_input ("Type 1 to get up now or 2 sleep longer" )

print " "

if A1 == "1":
 print "You drag yourself out of the bed and head to the shower. Upon heading to your personal bathroom you realize you left all the towels in the washer last night and forgot to dry them."
 raw_input ("Type 'stairs' to head downstairs" )
elif A1 == "2":
 print " "
 print "You tell yourself you’re going to sleep 5 more minutes, but end up sleeping 20 more minutes. You leap out of the bed and head to the shower. Upon heading to your personal bathroom you realize you left all the towels in the washer last night and forgot to dry them."
 raw_input ("Type 'run' to run downstairs" )

print " "

print "Annoyed, you head downstairs to shower in your dad’s bathroom. As you shower sleepily, you hear yelling coming from your dad’s room. He seems really upset, and if you turn the water off you could really hear him, but maybe it’s none of your business. Do you cut the shower to hear better, or keep showering and mind your business?"

A2 = raw_input ("'cut' to cut the shower off or type “business” to mind your business" )

print " "

if A2 == "cut":
 print 'Upon cutting the shower off you begin to hear your dad say, ‘$200 late fee for the rent is ridiculous. I plan on paying it tomorrow. Please extend me a day, I’m a valued customer I’ve been renting this space for 14 years.’ You’re curious so you begin to get out the shower.'
 raw_input ("'dress' to put on your clothes" )
 print " "

if A2 == "business":
 print "You finish washing up and try to ignore the outrageous yelling. Upon getting out the shower you hear the end of a conversation, ‘I’ve been renting this space for 14 years.’ You’re curious so you begin get dressed so that you can go in your dad’s room."
 raw_input ("Type 'dress' to put on your clothes" )
 print " "

print "You put on your clothes and head to your dad’s room and find him rushing to leave. Do you ask him to wait so you can inquire about the phone call? Or do you let him leave?"

A3 = raw_input ("Type 'WAIT' to stop him and ask or type 'leave' to let him leave" )

print " "

if A3 == "WAIT" or "wait":
 print "Your dad stops in the middle of the doorway and tells you you need to be heading to school. You say, ‘I overheard the yelling and was trying to make sure everything is okay.’ He reassures you everything is fine kisses you on the forehead and rushes out the door. You start to head back to your room to get ready for school, but you’re stopped by a, 'bRRIIIIIIINNNGGGG' You realize your dad left his phone. Do you answer the phone or just leave it be?"
 A4 = raw_input ("Type 'answer' to answer the phone call or 'walk away' to leave it be." )
 print " "
 if A4 == "answer":
   print "You answer the phone call and a man immediately starts talking. ‘Mr.Lopez, we really have a problem. I need you to come to the cabin right now. I think she may be pregnant… Mr. Lopez?? Mr. Lopez??’ You hang up the phone quickly, and stare for a minute. You try to understand what he was saying, but can’t seem to make sense of it."
   print " "
 elif A4 == "walk away":
   print "The phone stops ringing and you start to walk away. But then you see a notification pop up that says ‘Voicemail received’, your curiosity gets the best of you so you listen to the voicemail. A male’s voice comes through the speakers. ‘Mr.Lopez we have a problem. I think she’s pregnant. Meet me at the cabin. You stare for a minute and try to understand what he was saying, but can’t seem to make sense of it."
   print " "
if A3 == "leave":
 print "You start to head back to your room, and make a mental note to act like you didn’t hear anything. You start to head back to your room to get ready for school, but you’re stopped by a, 'bRRIIIIIIINNNGGGG' You realize your dad left his Macbook which is hooked to his phone. He’s getting a call from someone under a blocked caller ID. Do you answer the phone or just leave it be?"
 raw_input ("Type 'Answer' to answer the phone call or 'walk away' to leave it be." )
 if A4 == "answer":
   print "You answer the phone call and a man immediately starts talking. ‘Mr.Lopez, we really have a problem. I need you to come to the cabin right now. I think she may be pregnant… Mr. Lopez?? Mr. Lopez??’ You hang up the phone quickly, and stare for a minute. You try to understand what he was saying, but can’t seem to make sense of it."
   print " "
 elif A4 == "walk away":
   print "The phone stops ringing and you start to walk away. But then you see a notification pop up that says ‘Voicemail received’, your curiosity gets the best of you so you listen to the voicemail. A male’s voice comes through the speakers. ‘Mr.Lopez we have a problem. I think she’s pregnant. Meet me at the cabin. You stare for a minute and try to understand what he was saying, but can’t seem to make sense of it."
   print " "
print "A million thoughts are going through your head. Pregnant??? Cabin???? What could he be talking about?? You try to go back to getting ready for school but so many thoughts run through your head. You can’t go you have to figure out what’s going on. Or maybe you should go, and worry about it later."
print " "

A5 = raw_input ("Type 'worry' if you want to skip school and search for clues or 'don’t worry' if you want to go to school and forget about it")

if A5 == "worry":
 print "You can’t shake the mysterious thoughts from your brain. You have to know more. You start looking around to find things. You start thinking of hiding places for information."
 print " "
 raw_input ("Type 'open’ to open the drawers." )
 print " "
 print "You open the drawers to find nothing but clothes. You see cabinets."
 raw_input ("'search' to search the cabinets" )
 print " "
 print "You open the cabinets to find some pills in a plastic bag. You don’t know what the pills are for, but they don’t seem to be for medical use. Put those in your pocket."
 raw_input ("'pocket' to put the pills in your pocket" )
 print " "
 print "'You keep searching and eventually you run across a rent bill for an address that is not yours. Curiosity is killing you, so you decide to type the address in on your phone."
 raw_input ("'google maps' to search the address.")
 print " "
 print "The address comes up as a location about an hour away, in the woods. You realize this has to be the cabin that was being talked about on the phone. You look a little closer to see something."
 raw_input ("'look closer' to see something else")
 print " "
 print "You see that this bill was due and paid on the 17th of last month. You look at the date on your phone and it’s the 17th! Things are starting to add up! You rush to your car and call out 'Hey siri, give me directions to 1625 bulldog dr.' and speed off in hopes of figuring out this mystery!"
 raw_input ("Type 'hey siri'")
 print " "
if A5 == "don't worry":
 print "You decide not to worry about it and begin to gather your supplies for school. On your way out the door you realize you have a headache and decide to go to the cabinet to find some Advil. You grab your advi, but next to it you see a bag of mysterious pills. You realize you can’t go to school with all these mysteries going on. You don’t know what the pills are for, but they don’t seem to be for medical use. Put those in your pocket."
 raw_input ("'pocket' to put the pills in your pocket" )
 print " "
 print "'You keep searching and eventually you run across a rent bill for an address that is not yours. Curiosity is killing you, so you decide to type the address in on your phone."
 raw_input ("'google maps' to search the address.")
 print " "
 print "The address comes up as a location about an hour away, in the woods. You realize this has to be the cabin that was being talked about on the phone. You look a little closer to see something."
 raw_input ("'look closer' to see something else")
 print " "
 print "You see that this bill was due and paid on the 17th of last month. You look at the date on your phone and it’s the 17th! Things are starting to add up! You rush to your car and call out 'Hey siri, give me directions to 1625 bulldog dr.' and speed off in hopes of figuring out this mystery!"
 raw_input ("Type 'hey siri'" )
 print " "


print "The drive is long and you’re starting to get worrisome. It seems like you’ve been driving for hours upon hours. Speed up so that you can get there faster. You’re on a mission!"
raw_input ("Type 'accelerate' to speed up" )
print " "
print "You're just now hitting 65 mph and you still feel like you’re going slow. Speed up!"
raw_input ("'ACCELERATE' to speed up again." )
print " "
print "You speed up, and you’re happy to hear that you’re only 2 minutes away. You slack up off of the gas and realize you’re here. It’s an old abandoned cabin that you’ve never seen before. Why would you be here? Get out the car and go see."
raw_input ("'get out' to get out the car." )
print " "
print "You walk up to the front of the house and then think to yourself, Would it be smart for me to go in through the front door? Or should I go in through the side?"
A6 = raw_input ("'front' to go in through the front door or 'side' to go in through the side door" )

if A6 == "front":
 print "You decide that there’s no reason to sneak around, it’s your dad. You’re just going to walk in through the front door."
 raw_input ("Type 'twist the knob' to open the door." )
 print " "
 print "'You open the door slowly and you become ill from the anxiety. As you walk in you can hear some sort of metal sound.. Chains, maybe?"
 raw_input ("Type 'What is going on?'" )
 print " "
 print "'You whisper, ‘What is going on?’ This cabin looks a mess. You’re inside of the living room, but keep hearing noises coming from the basement. You’ve come so far, go check out the noises."
 raw_input ("'descend' to go down the stairs" )
 print " "
 print " You go down the stairs, and there’s a door. A single, steel, grey, door. A pad lock is on the floor next to the door.. Which creeps you out even more. You approach the door slowly, and you reach your hand out for the door knob.. As you start to twist you can hear a faint sobbing coming from behind the door"
 raw_input ("'open' to open the door.." )
 print " "

if A6 == "side":
 print "You creep around to the side of the house. On your way there’s you see scrap metal all around the house. As you dip down the hill to the side door, you began to have doubts about going inside."
 raw_input ("'reassure' to reassure yourself" )
 print " "
 print "You tell yourself 'it’s okay' nothing weird is going to be in there. You place your hand on the knob and slowly twist."
 raw_input ("'twist the knob' to open the door." )
 print " "
 print "'You open the door slowly and you become ill from the anxiety. As you walk in you can hear some sort of metal sound.. Chains, maybe?"
 raw_input ("Type 'What is going on?'" )
 print " "
 print "'You whisper, ‘What is going on?’ This cabin looks a mess. You’ve entered into the basement. You look around and you see a door. A single, steel, grey, door. A pad lock is on the floor next to the door.. Which creeps you out even more. You approach the door slowly, and you reach your hand out for the door knob.. As you start to twist you can hear a faint sobbing coming from behind the door"
 raw_input ("'open' to open the door.." )
 print " "

print "You go inside the door and you can not believe what you see."
raw_input ("'tell me' to find out what you see." )
print " "
print "'I can’t tell you.'"
raw_input ("'tell me!' to find out what you see." )
print " "
print "'Are you sure you want to know?'"
raw_input ("'TELL ME!' to find out what you see" )
print " "
print "'You see your supposedly dead mother sitting on a mattress, chained up, crying and sobbing. She snaps her head up in fear, but then you can see relief in her eyes. She says, 'Samantha? Baby?'"
raw_input ("'mom' to talk to her." )
print " "
print "‘Mom, is that you? Dad told me you were dead..’ She tries to talk through her obvious pain. ‘Baby, you have to get out of here.. He’ll be back.'"
raw_input (" Type 'Who?'" )
print " "
print "'Your father.. He will kill us both if he finds ----' She pauses and the look in her eyes shows nothing but terror. I pause and realize she’s looking past me and not at me. I slowly turn around to see my dad staring at me. He’s holding a gun, and it’s pointed at you… Do you run into him with all your might in hopes that he drops the gun? Or do you try to talk him out of shooting."
A7 = raw_input (" 'dive' to run into him or 'talk' to talk him out of it." )
print " "

if A7 == "dive":
 print "You lunge at him with all your might. He’s caught off guard and drops the gun. The gun slides across the floor close to the mattress your mom is sitting on! Your dad looks at you and you take off towards the gun. He pulls you by your legs and drags you back! Don’t let him get the gun find something!"
 print " "
if A7 == "talk":
 print "You begin to ask him questions… ‘why? Why would you lie to me? Why would you do this?’ He begins to speak in a calming manner. ‘Baby, it’s not what it looks like, she’s sick. She has to be here.’ Your mother yells, 'Don’t fall for his lies again baby!' Your dad speaks again, 'Baby, I would never lie to you.' he keeps lying and it’s making your rage become more apparent. In out of instinct You lunge at him with all your might. He’s caught off guard and drops the gun. The gun slides across the floor close to the mattress your mom is sitting on! Your dad looks at you and you take off towards the gun. He pulls you by your legs and drags you back! Don’t let him get the gun find something!"
 print " "

raw_input ("Type 'kick' to kick the table so that it will fall on him or  'throw' to throw a baseball bat to hit him in the head" )
print " "

print "He falls and is stunned for a minute, and in that time you lunge for the gun. You grab it, and points it at him and in that moment you think twice. Do you pull the trigger ? Or ask him questions on what’s going on? Time is ticking and you can’t think twice. This decision can make or break you. You have to make a smart decision."

A8 = raw_input ("'shoot' to pull the trigger or 'hesitate' to ask him the questions that’s bothering you" )
print " "

if A8 == "shoot":
 print "thinking quick on your feet, you aim the gun at his foot and pull the trigger. He isn’t dead, but he can’t chase you. You hurry and grab the keys from his belt loop as he screams in agony, and unchain your mother. You both run up the stairs and grab the nearest phone. You call 911 and they show up within minutes! Your father is taken to jail, but you have your mother back. All these years without her, and now she’s back! You both have a tragic story to tell, but now you both have the time to do so. Good choice."

if A8 == "hesitate":
 print "You start to shake, and your father sees a tear escape your eye. You blank out for a moment and in a blink of an eye, your father lunges at you, and sends you flying across the floor. The gun drops to the floor and he grabs it. He aims the gun at you and pulls it without hesitation. Your body becomes still as it collapses to the floor and the only sound you hear is your mother calling out to you as you slowly fade into oblivion….. You shouldn’t have hesitated..."







