import os
os.environ['PYTHON_VLC_MODULE_PATH'] = "E:/Software/vlc-3.0.20"
import time

time.sleep(2)
import vlc

instance = vlc.Instance()

player = instance.media_player_new()
event_manager = player.event_manager()
media = instance.media_new("E:/图片/弈弈/d48115a9bcd746a14760f6442b16c6ff_watermask.mp4")
player.set_media(media)
player.play()

event_manager = player.event_manager()

def on_endreached(event):
    print('Media has ended')
    player.stop()

event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, on_endreached)