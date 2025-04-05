from screenFunctions import Screen
from object_container import objectContainer
import random

container = objectContainer()

objectContainer.FP = [None] * 24
objectContainer.Fast = chr(234)
objectContainer.HideOpenWall = False
objectContainer.LavaRate = 0
objectContainer.GravOn = False
objectContainer.GravRate = 0
objectContainer.Sideways = False
objectContainer.HideGems = False
objectContainer.HideStairs = False
objectContainer.HideOpenWall = False
objectContainer.TreeRate = 0
objectContainer.HideCreate = True
objectContainer.MagicEWalls = True
objectContainer.PF = [[0 for _ in range(26)] for _ in range(67)]
objectContainer.XBot = 2
objectContainer.YBot = 2
objectContainer.XTop = 65
objectContainer.YTop = 24
objectContainer.TMax = 9
objectContainer.FloorPattern = False
objectContainer.T = [0] * (objectContainer.TMax + 1)
objectContainer.SX = [0] * 1001
objectContainer.SY = [0] * 1001
objectContainer.MX = [0] * 1001
objectContainer.MY = [0] * 1001
objectContainer.FX = [0] * 1001
objectContainer.FY = [0] * 1001
objectContainer.BX = [0] * 1301
objectContainer.BY = [0] * 1301
objectContainer.YSize = 23
objectContainer.XSize = 64
objectContainer.HideLevel = False

# Check how these should be defined
objectContainer.SNum = 0
objectContainer.MNum = 0
objectContainer.FNum = 0
objectContainer.BNum = 0
objectContainer.GenNum = 0
objectContainer.PX = 0
objectContainer.PY = 0
objectContainer.Slow = None
objectContainer.Medium = None
objectContainer.Fast = None
objectContainer.Difficulty = 2 # This needs to be integrated with menus!!!
objectContainer.FastPC = True # This needs to be integrated with menus!!!
objectContainer.MixUp = False # ??????????



# Constants representing game elements
objectContainer.Null = 0
objectContainer.Block = chr(178)      # Character code 178
objectContainer.Whip = chr(244)       # Character code 244
objectContainer.Stairs = chr(240)     # Character code 240
objectContainer.Chest = chr(67)       # Character code 67
objectContainer.SlowTime = chr(232)  # Character code 232
objectContainer.Gem = chr(4)          # Character code 4
objectContainer.Invisible = chr(173)   # Character code 173
objectContainer.Teleport = chr(24)    # Character code 24
objectContainer.Key = chr(140)        # Character code 140
objectContainer.Door = chr(236)       # Character code 236
objectContainer.Wall = chr(219)       # Character code 219
objectContainer.SpeedTime = chr(233) # Character code 233
objectContainer.Trap = chr(249)       # Character code 249
objectContainer.River = chr(247)      # Character code 247
objectContainer.Power = chr(9)        # Character code 9
objectContainer.Forest = chr(219)     # Character code 219
objectContainer.Tree = chr(5)         # Character code 5
objectContainer.Bomb = chr(157)       # Character code 157
objectContainer.Lava = chr(178)       # Character code 178
objectContainer.Pit = chr(176)        # Character code 176
objectContainer.Tome = chr(12)        # Character code 12
objectContainer.Tunnel = chr(239)     # Character code 239
objectContainer.Freeze = chr(159)     # Character code 159
objectContainer.Nugget = chr(15)      # Character code 15
objectContainer.Quake = chr(0)        # Character code 0
objectContainer.IBlock = chr(30)      # Character code 30
objectContainer.IWall = chr(0)        # Character code 0
objectContainer.IDoor = chr(0)        # Character code 0
objectContainer.Stop = chr(0)         # Character code 0
objectContainer.Trap2 = chr(0)        # Character code 0
objectContainer.Zap = chr(30)         # Character code 30
objectContainer.Create = chr(31)      # Character code 31
objectContainer.Generator = chr(6)    # Character code 6
objectContainer.Trap3 = chr(0)        # Character code 0
objectContainer.MBlock = chr(178)     # Character code 178
objectContainer.Trap4 = chr(0)        # Character code 0
objectContainer.Player = chr(2)       # Character code 2
objectContainer.Show_Gems = chr(0)    # Character code 0
objectContainer.Tablet = chr(254)     # Character code 254
objectContainer.ZBlock = chr(178)     # Character code 178
objectContainer.BlockSpell = chr(0)  # Character code 0
objectContainer.Chance = chr(63)      # Character code 63
objectContainer.Statue = chr(1)       # Character code 1
objectContainer.WallVanish = chr(0)  # Character code 0
objectContainer.K = chr(0)            # Placeholder for K
objectContainer.R = chr(0)            # Placeholder for R
objectContainer.O = chr(0)            # Placeholder for O
objectContainer.Z = chr(0)            # Placeholder for Z
objectContainer.OWall1 = chr(219)     # Character code 219
objectContainer.OWall2 = chr(219)     # Character code 219
objectContainer.OWall3 = chr(219)     # Character code 219
objectContainer.CWall1 = chr(0)       # Character code 0
objectContainer.CWall2 = chr(0)       # Character code 0
objectContainer.CWall3 = chr(0)       # Character code 0
objectContainer.OSpell1 = chr(127)    # Character code 127
objectContainer.OSpell2 = chr(127)    # Character code 127
objectContainer.OSpell3 = chr(127)    # Character code 127
objectContainer.CSpell1 = chr(0)      # Character code 0
objectContainer.CSpell2 = chr(0)      # Character code 0
objectContainer.CSpell3 = chr(0)      # Character code 0
objectContainer.GBlock = chr(178)     # Character code 178
objectContainer.Rock = chr(79)        # Character code 79
objectContainer.EWall = chr(88)       # Character code 88
objectContainer.Trap5 = chr(0)        # Character code 0
objectContainer.TBlock = chr(0)       # Character code 0
objectContainer.TRock = chr(0)        # Character code 0
objectContainer.TGem = chr(0)         # Character code 0
objectContainer.TBlind = chr(0)       # Character code 0

# Continuing the constants representing game elements
objectContainer.TWhip = chr(0)        # Character code 0
objectContainer.TGold = chr(0)        # Character code 0
objectContainer.TTree = chr(0)        # Character code 0
objectContainer.Rope = chr(179)       # Character code 179
objectContainer.DropRope = chr(25)   # Character code 25
objectContainer.Amulet = chr(12)      # Character code 12
objectContainer.ShootRight = chr(26) # Character code 26
objectContainer.ShootLeft = chr(27)  # Character code 27

# Additional traps with character codes
objectContainer.Trap6 = chr(0)        # Character code 0
objectContainer.Trap7 = chr(0)        # Character code 0
objectContainer.Trap8 = chr(0)        # Character code 0
objectContainer.Trap9 = chr(0)        # Character code 0
objectContainer.Trap10 = chr(0)       # Character code 0
objectContainer.Trap11 = chr(0)       # Character code 0
objectContainer.Trap12 = chr(0)       # Character code 0
objectContainer.Trap13 = chr(0)       # Character code 0

# Message constant
objectContainer.Message = chr(5)      # Character code 5






# Return game level of levelNumber
def Level(screen, levelNumber):
    #case statement
    switcher = {
        1: Level1(screen),
        2: Level2(screen),
        # No level 3
        4: Level4(screen),
        # No level 5
        6: Level6(screen),
        # No level 7
        8: Level8(screen),
        # No level 9
        10: Level10(screen),
        # No level 11
        12: Level12(screen),
        # No level 13
        14: Level14(screen),
        # No level 15
        16: Level16(screen),
        # No level 17
        18: Level18(screen),
        # No level 19
        20: Level20(screen),
        # No level 21
        22: Level22(screen),
        # No level 23
        24: Level24(screen),
        25: Level25(screen),
    }

    return switcher.get(levelNumber, "Invalid option")


# Return game level 1
def Level1(screen):
    global objectContainer
    objectContainer.FP[1]  = 'W W W W             2 2 2 2 2  C  2 2 2 2 2              W W W W'
    objectContainer.FP[2]  = 'XXXXXXXXXXXXXXXXXXX###########   ###########XXXXXXXXXXXXXXXXXXXX'
    objectContainer.FP[3]  = ' 1           1                               1                  '
    objectContainer.FP[4]  = '                                    1            XX         1   '
    objectContainer.FP[5]  = '       1            1                           XXXX            '
    objectContainer.FP[6]  = '#        XX                    +                 XX            #'
    objectContainer.FP[7]  = '##      XXXX  1                +          1          1        ##'
    objectContainer.FP[8]  = 'T##      XX               2    +    2                        ##T'
    objectContainer.FP[9]  = 'T1##                       W   +   W                        ##1T'
    objectContainer.FP[10] = 'T########X                 WX     XW             1    X########T'
    objectContainer.FP[11] = '.        X                2WX  P  XW2                 X        .'
    objectContainer.FP[12] = 'T########X         1       WX     XW                  X########T'
    objectContainer.FP[13] = 'T1##                       W   +   W         1              ##1T'
    objectContainer.FP[14] = 'T##                       2    +    2                        ##T'
    objectContainer.FP[15] = '##   1                         +                      XX      ##'
    objectContainer.FP[16] = '#       XX      1              +                 1   XXXX     1#'
    objectContainer.FP[17] = '       XXXX                 ##   ##                   XX        '
    objectContainer.FP[18] = '1       XX                 ##     ##     1        1           1 '
    objectContainer.FP[19] = '                    1#######       ########                     '
    objectContainer.FP[20] = '    1         ########11111  +++++  111111########              '
    objectContainer.FP[21] = 'WW     ########+++++        #######         WWWWW########1    WW'
    objectContainer.FP[22] = '########¯                    2 2 2                     C########'
    objectContainer.FP[23] = 'L2  +  X      #kingdom#of#kroz#ii#by#scott#miller#      X  +  2L'
    Fast = chr(234)
    Convert_Format(screen)

