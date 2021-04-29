import time
from plyer import notification

while True:
    notification.notify(
        title="WAKE UP BUDDY!!",
        message="check what r u dooing now..",
        app_icon="C:\\Users\\HP\\Desktop\\Visual code\\icon.ico",
        timeout=10


    )
    time.sleep(60*60)