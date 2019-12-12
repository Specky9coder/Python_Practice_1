class Greatest_Of_All_Time:
    def __init__(self, name ,Ballon_Dors, Goals, Int_Gaols, Dom_Goals):
        self.name = name
        self.Ballon_Dors = Ballon_Dors
        self.Goals = Goals
        self.Int_Goals = Int_Gaols
        self. Dom_Goals = Dom_Goals



Cristian_Ronaldo = Greatest_Of_All_Time('Cristiano Ronaldo', int(5), int(708), int(608), int(99))

print(Cristian_Ronaldo.name, Cristian_Ronaldo.Ballon_Dors, Cristian_Ronaldo.Goals, Cristian_Ronaldo.Int_Goals, Cristian_Ronaldo.Dom_Goals)


def __init__(self, name, Ballon_Dors, Goals, Int_Goals, Dom_Goals):
    self.name = name
    self.Ballon_Dors = Ballon_Dors
    self.Goals = Goals
    self.In_Goals = Int_Goals
    self.Dom_Goals = Dom_Goals


Lionel_Messi = Greatest_Of_All_Time('Lionel Messi',int(6), int(688), int(71), int(617))

print(Lionel_Messi.name, Lionel_Messi.Ballon_Dors, Lionel_Messi.Goals, Lionel_Messi.Int_Goals, Lionel_Messi.Dom_Goals )



class Ronaldo_vs__Messi:
    # R_Ballon_Dors = 5
    # R_Goals = 709
    # R_Int_Goals = 99
    # R_Dom_Goals = 608
    #
    # M_Ballon_Dors = 6
    # M_Goals = 688
    # M_Int_Goals = 71
    # M_Dom_Goals = 617
    # for Ronaldo_vs__Messi in Greatest_Of_All_Time:
    #     print(input(''))
    def ronaldo(self, R_Ballon_Dors, R_Goals, R_Int_Goals, R_Dom_Goals ):
        self.R_Bllon_Dors = R_Ballon_Dors
        self.R_Goals = R_Goals
        self.R_Int_Goals = R_Int_Goals
        self.R_Dom_Goals = R_Dom_Goals

    def messi(self,M_Ballon_Dors, M_Goals, M_Int_Goals, M_Dom_Goals):
        self.M_Ballon_Dors = M_Ballon_Dors
        self.M_Goals = M_Goals
        self.M_Int_Goals = M_Int_Goals
        self.M_Dom_Goals = M_Dom_Goals

    def Ronaldo_Messi_Stats(self):
        if self.R_Bllon_Dors >= 5:
            # print(input('Ronaldo Stats:'))
            # print(input('Messi Stats:'))
            if self.R_Goals >= 688:
                print('Cristiano Ronaldo Is The Greatest Player On The Galaxy')
            elif self.R_Int_Goals >= 71:
                print('Cristiano Ronaldo Is Still The Greastest Player On The Entire Galaxy')
            elif self.R_Dom_Goals >= 617:
                print('Cristiano Ronaldo Is One Of a Kind And God Of The Football')
            else:
                print('Messi Is The Best Footballer Ever')
