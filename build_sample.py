import random
from pytimeparse import parse
import re

data = open('data.csv', 'r')

print("Occurred,City,State,Shape,Duration,Report")
output = open('sampled_data.csv', 'w')
og = 0 
final = 0
for line in data: 
  og += 1
  if True: 
    line = line.split(',')

    # remove report and posted dates
    line.pop(1)
    line.pop(1)

    # Removed 'entered as' in occurance date
    line[0] = line[0].split('(')[0]
    line[0] = line[0].rstrip()

    # Clean location 
    line[1] = line[1][1:].rstrip()
    line[2] = line[2][:-1].rstrip()

    # Clean shape
    if not line[3].rstrip(): # remove entries with no shape
      continue 

    # Parse time
    line[4] = line[4].lower()

    line[4] = line[4].replace(".", "")
    line[4] = line[4].replace("~", "")
    line[4] = line[4].replace("about", "")
    line[4] = line[4].replace("apx.", "")
    line[4] = line[4].replace("approx", "")
    line[4] = line[4].replace("?", "")
    line[4] = line[4].replace("/", "-")
    line[4] = line[4].replace(" to ", "-")

    line[4] = line[4].replace("a", "1")
    line[4] = line[4].replace("a few", str(random.randint(2, 5)))
    line[4] = line[4].replace("few", str(random.randint(2, 5)))
    line[4] = line[4].replace("seconds", str(random.randint(2, 5)))
    line[4] = line[4].replace("a couple", str(random.randint(4, 6)))
    line[4] = line[4].replace("couple", str(random.randint(4, 6)))
    line[4] = line[4].replace("several", str(random.randint(5, 8)))
    line[4] = line[4].replace("+", "")
    line[4] = line[4].replace("plus", "")
    line[4] = line[4].replace("at least", "")
    line[4] = line[4].replace("less than", "")
    line[4] = line[4].replace("over", "")
    line[4] = line[4].replace(">", "")
    line[4] = line[4].replace("<", "")
    line[4] = line[4].replace("@", "")
    line[4] = line[4].replace("or", "")
    line[4] = line[4].replace("less", "")

    line[4] = line[4].replace("mn", "minutes")
    line[4] = line[4].replace("minutess", "minutes")
    line[4] = line[4].replace("minuites", "minutes")

    line[4] = line[4].replace("half", "0.5")
    line[4] = line[4].replace("one", "1")
    line[4] = line[4].replace("two", "2")
    line[4] = line[4].replace("three", "3")
    line[4] = line[4].replace("four", "4")
    line[4] = line[4].replace("five", "5")T
    line[4] = line[4].replace("six", "6")
    line[4] = line[4].replace("seven", "7")
    line[4] = line[4].replace("eight", "8")
    line[4] = line[4].replace("nine", "9")
    line[4] = line[4].replace("ten", "10")

    line[4] = re.sub(r'(\d)minutes', "\1 minutes", line[4])
    line[4] = re.sub(r'(\d)minutes', "\1 minutes", line[4])
    line[4] = re.sub(r'(\d)sec', "\1 minutes", line[4])
    line[4] = re.sub(r'(\d)seconds', "\1 minutes", line[4])

    if "-" in line[4]: 
      try: 
        lo = int(line[4].split('-')[0])
        hi = int(line[4].split('-')[1].split()[0])
        avg = (lo + hi) / 2.0
        line[4] = str(avg) + line[4].split()[1]
      except: pass

    time_in_sec = parse(line[4])
    # if not time_in_sec: 
    #     continue
    line[4] = str(time_in_sec)

    # Remove NUFORC Notes
    try: 
        line[5] = ",".join(line[5:])
        while "((" in line[5]: 
            line[5] = re.sub(r'\(\(.*(\)\)|$)', "", line[5][:-1]) + '"'
        line = ",".join(line[:6]).rstrip()
        output.write(line + "\n")
        final += 1 
    except: 
        line[4] = ",".join(line[4:])
        while "((" in line[4]: 
            line[4] = re.sub(r'\(\(.*(\)\)|$)', "", line[4][:-1]) + '"'
        line = ",".join(line[:5]).rstrip()
        output.write(line + "\n")
        final += 1 
print(og, final)