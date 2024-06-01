# Penis Printer
#  This program is used to print penis's
#
# Tyler Parshay
# 6/1/2024

print ( "\t\t\tPenis Printer\n\n " )

wouldYouLikeToPrintDicks = -1
wouldYouLikeToPrintDicks = input ( str ( "Would You like to Print Penis's (y/n): ") ).capitalize()

while (wouldYouLikeToPrintDicks != "N" ) :
    penisCounter = int ( input ( "how many times should I print Penis: " )  )
    for penisCounter in range ( penisCounter )  :  
    #dick statements

        if ( penisCounter > 20 ) :
            print ( "that is a whole lot of dick!" )
        elif ( penisCounter == 10 ) :
            print ( "getting closer...")
        elif ( penisCounter == 5 ) :
            print ( "almost there...")
        elif ( penisCounter == 0 ) :
            print ( "done! Thanks for enjoying" )

    #subtract from penis counter per print
        print ( "penis " )
        penisCounter = penisCounter - 1 
    wouldYouLikeToPrintDicks = input ( str  ( "Would You like to Print Penis's (y/n): ") ).capitalize()

