from Option1 import OptionNumber1

def MenuOptions():
    VALIDATOR = True
    while VALIDATOR:
        print("                   Welcome")
        print("=" * 50)
        print("=" * 50)
        print("1. Add product")
        print("2. Show inventory")
        print("3. Calculates statistics")
        print("4. Exit")
        
        #---------------------------------------------------------
        VALIDATOR_OPTIONS = True
        try:
            while VALIDATOR_OPTIONS:
                Options = float(input("What do you want to do?: "))
                print("      ")
                if (Options < 0) or (Options > 4):
                    int("Force Error") 
                elif Options == 1:
                    OptionNumber1(Options)
                elif Options == 2:
                    print("AQUI VA LA OPCION 2")
                elif Options == 3:
                    print("AQUI VA LA OPCION 3")
                elif Options == 4:
                    print("AQUI VA LA OPCION SALIR")                
         
        #------------------------------------------------------------        
        except ValueError:
            print("---------------------------------------")
            print("Error only shows the displayed options")
            print("---------------------------------------")
            print("     ")

