import speedtest
import time
from datetime import datetime

SLEEP_MINUTES = 15
OVERWRITE = False


def get_averaged_speed(average_runs=3):

    download = 0
    upload = 0
    ping = 0

    for i in range(average_runs):
        speedtest_helper = speedtest.Speedtest()

        speedtest_helper.get_best_server()
        speedtest_helper.download()
        speedtest_helper.upload()
        d = speedtest_helper.results.dict()

        download += d['download'] / 1000000
        upload += d['upload'] / 1000000
        ping += d['ping'] / 1000000

    download /= average_runs
    upload /= average_runs
    ping /= average_runs

    return download, upload, ping


results_path = 'speedtest_results.csv'
if OVERWRITE:
    with open(results_path, 'w') as f:
        f.write('date,download,upload,ping')

while True:

    download, upload, ping = get_averaged_speed()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    row = '{},{},{},{}\n'.format(dt_string, download, upload, ping)
    print(row)

    f = open(results_path, 'a')
    f.write(row)
    f.close()

    time.sleep(SLEEP_MINUTES)
