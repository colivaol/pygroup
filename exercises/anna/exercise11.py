# Write a getHoursMinutesSeconds() function that has a totalSeconds parameter. The argument for this parameter will be the number 
# of seconds to be translated into the number of hours, minutes, and seconds. If the amount for the hours, minutes, or seconds
# is zero, don’t show it: the function should return '10m' rather than '0h 10m 0s'. The only exception is that 
# sgetHoursMinutesSeconds(0) should return '0s'.

def getHoursMinutesSeconds(totalSeconds):
  hms = []

  if (totalSeconds == 0):
    return print('0s')

  if (totalSeconds >= 3600):
    hours = int(totalSeconds / 3600)
    totalSeconds = totalSeconds % 3600
    hms.append(str(hours) + 'h')
  if (totalSeconds >= 60):
    minutes = int(totalSeconds / 60)
    totalSeconds = totalSeconds % 60
    hms.append(str(minutes) + 'm')
  if (totalSeconds > 0):
    seconds = totalSeconds
    hms.append(str(seconds) + 's')
  return print(" ".join(hms))


# getHoursMinutesSeconds(30)
# getHoursMinutesSeconds(60)
getHoursMinutesSeconds(90042)