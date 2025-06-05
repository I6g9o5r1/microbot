#получение данных с телефона (ev-micro:bit приложение)
def on_uart_data_received():
    global data
    data = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
    if data == "f":
        f()
    elif data == "s" or data == "a" or data == "z":
        s()
    elif data == "r":
        r()
    elif data == "l":
        l()
    elif data == "b":
        b()
    elif data == "AC-1":
        sound()
    elif data == "AC1":
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        strip.show()
    elif data == "AU-1":
        strip.clear()
        strip.show()
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)
#функции робота
def f():
    robotbit.motor_run(robotbit.Motors.M1A, 200)
    robotbit.motor_run(robotbit.Motors.M2A, 200)
    robotbit.motor_run(robotbit.Motors.M1B, 200)
    robotbit.motor_run(robotbit.Motors.M2B, 200)
def r():
    robotbit.motor_run(robotbit.Motors.M1A, -200)
    robotbit.motor_run(robotbit.Motors.M2A, 200)
    robotbit.motor_run(robotbit.Motors.M1B, -200)
    robotbit.motor_run(robotbit.Motors.M2B, 200)
def l():
    robotbit.motor_run(robotbit.Motors.M1A, 200)
    robotbit.motor_run(robotbit.Motors.M2A, -200)
    robotbit.motor_run(robotbit.Motors.M1B, 200)
    robotbit.motor_run(robotbit.Motors.M2B, -200)
def s():
    robotbit.motor_run(robotbit.Motors.M1A, 0)
    robotbit.motor_run(robotbit.Motors.M2A, 0)
    robotbit.motor_run(robotbit.Motors.M1B, 0)
    robotbit.motor_run(robotbit.Motors.M2B, 0)
def b():
    robotbit.motor_run(robotbit.Motors.M1A, -200)
    robotbit.motor_run(robotbit.Motors.M2A, -200)
    robotbit.motor_run(robotbit.Motors.M1B, -200)
    robotbit.motor_run(robotbit.Motors.M2B, -200)
def sound():
    music.play(music.create_sound_expression(WaveShape.NOISE,
                    4980,
                    4980,
                    255,
                    0,
                    603,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LINEAR),
                music.PlaybackMode.UNTIL_DONE)
data = ""
bluetooth.start_uart_service()
basic.show_icon(IconNames.HAPPY)
strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
range2 = strip.range(0, 4)