# Return game level 2
def Level2(screen):
    global objectContainer
    objectContainer.FP[1]  = '                                                           .   '
    objectContainer.FP[2]  = '  2#############################K############################   '
    objectContainer.FP[3]  = '   ##  2    2   2 2    2   2  ###  2  2   2    2    2    2##   '
    objectContainer.FP[4]  = '  2##+#2   2   2    2  2 2   2  2 2  2   2 2   2   2    2  ##   '
    objectContainer.FP[5]  = '   ##+#   2  2    2   2   2   2    2    2  2    2    2   2 ##   '
    objectContainer.FP[6]  = '  2##+# 2    2  2   2  2 2 2 2  2 2  2 2 2   2    2   2   2##   '
    objectContainer.FP[7]  = '   ##+#2   2  2   2                            2   2   2   ## W '
    objectContainer.FP[8]  = '  2##+#  2   2   2   XXXXXXXXXXXXXXXXXXXXXXX  2    2  2   2##@@@'
    objectContainer.FP[9]  = '   ##+#2   2  2   2  XXXXXXXXXXXXXXXXXXXXXXX    2   2  2   ##   '
    objectContainer.FP[10] = '  2##+# 2   2  2 2   XXXXXXXXXXXXXXXXXXXXXXX   2  2   2  2 ##   '
    objectContainer.FP[11] = '   ##+#   2 2 2   2  XXXXXX    -+-    XXXXXX  2 2    2  2  ##   '
    objectContainer.FP[12] = '  2##+#2   2   2 2   XXXXXX1   -P-   1XXXXXX  2  2 2   2 2 ##   '
    objectContainer.FP[13] = '   ##+#  2  2  2  2  XXXXXX    -+-    XXXXXX   2  2 2     2##   '
    objectContainer.FP[14] = '  2##+# 2 2  2  2    XXXXXXXXXXXXXXXXXXXXXXX  2   2   2 2  ##   '
    objectContainer.FP[15] = '   ##+#2 2    2   2  XXXXXXXXXXXXXXXXXXXXXXX    2  2   2 2 ##   '
    objectContainer.FP[16] = '  2##+# 2  2  2  2   XXXXXXXXXXXXXXXXXXXXXXX   2    2 2 2  ##   '
    objectContainer.FP[17] = '   ##+#  2  2 2   2                           2  2   2   2 ##   '
    objectContainer.FP[18] = '  2##+#2   2    2   2 2  2  2  2 2  2 2  2  2   2   2  2  2##   '
    objectContainer.FP[19] = '   ##+# 2    2  2  2 2  2   2   2   2  2  2    2    2   2  ##   '
    objectContainer.FP[20] = '  2##3#   2   2   2   2   2   2   2   2 2    2    2   2   2##@@@'
    objectContainer.FP[21] = '   ##T#2   2     2  2  2 2   2 ###   2   2 2  2    2   2   ##222'
    objectContainer.FP[22] = '   #############################S#######################XXX##@@@'
    objectContainer.FP[23] = '                                                          I##LLL'
    Fast = chr(234)
    Convert_Format(screen)

# Return game level 4
def Level4(screen):
    global objectContainer
    objectContainer.FP[1]  = '-..............................3#1#2#3##------;------------;----'
    objectContainer.FP[2]  = '-##############################-##1#2#3#-######################-'
    objectContainer.FP[3]  = '-#.....----......- I#S###### ##K###1#2#3-#///////1///////////1//'
    objectContainer.FP[4]  = '-#.-..-....-....-.# # I####1# ######1#2#-#\1\\\\\\\\\\\\\1\\\\\\'
    objectContainer.FP[5]  = '-#-.-..-..-.....-.# # # ### ## ##1###1#2-#/////1////////////////'
    objectContainer.FP[6]  = '-#-.-.-..-..---..-# # ## # ##1## # ###1#-#CCC\\\\\\\\\1\\\\\\1\\'
    objectContainer.FP[7]  = '-#-.-..-.-.-..-..-# # ### ####  ### K##1-#CCC/////1//////1/////K'
    objectContainer.FP[8]  = '-#-..--...-....--.# # ##################-#######################'
    objectContainer.FP[9]  = '-#-################                                           à '
    objectContainer.FP[10] = '---3333333333-CC### #F######################XXXXXXXX###à####-##+'
    objectContainer.FP[11] = '################## ###------------------®###############2###-##+'
    objectContainer.FP[12] = 'big#######     ## ####22222222222222222#-##-----------###2##-##K'
    objectContainer.FP[13] = 'trouble## RRRRR  #######################-##-####U####-####2####+'
    objectContainer.FP[14] = '######## RRRKRRRR #########$;$$$$$$3$T##-##-----------#####2###3'
    objectContainer.FP[15] = '+++++### RR 2 2 RR ####Z###$############-##############Q###2###'
    objectContainer.FP[16] = '++T++## RR 2 P  2RR ### #-U--------------###TT.TT####----####2##'
    objectContainer.FP[17] = '+++++## RR2   2 RR ####1#-####################;###############2#'
    objectContainer.FP[18] = '#O#O#### RR 2  2RR #3## #C####3#3#3#3#3#3#3#3#3#3#3#3#3#3#3#3##D'
    objectContainer.FP[19] = '#X#X##### RRR2CRR ##3## # ###@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@###D'
    objectContainer.FP[20] = '#X#X###### RRRRRR ##3## #3##@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@##K#D'
    objectContainer.FP[21] = '-----; #### RRR  ### ## ###@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#D'
    objectContainer.FP[22] = '-----# #####   # ##W W# ##@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@##@#D'
    objectContainer.FP[23] = '22222#      #####       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#L'
    Fast = chr(234)
    Convert_Format(screen)

# Return game level 6
def Level6(screen):
    global objectContainer
    objectContainer.FP[1]  = '---###########RRRRR##W        ############W////1/C//\\//\\\\\\\\\\\\\\\\\\'
    objectContainer.FP[2]  = '-U---------Z###RRRRR##7######   ##KKô   Z##-//////\\///1/\\\\\\\\\\\\U\\'
    objectContainer.FP[3]  = '---###########RRRRR##7####### P ######## ###-////////\\///\\\\1\\\\\\\\'
    objectContainer.FP[4]  = '@#############RRRRR#7####                ####-///\\/////////\\\\\\\\\\'
    objectContainer.FP[5]  = '@2#------.###RRRRR##7#W3; ############## #####-////1//\\//1///\\\\\\'
    objectContainer.FP[6]  = '@##;-;###.##RRRRR##7##W3; #WWWWWWWWWWW## #2####--//////////\\///\\'
    objectContainer.FP[7]  = '@2#-;;##..##RRRRR##7##W3; ######-####### ##2#####-/////\\/////1//'
    objectContainer.FP[8]  = '@##;-;##..-##RRRRR##7#### #11111111111## ###2##2##-/////1/////\\/'
    objectContainer.FP[9]  = '@2#;;-##..#D##RRRRR##7##T #11111111111## #2##2##2##--///////\\///'
    objectContainer.FP[10] = '@##;;;##..#D###RRRRR##7####11111111111## ##2##2##2###---///////1'
    objectContainer.FP[11] = '@2#-;;##..#KK###RRRRR##7###11111111111## ###)##)##)#####--////\\/'
    objectContainer.FP[12] = '@##-;;##..#KK##RRRRRRR#7###11111B11111----)))))))))))#####---///'
    objectContainer.FP[13] = '@2#;;;##22####RRRR#RRR##7##11111111111##############)########--/'
    objectContainer.FP[14] = '@##;;-##22###RRRR###RRR##7#11111111111#?##---#*YYYY-63333####D#'
    objectContainer.FP[15] = '@2#;-;##22##RRRR##L##RRR#7#11111111111#O#T#-#-#*YYYY-63333---#D#'
    objectContainer.FP[16] = '@##;;;##22#RRRR##DD##RRR#7#11111111111#O#-4-#-#*YYYY-63333-#-4-#'
    objectContainer.FP[17] = '@2#;-;##-##RRRR#DDD#RRR##7###########-#O#-#-#-#*YYYY-63333-#-#-#'
    objectContainer.FP[18] = '@##;;-##C#RRRR##DDD##RRR##7###+++++##-#O#-#-#-#*YYYY-63333-#-#-#'
    objectContainer.FP[19] = '@2#;;;##H##RRRR#DDDD##RRR##7##+++++##-#O#-#-#-#*YYYY-63333-#-#-#'
    objectContainer.FP[20] = '@##;-;####RRRR##44444##RRR##7###.####-#O#-#-#-#*YYYY-63333-#-#-#'
    objectContainer.FP[21] = '@2#-;;###RRRR##ñññññññ##RRR#7###.#K-#-#O#-#-#-#*YYYY-63333-#-#-#'
    objectContainer.FP[22] = '@###-###RRRR##X--------#RRR##ô##.#--#-#-#---#-######-#####-#---#'
    objectContainer.FP[23] = '-----##RRRR##%X---U----##RRR#K##--------#111#--------------#111#'
    Fast = chr(234)
    HideOpenWall = true
    Convert_Format(screen)

