"""
Now that we have created our concrete remote control and two TVs, let's try them, push some
buttons and see if they work!
"""
from remote_control import ConcreteRemote, TclTV, SonyTV

sony_remote = ConcreteRemote(SonyTV)
sony_remote.on()
print('Default channel: {}'.format(sony_remote.current_channel))
sony_remote.set_channel(4)
sony_remote.next_channel()
sony_remote.prev_channel()
sony_remote.off()

print('\n=============\n')

tcl_remote = ConcreteRemote(TclTV)
tcl_remote.on()
print('Default channel: {}'.format(tcl_remote.current_channel))
tcl_remote.set_channel(4)
tcl_remote.next_channel()
tcl_remote.prev_channel()
tcl_remote.off()
