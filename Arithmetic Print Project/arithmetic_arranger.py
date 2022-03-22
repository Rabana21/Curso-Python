#Crea la linea de la resta o de la suma dependiendo del numero con mas tamaño
def crear_linea(num):
  linea = '--'
  for index in range(num):
    linea += '-'
  return linea


def arithmetic_arranger(problems, resolver = False):
  ln_up = ''
  ln_dwn = ''
  ln = ''
  lsol = ''
  
  error = False
  arranged_problems = ''
  if len(problems) > 5:
    arranged_problems = 'Error: Too many problems.'
    error = True
  else: 
    for prblm in problems:
      index = problems.index(prblm)
      suma = prblm.find( '+' )
      resta = prblm.find( '-' )
      if  suma != -1: #Es una suma
        (x,y) = prblm.split('+')
        smb_arit = '+'
      elif resta != -1:
        (x,y) = prblm.split('-')
        smb_arit = '-'
      else:
          arranged_problems ="Error: Operator must be \'+\' or \'-\'."
          error = True
          break
      x = x.strip()
      y = y.strip()
      try:
        x_int = int(x)
        y_int = int(y)
      except:
        arranged_problems ="Error: Numbers must only contain digits."
        error = True
        break
      spc_up = 0
      spc_dwn = 0
      spc_arit = 5
      spc_linea = 4
      if len(x)>4 or len(y)>4:
        arranged_problems ='Error: Numbers cannot be more than four digits.'
        error = True
        break
      if len(x) < len(y):
        spc_up = len( y ) - len( x )
        ln_ln = len( y )
      else:
        spc_dwn = len( x ) - len( y )
        ln_ln = len( x )
      #Añadimos la indentacion
      spc_up += 2
      spc_dwn += 1
      if index == 0:
        spc_up -= 4
        spc_arit = 1
        spc_linea = 0
      ln_up += x.rjust(spc_up + len(x) + 4)
      ln_dwn += smb_arit.rjust(spc_arit) + y.rjust(spc_dwn + len(y) )
      linea = crear_linea(ln_ln)
      ln += linea.rjust(spc_linea + len(linea))
      if smb_arit == '+':
        sol = str(x_int + y_int)
      else:
        sol = str(x_int - y_int)
      lsol += sol.rjust( len(linea) + spc_linea )

  if error == False:
    if resolver:
      arranged_problems = ln_up + '\n' + ln_dwn + '\n' + ln + '\n' + lsol
    else:
      arranged_problems = ln_up + '\n' + ln_dwn + '\n' + ln

  return arranged_problems