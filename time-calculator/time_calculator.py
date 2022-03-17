def add_time(start, duration, day=None):
  days_week=['Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
  #for start
  start_split=start.split()
  first_hour=start_split[0].split(':')
    
  #for duration
  second_hour=duration.split(':')

  #minutes
  minutes=int(first_hour[1])+int(second_hour[1])
  hour_sum=minutes//60
  final_minutes_int= minutes%60
  final_minutes=str(final_minutes_int).zfill(2)

  #hours
  if start_split[1]=='PM':
    first_hour_int=int(first_hour[0])+12
    
  else:
    first_hour_int=int(first_hour[0])
    
  hours_calc=first_hour_int+int(second_hour[0])+ hour_sum
  days=hours_calc//24
  hours=hours_calc%24
 
  
  if hours==12:
    final_hours=f"{str(hours)}:{final_minutes} PM"
  elif hours==0:
    final_hours_int=12
    final_hours=f"{str(final_hours_int)}:{final_minutes} AM"
  elif hours>13:
    final_hours_int=hours-12
    final_hours=f"{str(final_hours_int)}:{final_minutes} PM"
  else:
    final_hours_int=hours
    final_hours=f"{str(final_hours_int)}:{final_minutes} AM"
    
  #day calculator
  if day!=None:
    actual_day_week=days_week.index(day.capitalize())
    
    new_day=actual_day_week+days
    if new_day>6:
      position_days_week=new_day%7
      new_day_week=days_week[position_days_week]
    else:
      new_day_week=days_week[new_day]
  else:
      new_day_week=None
    
  if day!=None:
    if days==1:
      new_time=(f"{final_hours}, {new_day_week} (next day)")
    elif days>1:
      new_time=(f"{final_hours}, {new_day_week} ({days} days later)")
    else:
      new_time=(f"{final_hours}, {new_day_week}")
  else:
    if days==1:
      new_time=(f"{final_hours} (next day)")
    elif days>1:
      new_time=(f"{final_hours} ({days} days later)")
    else:
      new_time=(f"{final_hours}")



  return new_time