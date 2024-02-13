n: int = 1000000000 # 1_000_000_000 or 1e9
print(f'{n:_}') # >> 1_000_000_000
print(f'{n:,}') # >> 1,000,000,000

var: str = 'var'
print(f'{var:>20}:') # >>                  var:
print(f'{var:<20}:') # >> var                 :
print(f'{var:^20}:') # >>         var         : 
print(f'{var:_>20}:') # >> ________________var:
print(f'{var:#<20}:') # >> var################:
print(f'{var:|^20}:') # >> ||||||||var||||||||:

from datetime import datetime
now: datetime = datetime.now()
print(f'{now:%d.%m.%y (%H:%M:%S)}') # >> 13.02.24 (20:40:12)
print(f'{now:%c}') # >> Tue Feb 13 20:40:12 2024
print(f'{now:%I%p}') # >> 08PM

n: float = 1234.5678
print(f'{n:.2f}') # >> 1234.57
print(f'{n:.0f}') # >> 1234
print(f'{n:,.3f}') # >> 1,234.568
print(f'{n:_.3f}') # >> 1_234.568

a = 5
b = 10
my_var = 'Bob says hi'
print(f'a + b = {a + b}') # >> a + b = 15
print(f'{a + b = }') # >> a + b = 15
print(f'{bool(a) = }') # >> bool(a) = True
print(f'{my_var = }') # >> my_var = 'Bob says hi'
print(f'{my_var = }') # >> my_var = 'Bob says hi'