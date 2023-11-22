temperature_input = input("请输入带有符号的温度值：")

if temperature_input.endswith('C') or temperature_input.endswith('c'):
        temp_c = float(temperature_input[:-1])
        temp_f = 1.8 * temp_c + 32

        print("转换后的温度是{:.2f}F".format(temp_f))

elif temperature_input.endswith('F') or temperature_input.endswith('f'):
        temp_f = float(temperature_input[:-1])
        temp_c = (temp_f - 32) / 1.8

        print("转换后的温度是{:.2f}C".format(temp_c))

else:
    print("输入格式错误")
