sty1, lut1, mar1, kwi1, maj1, cze1, lip1, sie1, wrz1, paz1, lis1, gru1 = (1.592824484,
 -0.453509101, 2.324671717, 1.261254407, 1.782526286, 2.329384541, 1.502229842,
1.782526286, 2.328848994, 0.616921348, 2.352295886, 0.337779545)
sty2, lut2, mar2, kwi2, maj2, cze2, lip2, sie2, wrz2, paz2, lis2, gru2 = (1.577035247,
-0.292781443, 2.48619659, 0.267110318, 1.417952672, 1.054243267, 1.480520104,
1.577035247,  -0.07742069, 1.165733399, -0.404186718, 1.499708521)
print("Witaj w kalkulatorze kredytowym")
print("Podaj wysokość kredytu")
wysokosc_kredyt = int(input())
print("teraz podaj oprocentowanie kredytu w %")
oprocentowanie = float(input())
print("na koniec podaj kwotę raty")
rata = int(input())
formula =(1+((sty1+oprocentowanie)/1200))*wysokosc_kredyt-200
roznica = wysokosc_kredyt - formula
print("W styczniu twoja pozostała kwota kredytu to {:.5f}zł, to {:.5f}zł mniej niż w poprzednim "
      "miesiącu".format(formula, roznica))
wysokosc_kredyt = formula
formula =(1+((lut1+oprocentowanie)/1200))*wysokosc_kredyt-200
roznica = wysokosc_kredyt - formula
print("W lutym twoja pozostała kwota kredytu to {:.5f}zł, to {:.5f}zł mniej niż w poprzednim "
      "miesiącu".format(formula, roznica))
wysokosc_kredyt = formula
formula =(1+((mar1+oprocentowanie)/1200))*wysokosc_kredyt-200
roznica = wysokosc_kredyt - formula
print("W marcu twoja pozostała kwota kredytu to {:.5f}zł, to {:.5f}zł mniej niż w poprzednim "
      "miesiącu".format(formula, roznica))
wysokosc_kredyt = formula
formula =(1+((kwi1+oprocentowanie)/1200))*wysokosc_kredyt-200
roznica = wysokosc_kredyt - formula
print("W kwietniu twoja pozostała kwota kredytu to {:.5f}zł, to {:.5f}zł mniej niż w poprzednim "
      "miesiącu".format(formula, roznica))
wysokosc_kredyt = formula
formula =(1+((maj1+oprocentowanie)/1200))*wysokosc_kredyt-200
roznica = wysokosc_kredyt - formula
print("W maju twoja pozostała kwota kredytu to {:.5f}zł, to {:.5f}zł mniej niż w poprzednim "
      "miesiącu".format(formula, roznica))
wysokosc_kredyt = formula
formula =(1+((cze1+oprocentowanie)/1200))*wysokosc_kredyt-200
roznica = wysokosc_kredyt - formula
print("W czerwcu twoja pozostała kwota kredytu to {:.5f}zł, to {:.5f}zł mniej niż w poprzednim "
      "miesiącu".format(formula, roznica))
wysokosc_kredyt = formula
formula =(1+((lip1+oprocentowanie)/1200))*wysokosc_kredyt-200
roznica = wysokosc_kredyt - formula
print("W lipcu twoja pozostała kwota kredytu to {:.5f}zł, to {:.5f}zł mniej niż w poprzednim "
      "miesiącu".format(formula, roznica))
wysokosc_kredyt = formula
formula =(1+((sie1+oprocentowanie)/1200))*wysokosc_kredyt-200
roznica = wysokosc_kredyt - formula
print("W sierpniu twoja pozostała kwota kredytu to {:.5f}zł, to {:.5f}zł mniej niż w poprzednim "
      "miesiącu".format(formula, roznica))
wysokosc_kredyt = formula
formula =(1+((wrz1+oprocentowanie)/1200))*wysokosc_kredyt-200
roznica = wysokosc_kredyt - formula
print("We wrześniu twoja pozostała kwota kredytu to {:.5f}zł, to {:.5f}zł mniej niż w poprzednim "
      "miesiącu".format(formula, roznica))
wysokosc_kredyt = formula
formula =(1+((paz1+oprocentowanie)/1200))*wysokosc_kredyt-200
roznica = wysokosc_kredyt - formula
print("W październiku twoja pozostała kwota kredytu to {:.5f}zł, to {:.5f}zł mniej niż w poprzednim "
      "miesiącu".format(formula, roznica))
wysokosc_kredyt = formula
formula =(1+((lis1+oprocentowanie)/1200))*wysokosc_kredyt-200
roznica = wysokosc_kredyt - formula
print("W listopadzie twoja pozostała kwota kredytu to {:.5f}zł, to {:.5f}zł mniej niż w poprzednim "
      "miesiącu".format(formula, roznica))
wysokosc_kredyt = formula
formula =(1+((gru1+oprocentowanie)/1200))*wysokosc_kredyt-200
roznica = wysokosc_kredyt - formula
print("W grudniu twoja pozostała kwota kredytu to {:.5f}zł, to {:.5f}zł mniej niż w poprzednim "
      "miesiącu".format(formula, roznica))