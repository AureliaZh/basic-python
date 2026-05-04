from datetime import datetime

datetime.now().second

datetime.now().second+2

wait_until=(datetime.now().second+2)%60 

while datetime.now().second != wait_until:
    print('still waiting')
print(f'We are at {wait_until} seconds now! ')
  