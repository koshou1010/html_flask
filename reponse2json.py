import datetime
import json

content = "Rsponse: nNO2: -25.390625 nA, -0.013000 V, nSO2: 988.281250 nA, 0.506000 V, nO3: 1.953125 nA, 0.001000 V, nCO: 25.390625 nA, 0.013000 V, nT1: 0.000000, 24.422150 C, nH1: 0.000000, 44.725037 % , nF1: 0.000000 , 0.000000 sml/min,"
keylist = ["name", "meta_index", "l_date", "channel"]
#print(content.split(','))
NO2 = float(content.split(',')[0].split(':')[-1].split(' ')[1])
SO2 = float(content.split(',')[2].split(':')[-1].split(' ')[1])
O3 = float(content.split(',')[4].split(':')[-1].split(' ')[1])
CO = float(content.split(',')[6].split(':')[-1].split(' ')[1])
Temp=float(content.split(',')[9].split(' ')[1])
RH=float(content.split(',')[11].split(' ')[1])
Flow=float(content.split(',')[13].split(' ')[1])
Time = datetime.datetime.now().isoformat() + "+08:00"
channellist = [NO2, SO2, O3, CO, Temp, RH, Flow]
# print(keylist)
# print(Time)
# print(channellist)

dataset = {"name": "data", "meta_index": 0, "l_date": Time,"channel":channellist}
json_dump = json.dumps(dataset)
print(json_dump)
