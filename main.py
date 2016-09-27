from Digger import Digger
import time
from CellularAutomata import CellAutomata
from BSP import BSP

bsp = BSP()
digger = Digger()
cave_gen = CellAutomata(10)
start = time.time()
digger.dig(5, 5)
end = time.time()
print('digger time = ', end - start)

start = time.time()
cave_gen.generate_cave()
end = time.time()
print('cave time = ', end - start)

start = time.time()
bsp.generate()
end = time.time()
print('BSP time = ', end - start)
