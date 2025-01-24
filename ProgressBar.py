# https://www.geeksforgeeks.org/progress-bars-in-python/

import sys

def progressBar(count_value, total, suffix=''):
    bar_length = 100
    filled_up_Length = int(round(bar_length* count_value / float(total)))
    percentage = round(100.0 * count_value/float(total),1)
    bar = '=' * filled_up_Length + ">" * (bar_length - filled_up_Length != 0) + '-' * (bar_length - filled_up_Length - 1)
    sys.stdout.write('[%s] %s%s ...%s\r' %(bar, percentage, '%', suffix))
    sys.stdout.flush()