# Return game level 8
def Level8(screen):
    global objectContainer
    objectContainer.FP[1]  = '-------¼--------44---³³³³³³³³³³³³º---º³³³³³³³³³³³------K---¹;-U-'
    objectContainer.FP[2]  = 'XXXXXXX-XXX-----44---      -----------------    ----#######-;---'
    objectContainer.FP[3]  = '--------------71#####       ---------------      #####¹-----;;;;'
    objectContainer.FP[4]  = 'K------------71###           -------------          #####³##; P '
    objectContainer.FP[5]  = '#17---------71####****        -----------       ****##----W;   '
    objectContainer.FP[6]  = '##17-------71#####*###         ----K----        ###*##³#####;   '
    objectContainer.FP[7]  = '###17-----71######*#             #####            #*## 1   7;   '
    objectContainer.FP[8]  = '####17---71#######*;     W    W    W    W    W    :*#######³;   '
    objectContainer.FP[9]  = '#####17-71########*#444444444444444444444444444444#*##ñ     ;   '
    objectContainer.FP[10] = '######---#########*#                              #*##444³##;   '
    objectContainer.FP[11] = '#######ä##########U#                              #!##     ;   '
    objectContainer.FP[12] = '----------------####                              ######³###;   '
    objectContainer.FP[13] = '----------------##VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV##     ;   '
    objectContainer.FP[14] = '----------------##VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV###³####;   '
    objectContainer.FP[15] = '»ä-------------ò######################################      ;   '
    objectContainer.FP[16] = '5555555555555555#############the#lava#pit#################³#;   '
    objectContainer.FP[17] = '            -------         ------------***********-##+   C;   '
    objectContainer.FP[18] = '              000            ---»######-###########-####³###;   '
    objectContainer.FP[19] = '                                ------7##LL-D-D-D-³##      ;   '
    objectContainer.FP[20] = '                                     ##-###########³#######³;   '
    objectContainer.FP[21] = '                                     ##-7  1   TTT7³##     ;   '
    objectContainer.FP[22] = '¼       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1##--#########³###³####;   '
    objectContainer.FP[23] = '###this#is#the#first#sideways#level####111111111  äC##        '
    Fast = chr(234)
    LavaFlow = true
    LavaRate = 75
    GravOn = True
    GravRate = 0
    Sideways = True
    Convert_Format(screen)

# Return game level 10
def Level10(screen):
    global objectContainer
    objectContainer.FP[1]  = '!+-----+----+------+##%VVOOOOO44U44OOOOVV%##3333333333333333333K'
    objectContainer.FP[2]  = '-----+--+-----+-----##VVVOOOOO44444OOOOVVV##66666666666666666663'
    objectContainer.FP[3]  = '+--+------+--------+##OOOOOOOO##5##OOOOOOO##                  63'
    objectContainer.FP[4]  = '-----+-------+----+-##OOOOOOOO##?##OOOOOOO##                  63'
    objectContainer.FP[5]  = '---+-----+------+---##VVVOOOOOO###OOOOOVVV##XXXXX             63'
    objectContainer.FP[6]  = '-+----+-------+-----##CVVOOOOOOO#OOOOOOVVC##XXXXX             63'
    objectContainer.FP[7]  = '+-------+--------+-U##CVVOOOOOOOOOOOOOOVVC##UXXXX             63'
    objectContainer.FP[8]  = '###############################OOO##############################'
    objectContainer.FP[9]  = 'MMMMMMMMMMMMMMMMMMMM##S                  S##11111111111111111111'
    objectContainer.FP[10] = 'MMMMMMMMMMMMMMMMMMMM##                    ##11111111111111111111'
    objectContainer.FP[11] = '@@@@@@@@@@@@@@@@@@@@##         000        ##11111111111111111111'
    objectContainer.FP[12] = 'K@@@@@@@@@@@@W                 0P0        HB11111111111B1111111ñ'
    objectContainer.FP[13] = '@@@@@@@@@@@@@@@@@@@@##         000        ##11111111111111111111'
    objectContainer.FP[14] = 'MMMMMMMMMMMMMMMMMMMM##                    ##11111111111111111111'
    objectContainer.FP[15] = 'MMMMMMMMMMMMMMMMMMMM##S                  S##11111111111111111111'
    objectContainer.FP[16] = '###############################~~~##############################'
    objectContainer.FP[17] = '111111111111111111-U##C00000000---0-000---##U-))I)))))))333))))-'
    objectContainer.FP[18] = '1(((((((((((((((((--##-0000H---0000---0-0-##--)I)))))))333))))-*'
    objectContainer.FP[19] = '1(((((((TTT((((((((1##00000000 00000000000##))I)))))))333))))-*I'
    objectContainer.FP[20] = '1(((((((TTT((((((((1##-0-00000000000000-00##)I)))))))333))))-*I*'
    objectContainer.FP[21] = '1(((((((TTT((((((((1##00-0-----0000000<[|"##I)))))))333))))-*I*I'
    objectContainer.FP[22] = '1((((((((((((((((((1##-#####################)))))))333))))-*I*I*'
    objectContainer.FP[23] = 'ó1111111111111111111##C-------D-D-D]]Eò&LL##K)))))333))))-*I*I*C'
    Fast = chr(234)
    HideGems = true
    Convert_Format(screen)

# Return game level 12
def Level12(screen):
    global objectContainer
    objectContainer.FP[1]  = 'LLL##U##@@@@@@@@@@@|000---0000000000000000-0--00000000VVV000Y-0V'
    objectContainer.FP[2]  = '```##-##@00000000000000---0000222222220---0000-00000000000--Y-0V'
    objectContainer.FP[3]  = '```##K##@@022222222K000---0000-0000000000-0000-0)))))YYYW-W0Y-0V'
    objectContainer.FP[4]  = '```##6##@@@222222222000---000U*******00000000000)))0000000000-00'
    objectContainer.FP[5]  = '```##6##@@@222222222000---000000000000000000000000222222--000---'
    objectContainer.FP[6]  = '```##6##@@0222222222000---(((((((((((((((ñ(((((000222222-C00000-'
    objectContainer.FP[7]  = '333##6##@00000000000000---00004444444444444444(0000000000000000-'
    objectContainer.FP[8]  = '333##6##3CCC....0---------00022222222222222222(K(---------------'
    objectContainer.FP[9]  = '$$$##6##000000000000000---00000000000000000000000000000000000000'
    objectContainer.FP[10] = '   0--00000000000000000---000000000000000000000===============--'
    objectContainer.FP[11] = ' P 00-00+02222222220--------------------------0="===-=--===-==-='
    objectContainer.FP[12] = '$$$00-00+02222222220-00---0000000000000000000-0==I=-=-==-=-=-==-'
    objectContainer.FP[13] = ' ! 00-00+02222222220-00-Z-0000000000000000000-0=H==-===T==-==--='
    objectContainer.FP[14] = '00000-00[02222B22220-00---00----03333333CC----0==I==-===-==-===='
    objectContainer.FP[15] = '0--00-00+02222222220-00---00-0000000000000000-0===--==-==-==--=='
    objectContainer.FP[16] = '-0000-00+02222222220-00---00-0000000000000000-0==-===-=-=-====-='
    objectContainer.FP[17] = '00000-00+02222222220W00---00-----0--------000-0=-==--==-=-=--=T='
    objectContainer.FP[18] = '0--00-00000000000000000---000000000001110-000-0==T-===-===-==-=='
    objectContainer.FP[19] = '00000-00000000000000000---000000000001110-00000=======-========='
    objectContainer.FP[20] = '--000----------------- ---0WWWWWWWWK01110-000-000000000000000000'
    objectContainer.FP[21] = '00000-00000000000000000---000-00000001110-000K--<000OO000OOOOOó*'
    objectContainer.FP[22] = '--000-000000~~~0000000#---#00-00000000000-000000000000OOOO000000'
    objectContainer.FP[23] = '00C000000********3000##VVV##0-------------00000000bouldervilleÃ0'
    Fast = chr(234)
    LavaFlow = True
    LavaRate = 30;
    Convert_Format(screen)

