import math

BASE = 20.0
MAX_LENGTH = 15.0

def paracordF():
  paracord = float(input("Cable Length (ft): "))

  while (paracord > MAX_LENGTH):
    print("Cable length exceeds maximum length of 15 ft.")
    paracord = float(input("Cable Length (ft): "))

  return float(math.ceil(paracord))

def techflexC():
  check = str(input("Techflex - Yes/No: "))
  check.lower()
  
  if (check == "yes"):
    return True
  else:
    return False

def techflexF(check, paracord):
  if (check):
    return float(paracord)
  else:
    return 0.0

def hostF():
  host = str(input("Host Connector - Silver/Gold: "))
  host.lower()
  
  if (host == "silver"):
    return 0.0
  else:
    return 0.75

def deviceF():
  device = str(input("Device Connector - Silver/Gold/Type C: "))
  device.lower()

  if (device == "silver"):
    return 0.0
  elif (device == "gold"):
    return 0.75
  else:
    return 2.0

def coilF(check, paracord):
  avail_length = MAX_LENGTH - paracord

  if (avail_length < 3):
    return 0
  elif (avail_length < 4):
    coil = int(input("Coil Length (in) - 0, 4: "))
  elif (avail_length < 5):
    coil = int(input("Coil Length (in) - 0, 4, 5: "))
  elif (avail_length < 6):
    coil = int(input("Coil Length (in) - 0, 4, 5, 6: "))
  elif (avail_length < 7):
    coil = int(input("Coil Length (in) - 0, 4, 5, 6, 7: "))
  else:
    coil = int(input("Coil Length (in) - 0, 4, 5, 6, 7, 8: "))

  if (check):
    if (coil == 4):
      return 9.5
    if (coil == 5):
      return 12.0
    if (coil == 6):
      return 14.5
    if (coil == 7):
      return 17.0
    if (coil == 8):
      return 19.5
  elif (not check):
    if (coil == 4):
      return 7.5
    if (coil == 5):
      return 8.0
    if (coil == 6):
      return 9.5
    if (coil == 7):
      return 11.0
    if (coil == 8):
      return 12.5
  else:
    return 0.0

def detachF():
  detach = str(input("Detachable - None/Silver/CE/LE/SE: "))
  detach.lower()
  
  if (detach == "none"):
    return 0.0
  elif (detach == "silver"):
    return 11.0
  else:
    return 20.0

def accentF():
  accent = str(input("Accents - Yes/No: "))
  accent.lower()
  
  if (accent == "yes"):
    return 3.5
  else:
    return 0.0

def extraF():
  ends = str(input("Extra Ends - Yes/No: "))
  ends.lower()
  
  if (ends == "yes"):
    color = str(input("Extra Ends Color - Silver/Colored: "))
    color.lower()
    
    if (color == "silver"):
      return 21.0
    else:
      return 26.0
  else:
    return 0.0

def shipF():
  ship = str(input("Shipping - USA/Can/Int: "))
  ship.lower()
  
  if (ship == "usa"):
    return 3.79
  elif (ship == "can"):
    return 10.0
  else:
    return 14.0

def main():
  print("Summitcables Price Calculator\n-----------------------------\n")

  paracord = paracordF()
  check = techflexC()
  techflex = techflexF(check, paracord)
  host = hostF()
  device = deviceF()
  coil = coilF(check, paracord)
  detach = detachF()
  accent = accentF()
  extra = extraF()
  ship = shipF()

  total = BASE + ((paracord - 1) * 0.5) + techflex + host + device + coil + detach + accent + extra + ship

  print("Total: $",total)

main()