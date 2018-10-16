import Xlib
import Xlib.display
import time
import sys

try:
    display = Xlib.display.Display()
    root = display.screen().root
    windowID = root.get_full_property(display.intern_atom('_NET_ACTIVE_WINDOW'), Xlib.X.AnyPropertyType).value[0]
    window = display.create_resource_object('window', windowID)
    
    print (window.get_wm_class()[1])
except KeyboardInterrupt:
    run = False
