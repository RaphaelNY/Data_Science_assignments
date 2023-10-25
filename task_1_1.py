temperature_input = input("请输入带有符号的温度值：")

if temperature_input.endswith('C') or temperature_input.endswith('c'):
        temperature_celsius = float(temperature_input[:-1])

        temperature_fahrenheit = 1.8 * temperature_celsius + 32

        print("转换后的温度是{:.2f}F".format(temperature_fahrenheit))

elif temperature_input.endswith('F') or temperature_input.endswith('f'):
        temperature_fahrenheit = float(temperature_input[:-1])

        temperature_celsius = (temperature_fahrenheit - 32) / 1.8

        print("转换后的温度是{:.2f}C".format(temperature_celsius))

else:
    print("输入格式错误")