# Return game level 14
def Level14(screen):
    global objectContainer
    objectContainer.FP[1]  = '###<@@@@@@@@@@@@@@@@@@@@@@@@@#one#@@@@@@@@@@@@@@@@@@@@@@@@@FK###'
    objectContainer.FP[2]  = 'Kö###@@@@@@@@@@@@@@@@@@@@@@@@@;!:@@@@@@@@@@@@@@@@@@@@@@@@@@###$['
    objectContainer.FP[3]  = 'öö((###@@@@@@@@@@@@@@@@@@@@@@@:::@@@@@@@@@@@@@@@@@@@@@@@@###$$$$'
    objectContainer.FP[4]  = '((((((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###$$$$$$'
    objectContainer.FP[5]  = '(((((((2###222222222222222222222222222222222222222222###2$$$$$$$'
    objectContainer.FP[6]  = '(((((((2((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###$$2$$$$$$$'
    objectContainer.FP[7]  = '(((((((2((((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###$$$$2$$$$$$$'
    objectContainer.FP[8]  = '(((((((2((((((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###$$$$$$2$$$$$$$'
    objectContainer.FP[9]  = 'DD##(((2((((((((###@@@@@@@@@@@@@@@@@@@@@@@@@@###$$$$$$$$2$$$####'
    objectContainer.FP[10] = 'DD#f(((2(((((((((##############77##############$$$$$$$$$2$$$##CC'
    objectContainer.FP[11] = 'DD#o(((2((((((((ö##2------------------------2##ô$$$$$$$$2$$$t#àà'
    objectContainer.FP[12] = 'DD#u(((2((((((((ö----------F---P----S--------88ô$$$$$$$$2$$$w#MM'
    objectContainer.FP[13] = '&&#r(((2((((((((ö##2------------------------2##ô$$$$$$$$2$$$o#MM'
    objectContainer.FP[14] = 'LL##(((2(((((((((##############99##############$$$$$$$$$2$$$##MM'
    objectContainer.FP[15] = '####(((2((((((((###)))))))))))õõõõ)))))))))))###$$$$$$$$2$$$##àà'
    objectContainer.FP[16] = '(((((((2((((((###))))))))))))))))))))))))))))))###$$$$$$2$$$$$$$'
    objectContainer.FP[17] = '(((((((2((((###))))))))))))))))))))))))))))))))))###$$$$2$$$$$$$'
    objectContainer.FP[18] = '(((((((2((###))))))))))))))))))))))))))))))))))))))###$$2$$$$$$$'
    objectContainer.FP[19] = '(((((((2###))))))))))))))))))))))))))))))))))))))))))###2$$$$$$$'
    objectContainer.FP[20] = '((((((###2222222222222222222222222222222222222222222222###$$$$$$'
    objectContainer.FP[21] = '((((###))))))))))))))))))))))))))))))))))))))))))))))))))###$$ôô'
    objectContainer.FP[22] = '"(###))))))))))))))))))))))))))))))))))))))))))))))))))))))###ôK'
    objectContainer.FP[23] = '###Kõ)))))))))))))))))))))))#three#))))))))))))))))))))))))F|###'
    Fast = chr(234)
    Convert_Format(screen)

# Return game level 16
def Level16(screen):
    global objectContainer
    objectContainer.FP[1]  = '##tunnels#of#kroz###########-P--################################'
    objectContainer.FP[2]  = '########################X###----######X##---------------##X####'
    objectContainer.FP[3]  = '############################----#########----------------#######'
    objectContainer.FP[4]  = 'L---N----H######ò  ò ò######-----------------########----#######'
    objectContainer.FP[5]  = 'L---N-----##X###  CC  555555-----------------#####X##1111#######'
    objectContainer.FP[6]  = '######----######ò ò  ò###############################----#####X#'
    objectContainer.FP[7]  = '######1111###########################################1111#######'
    objectContainer.FP[8]  = '#X####----##############X#######magic#####X##########----#######'
    objectContainer.FP[9]  = '######1111####################----##############----N-----#'
    objectContainer.FP[10] = '######----####################----K----##############----N-----#'
    objectContainer.FP[11] = '######1111#######X############----#########X##########----#'
    objectContainer.FP[12] = '######----########################-########################1111#'
    objectContainer.FP[13] = '######1111################X#######-########################----#'
    objectContainer.FP[14] = '######----########################---------N-------------------#'
    objectContainer.FP[15] = '###X##----##########################################-----------#'
    objectContainer.FP[16] = '######---------------7ñ########################X####----########'
    objectContainer.FP[17] = '######---------------7-444444444444444444###########1111########'
    objectContainer.FP[18] = '#####O#############--77##################444########----#####X##'
    objectContainer.FP[19] = '####O##############1111#############X#######4ô%-####1111########'
    objectContainer.FP[20] = '###O#####XXX#######----#############################----########'
    objectContainer.FP[21] = '##O#####X###Q######-------N------`----------------------########'
    objectContainer.FP[22] = '##O##OOO###########-------N------`---------------------##X#####'
    objectContainer.FP[23] = '###OO###########################################################'
    Fast = chr(234)
    HideStairs = True
    HideOpenWall = True
    Convert_Format(screen)

# Return game level 18
def Level18(screen):
    global objectContainer
    objectContainer.FP[1]  = '###########klose#enkounters#of#the#krazy#kubikal#kindÃ##########'
    objectContainer.FP[2]  = '3                               P                              3'
    objectContainer.FP[3]  = '##-##############:########:#######:###########:##############:##'
    objectContainer.FP[4]  = 'XXXXXXXXX##~W~W~W~W~##-M----M.--$$$$$$$$$-9/-/\\--\\-|##---ò---'
    objectContainer.FP[5]  = '---------##*~*~*~*~*##-.-M--##$$$$$$$$$##\\--/-\\-/\\##YYYYYYYYY'
    objectContainer.FP[6]  = 'MMMMMMMMM##~W~W~W~W~##M---.-M-##111111111##-/-\\/--/-##((((((((('
    objectContainer.FP[7]  = ')))))))))##*~*~*~*~*##.-.--.##222222222##/\\--\\-\\-/##((((((((('
    objectContainer.FP[8]  = 'C))))))))--~W~W~W~W~##ó.----M##333333333##ü-//-\\-/-9-((((((((('
    objectContainer.FP[9]  = '###################-################################9##55555555-'
    objectContainer.FP[10] = '----##YYYYYYYYY##222222222------0---W##RRRRRRRRR##MMMMMMMMM'
    objectContainer.FP[11] = '-----------YYYYYYYYY##@@@@@@@@@##---000---##RXXXXXXXR##MMMMMMMMM'
    objectContainer.FP[12] = 'XXXXXXXXX##YYYYYYYYY##@@@@@@@@@##--00G00--##RXXXKXXXR##MMMMMMMMM'
    objectContainer.FP[13] = '---------##YYYYYYYYY##@@XXX@@@@##---000---##RXXXXXXXR##MMMMMMMMM'
    objectContainer.FP[14] = '##YYYYYYYYK##@@XZX@@@@##----0---W##RRRRRRRRR##MMMMMMMMK'
    objectContainer.FP[15] = '-#####################-##########ô##################H##Z########'
    objectContainer.FP[16] = '~-~[~-~-~##WWW......à1:1:1:1:1:##-773C7--7##=--=I==-=##ááááááY0"'
    objectContainer.FP[17] = '-~-~-~-~-##WWW......##1:1:1:1:1##7-777-77-##!==-=--==##ááááááY00'
    objectContainer.FP[18] = '~-~-~-~-~##.........##:1:1:1:1:##-77--77-7##=======-=##ááááááYYY'
    objectContainer.FP[19] = '-~-~-~-~-##.........##1:1:1:1:1##7-7-77-77##-==-=-==I##ááááááááá'
    objectContainer.FP[20] = 'K-~-~-~-~-à..<......##:1:1:1:1ñ##77-7777---I=--=-=--=##222222222'
    objectContainer.FP[21] = '############################################################44##'
    objectContainer.FP[22] = 'LL---V--V-VV-V--VV---D-----D----D----D--66333333333333333-WWWW'
    objectContainer.FP[23] = 'LL--V-VV-V--V-VV--V--D-----D----D----D--66YYYYYYYYYYYYYYYYYYYY'
    Fast = chr(234)
    TreeRate = 35
    Convert_Format(screen)

