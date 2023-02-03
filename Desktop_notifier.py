from plyer import notification
from datetime import datetime
now = datetime.now()
current_time = " Time is : "+" "+now.strftime("%H:%M:%S")
notification.notify(title= "Good Evening",
                    message= (current_time),
                    app_icon = "a.ico",
                    timeout= 10,
                    toast=True)
                    