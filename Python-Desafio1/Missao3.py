suaNota = float(input('Digite sua nota'))

if suaNota >= 90 and suaNota <=100 :
    print('Parabéns, você tirou A!') 
elif suaNota >=80 and suaNota <=89 :
    print('Muito bem, você tirou B.')
elif suaNota >= 70 and suaNota <= 79:
    print('Bom trabalho, você tirou C.')
elif suaNota >= 60 and suaNota <=69:
    print('Fique atento, você tirou D.')
elif suaNota < 60:
    print('Estude um pouco mais, você tirou F.')
elif suaNota > 100:
    print('DIGITE SUA NOTA CERTA !!!!!!!')