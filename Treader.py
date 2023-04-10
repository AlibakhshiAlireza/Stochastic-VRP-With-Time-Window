ins = ['A1','A2','A3','A4','A5','A6','A7','B1','B2','B3','B4','B5','B6','B7','C1','C2','C3','C4','C5','C6','C7']
for i in ins:
    with open('PSOSOL/'+i+'.txt', 'r') as f:
        a = f.readlines()
        print(a[0])
        print(a[1])