def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3 :
        return 'Rp.' + y
    else :
        p = y[-3:]
        q = y[:-3]
        return   formatrupiah(q) + '.' + p
        print ('Rp.'+formatrupiah(q) + '.' + p)
def report(petak_sawah):
    print("===== Report Hasil Panen Per Tahun =====")
    total_gabah = 0;
    total_penjualan =0;
    for i in petak_sawah:
        total_gabah += float(petak_sawah[i][1])
        temp = (int(float(petak_sawah[i][1])*100))*int(petak_sawah[i][2])
        total_penjualan +=temp
    print('Total Gabah =',total_gabah ,'Ton')
    print('Total Penjualan =',formatrupiah(total_penjualan))


def rerata(petak_sawah):
    gabah = {}
    for i in petak_sawah:
        x = i.split('-')
        if x[0] not in gabah:
            gabah[x[0]] = [float(petak_sawah[i][1]),1]
        else:
            gabah[x[0]] = [float(gabah[x[0]][0])+float(petak_sawah[i][1]),int(gabah[x[0]][1])+1]
    print("===== Rata Rata Hasil Panen Per Lokasi =====")
    for i in gabah:
        print(i+" =",gabah[i][0]/gabah[i][1] ,'Ton')


def produktif(petak_sawah):
    lokasi = {}
    for i in petak_sawah:
        x = i.split('-')
        if x[0] not in lokasi:
            lokasi[x[0]] = 1
        else:
            lokasi[x[0]] += 1
    print("===== Lokasi Sawah Yang Produktif =====")
    for i in lokasi:
        if lokasi[i]  > 1:
            print(i)

if __name__ == '__main__':
    #read file
    data = open('panen.txt').read().split('\n')
    #deklarasi dictionary
    petak_sawah = {}
    cc =0
    for i in data:
        x = i.split(' ');
        petak_sawah[x[0]+'-'+str(cc)] = [int(x[1]),float(x[2]),int(x[3])];
        cc+=1
    #report
    report(petak_sawah)
    print()
    # rerata
    rerata(petak_sawah)
    print()
    # produktif
    produktif(petak_sawah)