
import webview
import win32gui as wg
import time

width = 400
height = 300

def close_window(window,ogx,ogy):
  window.hide()
  while True:
    print("HI")
    cursorStatus = wg.GetCursorInfo()[1]
    x,y = wg.GetCursorInfo()[2]
    print(cursorStatus,x,y)
    if (cursorStatus == 65567):
      window.show()
      window.move(int(x-(width/2)),int(y-(height/2)))
      ogx, ogy = (int(x-(width/2)),int(y-(height/2)))
      print("SHOW ME")
    elif x < ogx or x > ogx + width or y < ogy or y > ogy + height:
      print ("Outside window")
      window.hide()
    else:
      print ("inside window")

x,y = wg.GetCursorInfo()[2]
ogx,ogy = int(x-(width/2)), int(y-(height/2))
current_win = webview.create_window('SSVEP Selector', 'http://127.0.0.1:5000',frameless=True,on_top=True,width=width,height=height,x=int(x-(width/2)),y=int(y-(height/2)))
webview.start(func=close_window,args=(current_win,int(ogx),int(ogy)),http_server=False)


    