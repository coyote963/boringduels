from session_manager.PlayerQueue import PlayerQueue
import time
from threading import Thread, Event

def start_session(e):
    session_thread = Thread(target=session_process, args= (e))
    session_thread.setDaemon(True)
    session_thread.start()

def session_process(e):
    '''Process to handle passive queue behavior'''
    pq = PlayerQueue()
    while True:
        # keep advancing the queue until there are insufficient players to play
        while len(pq.players) > 1:
            pq.advance_queue()
            # now restricted mode
            pq.togglelock(True)
            # let the match begin for 60 seconds
            time.sleep(60)
        # now free play mode: anyone can join
        pq.togglelock(False)
        e.wait()
        e.clear()