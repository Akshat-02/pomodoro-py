from plyer import notification

def notify_sbreak():

    short_break_title = "Short Break"
    short_break_message = "Time to stretch and relax"

    notification.notify(title= short_break_title, message = short_break_message, app_name= "Pomodoro")

def notify_lbreak():

    long_break_title = "Long Break"
    long_break_message = "You have completed your session, Reset to start again after some time."

    notification.notify(title= long_break_title, message = long_break_message, app_name= "Pomodoro")

def notify_work():

    work_title = "Break Over"
    work_message = "Time to get back to the work!"

    notification.notify(title= work_title, message = work_message, app_name= "Pomodoro")