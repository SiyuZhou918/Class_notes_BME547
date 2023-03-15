# Here I will write pseudocode for VVI design

## Here is the sample code for AAI

def process_LRL_only_state():
    pace_Off()
    reset_AB_timer(AB_T - PACE_T)
    reset_ARP_timer(ARP_T - PACE_T)

if (atrial_Sense()) is True:
    next_state = "AB"

if (test_LRL_timer()) is True:
    next_state = "PACE"

def atrial_Sense():
    return True

def test_LRL_timer():
    return True

def reset_LRL_time():
    return

def start_LRL_timer():
    return

def stop_LRL_timer():
    pace_on
    pace_Off
    activate_Sensor()
    deactivate_Sensor()

def process_PACE_state():
    deactivate_Sensor()
    pace_on()
    start_PACE_timer()
    reset_LRL_timer(LRL_T - PACE_T)
    reset_AB_timer(AB_T - PACE_T)
    reset_ARP_timer(ARP_T - PACE_T)
    if test_PACE_timer is True:
        next_state = AB

def process_AB_state():
    return

def pace_on():
    return

def pace_Off():
    return

def activate_Sensor():
    return

def deactivate_Sensor():
    return

def reset_AB_timer(AB_T - PACE_T):
    return

def reset_ARP_timer(APP_T - PACE_T):
    return

def test_PACE_timer():
    return True


if __name__ == "main":
    next_state = process_LRL_only_State
    process_LRL_only_State
    while True:
        if next_state == "LRL_only":
            process_LRL_only_state()
            break
        if next_state == "PACE":
            process_PACE_state()
        if next_state == "AB":
            process_AB_state