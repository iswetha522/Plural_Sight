colors = ' ;'.join(['#45ff23', '#2321fa', '#1298a3', '#a32312'])
print(colors)

print(colors.split(' ;'))
print(''.join(['high', 'way', 'man']))

print("unforgetable".partition('forget'))
departure, separator, survival = "London:Edinburgh".partition(':')
print(departure, separator, survival)
origin, _, destination = "Seattle_Boston".partition('-')
print(origin, _, destination)