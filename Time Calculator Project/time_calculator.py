lista_dias = ['monday', 'tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def calcular_dia(day,past):
  if past == '' or day == '':
    return day
  else:
    index_day = (lista_dias.index(day.lower()) + past) % 7
    return lista_dias[index_day]    
    
def calcular_hora(h, m, day):
  if h < 12 :
    return [h,m,day]  
  if h == 12 and m == 'AM':
    return [h,'PM',day] 
  if h == 12 and m == 'PM':
    return [h,'AM',day+1]
  if h > 12 and m == 'AM':
    return calcular_hora(h-12,'PM',day)
  if h > 12 and m == 'PM':
    return calcular_hora(h-12,'AM',day+1)

def add_time(start, duration, day = ''):
  (h_ini, m) = start.split(' ')
  (h,min) = h_ini.split(':')
  (hd,mind) = duration.split(':')

  h = int(h)
  min = int(min)
  hd = int(hd)
  mind = int(mind)
  
  minf = min + mind

  hadd = 0
  if minf >= 60:
    hadd = minf // 60
    minf = minf % 60

  hf = h + hd + hadd
  lst = calcular_hora(hf, m, 0)
  past = ''
  if  lst[2] == 1:
    past = '(next day)'
  elif lst[2] > 1:
    past = '(' + str(lst[2]) + ' days later)'
  day = calcular_dia(day,lst[2])


  ##Indincando la solucion
  if len(str(minf)) == 1:
    minf = '0'+str(minf)
  if day != '' and past != '':
    new_time = str(lst[0]) + ':' + str(minf) + ' '+ str(lst[1]) + ', '+ day.capitalize() + ' '+ past
  elif day != '' and past == '':
    new_time = str(lst[0]) + ':' + str(minf) + ' '+ str(lst[1]) + ', '+ day.capitalize()
  elif past != '':
    new_time = str(lst[0]) + ':' + str(minf) + ' '+ str(lst[1]) + ' '+ past
  else:
    new_time = str(lst[0]) + ':' + str(minf) + ' '+ str(lst[1])

  return new_time