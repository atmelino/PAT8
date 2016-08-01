from jplephem.spk import SPK
kernel = SPK.open('de430.bsp')
print(kernel)
position = kernel[0,4].compute(2457061.5)
print(position)

