from screenFunctions import Screen
from objectContainer import objectContainer
import random
import time
import pygame

class levelLoader:
    def __init__(self, objectContainer):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("KINGDOM OF KROZ 2")

        self.objectContainer = objectContainer

        self.objectContainer.FP = [None] * 24
        self.objectContainer.Fast = chr(234)
        self.objectContainer.HideOpenWall = False
        self.objectContainer.LavaRate = 0
        self.objectContainer.GravOn = False
        self.objectContainer.GravRate = 0
        self.objectContainer.Sideways = False
        self.objectContainer.HideGems = False
        self.objectContainer.HideStairs = False
        self.objectContainer.HideOpenWall = False
        self.objectContainer.TreeRate = 0
        self.objectContainer.HideCreate = True
        self.objectContainer.MagicEWalls = True
        self.objectContainer.PF = [[0 for _ in range(26)] for _ in range(67)]
        self.objectContainer.XBot = 2
        self.objectContainer.YBot = 2
        self.objectContainer.XTop = 65
        self.objectContainer.YTop = 24
        self.objectContainer.TMax = 9
        self.objectContainer.FloorPattern = False
        self.objectContainer.T = [0] * (objectContainer.TMax + 1)
        self.objectContainer.SX = [0] * 1001
        self.objectContainer.SY = [0] * 1001
        self.objectContainer.MX = [0] * 1001
        self.objectContainer.MY = [0] * 1001
        self.objectContainer.FX = [0] * 1001
        self.objectContainer.FY = [0] * 1001
        self.objectContainer.BX = [0] * 1301
        self.objectContainer.BY = [0] * 1301
        self.objectContainer.YSize = 23
        self.objectContainer.XSize = 64
        self.objectContainer.HideLevel = False
        self.objectContainer.SNum = 0
        self.objectContainer.MNum = 0
        self.objectContainer.FNum = 0
        self.objectContainer.BNum = 0
        self.objectContainer.GenNum = 0
        self.objectContainer.PX = 0
        self.objectContainer.PY = 0
        self.objectContainer.Slow = '' #None
        self.objectContainer.Medium = '”' #None
        self.objectContainer.Fast = 'ê' #None
        self.objectContainer.Difficulty = 2 # This needs to be integrated with menus!!!
        self.objectContainer.FastPC = True # This needs to be integrated with menus!!!
        self.objectContainer.MixUp = False # ??????????
        self.objectContainer.GemColor = 0
        self.objectContainer.HideTrap = False
        self.objectContainer.Null = 0
        self.objectContainer.Block = chr(178)      # Character code 178
        self.objectContainer.Whip = chr(244)       # Character code 244
        self.objectContainer.Stairs = chr(240)     # Character code 240
        self.objectContainer.Chest = chr(67)       # Character code 67
        self.objectContainer.SlowTime = chr(232)  # Character code 232
        self.objectContainer.Gem = 'ø'          # Character code 4
        self.objectContainer.Invisible = ' ' # chr(173)   # Character code 173
        self.objectContainer.Teleport = chr(24)    # Character code 24
        self.objectContainer.Key = chr(140)        # Character code 140
        self.objectContainer.Door = chr(236)       # Character code 236
        self.objectContainer.Wall = chr(219)       # Character code 219
        self.objectContainer.SpeedTime = chr(233) # Character code 233
        self.objectContainer.Trap = chr(249)       # Character code 249
        self.objectContainer.River = chr(247)      # Character code 247
        self.objectContainer.Power = chr(9)        # Character code 9
        self.objectContainer.Forest = chr(219)     # Character code 219
        self.objectContainer.Tree = chr(5)         # Character code 5
        self.objectContainer.Bomb = chr(157)       # Character code 157
        self.objectContainer.Lava = chr(178)       # Character code 178
        self.objectContainer.Pit = chr(176)        # Character code 176
        self.objectContainer.Tome = chr(12)        # Character code 12
        self.objectContainer.Tunnel = chr(239)     # Character code 239
        self.objectContainer.Freeze = chr(159)     # Character code 159
        self.objectContainer.Nugget = chr(15)      # Character code 15
        self.objectContainer.Quake = chr(0)        # Character code 0
        self.objectContainer.IBlock = chr(30)      # Character code 30
        self.objectContainer.IWall = chr(0)        # Character code 0
        self.objectContainer.IDoor = chr(0)        # Character code 0
        self.objectContainer.Stop = chr(0)         # Character code 0
        self.objectContainer.Trap2 = chr(0)        # Character code 0
        self.objectContainer.Zap = chr(30)         # Character code 30
        self.objectContainer.Create = chr(31)      # Character code 31
        self.objectContainer.Generator = chr(6)    # Character code 6
        self.objectContainer.Trap3 = chr(0)        # Character code 0
        self.objectContainer.MBlock = chr(178)     # Character code 178
        self.objectContainer.Trap4 = chr(0)        # Character code 0
        self.objectContainer.Player = '' #chr(2)       # Character code 2
        self.objectContainer.Show_Gems = chr(0)    # Character code 0
        self.objectContainer.Tablet = chr(254)     # Character code 254
        self.objectContainer.ZBlock = chr(178)     # Character code 178
        self.objectContainer.BlockSpell = chr(0)  # Character code 0
        self.objectContainer.Chance = chr(63)      # Character code 63
        self.objectContainer.Statue = chr(1)       # Character code 1
        self.objectContainer.WallVanish = chr(0)  # Character code 0
        self.objectContainer.K = chr(0)            # Placeholder for K
        self.objectContainer.R = chr(0)            # Placeholder for R
        self.objectContainer.O = chr(0)            # Placeholder for O
        self.objectContainer.Z = chr(0)            # Placeholder for Z
        self.objectContainer.OWall1 = chr(219)     # Character code 219
        self.objectContainer.OWall2 = chr(219)     # Character code 219
        self.objectContainer.OWall3 = chr(219)     # Character code 219
        self.objectContainer.CWall1 = chr(0)       # Character code 0
        self.objectContainer.CWall2 = chr(0)       # Character code 0
        self.objectContainer.CWall3 = chr(0)       # Character code 0
        self.objectContainer.OSpell1 = chr(127)    # Character code 127
        self.objectContainer.OSpell2 = chr(127)    # Character code 127
        self.objectContainer.OSpell3 = chr(127)    # Character code 127
        self.objectContainer.CSpell1 = chr(0)      # Character code 0
        self.objectContainer.CSpell2 = chr(0)      # Character code 0
        self.objectContainer.CSpell3 = chr(0)      # Character code 0
        self.objectContainer.GBlock = chr(178)     # Character code 178
        self.objectContainer.Rock = chr(79)        # Character code 79
        self.objectContainer.EWall = chr(88)       # Character code 88
        self.objectContainer.Trap5 = chr(0)        # Character code 0
        self.objectContainer.TBlock = chr(0)       # Character code 0
        self.objectContainer.TRock = chr(0)        # Character code 0
        self.objectContainer.TGem = chr(0)         # Character code 0
        self.objectContainer.TBlind = chr(0)       # Character code 0
        self.objectContainer.TWhip = chr(0)        # Character code 0
        self.objectContainer.TGold = chr(0)        # Character code 0
        self.objectContainer.TTree = chr(0)        # Character code 0
        self.objectContainer.Rope = chr(179)       # Character code 179
        self.objectContainer.DropRope = chr(25)   # Character code 25
        self.objectContainer.Amulet = chr(12)      # Character code 12
        self.objectContainer.ShootRight = chr(26) # Character code 26
        self.objectContainer.ShootLeft = chr(27)  # Character code 27
        self.objectContainer.Trap6 = chr(0)        # Character code 0
        self.objectContainer.Trap7 = chr(0)        # Character code 0
        self.objectContainer.Trap8 = chr(0)        # Character code 0
        self.objectContainer.Trap9 = chr(0)        # Character code 0
        self.objectContainer.Trap10 = chr(0)       # Character code 0
        self.objectContainer.Trap11 = chr(0)       # Character code 0
        self.objectContainer.Trap12 = chr(0)       # Character code 0
        self.objectContainer.Trap13 = chr(0)       # Character code 0

        # Message constant
        self.objectContainer.Message = chr(5)      # Character code 5

        # Start on level 1
        self.objectContainer.LevelNumber = 1





    # Return game level of levelNumber
    def Level(self, levelNumber):
        # case statement
        switcher = {
            1: self.Level1,
            2: self.Level2,
            # No level 3
            4: self.Level4,
            # No level 5
            6: self.Level6,
            # No level 7
            8: self.Level8,
            # No level 9
            10: self.Level10,
            # No level 11
            12: self.Level12,
            # No level 13
            14: self.Level14,
            # No level 15
            16: self.Level16,
            # No level 17
            18: self.Level18,
            # No level 19
            20: self.Level20,
            # No level 21
            22: self.Level22,
            # No level 23
            24: self.Level24,
            25: self.Level25,
        }
    
        # Get the function from the switcher dictionary
        level_function = switcher.get(levelNumber, None)
    
        if level_function:
            return level_function()  # Call the function with the screen argument
        else:
            return "Invalid option"
    
    
    # Return game level 1
    def Level1(self):
        global objectContainer
        self.objectContainer.FP[1]  = 'W W W W             2 2 2 2 2  C  2 2 2 2 2              W W W W'
        self.objectContainer.FP[2]  = 'XXXXXXXXXXXXXXXXXXX###########   ###########XXXXXXXXXXXXXXXXXXXX'
        self.objectContainer.FP[3]  = ' 1           1                               1                  '
        self.objectContainer.FP[4]  = '                                    1            XX         1   '
        self.objectContainer.FP[5]  = '       1            1                           XXXX            '
        self.objectContainer.FP[6]  = '#        XX                    +                 XX            #'
        self.objectContainer.FP[7]  = '##      XXXX  1                +          1          1        ##'
        self.objectContainer.FP[8]  = 'T##      XX               2    +    2                        ##T'
        self.objectContainer.FP[9]  = 'T1##                       W   +   W                        ##1T'
        self.objectContainer.FP[10] = 'T########X                 WX     XW             1    X########T'
        self.objectContainer.FP[11] = '.        X                2WX  P  XW2                 X        .'
        self.objectContainer.FP[12] = 'T########X         1       WX     XW                  X########T'
        self.objectContainer.FP[13] = 'T1##                       W   +   W         1              ##1T'
        self.objectContainer.FP[14] = 'T##                       2    +    2                        ##T'
        self.objectContainer.FP[15] = '##   1                         +                      XX      ##'
        self.objectContainer.FP[16] = '#       XX      1              +                 1   XXXX     1#'
        self.objectContainer.FP[17] = '       XXXX                 ##   ##                   XX        '
        self.objectContainer.FP[18] = '1       XX                 ##     ##     1        1           1 '
        self.objectContainer.FP[19] = '                    1#######       ########                     '
        self.objectContainer.FP[20] = '    1         ########11111  +++++  111111########              '
        self.objectContainer.FP[21] = 'WW     ########+++++        #######         WWWWW########1    WW'
        self.objectContainer.FP[22] = '########¯                    2 2 2                     C########'
        self.objectContainer.FP[23] = 'L2  +  X      #kingdom#of#kroz#ii#by#scott#miller#      X  +  2L'
        self.objectContainer.Fast = chr(234)
        self.Convert_Format()
    
    # Return game level 2
    def Level2(self):
        global objectContainer
        self.objectContainer.FP[1]  = '                                                           .   '
        self.objectContainer.FP[2]  = '  2#############################K############################   '
        self.objectContainer.FP[3]  = '   ##  2    2   2 2    2   2  ###  2  2   2    2    2    2##   '
        self.objectContainer.FP[4]  = '  2##+#2   2   2    2  2 2   2  2 2  2   2 2   2   2    2  ##   '
        self.objectContainer.FP[5]  = '   ##+#   2  2    2   2   2   2    2    2  2    2    2   2 ##   '
        self.objectContainer.FP[6]  = '  2##+# 2    2  2   2  2 2 2 2  2 2  2 2 2   2    2   2   2##   '
        self.objectContainer.FP[7]  = '   ##+#2   2  2   2                            2   2   2   ## W '
        self.objectContainer.FP[8]  = '  2##+#  2   2   2   XXXXXXXXXXXXXXXXXXXXXXX  2    2  2   2##@@@'
        self.objectContainer.FP[9]  = '   ##+#2   2  2   2  XXXXXXXXXXXXXXXXXXXXXXX    2   2  2   ##   '
        self.objectContainer.FP[10] = '  2##+# 2   2  2 2   XXXXXXXXXXXXXXXXXXXXXXX   2  2   2  2 ##   '
        self.objectContainer.FP[11] = '   ##+#   2 2 2   2  XXXXXX    -+-    XXXXXX  2 2    2  2  ##   '
        self.objectContainer.FP[12] = '  2##+#2   2   2 2   XXXXXX1   -P-   1XXXXXX  2  2 2   2 2 ##   '
        self.objectContainer.FP[13] = '   ##+#  2  2  2  2  XXXXXX    -+-    XXXXXX   2  2 2     2##   '
        self.objectContainer.FP[14] = '  2##+# 2 2  2  2    XXXXXXXXXXXXXXXXXXXXXXX  2   2   2 2  ##   '
        self.objectContainer.FP[15] = '   ##+#2 2    2   2  XXXXXXXXXXXXXXXXXXXXXXX    2  2   2 2 ##   '
        self.objectContainer.FP[16] = '  2##+# 2  2  2  2   XXXXXXXXXXXXXXXXXXXXXXX   2    2 2 2  ##   '
        self.objectContainer.FP[17] = '   ##+#  2  2 2   2                           2  2   2   2 ##   '
        self.objectContainer.FP[18] = '  2##+#2   2    2   2 2  2  2  2 2  2 2  2  2   2   2  2  2##   '
        self.objectContainer.FP[19] = '   ##+# 2    2  2  2 2  2   2   2   2  2  2    2    2   2  ##   '
        self.objectContainer.FP[20] = '  2##3#   2   2   2   2   2   2   2   2 2    2    2   2   2##@@@'
        self.objectContainer.FP[21] = '   ##T#2   2     2  2  2 2   2 ###   2   2 2  2    2   2   ##222'
        self.objectContainer.FP[22] = '   #############################S#######################XXX##@@@'
        self.objectContainer.FP[23] = '                                                          I##LLL'
        self.objectContainer.Fast = chr(234)
        self.Convert_Format()
    
    # Return game level 4
    def Level4(self):
        global objectContainer
        self.objectContainer.FP[1]  = '-..............................3#1#2#3##------;------------;----'
        self.objectContainer.FP[2]  = '-##############################-##1#2#3#-######################-'
        self.objectContainer.FP[3]  = '-#.....----......- I#S###### ##K###1#2#3-#///////1///////////1//'
        self.objectContainer.FP[4]  = '-#.-..-....-....-.# # I####1# ######1#2#-#\\1\\\\\\\\\\\\\\\\\\\\\\\\\\1\\\\\\\\\\\\'
        self.objectContainer.FP[5]  = '-#-.-..-..-.....-.# # # ### ## ##1###1#2-#/////1////////////////'
        self.objectContainer.FP[6]  = '-#-.-.-..-..---..-# # ## # ##1## # ###1#-#CCC\\\\\\\\\\\\\\\\\\1\\\\\\\\\\\\1\\\\'
        self.objectContainer.FP[7]  = '-#-.-..-.-.-..-..-# # ### ####  ### K##1-#CCC/////1//////1/////K'
        self.objectContainer.FP[8]  = '-#-..--...-....--.# # ##################-#######################'
        self.objectContainer.FP[9]  = '-#-################                                           à '
        self.objectContainer.FP[10] = '---3333333333-CC### #F######################XXXXXXXX###à####-##+'
        self.objectContainer.FP[11] = '################## ###------------------®###############2###-##+'
        self.objectContainer.FP[12] = 'big#######     ## ####22222222222222222#-##-----------###2##-##K'
        self.objectContainer.FP[13] = 'trouble## RRRRR  #######################-##-####U####-####2####+'
        self.objectContainer.FP[14] = '######## RRRKRRRR #########$;$$$$$$3$T##-##-----------#####2###3'
        self.objectContainer.FP[15] = '+++++### RR 2 2 RR ####Z###$############-##############Q###2###'
        self.objectContainer.FP[16] = '++T++## RR 2 P  2RR ### #-U--------------###TT.TT####----####2##'
        self.objectContainer.FP[17] = '+++++## RR2   2 RR ####1#-####################;###############2#'
        self.objectContainer.FP[18] = '#O#O#### RR 2  2RR #3## #C####3#3#3#3#3#3#3#3#3#3#3#3#3#3#3#3##D'
        self.objectContainer.FP[19] = '#X#X##### RRR2CRR ##3## # ###@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@###D'
        self.objectContainer.FP[20] = '#X#X###### RRRRRR ##3## #3##@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@##K#D'
        self.objectContainer.FP[21] = '-----; #### RRR  ### ## ###@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#D'
        self.objectContainer.FP[22] = '-----# #####   # ##W W# ##@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@##@#D'
        self.objectContainer.FP[23] = '22222#      #####       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#L'
        self.objectContainer.Fast = chr(234)
        self.Convert_Format()
    
    # Return game level 6
    def Level6(self):
        global objectContainer
        self.objectContainer.FP[1]  = '---###########RRRRR##W        ############W////1/C//\\//\\\\\\\\\\\\\\\\\\'
        self.objectContainer.FP[2]  = '-U---------Z###RRRRR##7######   ##KKô   Z##-//////\\///1/\\\\\\\\\\\\U\\'
        self.objectContainer.FP[3]  = '---###########RRRRR##7####### P ######## ###-////////\\///\\\\1\\\\\\\\'
        self.objectContainer.FP[4]  = '@#############RRRRR#7####                ####-///\\/////////\\\\\\\\\\'
        self.objectContainer.FP[5]  = '@2#------.###RRRRR##7#W3; ############## #####-////1//\\//1///\\\\\\'
        self.objectContainer.FP[6]  = '@##;-;###.##RRRRR##7##W3; #WWWWWWWWWWW## #2####--//////////\\///\\'
        self.objectContainer.FP[7]  = '@2#-;;##..##RRRRR##7##W3; ######-####### ##2#####-/////\\/////1//'
        self.objectContainer.FP[8]  = '@##;-;##..-##RRRRR##7#### #11111111111## ###2##2##-/////1/////\\/'
        self.objectContainer.FP[9]  = '@2#;;-##..#D##RRRRR##7##T #11111111111## #2##2##2##--///////\\///'
        self.objectContainer.FP[10] = '@##;;;##..#D###RRRRR##7####11111111111## ##2##2##2###---///////1'
        self.objectContainer.FP[11] = '@2#-;;##..#KK###RRRRR##7###11111111111## ###)##)##)#####--////\\/'
        self.objectContainer.FP[12] = '@##-;;##..#KK##RRRRRRR#7###11111B11111----)))))))))))#####---///'
        self.objectContainer.FP[13] = '@2#;;;##22####RRRR#RRR##7##11111111111##############)########--/'
        self.objectContainer.FP[14] = '@##;;-##22###RRRR###RRR##7#11111111111#?##---#*YYYY-63333####D#'
        self.objectContainer.FP[15] = '@2#;-;##22##RRRR##L##RRR#7#11111111111#O#T#-#-#*YYYY-63333---#D#'
        self.objectContainer.FP[16] = '@##;;;##22#RRRR##DD##RRR#7#11111111111#O#-4-#-#*YYYY-63333-#-4-#'
        self.objectContainer.FP[17] = '@2#;-;##-##RRRR#DDD#RRR##7###########-#O#-#-#-#*YYYY-63333-#-#-#'
        self.objectContainer.FP[18] = '@##;;-##C#RRRR##DDD##RRR##7###+++++##-#O#-#-#-#*YYYY-63333-#-#-#'
        self.objectContainer.FP[19] = '@2#;;;##H##RRRR#DDDD##RRR##7##+++++##-#O#-#-#-#*YYYY-63333-#-#-#'
        self.objectContainer.FP[20] = '@##;-;####RRRR##44444##RRR##7###.####-#O#-#-#-#*YYYY-63333-#-#-#'
        self.objectContainer.FP[21] = '@2#-;;###RRRR##ñññññññ##RRR#7###.#K-#-#O#-#-#-#*YYYY-63333-#-#-#'
        self.objectContainer.FP[22] = '@###-###RRRR##X--------#RRR##ô##.#--#-#-#---#-######-#####-#---#'
        self.objectContainer.FP[23] = '-----##RRRR##%X---U----##RRR#K##--------#111#--------------#111#'
        self.objectContainer.Fast = chr(234)
        self.objectContainer.HideOpenWall = True
        self.Convert_Format()
    
    # Return game level 8
    def Level8(self):
        global objectContainer
        self.objectContainer.FP[1]  = '-------¼--------44---³³³³³³³³³³³³º---º³³³³³³³³³³³------K---¹;-U-'
        self.objectContainer.FP[2]  = 'XXXXXXX-XXX-----44---      -----------------    ----#######-;---'
        self.objectContainer.FP[3]  = '--------------71#####       ---------------      #####¹-----;;;;'
        self.objectContainer.FP[4]  = 'K------------71###           -------------          #####³##; P '
        self.objectContainer.FP[5]  = '#17---------71####****        -----------       ****##----W;   '
        self.objectContainer.FP[6]  = '##17-------71#####*###         ----K----        ###*##³#####;   '
        self.objectContainer.FP[7]  = '###17-----71######*#             #####            #*## 1   7;   '
        self.objectContainer.FP[8]  = '####17---71#######*;     W    W    W    W    W    :*#######³;   '
        self.objectContainer.FP[9]  = '#####17-71########*#444444444444444444444444444444#*##ñ     ;   '
        self.objectContainer.FP[10] = '######---#########*#                              #*##444³##;   '
        self.objectContainer.FP[11] = '#######ä##########U#                              #!##     ;   '
        self.objectContainer.FP[12] = '----------------####                              ######³###;   '
        self.objectContainer.FP[13] = '----------------##VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV##     ;   '
        self.objectContainer.FP[14] = '----------------##VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV###³####;   '
        self.objectContainer.FP[15] = '»ä-------------ò######################################      ;   '
        self.objectContainer.FP[16] = '5555555555555555#############the#lava#pit#################³#;   '
        self.objectContainer.FP[17] = '            -------         ------------***********-##+   C;   '
        self.objectContainer.FP[18] = '              000            ---»######-###########-####³###;   '
        self.objectContainer.FP[19] = '                                ------7##LL-D-D-D-³##      ;   '
        self.objectContainer.FP[20] = '                                     ##-###########³#######³;   '
        self.objectContainer.FP[21] = '                                     ##-7  1   TTT7³##     ;   '
        self.objectContainer.FP[22] = '¼       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1##--#########³###³####;   '
        self.objectContainer.FP[23] = '###this#is#the#first#sideways#level####111111111  äC##        '
        self.objectContainer.Fast = chr(234)
        self.objectContainer.LavaFlow = True
        self.objectContainer.LavaRate = 75
        self.objectContainer.GravOn = True
        self.objectContainer.GravRate = 0
        self.objectContainer.Sideways = True
        self.Convert_Format()
    
    # Return game level 10
    def Level10(self):
        global objectContainer
        self.objectContainer.FP[1]  = '!+-----+----+------+##%VVOOOOO44U44OOOOVV%##3333333333333333333K'
        self.objectContainer.FP[2]  = '-----+--+-----+-----##VVVOOOOO44444OOOOVVV##66666666666666666663'
        self.objectContainer.FP[3]  = '+--+------+--------+##OOOOOOOO##5##OOOOOOO##                  63'
        self.objectContainer.FP[4]  = '-----+-------+----+-##OOOOOOOO##?##OOOOOOO##                  63'
        self.objectContainer.FP[5]  = '---+-----+------+---##VVVOOOOOO###OOOOOVVV##XXXXX             63'
        self.objectContainer.FP[6]  = '-+----+-------+-----##CVVOOOOOOO#OOOOOOVVC##XXXXX             63'
        self.objectContainer.FP[7]  = '+-------+--------+-U##CVVOOOOOOOOOOOOOOVVC##UXXXX             63'
        self.objectContainer.FP[8]  = '###############################OOO##############################'
        self.objectContainer.FP[9]  = 'MMMMMMMMMMMMMMMMMMMM##S                  S##11111111111111111111'
        self.objectContainer.FP[10] = 'MMMMMMMMMMMMMMMMMMMM##                    ##11111111111111111111'
        self.objectContainer.FP[11] = '@@@@@@@@@@@@@@@@@@@@##         000        ##11111111111111111111'
        self.objectContainer.FP[12] = 'K@@@@@@@@@@@@W                 0P0        HB11111111111B1111111ñ'
        self.objectContainer.FP[13] = '@@@@@@@@@@@@@@@@@@@@##         000        ##11111111111111111111'
        self.objectContainer.FP[14] = 'MMMMMMMMMMMMMMMMMMMM##                    ##11111111111111111111'
        self.objectContainer.FP[15] = 'MMMMMMMMMMMMMMMMMMMM##S                  S##11111111111111111111'
        self.objectContainer.FP[16] = '###############################~~~##############################'
        self.objectContainer.FP[17] = '111111111111111111-U##C00000000---0-000---##U-))I)))))))333))))-'
        self.objectContainer.FP[18] = '1(((((((((((((((((--##-0000H---0000---0-0-##--)I)))))))333))))-*'
        self.objectContainer.FP[19] = '1(((((((TTT((((((((1##00000000 00000000000##))I)))))))333))))-*I'
        self.objectContainer.FP[20] = '1(((((((TTT((((((((1##-0-00000000000000-00##)I)))))))333))))-*I*'
        self.objectContainer.FP[21] = '1(((((((TTT((((((((1##00-0-----0000000<[|"##I)))))))333))))-*I*I'
        self.objectContainer.FP[22] = '1((((((((((((((((((1##-#####################)))))))333))))-*I*I*'
        self.objectContainer.FP[23] = 'ó1111111111111111111##C-------D-D-D]]Eò&LL##K)))))333))))-*I*I*C'
        self.objectContainer.Fast = chr(234)
        self.objectContainer.HideGems = True
        self.Convert_Format()
    
    # Return game level 12
    def Level12(self):
        global objectContainer
        self.objectContainer.FP[1]  = 'LLL##U##@@@@@@@@@@@|000---0000000000000000-0--00000000VVV000Y-0V'
        self.objectContainer.FP[2]  = '```##-##@00000000000000---0000222222220---0000-00000000000--Y-0V'
        self.objectContainer.FP[3]  = '```##K##@@022222222K000---0000-0000000000-0000-0)))))YYYW-W0Y-0V'
        self.objectContainer.FP[4]  = '```##6##@@@222222222000---000U*******00000000000)))0000000000-00'
        self.objectContainer.FP[5]  = '```##6##@@@222222222000---000000000000000000000000222222--000---'
        self.objectContainer.FP[6]  = '```##6##@@0222222222000---(((((((((((((((ñ(((((000222222-C00000-'
        self.objectContainer.FP[7]  = '333##6##@00000000000000---00004444444444444444(0000000000000000-'
        self.objectContainer.FP[8]  = '333##6##3CCC....0---------00022222222222222222(K(---------------'
        self.objectContainer.FP[9]  = '$$$##6##000000000000000---00000000000000000000000000000000000000'
        self.objectContainer.FP[10] = '   0--00000000000000000---000000000000000000000===============--'
        self.objectContainer.FP[11] = ' P 00-00+02222222220--------------------------0="===-=--===-==-='
        self.objectContainer.FP[12] = '$$$00-00+02222222220-00---0000000000000000000-0==I=-=-==-=-=-==-'
        self.objectContainer.FP[13] = ' ! 00-00+02222222220-00-Z-0000000000000000000-0=H==-===T==-==--='
        self.objectContainer.FP[14] = '00000-00[02222B22220-00---00----03333333CC----0==I==-===-==-===='
        self.objectContainer.FP[15] = '0--00-00+02222222220-00---00-0000000000000000-0===--==-==-==--=='
        self.objectContainer.FP[16] = '-0000-00+02222222220-00---00-0000000000000000-0==-===-=-=-====-='
        self.objectContainer.FP[17] = '00000-00+02222222220W00---00-----0--------000-0=-==--==-=-=--=T='
        self.objectContainer.FP[18] = '0--00-00000000000000000---000000000001110-000-0==T-===-===-==-=='
        self.objectContainer.FP[19] = '00000-00000000000000000---000000000001110-00000=======-========='
        self.objectContainer.FP[20] = '--000----------------- ---0WWWWWWWWK01110-000-000000000000000000'
        self.objectContainer.FP[21] = '00000-00000000000000000---000-00000001110-000K--<000OO000OOOOOó*'
        self.objectContainer.FP[22] = '--000-000000~~~0000000#---#00-00000000000-000000000000OOOO000000'
        self.objectContainer.FP[23] = '00C000000********3000##VVV##0-------------00000000bouldervilleÃ0'
        self.objectContainer.Fast = chr(234)
        self.objectContainer.LavaFlow = True
        self.objectContainer.LavaRate = 30;
        self.Convert_Format()
    
    # Return game level 14
    def Level14(self):
        global objectContainer
        self.objectContainer.FP[1]  = '###<@@@@@@@@@@@@@@@@@@@@@@@@@#one#@@@@@@@@@@@@@@@@@@@@@@@@@FK###'
        self.objectContainer.FP[2]  = 'Kö###@@@@@@@@@@@@@@@@@@@@@@@@@;!:@@@@@@@@@@@@@@@@@@@@@@@@@@###$['
        self.objectContainer.FP[3]  = 'öö((###@@@@@@@@@@@@@@@@@@@@@@@:::@@@@@@@@@@@@@@@@@@@@@@@@###$$$$'
        self.objectContainer.FP[4]  = '((((((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###$$$$$$'
        self.objectContainer.FP[5]  = '(((((((2###222222222222222222222222222222222222222222###2$$$$$$$'
        self.objectContainer.FP[6]  = '(((((((2((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###$$2$$$$$$$'
        self.objectContainer.FP[7]  = '(((((((2((((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###$$$$2$$$$$$$'
        self.objectContainer.FP[8]  = '(((((((2((((((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###$$$$$$2$$$$$$$'
        self.objectContainer.FP[9]  = 'DD##(((2((((((((###@@@@@@@@@@@@@@@@@@@@@@@@@@###$$$$$$$$2$$$####'
        self.objectContainer.FP[10] = 'DD#f(((2(((((((((##############77##############$$$$$$$$$2$$$##CC'
        self.objectContainer.FP[11] = 'DD#o(((2((((((((ö##2------------------------2##ô$$$$$$$$2$$$t#àà'
        self.objectContainer.FP[12] = 'DD#u(((2((((((((ö----------F---P----S--------88ô$$$$$$$$2$$$w#MM'
        self.objectContainer.FP[13] = '&&#r(((2((((((((ö##2------------------------2##ô$$$$$$$$2$$$o#MM'
        self.objectContainer.FP[14] = 'LL##(((2(((((((((##############99##############$$$$$$$$$2$$$##MM'
        self.objectContainer.FP[15] = '####(((2((((((((###)))))))))))õõõõ)))))))))))###$$$$$$$$2$$$##àà'
        self.objectContainer.FP[16] = '(((((((2((((((###))))))))))))))))))))))))))))))###$$$$$$2$$$$$$$'
        self.objectContainer.FP[17] = '(((((((2((((###))))))))))))))))))))))))))))))))))###$$$$2$$$$$$$'
        self.objectContainer.FP[18] = '(((((((2((###))))))))))))))))))))))))))))))))))))))###$$2$$$$$$$'
        self.objectContainer.FP[19] = '(((((((2###))))))))))))))))))))))))))))))))))))))))))###2$$$$$$$'
        self.objectContainer.FP[20] = '((((((###2222222222222222222222222222222222222222222222###$$$$$$'
        self.objectContainer.FP[21] = '((((###))))))))))))))))))))))))))))))))))))))))))))))))))###$$ôô'
        self.objectContainer.FP[22] = '"(###))))))))))))))))))))))))))))))))))))))))))))))))))))))###ôK'
        self.objectContainer.FP[23] = '###Kõ)))))))))))))))))))))))#three#))))))))))))))))))))))))F|###'
        self.objectContainer.Fast = chr(234)
        self.Convert_Format()
    
    # Return game level 16
    def Level16(self):
        global objectContainer
        self.objectContainer.FP[1]  = '##tunnels#of#kroz###########-P--################################'
        self.objectContainer.FP[2]  = '########################X###----######X##---------------##X####'
        self.objectContainer.FP[3]  = '############################----#########----------------#######'
        self.objectContainer.FP[4]  = 'L---N----H######ò  ò ò######-----------------########----#######'
        self.objectContainer.FP[5]  = 'L---N-----##X###  CC  555555-----------------#####X##1111#######'
        self.objectContainer.FP[6]  = '######----######ò ò  ò###############################----#####X#'
        self.objectContainer.FP[7]  = '######1111###########################################1111#######'
        self.objectContainer.FP[8]  = '#X####----##############X#######magic#####X##########----#######'
        self.objectContainer.FP[9]  = '######1111####################----##############----N-----#'
        self.objectContainer.FP[10] = '######----####################----K----##############----N-----#'
        self.objectContainer.FP[11] = '######1111#######X############----#########X##########----#'
        self.objectContainer.FP[12] = '######----########################-########################1111#'
        self.objectContainer.FP[13] = '######1111################X#######-########################----#'
        self.objectContainer.FP[14] = '######----########################---------N-------------------#'
        self.objectContainer.FP[15] = '###X##----##########################################-----------#'
        self.objectContainer.FP[16] = '######---------------7ñ########################X####----########'
        self.objectContainer.FP[17] = '######---------------7-444444444444444444###########1111########'
        self.objectContainer.FP[18] = '#####O#############--77##################444########----#####X##'
        self.objectContainer.FP[19] = '####O##############1111#############X#######4ô%-####1111########'
        self.objectContainer.FP[20] = '###O#####XXX#######----#############################----########'
        self.objectContainer.FP[21] = '##O#####X###Q######-------N------`----------------------########'
        self.objectContainer.FP[22] = '##O##OOO###########-------N------`---------------------##X#####'
        self.objectContainer.FP[23] = '###OO###########################################################'
        self.objectContainer.Fast = chr(234)
        self.objectContainer.HideStairs = True
        self.objectContainer.HideOpenWall = True
        self.Convert_Format()
    
    # Return game level 18
    def Level18(self):
        global objectContainer
        self.objectContainer.FP[1]  = '###########klose#enkounters#of#the#krazy#kubikal#kindÃ##########'
        self.objectContainer.FP[2]  = '3                               P                              3'
        self.objectContainer.FP[3]  = '##-##############:########:#######:###########:##############:##'
        self.objectContainer.FP[4]  = 'XXXXXXXXX##~W~W~W~W~##-M----M.--$$$$$$$$$-9/-/\\--\\-|##---ò---'
        self.objectContainer.FP[5]  = '---------##*~*~*~*~*##-.-M--##$$$$$$$$$##\\--/-\\-/\\##YYYYYYYYY'
        self.objectContainer.FP[6]  = 'MMMMMMMMM##~W~W~W~W~##M---.-M-##111111111##-/-\\/--/-##((((((((('
        self.objectContainer.FP[7]  = ')))))))))##*~*~*~*~*##.-.--.##222222222##/\\--\\-\\-/##((((((((('
        self.objectContainer.FP[8]  = 'C))))))))--~W~W~W~W~##ó.----M##333333333##ü-//-\\-/-9-((((((((('
        self.objectContainer.FP[9]  = '###################-################################9##55555555-'
        self.objectContainer.FP[10] = '----##YYYYYYYYY##222222222------0---W##RRRRRRRRR##MMMMMMMMM'
        self.objectContainer.FP[11] = '-----------YYYYYYYYY##@@@@@@@@@##---000---##RXXXXXXXR##MMMMMMMMM'
        self.objectContainer.FP[12] = 'XXXXXXXXX##YYYYYYYYY##@@@@@@@@@##--00G00--##RXXXKXXXR##MMMMMMMMM'
        self.objectContainer.FP[13] = '---------##YYYYYYYYY##@@XXX@@@@##---000---##RXXXXXXXR##MMMMMMMMM'
        self.objectContainer.FP[14] = '##YYYYYYYYK##@@XZX@@@@##----0---W##RRRRRRRRR##MMMMMMMMK'
        self.objectContainer.FP[15] = '-#####################-##########ô##################H##Z########'
        self.objectContainer.FP[16] = '~-~[~-~-~##WWW......à1:1:1:1:1:##-773C7--7##=--=I==-=##ááááááY0"'
        self.objectContainer.FP[17] = '-~-~-~-~-##WWW......##1:1:1:1:1##7-777-77-##!==-=--==##ááááááY00'
        self.objectContainer.FP[18] = '~-~-~-~-~##.........##:1:1:1:1:##-77--77-7##=======-=##ááááááYYY'
        self.objectContainer.FP[19] = '-~-~-~-~-##.........##1:1:1:1:1##7-7-77-77##-==-=-==I##ááááááááá'
        self.objectContainer.FP[20] = 'K-~-~-~-~-à..<......##:1:1:1:1ñ##77-7777---I=--=-=--=##222222222'
        self.objectContainer.FP[21] = '############################################################44##'
        self.objectContainer.FP[22] = 'LL---V--V-VV-V--VV---D-----D----D----D--66333333333333333-WWWW'
        self.objectContainer.FP[23] = 'LL--V-VV-V--V-VV--V--D-----D----D----D--66YYYYYYYYYYYYYYYYYYYY'
        self.objectContainer.Fast = chr(234)
        self.objectContainer.TreeRate = 35
        self.Convert_Format()
    
    # Return game level 20
    def Level20(self):
        global objectContainer
        self.objectContainer.FP[1]  = '###key#shop###MTMMMMMMMMMMMMMMMMMMMMM-----MMMMMMMMMMMM-MM--!##LL'
        self.objectContainer.FP[2]  = '##Káà44@@@@@##MMMMMMMMMMMMMMMMMMMMMM-MMMMM-MMMMMMMMMM-M-M-P-##LL'
        self.objectContainer.FP[3]  = '##Ká3##@@@@@@DMMMMMMCMMMMMMMMMMMMMM-MMMMMMM-MMM<MMMM-MMM----##DD'
        self.objectContainer.FP[4]  = '##Káà##@@@@@##M-MMMMMMMMMMMMMMMM---MMMMMMMM-MMMMMMM-MMMMMMMM##DD'
        self.objectContainer.FP[5]  = '#######X######MM-MMMMMMMMMMM----MMMMMMMMMMMM-MMMMM-MMMMMMMMM##DD'
        self.objectContainer.FP[6]  = '##ñ-----##MMMMMMM-MMMMM-----MMMMMMMMMMMKMMMMM-MMM-MMMMMMMMMM##DD'
        self.objectContainer.FP[7]  = '##########MMMMMMTMMMMM-MMMMMMMMMMMMMMMMMMMMMMM-M-MMMMMMMMMMMMMMM'
        self.objectContainer.FP[8]  = 'MMMMMMMMMMMMMMMMMMMMM-MMMMMMMMMMMMMMMMMMMMMMMMM-MMMMMMCMMMMMM-MM'
        self.objectContainer.FP[9]  = 'MMMMMMMM-----MMMM----MMMMMMMM[MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MMM'
        self.objectContainer.FP[10] = 'MMMM----MMMMM----MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMTMMMMMMMMMMM-MMMM'
        self.objectContainer.FP[11] = 'MMM-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MMM'
        self.objectContainer.FP[12] = 'MM-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MM'
        self.objectContainer.FP[13] = 'MM-MMMMMMCMMMMMMMMMMMMMMMBWWWWWWWWWW-------------------------MMM'
        self.objectContainer.FP[14] = 'MM-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MM'
        self.objectContainer.FP[15] = 'MM-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMTMMMMMMMMMMMMMMM-M'
        self.objectContainer.FP[16] = 'MMM-------MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MM'
        self.objectContainer.FP[17] = 'MMMMMMMMMM-----MMMMMMMMMMMMMMMM]MMMMMMMMM-M-MMMMMMMMMMMMMMMM-MMM'
        self.objectContainer.FP[18] = ')))))))))MMMMMM-MMMMMMMMMMMMMMMMMMMMMM-M-M-M-MMMMMMMMCMMMMM-MMMM'
        self.objectContainer.FP[19] = '22222222)MMTMMM-MMMMMCMMMMMMMMMMMMMMM-M-MMMMM-MMM-MMMMMMMM-MMMMM'
        self.objectContainer.FP[20] = '22222222)MMMMMM-MMMMMMMMMMMMMMM------MMMMMMM-MMM-M-MMMMMM-MMMMMM'
        self.objectContainer.FP[21] = '22222222)MMMMMM-MMMMMMMMMM-----MMMMMMMMMMMM-MMM-MM-MMMMM-MMMMMMM'
        self.objectContainer.FP[22] = '--222222)MMMMMM-----------MMMMMMMMMMMMMMMM-MM-M-MMM-M-M-MMMMM"MM'
        self.objectContainer.FP[23] = 'K-222222)MMMMMMMMMMMMMMMMMMMMMMMMMM|MMMMMMM--M-MMMMM-M-MMMMMMMMM'
        self.objectContainer.Fast = chr(234)
        self.Convert_Format()
    
    # Return game level 22
    def Level22(self):
        global objectContainer
        self.objectContainer.FP[1]  = '1111144       ##C######locksmith#shoppe######C##         RRRRRRR'
        self.objectContainer.FP[2]  = '1111144       ##]##K#K#K#K#K#-3-3#K#K#K#K#K##]##        RRRRRRRñ'
        self.objectContainer.FP[3]  = '1111144          ##:::::::::######::::::::;##         RRRRRRRCYY'
        self.objectContainer.FP[4]  = '1111144          ##------------------------##     666RRRRRRRR66 '
        self.objectContainer.FP[5]  = '1111144          #############--#############     6666666666666 '
        self.objectContainer.FP[6]  = '1111144                                           HOOOOOOOOH    '
        self.objectContainer.FP[7]  = '1111144                                        6666666666666    '
        self.objectContainer.FP[8]  = '1111144                                        66RRRRRRR6666    '
        self.objectContainer.FP[9]  = '1111144                                        RRRRRRR          '
        self.objectContainer.FP[10] = '1111144                                      RRRRRR           YY'
        self.objectContainer.FP[11] = '1111144               P                    RRRRRR             YZ'
        self.objectContainer.FP[12] = '1111144                                 RRRRRRRRRR            YY'
        self.objectContainer.FP[13] = '1111144                              RRRRR333RRRRR              '
        self.objectContainer.FP[14] = '1111144                             RRR3333333RRRRR             '
        self.objectContainer.FP[15] = '@@@@@##                           RRR3333333333RRRRR            '
        self.objectContainer.FP[16] = 'MMMMM##                           RRR333333333RRRRR             '
        self.objectContainer.FP[17] = ')))))##                          RRR33333333RRRRR               '
        self.objectContainer.FP[18] = 'MMMMM##                        RRRR333333RRRRRRR        DDDDDDDD'
        self.objectContainer.FP[19] = '(((((##                       RRRR3LL3RRRRRRRR          DDDDDDDD'
        self.objectContainer.FP[20] = 'MMMMM##                      RRRRRRRRRRRRRR             DDDDDDDD'
        self.objectContainer.FP[21] = '$$$$$##                     RRRRRRRRRRRR                DDDD7777'
        self.objectContainer.FP[22] = 'MMMMM##                     RRRRRRRR                    DDDD77ôô'
        self.objectContainer.FP[23] = ']]K]]##                   RRRRRRK]                     DDDD77ô!'
        self.objectContainer.Fast = chr(234)
        self.objectContainer.HideCreate = True
        self.Convert_Format()
    
    # Return game level 24
    def Level24(self):
        global objectContainer
        self.objectContainer.FP[1]  = 'T    P  #the#step#of#faith#------~Kñ-------U-----#---D-D-D-D-LL'
        self.objectContainer.FP[2]  = '######----------------------º44444444-------»-K--#½############'
        self.objectContainer.FP[3]  = '-----------------------------#       ------#####»-#-----³-------'
        self.objectContainer.FP[4]  = '-----------------------------#        -----:------#----³-³------'
        self.objectContainer.FP[5]  = '------###--------------------#        -----:------#--³³---³-----'
        self.objectContainer.FP[6]  = '--------#--------------------#        -----:------#-#------¼----'
        self.objectContainer.FP[7]  = '--------#--------------------#        -----#####--#-#-----------'
        self.objectContainer.FP[8]  = '--------#--------------------#        -----#---;--#-#------¼----'
        self.objectContainer.FP[9]  = '--------#--------------------#        -----#<###--#-#-----------'
        self.objectContainer.FP[10] = '--------#---------õ---------º#         ----#[#----#-#-----³-----'
        self.objectContainer.FP[11] = '--K-----#¹########88888888888#         ----#|#----#-#----³--W---'
        self.objectContainer.FP[12] = '-XXX----#      #             #         ----#"#----#-#-------W---'
        self.objectContainer.FP[13] = '        #      #             #          ---#-#----#-#---³---W---'
        self.objectContainer.FP[14] = '        #     #             #          ----------#-##-³----W---'
        self.objectContainer.FP[15] = '        #      #             #             ;;;;;- #½K#³-----W---'
        self.objectContainer.FP[16] = '        #      #             #                 +-+####------W---'
        self.objectContainer.FP[17] = '        #      #             #                 +-+----³-----W---'
        self.objectContainer.FP[18] = '    XXXX#      #             #                 +-+---³------W---'
        self.objectContainer.FP[19] = '         ¹     #             #                 +-+###-----------'
        self.objectContainer.FP[20] = '       ###     #             #    U            +-+#--------7----'
        self.objectContainer.FP[21] = '               #             #                 + +#   ##C.!.C## '
        self.objectContainer.FP[22] = '               #             #                 + +#   ######### '
        self.objectContainer.FP[23] = 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV'
        self.objectContainer.Fast = chr(234)
        self.objectContainer.GravOn = True
        self.objectContainer.GravRate = 0
        self.objectContainer.Sideways = True
        self.objectContainer.LavaFlow = True
        self.objectContainer.LavaRate = 75
        self.Convert_Format()
    
    # Return game level 25
    def Level25(self):
        global objectContainer
        self.objectContainer.FP[1]  = 'K¯    -++++++++++++++++#the#sacred#temple#+++++++++++++++-    ®K'
        self.objectContainer.FP[2]  = ' VVVVVV11111111111111111111111111111111111111111111111111\\\\\\\\\\\\ '
        self.objectContainer.FP[3]  = ' VVVV;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\\\\\\\\ '
        self.objectContainer.FP[4]  = ' VV1111111111;:::-:::111111111#####111111111::-:::::111111111\\\\ '
        self.objectContainer.FP[5]  = ' V11         :-:-:-::        ###A###        :-:-:--:        11\\ '
        self.objectContainer.FP[6]  = 'X 1          ::-:::B:        RR#`#RR        :B::-::;         1 X'
        self.objectContainer.FP[7]  = 'X  22####-####-------------RRRR#D#RRRR-------------####-####22 X'
        self.objectContainer.FP[8]  = 'X  22##3@-@3##;3;3;3;3;3;3RRRRR#`#RRRRR3;3;3;3;3;3;##~~~~~##22 X'
        self.objectContainer.FP[9]  = 'X  22##3@-@3##3;3;3;3;3;3RR1C##D##C1RR3;3;3;3;3;3##~~~~~##22 X'
        self.objectContainer.FP[10] = 'X  22##3@-@3##;3;3;3;3;3RR11##`##11RR3;3;3;3;3;##~~~~~##22 X'
        self.objectContainer.FP[11] = 'X--####3@-@3####3;3;3;3RR11#####D#####11RR3;3;3;3####~~~~~####-X'
        self.objectContainer.FP[12] = 'X   U##3@@@3##U ;3;3;3RRB11-+T1   1T+-11BRR3;3;3; U##~~~~~##U  X'
        self.objectContainer.FP[13] = 'X--####3@@@3####3;3;3;3RR11#####P#####11RR3;3;3;3####~~~~~####-X'
        self.objectContainer.FP[14] = 'X  22##3@@@3##;3;3;3;3;3RR1111##U##1111RR3;3;3;3;3;##~~~~~##22 X'
        self.objectContainer.FP[15] = 'X  22##3@@@3##3;3;3;3;3;3RR111#####111RR3;3;3;3;3;3##~~~~~##22 X'
        self.objectContainer.FP[16] = 'X  22##3@K@3##;3;3;3;3;3;3RR111äää111RR3;3;3;3;3;3;##~~K~~##22 X'
        self.objectContainer.FP[17] = 'X  22#########-----B-------RRRRäCäRRRR-------B-----#########22 X'
        self.objectContainer.FP[18] = 'X 1  ##|0<0                   RRRRR                   0[0"## 1 X'
        self.objectContainer.FP[19] = ' R11 #######  11111111111111;--->---;11111111111111  #######11= '
        self.objectContainer.FP[20] = ' RR111111111111-VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV-11111111111== '
        self.objectContainer.FP[21] = ' RRRR111111111-V V V-V V V-2-V*VCV*V-2-V V-V-V V V-11111111==== '
        self.objectContainer.FP[22] = 'áRRRRRR111111-V V V-2-V V V-V*V*V*V*V-V V V-2-V V V-11111======â'
        self.objectContainer.FP[23] = 'KááááááááááááVGVV V V V VV*V*V*V*V*VV V V V VVGVâââââââââââK'
        self.objectContainer.Fast = chr(234)
        self.objectContainer.MagicEWalls = True
        self.Convert_Format()
    
    
    def Display_Playfield(self):
        global objectContainer
    
        self.objectContainer.screen.Bak(0, 0)
        self.clearAreaOtherThanPlayer(1, 1, 66, 25)
    
        for XLoop in range(self.objectContainer.XBot, self.objectContainer.XTop + 1):
            for YLoop in range(self.objectContainer.YBot, self.objectContainer.YTop + 1):
                if (self.objectContainer.PF[XLoop][YLoop] != 0 or self.objectContainer.FloorPattern) and not self.objectContainer.HideLevel:
                    self.objectContainer.screen.GotoXY(XLoop + 1, YLoop + 1)
                    tile = self.objectContainer.PF[XLoop][YLoop]
    
                    if tile == None:
                        self.objectContainer.screen.Bak(0, 0)
                        self.objectContainer.screen.Write(' ')
                    elif tile == ' ':
                        self.objectContainer.screen.Bak(0, 0)
                        self.objectContainer.screen.Write(' ')
                    elif tile == 0:  # Floor
                        self.objectContainer.screen.Col(CF1, CF2)
                        self.objectContainer.screen.Bak(BF1, BF2)
                        self.objectContainer.screen.Write(Tile)
                        self.objectContainer.screen.Bak(0, 0)
                    elif tile == 1:  # Slow
                        self.objectContainer.screen.Col(12, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Slow)
                    elif tile == 2:  # Medium
                        self.objectContainer.screen.Col(10, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Medium)
                    elif tile == 3:  # Fast
                        self.objectContainer.screen.Col(9, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Fast)
                    elif tile == 4:  # Block
                        if self.objectContainer.Level != 71:
                            self.objectContainer.screen.Col(6, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Block)
                    elif tile == 5:  # Whip
                        self.objectContainer.screen.Col(15, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Whip)
                    elif tile == 6:  # Stairs
                        if not self.objectContainer.HideStairs:
                            self.objectContainer.screen.Bak(7, 7)
                            # Should set blink
                            self.objectContainer.screen.Col(1, 1)
                            self.objectContainer.screen.Write(self.objectContainer.Stairs)
                            self.objectContainer.screen.Bak(0, 0)
                    elif tile == 7:  # Chest
                        if random.randint(0, 19) == 0:
                            self.objectContainer.screen.Col(15, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Chance)
                        else:
                            self.objectContainer.screen.Col(14, 7)
                            self.objectContainer.screen.Bak(4, 0)
                            self.objectContainer.screen.Write(self.objectContainer.Chest)
                            self.objectContainer.screen.Bak(0, 0)
                    elif tile == 8:  # SlowTime
                        if random.randint(0, 34) == 0:
                            self.objectContainer.screen.Col(15, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Chance)
                        else:
                            self.objectContainer.screen.Col(11, 7)
                            self.objectContainer.screen.Write(self.objectContainer.SlowTime)
                    elif tile == 9:  # Gem
                        if not self.objectContainer.HideGems:
                            self.objectContainer.screen.Col(self.objectContainer.GemColor, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Gem)
                    elif tile == 10:  # Invisible
                        self.objectContainer.screen.Col(2, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Invisible)
                    elif tile == 11:  # Teleport
                        self.objectContainer.screen.Col(13, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Teleport)
                    elif tile == 12:  # Key
                        if random.randint(0, 24) == 0:
                            self.objectContainer.screen.Col(15, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Chance)
                        else:
                            self.objectContainer.screen.Col(12, 15)
                            self.objectContainer.screen.Write(self.objectContainer.Key)
                    elif tile == 13:  # Door
                        self.objectContainer.screen.Bak(5, 7)
                        self.objectContainer.screen.Col(3, 0)
                        self.objectContainer.screen.Write(self.objectContainer.Door)
                        self.objectContainer.screen.Bak(0, 0)
                    elif tile == 14:  # Wall
                        self.objectContainer.screen.Col(6, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Wall)
                    elif tile == 15:  # SpeedTime
                        if random.randint(0, 9) == 0:
                            self.objectContainer.screen.Col(15, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Chance)
                        else:
                            self.objectContainer.screen.Col(11, 7)
                            self.objectContainer.screen.Write(self.objectContainer.SpeedTime)
                    elif tile == 16:  # Trap
                        if not self.objectContainer.HideTrap:
                            self.objectContainer.screen.Col(7, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Trap)
                    elif tile == 17:  # River or Lava
                        if self.objectContainer.Level == 56:
                            self.objectContainer.screen.Col(12, 16)
                            self.objectContainer.screen.Bak(4, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Lava)
                            self.objectContainer.screen.Bak(0, 0)
                        else:
                            self.objectContainer.screen.Col(9, 0)
                            self.objectContainer.screen.Bak(1, 7)
                            self.objectContainer.screen.Write(self.objectContainer.River)
                            self.objectContainer.screen.Bak(0, 0)
                    elif tile == 18:  # Power
                        if random.randint(0, 14) == 0:
                            self.objectContainer.screen.Col(15, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Chance)
                        else:
                            self.objectContainer.screen.Col(15, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Power)
                    elif tile == 19:  # Forest
                        self.objectContainer.screen.Col(2, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Forest)
                        self.objectContainer.screen.Bak(0, 0)
                    elif tile in [20, 252]:  # Tree
                        self.objectContainer.screen.Col(6, 0)
                        self.objectContainer.screen.Bak(2, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Tree)
                        self.objectContainer.screen.Bak(0, 0)
                    elif tile == 21:  # Bomb
                        if random.randint(0, 39) == 0:
                            self.objectContainer.screen.Col(15, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Chance)
                        else:
                            self.objectContainer.screen.Col(15, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Bomb)
                    elif tile == 22:  # Lava
                        self.objectContainer.screen.Col(12, 16)
                        self.objectContainer.screen.Bak(4, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Lava)
                        self.objectContainer.screen.Bak(0, 0)
                    elif tile == 23:  # Pit
                        self.objectContainer.screen.Col(7, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Pit)
                    elif tile == 24:  # Tome
                        self.objectContainer.screen.Col(2, 2)
                        self.objectContainer.screen.Bak(5, 0)
                        self.objectContainer.screen.Write(self.objectContainer.Tome)
                        self.objectContainer.screen.Bak(0, 0)
                    elif tile == 25:  # Tunnel
                        self.objectContainer.screen.Col(15, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Tunnel)
                    elif tile == 26:  # Freeze
                        self.objectContainer.screen.Col(11, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Freeze)
                    elif tile == 27:  # Nugget
                        self.objectContainer.screen.Col(14, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Nugget)
                    elif tile == 28:  # Quake
                        if random.randint(0, 14) == 0:
                            self.objectContainer.screen.Col(15, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Chance)
                    elif tile == 29:  # IBlock
                        pass
                    elif tile == 30:  # IWall
                        pass
                    elif tile == 31:  # IDoor
                        pass
                    elif tile == 32:  # Stop
                        pass
                    elif tile == 34:  # Zap
                        self.objectContainer.screen.Col(12, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Zap)
                    elif tile == 35:  # Create
                        if not self.objectContainer.HideCreate:
                            self.objectContainer.screen.Col(15, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Chance)
                    elif tile == 36:  # Generator
                        self.objectContainer.screen.Col(15, 15)
                        self.objectContainer.screen.Write(self.objectContainer.Generator)
                    elif tile == 38:  # MBlock
                        if not self.objectContainer.HideMBlock:
                            self.objectContainer.screen.Col(6, 7)
                            self.objectContainer.screen.Write(self.objectContainer.MBlock)
                    elif tile in [33, 37, 39, 67] or 224 <= tile <= 231:  # Trap2-13
                        pass
                    elif tile == 40:  # Player
                        self.objectContainer.screen.Bak(0, 0)
                        # Should set blink
                        self.objectContainer.screen.Col(14, 1)
                        self.objectContainer.screen.Write(self.objectContainer.Player)
                        self.objectContainer.screen.Bak(0, 0)
                    elif tile == 41:  # ShowGems
                        pass
                    elif tile == 42:  # Tablet
                        self.objectContainer.screen.Col(9, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Tablet)
                    elif tile == 43:  # ZBlock
                        self.objectContainer.screen.Col(6, 7)
                        self.objectContainer.screen.Write(self.objectContainer.ZBlock)
                    elif tile == 44:  # BlockSpell
                        pass
                    elif tile == 45:  # Chance
                        self.objectContainer.screen.Col(15, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Chance)
                    elif tile == 46:  # Statue
                        self.objectContainer.screen.Col(2, 8)
                        self.objectContainer.screen.Write(objectContainer.Statue)
                    elif tile == 48:  # K
                        self.objectContainer.screen.Col(14, 15)
                        self.objectContainer.screen.Write('K')
                    elif tile == 49:  # R
                        self.objectContainer.screen.Col(14, 15)
                        self.objectContainer.screen.Write('R')
                    elif tile == 50:  # O
                        self.objectContainer.screen.Col(14, 15)
                        self.objectContainer.screen.Write('O')
                    elif tile == 51:  # Z
                        self.objectContainer.screen.Col(14, 15)
                        self.objectContainer.screen.Write('Z')
                    elif tile in [52, 53]:  # OWall1,2
                        self.objectContainer.screen.Col(6, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Wall)
                    elif tile == 54:  # OWall3
                        self.objectContainer.screen.Col(7, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Wall)
                    elif 55 <= tile <= 57:  # CWall1..3
                        pass
                    elif 58 <= tile <= 60:  # OSpell1..3
                        if not HideOpenWall:
                            self.objectContainer.screen.Col(11, 7)
                            self.objectContainer.screen.Write(self.objectContainer.OSpell1)
                    elif 61 <= tile <= 63:  # CSpell1..3
                        pass
                    elif 68 <= tile <= 74:  # Triggers
                        pass
                    elif tile == 64:  # GBlock
                        self.objectContainer.screen.Col(7, 7)
                        self.objectContainer.screen.Write(self.objectContainer.GBlock)
                    elif tile == 65:  # Rock
                        if not self.objectContainer.HideRock:
                            self.objectContainer.screen.Col(7, 7)
                            self.objectContainer.screen.Write(self.objectContainer.Rock)
                    elif tile == 66:  # EWall
                        self.objectContainer.screen.Col(12, 0)
                        self.objectContainer.screen.Bak(4, 7)
                        self.objectContainer.screen.Write(objectContainer.EWall)
                        self.objectContainer.screen.Bak(0, 0)
                    elif tile == 47:  # WallVanish
                        if random.randint(0, 19) == 0:
                            self.objectContainer.screen.Col(15, 7)
                            self.objectContainer.screen.Write(objectContainer.Chance)
                    elif tile == 75:  # Rope
                        self.objectContainer.screen.Col(7, 7)
                        self.objectContainer.screen.Write(self.objectContainer.Rope)
                    elif 76 <= tile <= 80:  # DropRope
                        self.objectContainer.screen.Col(7, 7)
                        self.objectContainer.screen.Write(self.objectContainer.DropRope)
                    elif tile == 82:  # ShootRight
                        self.objectContainer.screen.Col(7, 7)
                        self.objectContainer.screen.Write(self.objectContainer.ShootRight)
                    elif tile == 83:  # ShootLeft
                        self.objectContainer.screen.Col(7, 7)
                        self.objectContainer.screen.Write(self.objectContainer.ShootLeft)
                    elif tile == 81:  # Amulet
                        self.objectContainer.screen.Col(2, 2)
                        self.objectContainer.screen.Write(self.objectContainer.Amulet)
                    elif tile == 180:  # punct.
                        self.objectContainer.screen.Col(15, 0)
                        self.objectContainer.screen.Bak(6, 7)
                        self.objectContainer.screen.Write('.')
                        self.objectContainer.screen.Bak(0, 0)
                    elif tile == 181:  # punct.
                        self.objectContainer.screen.Col(15, 0)
                        self.objectContainer.screen.Bak(6, 7)
                        self.objectContainer.screen.Write('?')
                        self.objectContainer.screen.Bak(0, 0)
                    elif tile == 182:  # punct.
                        self.objectContainer.screen.Col(15, 0)
                        self.objectContainer.screen.Bak(6, 7)
                        self.objectContainer.screen.Write('\'')
                        self.objectContainer.screen.Bak(0, 0)
                    elif tile == 183:  # punct.
                        self.objectContainer.screen.Col(15, 0)
                        self.objectContainer.screen.Bak(6, 7)
                        self.objectContainer.screen.Write(',')
                        self.objectContainer.screen.Bak(0, 0)
                    elif tile == 184:  # punct.
                        self.objectContainer.screen.Col(15, 0)
                        self.objectContainer.screen.Bak(6, 7)
                        self.objectContainer.screen.Write(':')
                        self.objectContainer.screen.Bak(0, 0)
                    elif tile == 195:  # punct.
                        self.objectContainer.screen.Col(15, 0)
                        self.objectContainer.screen.Bak(6, 7)
                        self.objectContainer.screen.Write('!')
                        self.objectContainer.screen.Bak(0, 0)
                    else:  # Letters
                        self.objectContainer.screen.Col(15, 0)
                        self.objectContainer.screen.Bak(6, 7)
                        self.objectContainer.screen.Write(chr(tile).upper())
                        self.objectContainer.screen.Bak(0, 0)
    
        FloorPattern = False
    
    
    
    def Convert_Format(self):
        global objectContainer
    
        # Reset PF array
        for x in range(1, 67):  # 1 to 66 inclusive
            for y in range(1, 26):  # 1 to 25 inclusive
                self.objectContainer.PF[x][y] = 0
    
        # Reset monster's X, Y coordinates
        for x in range(1, 1000):  # 1 to 999 inclusive
            self.objectContainer.SX[x] = 0
            self.objectContainer.SY[x] = 0
            self.objectContainer.MX[x] = 0
            self.objectContainer.MY[x] = 0
            self.objectContainer.FX[x] = 0
            self.objectContainer.FY[x] = 0
    
        # Reset B arrays
        for x in range(1, 1301):  # 1 to 1300 inclusive
            self.objectContainer.BX[x] = 0
            self.objectContainer.BY[x] = 0
    
        self.New_Gem_Color()
    
        # Convert format based on FP array
        for YLoop in range(1, self.objectContainer.YSize + 1):  # 1 to YSize inclusive
            for XLoop in range(1, self.objectContainer.XSize):
                self.tempstr = self.objectContainer.FP[YLoop][XLoop]
                char_temp = self.tempstr[0]  # Get the first character
                
                # Map characters to PF values
                if char_temp == ' ':
                    self.objectContainer.PF[XLoop][YLoop] = None
                elif char_temp == '1':
                    self.objectContainer.SNum += 1
                    self.objectContainer.SX[self.objectContainer.SNum] = XLoop
                    self.objectContainer.SY[self.objectContainer.SNum] = YLoop
                    self.objectContainer.PF[XLoop][YLoop] = 1
                elif char_temp == '2':
                    self.objectContainer.MNum += 1
                    self.objectContainer.MX[self.objectContainer.MNum] = XLoop
                    self.objectContainer.MY[self.objectContainer.MNum] = YLoop
                    self.objectContainer.PF[XLoop][YLoop] = 2
                elif char_temp == '3':
                    self.objectContainer.FNum += 1
                    self.objectContainer.FX[self.objectContainer.FNum] = XLoop
                    self.objectContainer.FY[self.objectContainer.FNum] = YLoop
                    self.objectContainer.PF[XLoop][YLoop] = 3
                elif char_temp == 'X':
                    self.objectContainer.PF[XLoop][YLoop] = 4
                elif char_temp == 'W':
                    self.objectContainer.PF[XLoop][YLoop] = 5
                elif char_temp == 'L':
                    self.objectContainer.PF[XLoop][YLoop] = 6
                elif char_temp == 'C':
                    self.objectContainer.PF[XLoop][YLoop] = 7
                elif char_temp == 'S':
                    self.objectContainer.PF[XLoop][YLoop] = 8
                elif char_temp == '+':
                    self.objectContainer.PF[XLoop][YLoop] = 9
                elif char_temp == 'I':
                    self.objectContainer.PF[XLoop][YLoop] = 10
                elif char_temp == 'T':
                    self.objectContainer.PF[XLoop][YLoop] = 11
                elif char_temp == 'K':
                    self.objectContainer.PF[XLoop][YLoop] = 12
                elif char_temp == 'D':
                    self.objectContainer.PF[XLoop][YLoop] = 13
                elif char_temp == '#':
                    self.objectContainer.PF[XLoop][YLoop] = 14
                elif char_temp == 'F':
                    self.objectContainer.PF[XLoop][YLoop] = 15
                elif char_temp == '.':
                    self.objectContainer.PF[XLoop][YLoop] = 16
                elif char_temp == 'R':
                    self.objectContainer.PF[XLoop][YLoop] = 17
                elif char_temp == 'Q':
                    self.objectContainer.PF[XLoop][YLoop] = 18
                elif char_temp == '/':
                    self.objectContainer.PF[XLoop][YLoop] = 19
                elif char_temp == '\\':
                    self.objectContainer.PF[XLoop][YLoop] = 20
                elif char_temp == 'B':
                    self.objectContainer.PF[XLoop][YLoop] = 21
                elif char_temp == 'V':
                    self.objectContainer.PF[XLoop][YLoop] = 22
                elif char_temp == '=':
                    self.objectContainer.PF[XLoop][YLoop] = 23
                elif char_temp == 'A':
                    self.objectContainer.PF[XLoop][YLoop] = 24
                elif char_temp == 'U':
                    self.objectContainer.PF[XLoop][YLoop] = 25
                elif char_temp == 'Z':
                    self.objectContainer.PF[XLoop][YLoop] = 26
                elif char_temp == '*':
                    self.objectContainer.PF[XLoop][YLoop] = 27
                elif char_temp == 'E':
                    self.objectContainer.PF[XLoop][YLoop] = 28
                elif char_temp == ';':
                    self.objectContainer.PF[XLoop][YLoop] = 29
                elif char_temp == ':':
                    self.objectContainer.PF[XLoop][YLoop] = 30
                elif char_temp == '`':
                    self.objectContainer.PF[XLoop][YLoop] = 31
                elif char_temp == '-':
                    self.objectContainer.PF[XLoop][YLoop] = 32
                elif char_temp == '@':
                    self.objectContainer.PF[XLoop][YLoop] = 33
                elif char_temp == '%':
                    self.objectContainer.PF[XLoop][YLoop] = 34
                elif char_temp == ']':
                    self.objectContainer.PF[XLoop][YLoop] = 35
                elif char_temp == 'G':
                    self.objectContainer.PF[XLoop][YLoop] = 36
                    self.objectContainer.GenNum += 1
                elif char_temp == '(':
                    objectContainer.PF[XLoop][YLoop] = 37
                elif char_temp == 'M':
                    self.objectContainer.BNum += 1
                    self.objectContainer.BX[objectContainer.BNum] = XLoop
                    self.objectContainer.BY[objectContainer.BNum] = YLoop
                    self.objectContainer.PF[XLoop][YLoop] = 38
                elif char_temp == ')':
                    self.objectContainer.PF[XLoop][YLoop] = 39
                elif char_temp == 'P':
                    self.objectContainer.PF[XLoop][YLoop] = 40
                    self.objectContainer.PX = XLoop
                    self.objectContainer.PY = YLoop
                elif char_temp == '&':
                    self.objectContainer.PF[XLoop][YLoop] = 41
                elif char_temp == '!':
                    self.objectContainer.PF[XLoop][YLoop] = 42
                elif char_temp == 'O':
                    self.objectContainer.PF[XLoop][YLoop] = 43
                elif char_temp == 'H':
                    self.objectContainer.PF[XLoop][YLoop] = 44
                elif char_temp == '?':
                    self.objectContainer.PF[XLoop][YLoop] = 45
                elif char_temp == '>':
                    self.objectContainer.PF[XLoop][YLoop] = 46
                    self.objectContainer.T[9] = 32000
                elif char_temp == 'N':
                    self.objectContainer.PF[XLoop][YLoop] = 47
                elif char_temp == '<':
                    self.objectContainer.PF[XLoop][YLoop] = 48
                elif char_temp == '[':
                    self.objectContainer.PF[XLoop][YLoop] = 49
                elif char_temp == '|':
                    self.objectContainer.PF[XLoop][YLoop] = 50
                elif char_temp == '"':
                    self.objectContainer.PF[XLoop][YLoop] = 51
                elif char_temp == '4':
                    self.objectContainer.PF[XLoop][YLoop] = 52
                elif char_temp == '5':
                    self.objectContainer.PF[XLoop][YLoop] = 53
                elif char_temp == '6':
                    self.objectContainer.PF[XLoop][YLoop] = 54
                elif char_temp == '7':
                    self.objectContainer.PF[XLoop][YLoop] = 55
                elif char_temp == '8':
                    self.objectContainer.PF[XLoop][YLoop] = 56
                elif char_temp == '9':
                    self.objectContainer.PF[XLoop][YLoop] = 57
                elif char_temp == 'Ã±':
                    self.objectContainer.PF[XLoop][YLoop] = 58
                elif char_temp == 'Ã²':
                    self.objectContainer.PF[XLoop][YLoop] = 59
                elif char_temp == 'Ã³':
                    self.objectContainer.PF[XLoop][YLoop] = 60
                elif char_temp == 'Ã´':
                    self.objectContainer.PF[XLoop][YLoop] = 61
                elif char_temp == 'Ãµ':
                    self.objectContainer.PF[XLoop][YLoop] = 62
                elif char_temp == 'Ã¶':
                    self.objectContainer.PF[XLoop][YLoop] = 63
                elif char_temp == 'Y':
                    self.objectContainer.PF[XLoop][YLoop] = 64
                elif char_temp == '0':
                    self.objectContainer.PF[XLoop][YLoop] = 65
                elif char_temp == '~':
                    self.objectContainer.PF[XLoop][YLoop] = 66
                elif char_temp == '$':
                    self.objectContainer.PF[XLoop][YLoop] = 67
                elif char_temp == 'Â':
                    self.objectContainer.PF[XLoop][YLoop] = 68
                elif char_temp == 'Â':
                    self.objectContainer.PF[XLoop][YLoop] = 69
                elif char_temp == 'Â':
                    self.objectContainer.PF[XLoop][YLoop] = 70
                elif char_temp == 'Â':
                    self.objectContainer.PF[XLoop][YLoop] = 71
                elif char_temp == 'Â':
                    self.objectContainer.PF[XLoop][YLoop] = 72
                elif char_temp == 'Â':
                    self.objectContainer.PF[XLoop][YLoop] = 73
                elif char_temp == 'Â':
                    self.objectContainer.PF[XLoop][YLoop] = 74
                elif char_temp == 'Â³':
                    self.objectContainer.PF[XLoop][YLoop] = 75
                elif char_temp == 'Â¹':
                    self.objectContainer.PF[XLoop][YLoop] = 76
                elif char_temp == 'Âº':
                    self.objectContainer.PF[XLoop][YLoop] = 77
                elif char_temp == 'Â»':
                    self.objectContainer.PF[XLoop][YLoop] = 78
                elif char_temp == 'Â¼':
                    self.objectContainer.PF[XLoop][YLoop] = 79
                elif char_temp == 'Â½':
                    self.objectContainer.PF[XLoop][YLoop] = 80
                elif char_temp == 'Â':
                    self.objectContainer.PF[XLoop][YLoop] = 81
                elif char_temp == 'Â´':
                    self.objectContainer.PF[XLoop][YLoop] = 180
                elif char_temp == 'Âµ':
                    self.objectContainer.PF[XLoop][YLoop] = 181
                elif char_temp == 'Â¶':
                    self.objectContainer.PF[XLoop][YLoop] = 182
                elif char_temp == 'Â·':
                    self.objectContainer.PF[XLoop][YLoop] = 183
                elif char_temp == 'Â¸':
                    self.objectContainer.PF[XLoop][YLoop] = 184
                elif char_temp == 'Ã ':
                    self.objectContainer.PF[XLoop][YLoop] = 224
                elif char_temp == 'Ã¡':
                    self.objectContainer.PF[XLoop][YLoop] = 225
                elif char_temp == 'Ã¢':
                    self.objectContainer.PF[XLoop][YLoop] = 226
                elif char_temp == 'Ã£':
                    self.objectContainer.PF[XLoop][YLoop] = 227
                elif char_temp == 'Ã¤':
                    self.objectContainer.PF[XLoop][YLoop] = 228
                elif char_temp == 'Ã¥':
                    self.objectContainer.PF[XLoop][YLoop] = 229
                elif char_temp == 'Ã¦':
                    self.objectContainer.PF[XLoop][YLoop] = 230
                elif char_temp == 'Ã§':
                    self.objectContainer.PF[XLoop][YLoop] = 231
                elif char_temp == 'Â¯':
                    self.objectContainer.PF[XLoop][YLoop] = 82
                elif char_temp == 'Â®':
                    self.objectContainer.PF[XLoop][YLoop] = 83
                elif char_temp == 'Ã¼':
                    self.objectContainer.PF[XLoop][YLoop] = 252
                else:
                    # If the character is not recognized, use its ASCII value
                    self.objectContainer.PF[XLoop][YLoop] = ord(char_temp)
    
    def New_Gem_Color(self):
        global objectContainer
    
        while True:
            self.objectContainer.GemColor = random.randint(1, 15)  # Generates a random integer between 1 and 15
            if self.objectContainer.screen.getMonochrome():
                objectContainer.GemColor = 7
            if self.objectContainer.GemColor != 8:
                break
    
    def Init_Screen(self):
        global objectContainer 
    
        objectContainer.Restart = False
        objectContainer.Score = 0
        objectContainer.Level = 1
        objectContainer.Whips = 0
        objectContainer.Teleports = 0
        objectContainer.Keys = 0
        objectContainer.WhipPower = 2
    
        if self.objectContainer.Difficulty == 9:
            self.objectContainer.Gems = 250
            self.objectContainer.Whips = 100
            self.objectContainer.Teleports = 50
            self.objectContainer.Keys = 1
            self.objectContainer.WhipPower = 3
        elif self.objectContainer.Difficulty == 8:
            self.objectContainer.Gems = 20
            self.objectContainer.Whips = 10
        elif self.objectContainer.Difficulty == 5:
            self.objectContainer.Gems = 15
        elif self.objectContainer.Difficulty == 2:
            self.objectContainer.Gems = 10
    
        self.objectContainer.FloorPattern = False
        self.objectContainer.Replacement = None
        self.objectContainer.Bonus = 0
        self.objectContainer.LavaFlow = False
        self.objectContainer.LavaRate = 0
        self.objectContainer.Evaporate = 0
        self.objectContainer.MagicEWalls = False
        self.objectContainer.GravOn = False
        self.objectContainer.GravRate = 20
        self.objectContainer.GravCounter = 0
        self.objectContainer.TreeRate = -1
        self.objectContainer.HideRock = False
        self.objectContainer.HideStairs = False
        self.objectContainer.HideLevel = False
        self.objectContainer.HideCreate = False
        self.objectContainer.HideOpenWall = False
        self.objectContainer.HideTrap = False
        self.objectContainer.HideGems = False
        self.objectContainer.HideMBlock = False
        self.objectContainer.FoundSet = set()
    
        if self.objectContainer.Difficulty in [2, 9]:
            FoundSet = set(range(256))
    
        self.objectContainer.GenNum = 0
        self.objectContainer.Sideways = False
        self.objectContainer.OneMove = False
    
        self.objectContainer.GenFactor = 28 if self.objectContainer.FastPC else 17
    
        if self.objectContainer.MixUp:
            self.objectContainer.Gems = 60
            self.objectContainer.Whips = 30
            self.objectContainer.Teleports = 15
            self.objectContainer.Keys = 2
            self.objectContainer.FoundSet = set(range(ToTObjects + 1))
    
        self.objectContainer.PX = random.randint(self.objectContainer.XBot, self.objectContainer.XBot + self.objectContainer.XSize - 1)
        self.objectContainer.PY = random.randint(self.objectContainer.YBot, self.objectContainer.YBot + self.objectContainer.YSize - 1)
    
        self.objectContainer.BTime = 9 if self.objectContainer.FastPC else 2
        self.objectContainer.STime = 10 if self.objectContainer.FastPC else 3
        self.objectContainer.MTime = 8 if self.objectContainer.FastPC else 2
        self.objectContainer.FTime = 6 if self.objectContainer.FastPC else 1
        self.objectContainer.SkipTime = 0
    
        for x in range(1, self.objectContainer.TMax + 1):
            self.objectContainer.T[x] = -1  # Reset timers
    
        self.objectContainer.T[1] = 5
        self.objectContainer.T[2] = 6
        self.objectContainer.T[3] = 7
        self.objectContainer.T[8] = 6
    
        if not self.objectContainer.screen.getMonochrome():
            self.objectContainer.screen.Bak(1, 0)
            self.clearArea(67, 1, 80, 25)
    
        self.objectContainer.screen.Col(14, 7)
        self.objectContainer.screen.GotoXY(71, 1)
        self.objectContainer.screen.Write('Score')
        self.objectContainer.screen.GotoXY(71, 4)
        self.objectContainer.screen.Write('Level')
        self.objectContainer.screen.GotoXY(71, 7)
        self.objectContainer.screen.Write('Gems')
        self.objectContainer.screen.GotoXY(71, 10)
        self.objectContainer.screen.Write('Whips')
        self.objectContainer.screen.GotoXY(69, 13)
        self.objectContainer.screen.Write('Teleports')
        self.objectContainer.screen.GotoXY(71, 16)
        self.objectContainer.screen.Write('Keys')
        self.objectContainer.screen.Col(11, 7)
        self.objectContainer.screen.Bak(4, 0)
        self.objectContainer.screen.GotoXY(70, 19)
        self.objectContainer.screen.Write('OPTIONS')
        self.objectContainer.screen.Bak(1, 0)
        self.objectContainer.screen.GotoXY(70, 20)
        self.objectContainer.screen.Col(15, 15)
        self.objectContainer.screen.Write('W')
        self.objectContainer.screen.Col(7, 7)
        self.objectContainer.screen.Write('hip')
        self.objectContainer.screen.GotoXY(70, 21)
        self.objectContainer.screen.Col(15, 15)
        self.objectContainer.screen.Write('T')
        self.objectContainer.screen.Col(7, 7)
        self.objectContainer.screen.Write('eleport')
        self.objectContainer.screen.GotoXY(70, 22)
        self.objectContainer.screen.Col(15, 15)
        self.objectContainer.screen.Write('P')
        self.objectContainer.screen.Col(7, 7)
        self.objectContainer.screen.Write('ause')
        self.objectContainer.screen.GotoXY(70, 23)
        self.objectContainer.screen.Col(15, 15)
        self.objectContainer.screen.Write('Q')
        self.objectContainer.screen.Col(7, 7)
        self.objectContainer.screen.Write('uit')
        self.objectContainer.screen.GotoXY(70, 24)
        self.objectContainer.screen.Col(15, 15)
        self.objectContainer.screen.Write('S')
        self.objectContainer.screen.Col(7, 7)
        self.objectContainer.screen.Write('ave')
        self.objectContainer.screen.GotoXY(70, 25)
        self.objectContainer.screen.Col(15, 15)
        self.objectContainer.screen.Write('R')
        self.objectContainer.screen.Col(7, 7)
        self.objectContainer.screen.Write('estore')
    
    def Next_Level(self):
        global objectContainer
    
        self.animatePlayerMovement()
    
        if (objectContainer.LevelNumber == 1):
            objectContainer.LevelNumber = 2
        elif (objectContainer.LevelNumber == 2):
            objectContainer.LevelNumber = 4
        elif (objectContainer.LevelNumber == 4):
            objectContainer.LevelNumber = 6
        elif (objectContainer.LevelNumber == 6):
            objectContainer.LevelNumber = 8
        elif (objectContainer.LevelNumber == 8):
            objectContainer.LevelNumber = 10
        elif (objectContainer.LevelNumber == 10):
            objectContainer.LevelNumber = 12
        elif (objectContainer.LevelNumber == 12):
            objectContainer.LevelNumber = 14
        elif (objectContainer.LevelNumber == 14):
            objectContainer.LevelNumber = 16
        elif (objectContainer.LevelNumber == 16):
            objectContainer.LevelNumber = 18
        elif (objectContainer.LevelNumber == 18):
            objectContainer.LevelNumber = 20
        elif (objectContainer.LevelNumber == 20):
            objectContainer.LevelNumber = 22
        elif (objectContainer.LevelNumber == 22):
            objectContainer.LevelNumber = 24
        elif (objectContainer.LevelNumber == 24):
            objectContainer.LevelNumber = 25
        else:
            print("No more levels available.")
    
        self.Level(objectContainer.LevelNumber)
        self.Display_Playfield()
    
    def animatePlayerMovement(self):
        global objectContainer
    
        self.clearAreaOtherThanPlayer(1, 1, 66, 25)
    
        targetX = 0
        targetY = 0
    
        if (objectContainer.LevelNumber == 1):
            targetX = 32
            targetY = 12
        elif (objectContainer.LevelNumber == 2):
            targetX = 13
            targetY = 16
        elif (objectContainer.LevelNumber == 4):
            targetX = 30
            targetY = 3
        elif (objectContainer.LevelNumber == 6):
            targetX = 62
            targetY = 4
        elif (objectContainer.LevelNumber == 8):
            targetX = 32
            targetY = 12
        elif (objectContainer.LevelNumber == 10):
            targetX = 1
            targetY = 11
        elif (objectContainer.LevelNumber == 12):
            targetX = 31
            targetY = 12
        elif (objectContainer.LevelNumber == 14):
            targetX = 29
            targetY = 1
        elif (objectContainer.LevelNumber == 16):
            targetX = 32
            targetY = 2
        elif (objectContainer.LevelNumber == 18):
            targetX = 58
            targetY = 2
        elif (objectContainer.LevelNumber == 20):
            targetX = 22
            targetY = 11
        elif (objectContainer.LevelNumber == 22):
            targetX = 5
            targetY = 1
        elif (objectContainer.LevelNumber == 24):
            targetX = 32
            targetY = 13
        elif (objectContainer.LevelNumber == 25):
            targetX = 32
            targetY = 13

        targetX = targetX + 1
        targetY = targetY + 1
    
        waypoint1X = random.randint(3, 64)
        waypoint1Y = random.randint(3, 23)
    
        waypoint2X = random.randint(3, 64)
        waypoint2Y = random.randint(3, 23)
    
        self.animatedPlayerMove(waypoint1X, waypoint1Y)
        self.animatedPlayerMove(waypoint2X, waypoint2Y)
        self.animatedPlayerMove(targetX, targetY)
    
    def animatedPlayerMove(self, targetX, targetY):
        global objectContainer

        currentX = objectContainer.PX
        currentY = objectContainer.PY

        objectContainer.screen.GotoXY(currentX + 1, currentY + 1)
        objectContainer.screen.Write(' ')
    
        objectContainer.screen.Bak(8, 0)
        objectContainer.screen.Col(14, 1)
    
        while(currentX != targetX or currentY != targetY):
            objectContainer.screen.GotoXY(currentX, currentY)
            objectContainer.screen.Write(' ')
    
            if (currentX < targetX):
                currentX += 1
            elif (currentX > targetX):
                currentX -= 1
    
            if (currentY < targetY):
                currentY += 1
            elif (currentY > targetY):
                currentY -= 1
    
            objectContainer.screen.GotoXY(currentX, currentY)
            objectContainer.screen.Write(objectContainer.Player)
    
            time.sleep(0.02)
    
        objectContainer.PX = currentX
        objectContainer.PY = currentY
    
        objectContainer.screen.Bak(0, 0)
        objectContainer.screen.GotoXY(currentX, currentY)
        objectContainer.screen.Write(objectContainer.Player)
    
    def clearArea(self, start_x, start_y, end_x, end_y):
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                self.objectContainer.screen.GotoXY(x, y)
                self.objectContainer.screen.Write(' ')
    
    def clearAreaOtherThanPlayer(self, start_x, start_y, end_x, end_y):
        global objectContainer
    
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if (x != self.objectContainer.PX + 1 or y != self.objectContainer.PY + 1):
                    self.objectContainer.screen.GotoXY(x, y)
                    self.objectContainer.screen.Write(' ')