# Return game level 20
def Level20(screen):
    global objectContainer
    objectContainer.FP[1]  = '###key#shop###MTMMMMMMMMMMMMMMMMMMMMM-----MMMMMMMMMMMM-MM--!##LL'
    objectContainer.FP[2]  = '##Káà44@@@@@##MMMMMMMMMMMMMMMMMMMMMM-MMMMM-MMMMMMMMMM-M-M-P-##LL'
    objectContainer.FP[3]  = '##Ká3##@@@@@@DMMMMMMCMMMMMMMMMMMMMM-MMMMMMM-MMM<MMMM-MMM----##DD'
    objectContainer.FP[4]  = '##Káà##@@@@@##M-MMMMMMMMMMMMMMMM---MMMMMMMM-MMMMMMM-MMMMMMMM##DD'
    objectContainer.FP[5]  = '#######X######MM-MMMMMMMMMMM----MMMMMMMMMMMM-MMMMM-MMMMMMMMM##DD'
    objectContainer.FP[6]  = '##ñ-----##MMMMMMM-MMMMM-----MMMMMMMMMMMKMMMMM-MMM-MMMMMMMMMM##DD'
    objectContainer.FP[7]  = '##########MMMMMMTMMMMM-MMMMMMMMMMMMMMMMMMMMMMM-M-MMMMMMMMMMMMMMM'
    objectContainer.FP[8]  = 'MMMMMMMMMMMMMMMMMMMMM-MMMMMMMMMMMMMMMMMMMMMMMMM-MMMMMMCMMMMMM-MM'
    objectContainer.FP[9]  = 'MMMMMMMM-----MMMM----MMMMMMMM[MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MMM'
    objectContainer.FP[10] = 'MMMM----MMMMM----MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMTMMMMMMMMMMM-MMMM'
    objectContainer.FP[11] = 'MMM-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MMM'
    objectContainer.FP[12] = 'MM-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MM'
    objectContainer.FP[13] = 'MM-MMMMMMCMMMMMMMMMMMMMMMBWWWWWWWWWW-------------------------MMM'
    objectContainer.FP[14] = 'MM-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MM'
    objectContainer.FP[15] = 'MM-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMTMMMMMMMMMMMMMMM-M'
    objectContainer.FP[16] = 'MMM-------MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MM'
    objectContainer.FP[17] = 'MMMMMMMMMM-----MMMMMMMMMMMMMMMM]MMMMMMMMM-M-MMMMMMMMMMMMMMMM-MMM'
    objectContainer.FP[18] = ')))))))))MMMMMM-MMMMMMMMMMMMMMMMMMMMMM-M-M-M-MMMMMMMMCMMMMM-MMMM'
    objectContainer.FP[19] = '22222222)MMTMMM-MMMMMCMMMMMMMMMMMMMMM-M-MMMMM-MMM-MMMMMMMM-MMMMM'
    objectContainer.FP[20] = '22222222)MMMMMM-MMMMMMMMMMMMMMM------MMMMMMM-MMM-M-MMMMMM-MMMMMM'
    objectContainer.FP[21] = '22222222)MMMMMM-MMMMMMMMMM-----MMMMMMMMMMMM-MMM-MM-MMMMM-MMMMMMM'
    objectContainer.FP[22] = '--222222)MMMMMM-----------MMMMMMMMMMMMMMMM-MM-M-MMM-M-M-MMMMM"MM'
    objectContainer.FP[23] = 'K-222222)MMMMMMMMMMMMMMMMMMMMMMMMMM|MMMMMMM--M-MMMMM-M-MMMMMMMMM'
    Fast = chr(234)
    Convert_Format(screen)

# Return game level 22
def Level22(screen):
    global objectContainer
    objectContainer.FP[1]  = '1111144       ##C######locksmith#shoppe######C##         RRRRRRR'
    objectContainer.FP[2]  = '1111144       ##]##K#K#K#K#K#-3-3#K#K#K#K#K##]##        RRRRRRRñ'
    objectContainer.FP[3]  = '1111144          ##:::::::::######::::::::;##         RRRRRRRCYY'
    objectContainer.FP[4]  = '1111144          ##------------------------##     666RRRRRRRR66 '
    objectContainer.FP[5]  = '1111144          #############--#############     6666666666666 '
    objectContainer.FP[6]  = '1111144                                           HOOOOOOOOH    '
    objectContainer.FP[7]  = '1111144                                        6666666666666    '
    objectContainer.FP[8]  = '1111144                                        66RRRRRRR6666    '
    objectContainer.FP[9]  = '1111144                                        RRRRRRR          '
    objectContainer.FP[10] = '1111144                                      RRRRRR           YY'
    objectContainer.FP[11] = '1111144               P                    RRRRRR             YZ'
    objectContainer.FP[12] = '1111144                                 RRRRRRRRRR            YY'
    objectContainer.FP[13] = '1111144                              RRRRR333RRRRR              '
    objectContainer.FP[14] = '1111144                             RRR3333333RRRRR             '
    objectContainer.FP[15] = '@@@@@##                           RRR3333333333RRRRR            '
    objectContainer.FP[16] = 'MMMMM##                           RRR333333333RRRRR             '
    objectContainer.FP[17] = ')))))##                          RRR33333333RRRRR               '
    objectContainer.FP[18] = 'MMMMM##                        RRRR333333RRRRRRR        DDDDDDDD'
    objectContainer.FP[19] = '(((((##                       RRRR3LL3RRRRRRRR          DDDDDDDD'
    objectContainer.FP[20] = 'MMMMM##                      RRRRRRRRRRRRRR             DDDDDDDD'
    objectContainer.FP[21] = '$$$$$##                     RRRRRRRRRRRR                DDDD7777'
    objectContainer.FP[22] = 'MMMMM##                     RRRRRRRR                    DDDD77ôô'
    objectContainer.FP[23] = ']]K]]##                   RRRRRRK]                     DDDD77ô!'
    Fast = chr(234)
    HideCreate = true
    Convert_Format(screen)

# Return game level 24
def Level24(screen):
    global objectContainer
    objectContainer.FP[1]  = 'T    P  #the#step#of#faith#------~Kñ-------U-----#---D-D-D-D-LL'
    objectContainer.FP[2]  = '######----------------------º44444444-------»-K--#½############'
    objectContainer.FP[3]  = '-----------------------------#       ------#####»-#-----³-------'
    objectContainer.FP[4]  = '-----------------------------#        -----:------#----³-³------'
    objectContainer.FP[5]  = '------###--------------------#        -----:------#--³³---³-----'
    objectContainer.FP[6]  = '--------#--------------------#        -----:------#-#------¼----'
    objectContainer.FP[7]  = '--------#--------------------#        -----#####--#-#-----------'
    objectContainer.FP[8]  = '--------#--------------------#        -----#---;--#-#------¼----'
    objectContainer.FP[9]  = '--------#--------------------#        -----#<###--#-#-----------'
    objectContainer.FP[10] = '--------#---------õ---------º#         ----#[#----#-#-----³-----'
    objectContainer.FP[11] = '--K-----#¹########88888888888#         ----#|#----#-#----³--W---'
    objectContainer.FP[12] = '-XXX----#      #             #         ----#"#----#-#-------W---'
    objectContainer.FP[13] = '        #      #             #          ---#-#----#-#---³---W---'
    objectContainer.FP[14] = '        #     #             #          ----------#-##-³----W---'
    objectContainer.FP[15] = '        #      #             #             ;;;;;- #½K#³-----W---'
    objectContainer.FP[16] = '        #      #             #                 +-+####------W---'
    objectContainer.FP[17] = '        #      #             #                 +-+----³-----W---'
    objectContainer.FP[18] = '    XXXX#      #             #                 +-+---³------W---'
    objectContainer.FP[19] = '         ¹     #             #                 +-+###-----------'
    objectContainer.FP[20] = '       ###     #             #    U            +-+#--------7----'
    objectContainer.FP[21] = '               #             #                 + +#   ##C.!.C## '
    objectContainer.FP[22] = '               #             #                 + +#   ######### '
    objectContainer.FP[23] = 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV'
    Fast = chr(234)
    GravOn = true
    GravRate = 0
    Sideways = true
    LavaFlow = true
    LavaRate = 75
    Convert_Format(screen)

# Return game level 25
def Level25(screen):
    global objectContainer
    objectContainer.FP[1]  = 'K¯    -++++++++++++++++#the#sacred#temple#+++++++++++++++-    ®K'
    objectContainer.FP[2]  = ' VVVVVV11111111111111111111111111111111111111111111111111\\\\\\ '
    objectContainer.FP[3]  = ' VVVV;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\\\\ '
    objectContainer.FP[4]  = ' VV1111111111;:::-:::111111111#####111111111::-:::::111111111\\ '
    objectContainer.FP[5]  = ' V11         :-:-:-::        ###A###        :-:-:--:        11\\ '
    objectContainer.FP[6]  = 'X 1          ::-:::B:        RR#`#RR        :B::-::;         1 X'
    objectContainer.FP[7]  = 'X  22####-####-------------RRRR#D#RRRR-------------####-####22 X'
    objectContainer.FP[8]  = 'X  22##3@-@3##;3;3;3;3;3;3RRRRR#`#RRRRR3;3;3;3;3;3;##~~~~~##22 X'
    objectContainer.FP[9]  = 'X  22##3@-@3##3;3;3;3;3;3RR1C##D##C1RR3;3;3;3;3;3##~~~~~##22 X'
    objectContainer.FP[10] = 'X  22##3@-@3##;3;3;3;3;3RR11##`##11RR3;3;3;3;3;##~~~~~##22 X'
    objectContainer.FP[11] = 'X--####3@-@3####3;3;3;3RR11#####D#####11RR3;3;3;3####~~~~~####-X'
    objectContainer.FP[12] = 'X   U##3@@@3##U ;3;3;3RRB11-+T1   1T+-11BRR3;3;3; U##~~~~~##U  X'
    objectContainer.FP[13] = 'X--####3@@@3####3;3;3;3RR11#####P#####11RR3;3;3;3####~~~~~####-X'
    objectContainer.FP[14] = 'X  22##3@@@3##;3;3;3;3;3RR1111##U##1111RR3;3;3;3;3;##~~~~~##22 X'
    objectContainer.FP[15] = 'X  22##3@@@3##3;3;3;3;3;3RR111#####111RR3;3;3;3;3;3##~~~~~##22 X'
    objectContainer.FP[16] = 'X  22##3@K@3##;3;3;3;3;3;3RR111äää111RR3;3;3;3;3;3;##~~K~~##22 X'
    objectContainer.FP[17] = 'X  22#########-----B-------RRRRäCäRRRR-------B-----#########22 X'
    objectContainer.FP[18] = 'X 1  ##|0<0                   RRRRR                   0[0"## 1 X'
    objectContainer.FP[19] = ' R11 #######  11111111111111;--->---;11111111111111  #######11= '
    objectContainer.FP[20] = ' RR111111111111-VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV-11111111111== '
    objectContainer.FP[21] = ' RRRR111111111-V V V-V V V-2-V*VCV*V-2-V V-V-V V V-11111111==== '
    objectContainer.FP[22] = 'áRRRRRR111111-V V V-2-V V V-V*V*V*V*V-V V V-2-V V V-11111======â'
    objectContainer.FP[23] = 'KááááááááááááVGVV V V V VV*V*V*V*V*VV V V V VVGVâââââââââââK'
    Fast = chr(234)
    MagicEWalls = true
    Convert_Format(screen)


