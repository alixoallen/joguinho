from random import randint
while True:
  a=int(input('digite um valor : '))
  ab=str(input('par ou impar ? : [P/I]')).upper()
  x=randint(0,10)
  ax= a+x
  print('---'*20)
  if ab == 'P':
    if ax%2==0:
      print(f'voce jogou {a} e o computador {x}, e o total deu {ax} é par!')
    else:
      print(f'voce jogou {a} e o  computador {x} o total deu {ax}, computador ganhou!')
      break
  else:
    if ax%2 != 0:
      print(f'voce jogou {a} e o computador {x}, e o total deu {ax} é impar! voce ganhou!!!!!')
    else:
      print(f'voce jogou {a} e o  computador {x} o total deu {ax}, computador ganhou!')
      break