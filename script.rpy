# Declare background images here

image titlescreen = "images/renpylive2dtitle.png"
image bg redbrickschool = "images/redbrickschool.png"
image rl2dchrscpt = "tlimages/RL2Dchrscpt.png"
image rl2dchrscpt2 = "tlimages/RL2Dchrscpt2.png"
image rl2dcubismSDKzip = "tlimages/RL2DCubismSDKzip.png"
image rl2dexpressions = "tlimages/RL2DExpressions.png"
image rl2dmotions = "tlimages/RL2DMotions.png"
image rl2dgameA = "tlimages/RL2DgameA.png"
image rl2dgameB = "tlimages/RL2DgameB.png"
image rl2dgameC = "tlimages/RL2DgameC.png"
image rl2dgameD = "tlimages/RL2DgameD.png"
image rl2dins = "tlimages/RL2Dins.png"
image rl2dpref = "tlimages/RL2Dpref.png"

# Declare Live2D characters here:

image Epsilon = Live2D("Resources/Epsilon", base=.8, loop=True)
image Hiyori = Live2D("Resources/Hiyori", base=.6, loop=True)
image Hibiki = Live2D("Resources/Hibiki", base=.6, loop=True)

# Define characters
define epi = Character("Epsilon")
define hyi = Character("Hiyori")
define hbi = Character("Hibiki")

# Start of Tutorial
label start:

    show bg redbrickschool
    with dissolve
    
    show Epsilon idle_01 at left
    with dissolve
    epi "Hi, my name is Epsilon."
    epi "I am Live2D character, here to tell you about a Live2D tutorial for Ren'py."
    epi "This lesson will help you how to place your Live2D characters for your visual novel game project."
    epi "Throughout this tutorial, you can call me Epi for short."
    epi "What we're learning today is how to you can display your Live2D character in Ren'py by using the updated scripting methods via Python, developed by PyTom."
    epi "I want to give thanks to PyTom in developing this wonderful visual novel game engine, Ren'py."
    epi "This will bring Live2D characters to life and have the opporturnity for helping all visual novel developers in stepping up their VN game development with Live2D."
    epi "Now it's time for the tutorial."
    epi "The first thing you have to do is download the Live2DCubismSDK Native on Live2D's website: {a=https://www.live2d.com/en/download/cubism-sdk/download-native/}https://www.live2d.com/en/download/cubism-sdk/download-native/{/a}."
    
    show rl2dcubismSDKzip at right with moveinright:
        yalign 1.0
        
        
    epi "Next, you place the downloaded Live2d Cubism SDK Native .zip file folder within the Renpy 7.4.0 SDK Directory Folder, as shown in the picture above."
    
    hide rl2dcubismSDKzip
    with moveoutright
    
    show rl2dpref at right with moveinright:
        yalign 1.0
    
    epi "After that, open your Renpy Launcher and click on \"Preference.\""
    
    epi "Then click \"Install libraries\", and click install Live 2D Cubism SDK Native, circled on the picture right above."
    
    hide rl2dpref
    with moveoutright
    
    show rl2dins at right with moveinright:
        yalign 1.0
    
    epi "Once you've finished, you should see \"successful install complete.\""
    
    hide rl2dins
    with moveoutright
    
    epi "If you don't see this message, make sure you place the Cubism SDK Native .zip folder in the correct Renpy folder path on either hard drive and repeat the previous steps as I mentioned again."
    epi "After you've successfully installed the Live2D Cubism SDK Native in your Renpy SDK folder path, open up the 'options.rpy' file in your game folder."
    epi "In the options.rpy screen, enter anywhere in the script by typing \"define config.gl2 = True\" script."
    epi "This will allow Renpy to access the OpenGL ES 2 rendering option for rendering low-level texture render images for Live 2D to work."
    epi "You can also place the \"define config.gl2 = True\" script in your main 'script.rpy' file, as long as you use it once per game."
    epi "However for the sake of this tutorial, we'll place the \"define config.gl2 = True\" script in the 'options.rpy' file."
    epi "Here's the fun part."
    epi "The next step is a bit tricky, so pay attention."
    epi "Before we dig any closer to display our Live2D characters in Renpy, let's open up the Cubism SDK Native folder."
    
    show rl2dcubismSDKzip at right with moveinright:
        yalign 1.0
        
    
    epi "Under the Cubism SDK Native folder, let's look under \"Resources.\""  
    epi "Now let's open the \"Hiyori\" folder."
    
    hide rl2dcubismSDKzip
    with moveoutright
    
    show rl2dgameB at right with moveinright:
        yalign 1.0
        
    
    epi "Pay close attention how the files are organized witin the 'Hiyori' folder."
    
    hide rl2dgameB
    with moveoutright
    
    show rl2dgameC at right with moveinright:
        yalign 1.0
        
    
    epi "What we see here is the .moc3, model3.json, and physics3.json files, along with the motions, expressions, and texture folder."
    epi "These are the necessary files for any Live2D character to display properly in Renpy's latest build version, whether you are using Live 2D Cubism 3 or Cubism 4."
    epi "Let's open up the motions folder, for example."
    
    hide rl2dgameC
    with moveoutright
    
    show rl2dgameD at right with moveinright:
        yalign 1.0
        
    
    epi "Inside the motions folder are various animation files that contains different types of animation expressions and movements for your Live2D character."
    epi "You'll notice each of the file starts with 'Live2D character name' and ends with _m01.motion3.json or _m02.motion3.json and so on."
    epi "Based on Renpy's Documentation, you will have to enter the motion animation indicator, i.e. m01, next to your character name when defining your character script."
    epi "This is also the same when defining static expressions for your Live 2D character, i.e. e01 or 'Blushing', etc."
    epi "Remember, if it's not done correctly, you will get the \"can only concatenate tuple (not as 'list') to tuple\" error message."
    # Add diagram pics
    epi "As a reminder, here are diagrams of how the \"Resources\" folder should be setup for both motions and expressions for each Live2D character."
    
    hide rl2dgameD
    with moveoutright
    
    show rl2dmotions at right with moveinright:
        yalign 0.5
    "Live2D Motions diagram."

    
    hide rl2dmotions
    with moveoutright

    
    show rl2dexpressions at right with moveinright:
        yalign 0.5
    
        
    "Live2D Expressions diagram."    
    hide rl2dexpressions
    with moveoutright
    
    
    epi "I will now show you how it's done."
    epi "First, copy the \"Resources\" folder from the Cubism SDK Native Folder and place it in your game project folder."
    
    show rl2dgameA at right with moveinright:
        yalign 1.0
        
        
    
    epi "You can also make a new folder and name it \"Resources\" and just copy the Hiyori character from the SDK folder for now."
    epi "One thing I want to add is make sure the letter 'R' is capitalized on 'Resources' when making a new folder or copying from the SDK into your game project folder."
    
    hide rl2dgameA
    with moveoutright
    
    epi "Now let's go to the main 'script.rpy' file."
    
    show rl2dchrscpt at right with moveinright
    
    epi "On the main 'script.rpy' file, type on the top exactly what I typed down on the picture above."
    epi "The first set declares the image to set your Live2D character, then equal sign to tell Renpy to open Live2D and find the character resource folder where it came from."
    epi "Renpy will search for the character's model3.json, if using Cubism 3, or model4.json when using Cubism 4."
    epi "Next to that is the base function."
    epi "The base function allow you to adjust the character's closeness value by placing it further away or near the viewscreen. The default value is 1.0"
    epi "Remember, the higher your base value, the farther your Live 2D character will be. The lower the base value, the closer your character will face the screen."
    epi "Right next to the base function is the loop function."
    epi "The loop function sets the animaton motion to loop continuously when assigning animation motion indicators."
    epi "If you want the character to play the animation motion once, set the loop to false, i.e. loop=False."
    epi "After your done declaring your Live2D character image, you can now define your Live2D character by typing like you would underneath it by following the script picture above."
    
    hide rl2dchrscpt
    with moveoutright
    
    show rl2dchrscpt2 at right with moveinright
    
    epi "The transform and effect properties should work the same way like other Renpy functions."
    epi "Now type in exactly of what I stated in the script picture above on the right."
    
    hide rl2dchrscpt2
    with moveoutright
    
    show Hiyori m01 at right
    with dissolve
    epi "...And presto, you did it!"
    hide Hiyori
    with dissolve
    epi "Now watch what happens when I do not type the motion indicators next to the defined character's name."
    
    hide Epsilon
    with dissolve

