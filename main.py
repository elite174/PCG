from Digger import Digger
import time
from CellularAutomata import CellAutomata
from BSP import BSP

bsp = BSP()
digger = Digger()
cave_gen = CellAutomata(10)

digger_list = []
bsp_list = []
cell_list = []

for i in range(10):
    bsp = BSP()
    digger = Digger()
    cave_gen = CellAutomata(10)
    start = time.time()
    digger.dig(5, 5)
    end = time.time()
    digger_list.append(end - start)
    # print('digger time = ', end-start)

    start = time.time()
    cave_gen.generate_cave()
    end = time.time()
    cell_list.append(end - start)
    # print('cave time = ', end-start)

    start = time.time()
    bsp.generate()
    end = time.time()
    bsp_list.append(end - start)
# print('BSP time = ', end-start)

sum_bsp = 0
sum_cell = 0
sum_digger = 0
for i in range(10):
    sum_bsp += bsp_list[i]
    sum_cell += cell_list[i]
    sum_digger += digger_list[i]

print('bsp avg:', sum_bsp / 10)
print('cell avg', sum_cell / 10)
print('digger avg', sum_digger / 10)
