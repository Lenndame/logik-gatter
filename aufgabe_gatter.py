A = True
B = True

"""
mittel

Implementiere das XOR-Gatter
# XOR Gatter: XOR ist wahr, wenn exklusiv A oder B wahr ist
#
A   B   A XOR B
0   0   0
0   1   1
1   0   1
1   1   0
"""


"""
Implementiere das NAND-Gatter mit zwei Eingängen
Ein NAND-Gatter ist True, wenn mindestens ein Eingang 0 ist

A   B   A NAND B
0   0   1
0   1   1
1   0   1
1   1   0
"""


"""
Implementiere das NOR-Gatter mit zwei Eingängen
# https://de.wikipedia.org/wiki/NOR-Gatter
Ein NOR-Gatter gibt am Ausgang 1 aus, wenn alle Eingänge 0 sind. 

A   B   A NOR B
0   0   1
0   1   0
1   0   0
1   1   0
"""

"""
Implementiere das XNOR-Gatter (exklusive not or) mit zwei Eingängen
https://de.wikipedia.org/wiki/XNOR-Gatter
A   B   A XNOR B
0   0   1
0   1   0
1   0   0
1   1   1
"""

#-----------------------------------------------------------------
# XOR
#-----------------------------------------------------------------

if A != B:
    print("XOR")
else:
    print("No XOR")

#-----------------------------------------------------------------
# NAND
#-----------------------------------------------------------------

if  not A  or not B:
    print("NAND")
else:
    print("No NAND")

#-----------------------------------------------------------------
# NOR
#-----------------------------------------------------------------

if not A and not B:
    print("NOR")
else:
    print("No NOR")

#-----------------------------------------------------------------
# XNOR
#-----------------------------------------------------------------

if (A and B) or (not A and not B):
    print("XNOR")
else:
    print("No XOR")