# Doing the error on purpose for tutorial purposes. This displays the concatenate tuple error message. Click ignore to move forward.
    
    show Hiyori
    with dissolve

# End of test error.
    
    show Epsilon m_sp_01 at left
    with dissolve
    
    epi "See what I mean?"
    
    menu:
        epi "Did I scare you?"
        with dissolve
        "Yes":
            jump yes
        "No":
            jump no

label yes:
    hide Epsilon
    with dissolve
    show Epsilon idle_01 at left
    with dissolve
    epi "Aww, I'm sorry."
    epi "I do apologize, if I scare you."
    epi "Don't worry, this is part of the lesson."
    epi "You always have to pay attention for any spelling errors and placing the motion or expression indicators next to your Live 2D characer."
    epi "Hopefully, you'll not have that error next time."
    jump normal
    
label no:
    hide Epsilon
    with dissolve
    show Epsilon idle_01 at left
    with dissolve
    epi "Excellent."
    epi "I'm glad that did not scare you."
    epi "I'm sure you did understand today's lesson when checking spelling errors and placing the motion or expression indicators next to your Live2D character."
    epi "Checking your work helps prevent errors like this next time."
    
label normal:
    epi "Ok, once again from the top."
    
    show rl2dchrscpt2 at right with moveinright
    epi "Type in again the Live2D character script on the top picture and we'll finish it off for the day."
    
    hide rl2dchrscpt2
    with moveoutright
    
    show Hiyori m01 at right
    with dissolve
    epi "Hey Hiyori."
    hyi "Hey Epi."
    epi "How's it going?"
    hyi "I'm doing fine. How about you?"
    epi "Same here, doing fine as well."
    epi "I'm here to teach a tutorial for all Renpy VN developers about Live2D."
    hyi "Sounds great!"
    hyi "Hope I'll be in your next visual novel project."
    hyi "Ok, it's great talking to you, Epi."
    epi "Same to you, Hiyori, you have a great day."
    hyi "You, too."
    hide Hiyori
    with dissolve
    
    epi "Ok, now that you've learn on how to place your Live2D character in Renpy, you are now ready display your Live2D characters in your next Renpy VN project."
    epi "Hope this tutorial helps all of you when making your Live2D characters come to life in Renpy."
    epi "This concludes the Renpy Live2D tutorial."
    epi "I wish everyone the best of luck when developing their visual novels with Live2D and Renpy."
    epi "Have a wonderful day."
    
    "---{b}END OF TUTORIAL{\b}---"
    
    return
