import time
import webbrowser

total_break = 3
break_count = 0

print("this program started on" + time.ctime())
while(break_count<total_break):
    time.sleep(2)
    webbrowser.open("https://www.youtube.com/watch?v=rPnQ61WCamY&t=2s")
    break_count = break_count + 1
    

