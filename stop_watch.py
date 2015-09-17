# "Stopwatch: The Game"

import simplegui

# define global variables
onetenths = 0
stop_count = 0
whole_sec = 0
timer_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format_t(number):
    var_d = number % 10
    var_c = (number / 10) % 10
    var_b = (number / 100) % 6
    var_a = ((number / 10) / 60)
    if (var_a > 9):
        var_a = 0
        var_b = 0
        var_c = 0
        var_d = 0
        
    time = str(var_a) + ":" + str(var_b) + str(var_c) + "." + str(var_d)
                                                                  
    return time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global timer_running
    timer1.start()
    timer_running = True
    
def stop_handler():
    global onetenths, stop_count, whole_sec, timer_running
    
    if (timer_running == False):
        return None
    
    timer1.stop()
    timer_running = False
    stop_count += 1
    if ((onetenths % 10) == 0):
        whole_sec += 1
    
def reset_handler():
    global onetenths, stop_count, whole_sec, timer_running
    onetenths = 0
    stop_count = 0
    whole_sec = 0
    timer1.stop()
    timer_running = False
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global onetenths
    onetenths += 1

# define draw handler
def draw_it(canvas):
    global onetenths, stop_count, whole_sec
    
    score = str(whole_sec) + "/" + str(stop_count)
    
    time = format_t(onetenths)
    canvas.draw_text(time, (10, 200), 150, 'Red')
    canvas.draw_text(score, (280, 40), 50, 'Green')
    
# create frame
frame = simplegui.create_frame("Stopwatch", 400, 300)
frame.set_draw_handler(draw_it)

# register event handlers
timer1 = simplegui.create_timer(100, timer_handler)
start = frame.add_button('Start', start_handler)
stop = frame.add_button('Stop', stop_handler)
reset = frame.add_button('Reset', reset_handler)

# start frame
frame.start()

# Please remember to review the grading rubric