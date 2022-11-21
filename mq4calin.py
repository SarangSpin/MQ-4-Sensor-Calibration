
#connect the analog in put to pin 26 of Pi Pico
ADC_ConvertedValue = machine.ADC(26)
conversion_factor = 3.3 / (65535)

AD_value = ADC_ConvertedValue.read_u16() * conversion_factor
RSL= 33000 / (AD_value)
RS = RSL - 10000
l = log(RS/R0)
v = l - 1.133
p = v / (0.325)
x =  (0.1**p)/1000

#x value is divided by 1000 to get the appropriate ppm, but you should get an idea based on the varying values of x upon different concentration of gas.
