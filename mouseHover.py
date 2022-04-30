
import webview
import win32gui as wg
import time

def close_window(window,ogx,ogy):
  window.hide()
  while True:
    print("HI")
    cursorStatus = wg.GetCursorInfo()[1]
    x,y = wg.GetCursorInfo()[2]
    print(cursorStatus,x,y)
    if (cursorStatus == 65567):
      window.show()
      window.move(x-400,y-300)
      ogx, ogy = (x-400,y-300)
      print("SHOW ME")
    elif x < ogx or x > ogx + 800 or y < ogy or y > ogy + 600:
      print ("Outside window")
      window.hide()
    else:
      print ("inside window")

x,y = wg.GetCursorInfo()[2]
current_win = webview.create_window('SSVEP Selector', 'http://127.0.0.1:5000',frameless=True,x=x-400,y=y-300)
webview.start(func=close_window,args=(current_win,x-400,y-300),http_server=False)


    