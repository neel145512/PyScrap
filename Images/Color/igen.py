from PIL import Image

filename = 'color.png'

col = list()

with open('colors.csv') as f:
    content = f.readlines()

for i in content:
    col.append(i.split(',')[:2])

for i in col:
    i[1] = i[1][1:]

    img = Image.open(filename)
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((int(i[1][0:2],16),int(i[1][2:4],16),int(i[1][4:6],16)))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(i[0] + '.png', "PNG")
    img.close()