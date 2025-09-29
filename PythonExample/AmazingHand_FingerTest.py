import time
import numpy as np

from rustypot import Scs0009PyController


ID_1 = 1 #Change to servo ID you want to calibrate 
ID_2 = 2 #Change to servo ID you want to calibrate 
ID_3 = 3 #Change to servo ID you want to calibrate 
ID_4 = 4 #Change to servo ID you want to calibrate 
ID_5 = 5 #Change to servo ID you want to calibrate 
ID_6 = 6 #Change to servo ID you want to calibrate 
ID_7 = 7 #Change to servo ID you want to calibrate 
ID_8 = 8 #Change to servo ID you want to calibrate 
MiddlePos_1 = 0 #Middle position for servo ID_1 
MiddlePos_2 = 0 #Middle position for servo ID_2

c = Scs0009PyController(
        serial_port="COM6",
        baudrate=1000000,
        timeout=0.5,
    )

def main():
    c.write_torque_enable(ID_1, 1) 
    c.write_torque_enable(ID_2, 1) 
    c.write_torque_enable(ID_3, 1)
    c.write_torque_enable(ID_4, 1)
    c.write_torque_enable(ID_5, 1)
    c.write_torque_enable(ID_6, 1)
    c.write_torque_enable(ID_7, 1)
    c.write_torque_enable(ID_8, 1)
    #1 = On / 2 = Off / 3 = Free
    
    while True:
        

        CloseFinger()
        time.sleep(3)


        OpenFinger()
        time.sleep(1)

        #c.sync_write_raw_goal_position([1,2], [50,50])
        #time.sleep(1)

        #a=c.read_present_position(1)
        #b=c.read_present_position(2)
        #a=np.rad2deg(a)
        #b=np.rad2deg(b)
        #print(f'{a} {b}')
        #time.sleep(0.001)



def CloseFinger ():
    
    c.write_goal_speed(ID_1, 6) # Set speed for ID_1 to 6 => Max Speed
    c.write_goal_speed(ID_2, 6) # Set speed for ID_2 to 6 => Max Speed
    c.write_goal_speed(ID_3, 6) # Set speed for ID_3 to 6 => Max Speed
    c.write_goal_speed(ID_4, 6) # Set speed for ID_4 to 6 => Max Speed
    c.write_goal_speed(ID_5, 6) # Set speed for ID_5 to 6 => Max Speed
    c.write_goal_speed(ID_6, 6) # Set speed for ID_6 to 6 => Max Speed
    c.write_goal_speed(ID_7, 6) # Set speed for ID_7 to 6 => Max Speed
    c.write_goal_speed(ID_8, 6) # Set speed for ID_8 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1+90)
    Pos_2 = np.deg2rad(MiddlePos_2-90)
    c.write_goal_position(ID_1, Pos_1)
    c.write_goal_position(ID_2, Pos_2)
    c.write_goal_position(ID_3, Pos_1)
    c.write_goal_position(ID_4, Pos_2)
    c.write_goal_position(ID_5, Pos_1)
    c.write_goal_position(ID_6, Pos_2)
    c.write_goal_position(ID_7, Pos_1)
    c.write_goal_position(ID_8, Pos_2)
    time.sleep(0.01)


def OpenFinger():
    c.write_goal_speed(ID_1, 6) # Set speed for ID_1 to 6 => Max Speed
    c.write_goal_speed(ID_2, 6) # Set speed for ID_2 to 6 => Max Speed
    c.write_goal_speed(ID_3, 6) # Set speed for ID_3 to 6 => Max Speed
    c.write_goal_speed(ID_4, 6) # Set speed for ID_4 to 6 => Max Speed
    c.write_goal_speed(ID_5, 6) # Set speed for ID_5 to 6 => Max Speed
    c.write_goal_speed(ID_6, 6) # Set speed for ID_6 to 6 => Max Speed
    c.write_goal_speed(ID_7, 6) # Set speed for ID_7 to 6 => Max Speed
    c.write_goal_speed(ID_8, 6) # Set speed for ID_8 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1-30)
    Pos_2 = np.deg2rad(MiddlePos_2+30)
    Pos_3 = np.deg2rad(MiddlePos_1-30)
    Pos_4 = np.deg2rad(MiddlePos_2+30)
    Pos_5 = np.deg2rad(MiddlePos_1-30)
    Pos_6 = np.deg2rad(MiddlePos_2+30)
    Pos_7 = np.deg2rad(MiddlePos_1-30)
    Pos_8 = np.deg2rad(MiddlePos_2+30)
    c.write_goal_position(ID_1, Pos_1)
    c.write_goal_position(ID_2, Pos_2)
    c.write_goal_position(ID_3, Pos_3)
    c.write_goal_position(ID_4, Pos_4)
    c.write_goal_position(ID_5, Pos_5)
    c.write_goal_position(ID_6, Pos_6)
    c.write_goal_position(ID_7, Pos_7)
    c.write_goal_position(ID_8, Pos_8)
    time.sleep(0.01)






if __name__ == '__main__':
    main()


