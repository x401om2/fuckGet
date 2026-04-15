import  RPi.GPIO as GPIO

dac_bits = [2,3,4,5,6,7,8,9]
dynamic_range = 3.3

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    for pin in dac_bits:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    
def voltage_to_number(voltage):
    if not (0.0<=voltage<=dynamic_range):
        print(f"Напряжение выходит за динмический диапазон ЦАП (0.00 - {dynamic_range: .2f}В)")
        print("устанавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range*255)

def number_to_dac(number):
    number = max(0, min(255,number))
    for i, pin in enumerate(dac_bits):
        bit = (number >> (7-i)) & 1
        GPIO.output(pin,bit)


try:
    setup_gpio()
    print("управление цап")
    while True:
        try:
            user_input = input("введите напряжение в вольтах")
            voltage = float(user_input)
            code = voltage_to_number(voltage)
            number_to_dac(code)
            print(f"установлено число  {code} - напряжение - {code /255 *dynamic_range:.2f} В)\n")
        except ValueError:
            print("")
            
finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()
