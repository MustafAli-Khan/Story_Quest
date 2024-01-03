OP = 0
print(r''' 

                                                             _____------------___
                                                    ._--':::::'-------____
                .___------__       /-.._.    _---_ '|:::::::::::::::::::::---
           ._--'.---::::::/ `      \ .-. '-'' *__*|/:::::::::::::::::::::::::
      .__-'  _-'::::::::/ ._------_| '_'  __--' _'/::::::::::::::::::::::::::
  _--'    _-'::::::::::|.'  ._----_\    -'  ._-':::::::::::::::::::::::::::::
       _-':::::::::::::\  .'       /  .__--' -':::::::::_--_:::::::::::.-----
   _-'::::::::::::::::::-_|       /    /   /::::::::::/      \:::::::/
  '::::::::::::::::::::::::----__-   .   .  |.--_:::/          \:::/
 .----_::::::::::::::::::::/                \  \ \/             \/
| ._.-_'-_:::.----.:::.:. . .    .         . |  \ 
 -_. -.\  \ .-.----..-----. .----. .---. .-.----:|\ 
  | | | |  | | .-. ||._-  || .-. || .-. | | .-. |\|
 .| |/__/  / | |  - .'.-. || '_' || | | | | | | |
|       ._- .| |.   | '-' |'___. || '_' |.| |.| |.
 -------    '---'    '----:--._| | '---' '---'---'
                          '______'.----_
                                  | ._.-_'-_
                                   -_. -.\  \ .-----. ----..---------.-.----.
                                    | | | |  ||._-  |  \  \'/ \ '\ /  | .-. |
                                   .| |/__/  /.'.-. |   \  ' . '' /   | | | |
                                  |       ._- | '-' |    \  / \  /   .| |.| |.                                                                                      
                                   -------     '----'     ''   ''    '---'---'         
                                                                                
                                                                                                                
_____________________________________________________________________________//\//\__/-\___||<_______________________________________________________________________                                                       
''')
print(
    "Welcome to the quest of the Dragon Dawn, \nThe world has suffered a fatal calamity, wrecking havoc on it. The Undead Ouroboros has plagued it for far to long.")
print(
    "\nOh child of Adam, would you embark on the quest of Dragon Dawn ? Would you free the world of the fangs of Undead Ouroboros ? Type 'Y' or 'N' to continue.")
choice = input("What do you choose ?")

if choice == "Y" or choice == "y":

    OP += 1
    print(
        "\nYou have chosen a path that demands courage, perseverance and most all of a pure heart go forth Oh child of Adam! you must find the Oracle, she will assist you in your quest.")
    print(
        "\nYou are teleported to the outskirts of the Netherwood, onyx-barked trees form an impenetrable canopy. \nSkeletal roots claw foul soil amid eerie whispers and ghostly fungi casting an otherworldly glow. \nTwisted creatures with unholy eyes emerge from shadows, thickening the air with malevolence.")
    print(
        "\nStumbling upon the forest floor, your gaze falls upon a hapless rabbit ensnared in the cruel clutches of a hidden trap.")
    print("\nWill you release the trapped rabbit ? Type 'Y' or 'N' to continue.")

    choice = input("What do you choose ?")

    if choice == "Y" or choice == "y":
        OP += 1
        print(r'''
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                  ___     ___
                 /   \   /   \       ___________________________
                /   / \_/ \   \     /                           \
                \__/\     /\__/    /  THANK YOU FOR SAVING ME :) \
                     \O O/         \      MY NAME IS NIBBLES     /
                  ___/ ^ \___      / ___________________________/
                     \___/        /_/
                     _/ \_
                  __//   \\__
                 /___\/_\/___\
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        ''')

        print("\nIn no time, Nibbles effortlessly hops into your heart, becoming an adorable and cherished friend.")
        print('''Nibbles, with a twitch of those fluffy ears, asks, "What's your name ?"\n ''')
        name = input("Enter your name.")
        print(f"Hi there, {name}, why did you came to the Netherwood ?")
        print("You tell Nibbles on every detail of your journey, from the twists in the plot to your relentless pursuit of the Oracle.\n")

        #   Stage 2

        print(r'''
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                  _
                 /_\
                 \__\     ___
                  \\\\   /   \        __________________________________
                   \\\\_/ \   \      /                                  \
                    \     /\__/     /    I know where the Oracle lives.  \
                     \O -/          \    It's a good thing u saved me    /
                  ___/ ^ \___       / __________________________________/
                     \___/         /_/
                     _/ \_
                  __//   \\__
                 /___\/_\/___\
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        
        ''')
        print("Follow me, I will lead you straight to the Oracle.")
        print("Exercise caution, for Netherwood teems with the malevolent minions of Undead Ouroboros.\n")
        print("Will you follow Nibbles ? type 'Y' or 'N' to continue.")
        choice = input("What do you choose ?")

        #   Stage 3

        if choice == "Y" or choice == "y":
            print(r''' 
                     _       _
                    / \     / \
                   {   }   {   }
                   {   {   }   }
                    \   \ /   /
                     \   Y   /
                     .-"`"`"-.
                   ,`         `.
                  /             \
                 /               \
                {     ;"";,       }
                {  /";`'`,;       }
                 \{  ;`,'`;.     /
                  {  }`""`  }   /}
                  {  }      {  //  
                  {||}      {  /
                  `"'       `"'
            
            ''')

        elif choice == "N" or choice == "n":
            print("exit")




    elif choice == "N" or choice == "n":
        OP -= 1
        print(
            "\nYou enter the forest, the haunting echo of the rabbit's final cry lingering in the air, a mournful melody that taints the serenity of the woods.")
        print(
            "You stumbled into a concealed pit, its jagged rocks below promising a grim demise in this treacherous and pitiful trap.\n")
        print(r'''
                     __.-/|
                     \`o_O'
                      =( )= +---------+
                        U|  | THE END |
              /\  /\   / |  +---------+
             ) /^\) ^\/ _)\      |
             )   /^\/   _) \     |
             )   _ /  / _)  \____|_
         /\  )/\/ ||  | )_)\____,|))
        <  >      |(,,) )__)     |
         ||      /    \)___)\_
         | \____(      )___) )____
          \______(_______;;;)__;;;)  ''')
elif choice == "N" or choice =="n":
    print(r'''
             __.-/|
             \`o_O'
              =( )= +---------+
                U|  | THE END |
      /\  /\   / |  +---------+
     ) /^\) ^\/ _)\      |
     )   /^\/   _) \     |
     )   _ /  / _)  \____|_
 /\  )/\/ ||  | )_)\____,|))
<  >      |(,,) )__)     |
 ||      /    \)___)\_
 | \____(      )___) )____
  \______(_______;;;)__;;;)  ''')
else:
    print(
        "\nOh, congratulations! Your intellectual prowess has dazzled the Council of MAK-Dragons. \nIn recognition of your genius, they've decided to graciously banish you to the nincompoop world. It's a realm where the air is infused with the fragrance of sheer cluelessness.\nBask in the glory of your newfound title as the sovereign ruler of the dum-dum dominion.")
