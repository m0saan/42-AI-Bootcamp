# from time import sleep
#
#
# def ft_progress(lst):
#    for element in lst:
#        yield element
#
#
# listy = range(1000)
# ret = 0
# for elem in ft_progress(listy):
#    ret += (elem + 3) % 5
#    sleep(0.01)
# print()
# print(ret)

import time
import sys


toolbar_width = 100

# setup toolbar
start = time.time()
for i in range(toolbar_width+1):
    sys.stdout.write('\r')
    # the exact output you're looking for:
    sys.stdout.write(f"ETA: 8.67s [%d%%] [%-{20}s] %d/%d  |  elapsed time %.2fs" %
                     ((i / toolbar_width * 100), '='*i, i, toolbar_width, (time.time() - start)))
    sys.stdout.flush()
    time.sleep(0.25)

# ETA: 8.67s [ 23%][=====>                  ] 233/1000 | elapsed time 2.33s


# 100 ==>
