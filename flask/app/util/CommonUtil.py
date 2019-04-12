import os, sys
import math
import datetime

#
# set_timecode
# time : 0 - 24

def get_day(day):
    search_day = day
    if  day == 'Today' :
        search_day = datetime.datetime.today().weekday()        # 오늘 요일 (월-일 : 0-6)
    return search_day


def get_time(time):
    search_time = time
    if  time == 'Now' :
        search_time = datetime.datetime.now().strftime('%H')    # 현재 시간
    return search_time


def get_timecode(time_set):
    search_time = time_set

    wcode = datetime.datetime.now().strftime('%w')
    if int(wcode) == 0 : wcode = '7'

    now_time = datetime.datetime.now().strftime('%H') #현재 시간
    if search_time == 'now' : search_time = now_time

    if len(str(search_time)) == 1 : search_time = '0'+str(search_time)
    else : search_time = str(search_time)

    timecode = wcode+search_time

    return timecode

def check_item(item, name) :
    if ( name in item ) and (item[name] != None) :
        return True
    return False

## Util Function
def get_distance_from_coordinates(x0, y0, x1, y1):
    x_ = float(x0)
    y_ = float(y0)
    _x = float(x1)
    _y = float(y1)

    p = 0.017453292519943295
    a = 0.5 - math.cos((_y - y_) * p)/2 + math.cos(y_ * p) * math.cos(_y * p) * (1 - math.cos((_x - x_) * p)) / 2
    return 12742 * math.asin(math.sqrt(a))


def progress_bar (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):

    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))

    bar = '#' * filledLength + '-' * (barLength - filledLength)

    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),

    if iteration == total:
        sys.stdout.write('\n')

    sys.stdout.flush()


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
