"""Now Consume those Right here"""
import time
from playLib.qbird import Qbird

from playLib.log_logger import log_make_logger

global log
log=log_make_logger('Q_BARFER')

def callback(ch, method, properties, body):
    msg = " [x] Received %r" % body
    print(msg)
    log.info(msg)


cnt=100;
while cnt>0:
    try:
        #qr=Qbird('localhost','tonyq')
        qr=Qbird('rabbitmq','tonyq')
    except:
        time.sleep(3)
        log.info('sleeping - waiting ... rabbitmq where are you?')
        continue
    break

qr.q_declare()

qr.q_set_callback(callback)

qr.q_consume()
