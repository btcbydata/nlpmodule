a2021 = [21582, 49330, 75273, 101009, 82451, 28781, 16463, 32416, 30993, 25150, 31287, 26034]
a2022 = [18708, 12324, 10549, 9734, 16679, 11166, 7302, 6004, 2534]
milesteone=101009

div01=[round(a2021[i]/milesteone,3) for i in range(len(a2021))]
div02=[round(a2022[j]/milesteone,3) for j in range(len(a2022))]

print(div01)
print(div02)