def Display_Playfield(screen):
    global objectContainer

    for XLoop in range(objectContainer.XBot, objectContainer.XTop + 1):
        for YLoop in range(objectContainer.YBot, objectContainer.YTop + 1):
            print("Hi Ho!!!: " + str(XLoop) + " " + str(YLoop) + " " + str(objectContainer.PF[XLoop][YLoop]))
            if (objectContainer.PF[XLoop][YLoop] != 0 or FloorPattern) and not HideLevel:
                screen.GotoXY(XLoop, YLoop)
                tile = objectContainer.PF[XLoop][YLoop]

                #Print this tile with a bit of text before the tile
                print(str(tile) + ":", end="")

                if tile == 0:  # Floor
                    screen.screen.Col(CF1, CF2)
                    screen.Bak(BF1, BF2)
                    screen.Write(Tile)
                    screen.Bak(0, 0)
                elif tile == 1:  # Slow
                    screen.Col(12, 7)
                    screen.Write(Slow)
                elif tile == 2:  # Medium
                    screen.screen.Col(10, 7)
                    screen.Write(Medium)
                elif tile == 3:  # Fast
                    screen.screen.Col(9, 7)
                    screen.Write(Fast)
                elif tile == 4:  # Block
                    if Level != 71:
                        screen.Col(6, 7)
                        screen.Write(objectContainer.Block)
                elif tile == 5:  # Whip
                    screen.screen.Col(15, 7)
                    screen.Write(Whip)
                elif tile == 6:  # Stairs
                    if not HideStairs:
                        screen.Bak(7, 7)
                        screen.screen.Col(16, 16)
                        screen.Write(Stairs)
                        screen.Bak(0, 0)
                elif tile == 7:  # Chest
                    if random.randint(0, 19) == 0:
                        screen.screen.Col(15, 7)
                        screen.Write(Chance)
                    else:
                        screen.screen.Col(14, 7)
                        screen.Bak(4, 0)
                        screen.Write(Chest)
                        screen.Bak(0, 0)
                elif tile == 8:  # SlowTime
                    if random.randint(0, 34) == 0:
                        screen.screen.Col(15, 7)
                        screen.Write(Chance)
                    else:
                        screen.screen.Col(11, 7)
                        screen.Write(SlowTime)
                elif tile == 9:  # Gem
                    if not HideGems:
                        screen.screen.Col(GemColor, 7)
                        screen.Write(Gem)
                elif tile == 10:  # Invisible
                    screen.screen.Col(2, 7)
                    screen.Write(Invisible)
                elif tile == 11:  # Teleport
                    screen.screen.Col(13, 7)
                    screen.Write(Teleport)
                elif tile == 12:  # Key
                    if random.randint(0, 24) == 0:
                        screen.screen.Col(15, 7)
                        screen.Write(Chance)
                    else:
                        screen.screen.Col(12, 15)
                        screen.Write(Key)
                elif tile == 13:  # Door
                    screen.Bak(5, 7)
                    screen.screen.Col(3, 0)
                    screen.Write(Door)
                    screen.Bak(0, 0)
                elif tile == 14:  # Wall
                    screen.screen.Col(6, 7)
                    screen.Write(Wall)
                elif tile == 15:  # SpeedTime
                    if random.randint(0, 9) == 0:
                        screen.screen.Col(15, 7)
                        screen.Write(Chance)
                    else:
                        screen.screen.Col(11, 7)
                        screen.Write(SpeedTime)
                elif tile == 16:  # Trap
                    if not HideTrap:
                        screen.screen.Col(7, 7)
                        screen.Write(Trap)
                elif tile == 17:  # River or Lava
                    if Level == 56:
                        screen.screen.Col(12, 16)
                        screen.Bak(4, 7)
                        screen.Write(Lava)
                        screen.Bak(0, 0)
                    else:
                        screen.screen.Col(9, 0)
                        screen.Bak(1, 7)
                        screen.Write(River)
                        screen.Bak(0, 0)
                elif tile == 18:  # Power
                    if random.randint(0, 14) == 0:
                        screen.screen.Col(15, 7)
                        screen.Write(Chance)
                    else:
                        screen.screen.Col(15, 7)
                        screen.Write(Power)
                elif tile == 19:  # Forest
                    screen.screen.Col(2, 7)
                    screen.Write(Forest)
                    screen.Bak(0, 0)
                elif tile in [20, 252]:  # Tree
                    screen.screen.Col(6, 0)
                    screen.Bak(2, 7)
                    screen.Write(Tree)
                    screen.Bak(0, 0)
                elif tile == 21:  # Bomb
                    if random.randint(0, 39) == 0:
                        screen.screen.Col(15, 7)
                        screen.Write(Chance)
                    else:
                        screen.screen.Col(15, 7)
                        screen.Write(Bomb)
                elif tile == 22:  # Lava
                    screen.screen.Col(12, 16)
                    screen.Bak(4, 7)
                    screen.Write(Lava)
                    screen.Bak(0, 0)
                elif tile == 23:  # Pit
                    screen.screen.Col(7, 7)
                    screen.Write(Pit)
                elif tile == 24:  # Tome
                    screen.screen.Col(31, 31)
                    screen.Bak(5, 0)
                    screen.Write(Tome)
                    screen.Bak(0, 0)
                elif tile == 25:  # Tunnel
                    screen.screen.Col(15, 7)
                    screen.Write(Tunnel)
                elif tile == 26:  # Freeze
                    screen.screen.Col(11, 7)
                    screen.Write(Freeze)
                elif tile == 27:  # Nugget
                    screen.screen.Col(14, 7)
                    screen.Write(Nugget)
                elif tile == 28:  # Quake
                    if random.randint(0, 14) == 0:
                        screen.screen.Col(15, 7)
                        screen.Write(Chance)
                elif tile == 29:  # IBlock
                    pass
                elif tile == 30:  # IWall
                    pass
                elif tile == 31:  # IDoor
                    pass
                elif tile == 32:  # Stop
                    pass
                elif tile == 34:  # Zap
                    screen.screen.Col(12, 7)
                    screen.Write(Zap)
                elif tile == 35:  # Create
                    if not HideCreate:
                        screen.screen.Col(15, 7)
                        screen.Write(Chance)
                elif tile == 36:  # Generator
                    screen.screen.Col(30, 31)
                    screen.Write(Generator)
                elif tile == 38:  # MBlock
                    if not hideMBlock:
                        screen.screen.Col(6, 7)
                        screen.Write(MBlock)
                elif tile in [33, 37, 39, 67] or 224 <= tile <= 231:  # Trap2-13
                    pass
                elif tile == 40:  # Player
                    screen.Bak(7, 7)
                    screen.screen.Col(16, 16)
                    screen.Write(Stairs)
                    screen.Bak(0, 0)
                elif tile == 41:  # ShowGems
                    pass
                elif tile == 42:  # Tablet
                    screen.screen.Col(9, 7)
                    screen.Write(Tablet)
                elif tile == 43:  # ZBlock
                    screen.screen.Col(6, 7)
                    screen.Write(ZBlock)
                elif tile == 44:  # BlockSpell
                    pass
                elif tile == 45:  # Chance
                    screen.screen.Col(15, 7)
                    screen.Write(Chance)
                elif tile == 46:  # Statue
                    screen.screen.Col(31, 23)
                    screen.Write(Statue)
                elif tile == 48:  # K
                    screen.screen.Col(14, 15)
                    screen.Write('K')
                elif tile == 49:  # R
                    screen.screen.Col(14, 15)
                    screen.Write('R')
                elif tile == 50:  # O
                    screen.screen.Col(14, 15)
                    screen.Write('O')
                elif tile == 51:  # Z
                    screen.screen.Col(14, 15)
                    screen.Write('Z')
                elif tile in [52, 53]:  # OWall1,2
                    screen.screen.Col(6, 7)
                    screen.Write(Wall)
                elif tile == 54:  # OWall3
                    screen.screen.Col(7, 7)
                    screen.Write(Wall)
                elif 55 <= tile <= 57:  # CWall1..3
                    pass
                elif 58 <= tile <= 60:  # OSpell1..3
                    if not HideOpenWall:
                        screen.screen.Col(11, 7)
                        screen.Write(OSpell1)
                elif 61 <= tile <= 63:  # CSpell1..3
                    pass
                elif 68 <= tile <= 74:  # Triggers
                    pass
                elif tile == 64:  # GBlock
                    screen.screen.Col(7, 7)
                    screen.Write(GBlock)
                elif tile == 65:  # Rock
                    if not HideRock:
                        screen.screen.Col(7, 7)
                        screen.Write(Rock)
                elif tile == 66:  # EWall
                    screen.screen.Col(12, 0)
                    screen.Bak(4, 7)
                    screen.Write(EWall)
                    screen.Bak(0, 0)
                elif tile == 47:  # WallVanish
                    if random.randint(0, 19) == 0:
                        screen.screen.Col(15, 7)
                        screen.Write(Chance)
                elif tile == 75:  # Rope
                    screen.screen.Col(7, 7)
                    screen.Write(Rope)
                elif 76 <= tile <= 80:  # DropRope
                    screen.screen.Col(7, 7)
                    screen.Write(DropRope)
                elif tile == 82:  # ShootRight
                    screen.screen.Col(7, 7)
                    screen.Write(ShootRight)
                elif tile == 83:  # ShootLeft
                    screen.screen.Col(7, 7)
                    screen.Write(ShootLeft)
                elif tile == 81:  # Amulet
                    screen.screen.Col(31, 31)
                    screen.Write(Amulet)
                elif tile == 180:  # punct.
                    screen.screen.Col(15, 0)
                    screen.Bak(6, 7)
                    screen.Write('.')
                    screen.Bak(0, 0)
                elif tile == 181:  # punct.
                    screen.screen.Col(15, 0)
                    screen.Bak(6, 7)
                    screen.Write('?')
                    screen.Bak(0, 0)
                elif tile == 182:  # punct.
                    screen.screen.Col(15, 0)
                    screen.Bak(6, 7)
                    screen.Write('\'')
                    screen.Bak(0, 0)
                elif tile == 183:  # punct.
                    screen.screen.Col(15, 0)
                    screen.Bak(6, 7)
                    screen.Write(',')
                    screen.Bak(0, 0)
                elif tile == 184:  # punct.
                    screen.screen.Col(15, 0)
                    screen.Bak(6, 7)
                    screen.Write(':')
                    screen.Bak(0, 0)
                elif tile == 195:  # punct.
                    screen.screen.Col(15, 0)
                    screen.Bak(6, 7)
                    screen.Write('!')
                    screen.Bak(0, 0)
                else:  # Letters
                    screen.screen.Col(15, 0)
                    screen.Bak(6, 7)
                    screen.Write(chr(tile).upper())
                    screen.Bak(0, 0)

    FloorPattern = False



