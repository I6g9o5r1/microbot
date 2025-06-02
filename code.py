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
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)
#функции моторов
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
data = ""
bluetooth.start_uart_service()
