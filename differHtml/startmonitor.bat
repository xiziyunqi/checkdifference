%1  mshta vbscript:createobject("wscript.shell").run("""%~0"" rem",0)(window.close)&&exit
@echo off
REM :start
REM ping /n 2 http://10.104.0.225/plugin.php?id=xj_event:event_list&pc=1|findstr "TTL="&&goto next||goto start
REM :next
:begin
cd D:\differHtml
start pythonw monitorHtml.py
ping -n 200 127.1>nul
goto begin