def Convert_Format(screen):
    global objectContainer

    # Reset PF array
    for x in range(1, 67):  # 1 to 66 inclusive
        for y in range(1, 26):  # 1 to 25 inclusive
            objectContainer.PF[x][y] = 0

    # Reset monster's X, Y coordinates
    for x in range(1, 1000):  # 1 to 999 inclusive
        objectContainer.SX[x] = 0
        objectContainer.SY[x] = 0
        objectContainer.MX[x] = 0
        objectContainer.MY[x] = 0
        objectContainer.FX[x] = 0
        objectContainer.FY[x] = 0

    # Reset B arrays
    for x in range(1, 1301):  # 1 to 1300 inclusive
        objectContainer.BX[x] = 0
        objectContainer.BY[x] = 0

    New_Gem_Color(screen)

    # Convert format based on FP array
    for YLoop in range(1, objectContainer.YSize + 1):  # 1 to YSize inclusive
        for XLoop in range(1, objectContainer.XSize + 1):  # 1 to XSize inclusive
            tempstr = objectContainer.FP[YLoop][XLoop - 1]  # Adjust for 0-based indexing in Python
            char_temp = tempstr[0]  # Get the first character
            
            # Map characters to PF values
            if char_temp == ' ':
                objectContainer.PF[XLoop][YLoop] = None
            elif char_temp == '1':
                objectContainer.SNum += 1
                objectContainer.SX[objectContainer.SNum] = XLoop
                objectContainer.SY[objectContainer.SNum] = YLoop
                objectContainer.PF[XLoop][YLoop] = 1
            elif char_temp == '2':
                objectContainer.MNum += 1
                objectContainer.MX[objectContainer.MNum] = XLoop
                objectContainer.MY[objectContainer.MNum] = YLoop
                objectContainer.PF[XLoop][YLoop] = 2
            elif char_temp == '3':
                FNum += 1
                FX[FNum] = XLoop
                FY[FNum] = YLoop
                objectContainer.PF[XLoop][YLoop] = 3
            elif char_temp == 'X':
                objectContainer.PF[XLoop][YLoop] = 4
            elif char_temp == 'W':
                objectContainer.PF[XLoop][YLoop] = 5
            elif char_temp == 'L':
                objectContainer.PF[XLoop][YLoop] = 6
            elif char_temp == 'C':
                objectContainer.PF[XLoop][YLoop] = 7
            elif char_temp == 'S':
                objectContainer.PF[XLoop][YLoop] = 8
            elif char_temp == '+':
                objectContainer.PF[XLoop][YLoop] = 9
            elif char_temp == 'I':
                objectContainer.PF[XLoop][YLoop] = 10
            elif char_temp == 'T':
                objectContainer.PF[XLoop][YLoop] = 11
            elif char_temp == 'K':
                objectContainer.PF[XLoop][YLoop] = 12
            elif char_temp == 'D':
                objectContainer.PF[XLoop][YLoop] = 13
            elif char_temp == '#':
                objectContainer.PF[XLoop][YLoop] = 14
            elif char_temp == 'F':
                objectContainer.PF[XLoop][YLoop] = 15
            elif char_temp == '.':
                objectContainer.PF[XLoop][YLoop] = 16
            elif char_temp == 'R':
                objectContainer.PF[XLoop][YLoop] = 17
            elif char_temp == 'Q':
                objectContainer.PF[XLoop][YLoop] = 18
            elif char_temp == '/':
                objectContainer.PF[XLoop][YLoop] = 19
            elif char_temp == '\\':
                objectContainer.PF[XLoop][YLoop] = 20
            elif char_temp == 'B':
                objectContainer.PF[XLoop][YLoop] = 21
            elif char_temp == 'V':
                objectContainer.PF[XLoop][YLoop] = 22
            elif char_temp == '=':
                objectContainer.PF[XLoop][YLoop] = 23
            elif char_temp == 'A':
                objectContainer.PF[XLoop][YLoop] = 24
            elif char_temp == 'U':
                objectContainer.PF[XLoop][YLoop] = 25
            elif char_temp == 'Z':
                objectContainer.PF[XLoop][YLoop] = 26
            elif char_temp == '*':
                objectContainer.PF[XLoop][YLoop] = 27
            elif char_temp == 'E':
                objectContainer.PF[XLoop][YLoop] = 28
            elif char_temp == ';':
                objectContainer.PF[XLoop][YLoop] = 29
            elif char_temp == ':':
                objectContainer.PF[XLoop][YLoop] = 30
            elif char_temp == '`':
                objectContainer.PF[XLoop][YLoop] = 31
            elif char_temp == '-':
                objectContainer.PF[XLoop][YLoop] = 32
            elif char_temp == '@':
                objectContainer.PF[XLoop][YLoop] = 33
            elif char_temp == '%':
                objectContainer.PF[XLoop][YLoop] = 34
            elif char_temp == ']':
                objectContainer.PF[XLoop][YLoop] = 35
            elif char_temp == 'G':
                objectContainer.PF[XLoop][YLoop] = 36
                GenNum += 1
            elif char_temp == '(':
                objectContainer.PF[XLoop][YLoop] = 37
            elif char_temp == 'M':
                BNum += 1
                BX[BNum] = XLoop
                BY[BNum] = YLoop
                objectContainer.PF[XLoop][YLoop] = 38
            elif char_temp == ')':
                objectContainer.PF[XLoop][YLoop] = 39
            elif char_temp == 'P':
                objectContainer.PF[XLoop][YLoop] = 40
                PX = XLoop
                PY = YLoop
            elif char_temp == '&':
                objectContainer.PF[XLoop][YLoop] = 41
            elif char_temp == '!':
                objectContainer.PF[XLoop][YLoop] = 42
            elif char_temp == 'O':
                objectContainer.PF[XLoop][YLoop] = 43
            elif char_temp == 'H':
                objectContainer.PF[XLoop][YLoop] = 44
            elif char_temp == '?':
                objectContainer.PF[XLoop][YLoop] = 45
            elif char_temp == '>':
                objectContainer.PF[XLoop][YLoop] = 46
                T[9] = 32000
            elif char_temp == 'N':
                objectContainer.PF[XLoop][YLoop] = 47
            elif char_temp == '<':
                objectContainer.PF[XLoop][YLoop] = 48
            elif char_temp == '[':
                objectContainer.PF[XLoop][YLoop] = 49
            elif char_temp == '|':
                objectContainer.PF[XLoop][YLoop] = 50
            elif char_temp == '"':
                objectContainer.PF[XLoop][YLoop] = 51
            elif char_temp == '4':
                objectContainer.PF[XLoop][YLoop] = 52
            elif char_temp == '5':
                objectContainer.PF[XLoop][YLoop] = 53
            elif char_temp == '6':
                objectContainer.PF[XLoop][YLoop] = 54
            elif char_temp == '7':
                objectContainer.PF[XLoop][YLoop] = 55
            elif char_temp == '8':
                objectContainer.PF[XLoop][YLoop] = 56
            elif char_temp == '9':
                objectContainer.PF[XLoop][YLoop] = 57
            elif char_temp == 'Ã±':
                objectContainer.PF[XLoop][YLoop] = 58
            elif char_temp == 'Ã²':
                objectContainer.PF[XLoop][YLoop] = 59
            elif char_temp == 'Ã³':
                objectContainer.PF[XLoop][YLoop] = 60
            elif char_temp == 'Ã´':
                objectContainer.PF[XLoop][YLoop] = 61
            elif char_temp == 'Ãµ':
                objectContainer.PF[XLoop][YLoop] = 62
            elif char_temp == 'Ã¶':
                objectContainer.PF[XLoop][YLoop] = 63
            elif char_temp == 'Y':
                objectContainer.PF[XLoop][YLoop] = 64
            elif char_temp == '0':
                objectContainer.PF[XLoop][YLoop] = 65
            elif char_temp == '~':
                objectContainer.PF[XLoop][YLoop] = 66
            elif char_temp == '$':
                objectContainer.PF[XLoop][YLoop] = 67
            elif char_temp == 'Â':
                objectContainer.PF[XLoop][YLoop] = 68
            elif char_temp == 'Â':
                objectContainer.PF[XLoop][YLoop] = 69
            elif char_temp == 'Â':
                objectContainer.PF[XLoop][YLoop] = 70
            elif char_temp == 'Â':
                objectContainer.PF[XLoop][YLoop] = 71
            elif char_temp == 'Â':
                objectContainer.PF[XLoop][YLoop] = 72
            elif char_temp == 'Â':
                objectContainer.PF[XLoop][YLoop] = 73
            elif char_temp == 'Â':
                objectContainer.PF[XLoop][YLoop] = 74
            elif char_temp == 'Â³':
                objectContainer.PF[XLoop][YLoop] = 75
            elif char_temp == 'Â¹':
                objectContainer.PF[XLoop][YLoop] = 76
            elif char_temp == 'Âº':
                objectContainer.PF[XLoop][YLoop] = 77
            elif char_temp == 'Â»':
                objectContainer.PF[XLoop][YLoop] = 78
            elif char_temp == 'Â¼':
                objectContainer.PF[XLoop][YLoop] = 79
            elif char_temp == 'Â½':
                objectContainer.PF[XLoop][YLoop] = 80
            elif char_temp == 'Â':
                objectContainer.PF[XLoop][YLoop] = 81
            elif char_temp == 'Â´':
                objectContainer.PF[XLoop][YLoop] = 180
            elif char_temp == 'Âµ':
                objectContainer.PF[XLoop][YLoop] = 181
            elif char_temp == 'Â¶':
                objectContainer.PF[XLoop][YLoop] = 182
            elif char_temp == 'Â·':
                objectContainer.PF[XLoop][YLoop] = 183
            elif char_temp == 'Â¸':
                objectContainer.PF[XLoop][YLoop] = 184
            elif char_temp == 'Ã ':
                objectContainer.PF[XLoop][YLoop] = 224
            elif char_temp == 'Ã¡':
                objectContainer.PF[XLoop][YLoop] = 225
            elif char_temp == 'Ã¢':
                objectContainer.PF[XLoop][YLoop] = 226
            elif char_temp == 'Ã£':
                objectContainer.PF[XLoop][YLoop] = 227
            elif char_temp == 'Ã¤':
                objectContainer.PF[XLoop][YLoop] = 228
            elif char_temp == 'Ã¥':
                objectContainer.PF[XLoop][YLoop] = 229
            elif char_temp == 'Ã¦':
                objectContainer.PF[XLoop][YLoop] = 230
            elif char_temp == 'Ã§':
                objectContainer.PF[XLoop][YLoop] = 231
            elif char_temp == 'Â¯':
                objectContainer.PF[XLoop][YLoop] = 82
            elif char_temp == 'Â®':
                objectContainer.PF[XLoop][YLoop] = 83
            elif char_temp == 'Ã¼':
                objectContainer.PF[XLoop][YLoop] = 252
            else:
                # If the character is not recognized, use its ASCII value
                objectContainer.PF[XLoop][YLoop] = ord(char_temp)

