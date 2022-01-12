"""!@file       main.py
    @brief      Lab 0: LED Control
    @details    This script will control the brightness on an LED.
    @author     Tori Bornino
    @author     Jackson Mclaughlin
    @author     Zachary Stednitz
    @date       January 6, 2022
"""
import pyb
import time

def led_setup(pinID=pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP),
              timerID=2,
              channelID=1 ):
    """!@brief      This will initialize an analog pin and return the channel
        @details    This function will initialize an analog pin when given the pin, timer and channel.
        @param      pinID     An initialized pin the LED is connected to. Defaut value PA0
        @param      timerID   The timer id the pin is connected to. Defaut value timer 2
        @param      channelID The channel id the timer is connected to. Defaut value channel 1
        @return     The initialized channel
    """
    # Initialize PA0 as a digital pin
    led_pin = pinID
    
    # Initialize timer and channel for PA0 analog control
    tim2 = pyb.Timer(timerID, freq=20000)
    ch1 = tim2.channel(channelID, pyb.Timer.PWM_INVERTED, pin=led_pin)
    
    return ch1


def led_brightness(channel, brightness):
    """!@brief      This will set the brightness of an led
        @details    This will take the given channel
                    and desired brightness and set the pin pulse width
        @param      channel     The channel to set the pulse width with
        @param      brightness  The desired brightness as a percent.
                                Valid entries between 0 and 100.
    """
    # Set dimmness of LED
    
    channel.pulse_width_percent(brightness)
    
    
if __name__ == "__main__":
    # Set dimmness of LED
    fadetime = 5
    led = led_setup()
    while True:
        for brightness in range(0, 101):
            led_brightness(led, brightness)
            time.sleep(fadetime/101)