def New_Gem_Color(screen):
    while True:
        gem_color = random.randint(1, 15)  # Generates a random integer between 1 and 15
        if screen.getMonochrome():
            gem_color = 7
        if gem_color != 8:
            break
    return gem_color

def Init_Screen(screen):
    global Slow, Medium, Fast, Restart, Score, Level, Whips, Teleports, Keys, WhipPower
    global Gems, FloorPattern, Replacement, Bonus, LavaFlow, LavaRate, Evaporate
    global MagicEWalls, GravOn, GravRate, GravCounter, TreeRate, HideRock, HideStairs
    global HideLevel, HideCreate, HideOpenWall, HideTrap, HideGems, HideMBlock
    global FoundSet, GenNum, Sideways, OneMove, GenFactor, PX, PY, BTime, STime
    global MTime, FTime, SkipTime, T, Color

    Slow = chr(142)
    Medium = chr(153)
    Fast = chr(234)
    Restart = False
    Score = 0
    Level = 1
    Whips = 0
    Teleports = 0
    Keys = 0
    WhipPower = 2

    if objectContainer.Difficulty == 9:
        Gems = 250
        Whips = 100
        Teleports = 50
        Keys = 1
        WhipPower = 3
    elif objectContainer.Difficulty == 8:
        Gems = 20
        Whips = 10
    elif objectContainer.Difficulty == 5:
        Gems = 15
    elif objectContainer.Difficulty == 2:
        Gems = 10

    FloorPattern = False
    Replacement = None
    Bonus = 0
    LavaFlow = False
    LavaRate = 0
    Evaporate = 0
    MagicEWalls = False
    GravOn = False
    GravRate = 20
    GravCounter = 0
    TreeRate = -1
    HideRock = False
    HideStairs = False
    HideLevel = False
    HideCreate = False
    HideOpenWall = False
    HideTrap = False
    HideGems = False
    HideMBlock = False
    FoundSet = set()

    if objectContainer.Difficulty in [2, 9]:
        FoundSet = set(range(256))

    GenNum = 0
    Sideways = False
    OneMove = False

    GenFactor = 28 if objectContainer.FastPC else 17

    if objectContainer.MixUp:
        Gems = 60
        Whips = 30
        Teleports = 15
        Keys = 2
        FoundSet = set(range(ToTObjects + 1))

    PX = random.randint(objectContainer.XBot, objectContainer.XBot + objectContainer.XSize - 1)
    PY = random.randint(objectContainer.YBot, objectContainer.YBot + objectContainer.YSize - 1)

    BTime = 9 if objectContainer.FastPC else 2
    STime = 10 if objectContainer.FastPC else 3
    MTime = 8 if objectContainer.FastPC else 2
    FTime = 6 if objectContainer.FastPC else 1
    SkipTime = 0

    for x in range(1, objectContainer.TMax + 1):
        objectContainer.T[x] = -1  # Reset timers

    objectContainer.T[1] = 5
    objectContainer.T[2] = 6
    objectContainer.T[3] = 7
    objectContainer.T[8] = 6

    if not screen.getMonochrome():
        window(67, 1, 80, 25)
        screen.Bak(1, 0)
        screen.ClearScreen()
        window(1, 1, 80, 25)

    screen.Col(14, 7)
    screen.GotoXY(71, 1)
    screen.Write('Score')
    screen.GotoXY(71, 4)
    screen.Write('Level')
    screen.GotoXY(71, 7)
    screen.Write('Gems')
    screen.GotoXY(71, 10)
    screen.Write('Whips')
    screen.GotoXY(69, 13)
    screen.Write('Teleports')
    screen.GotoXY(71, 16)
    screen.Write('Keys')
    screen.Col(11, 7)
    screen.Bak(4, 0)
    screen.GotoXY(70, 19)
    screen.Write('OPTIONS')
    screen.Bak(1, 0)
    screen.GotoXY(70, 20)
    screen.Col(15, 15)
    screen.Write('W')
    screen.Col(7, 7)
    screen.Write('hip')
    screen.GotoXY(70, 21)
    screen.Col(15, 15)
    screen.Write('T')
    screen.Col(7, 7)
    screen.Write('eleport')
    screen.GotoXY(70, 22)
    screen.Col(15, 15)
    screen.Write('P')
    screen.Col(7, 7)
    screen.Write('ause')
    screen.GotoXY(70, 23)
    screen.Col(15, 15)
    screen.Write('Q')
    screen.Col(7, 7)
    screen.Write('uit')
    screen.GotoXY(70, 24)
    screen.Col(15, 15)
    screen.Write('S')
    screen.Col(7, 7)
    screen.Write('ave')
    screen.GotoXY(70, 25)
    screen.Col(15, 15)
    screen.Write('R')
    screen.Col(7, 7)
    screen.Write('estore')

def window(a, b, c, d):
    print("Hi Ho, the boatman row!!!")

