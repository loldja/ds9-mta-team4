import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#top_30_entries = [2524667.0, 2120443.0, 1583597.0, 1540467.0, 1410638.0, 1283079.0, 
#                  1137239.0, 1087336.0, 1035401.0, 1024708.0, 956146.0, 944312.0, 
#                  913029.0, 867367.0, 839989.0, 769928.0, 729477.0, 725828.0, 718493.0, 
#                  715246.0, 700475.0, 695195.0, 597444.0, 593650.0, 589648.0, 579541.0, 
#                  572565.0, 557362.0, 550582.0, 543061.0,456986,432956,340943,290514]
#top_30_stations = ['GRD CNTRL-42 ST4567S', '34 ST-HERALD SQBDFMNQR', 
 #                  '42 ST-PORT AUTHACENQRS1237', 'TIMES SQ-42 ST1237ACENQRS', 
 #                  '34 ST-PENN STAACE', '14 ST-UNION SQLNQR456', 'FLUSHING-MAIN7', 
 #                  '86 ST456', '59 ST COLUMBUSABCD1', 'FULTON ST2345ACJZ', 
  #                 '34 ST-PENN STA123ACE', '47-50 STS ROCKBDFM', 'JKSN HT-ROOSVLTEFMR7',
  #                 'CANAL STJNQRZ6', '59 ST456NQR', 'W 4 ST-WASH SQABCDEFM', 
  #                 'JAY ST-METROTECACF', 'JAMAICA CENTEREJZ', '42 ST-BRYANT PKBDFM7', 
  #                 '96 ST123', '72 ST123', 'LEXINGTON AV/53EM6', '14 ST-UNION SQ456LNQR', 
  #                 'BOROUGH HALL2345R', '68ST-HUNTER CO6', '77 ST6', '34 ST-PENN STA123', 
  #                 'CHAMBERS STACE23', 'BEDFORD AVL', 'BOWLING GREEN45', '23 STNR',
  #                 '96 ST6','8 ST-NYUNR','116 ST-COLUMBIA']

top_30_entries = [2524667.0, 2120443.0, 1583597.0, 1540467.0, 1410638.0, 1283079.0, 
                  1137239.0, 1087336.0, 1035401.0, 1024708.0, 956146.0, 944312.0, 
                  913029.0, 867367.0, 839989.0, 769928.0, 729477.0, 725828.0, 718493.0, 
                  456986,432956,340943,290514]
top_30_stations = ['GRD CNTRL-42 ST4567S', '34 ST-HERALD SQBDFMNQR', 
                   '42 ST-PORT AUTHACENQRS1237', 'TIMES SQ-42 ST1237ACENQRS', 
                   '34 ST-PENN STAACE', '14 ST-UNION SQLNQR456', 'FLUSHING-MAIN7', 
                   '86 ST456', '59 ST COLUMBUSABCD1', 'FULTON ST2345ACJZ', 
                   '34 ST-PENN STA123ACE', '47-50 STS ROCKBDFM', 'JKSN HT-ROOSVLTEFMR7',
                   'CANAL STJNQRZ6', '59 ST456NQR', 'W 4 ST-WASH SQABCDEFM', 
                   'JAY ST-METROTECACF', 'JAMAICA CENTEREJZ', '42 ST-BRYANT PKBDFM7', 
                   '23 STNR',
                   '96 ST6','8 ST-NYUNR','116 ST-COLUMBIA']                   
                   
our_stations = ['23 STNR',
                '96 ST6',
                '8 ST-NYUNR',
                '116 ST-COLUMBIA']
                
entries = [456986,432956,340943,290514]

complete_entries=[top_30_entries[::-1], entries]
complete_stations = [top_30_stations[::-1],our_stations]
xtick=['0','0.5M', '1.0M', '1.5M', '2M','2.5M']

y_pos = np.arange(len(top_30_stations))
#fig = plt.figure()
#ax = fig.add_subplot(111)
plt.rcParams.update({'font.size': 10})
barlist = plt.barh(y_pos, top_30_entries[::-1], align = 'center', height = .4)
#ax.barh(y_pos, top_30_entries[::-1], align = 'center', height = .2)
plt.yticks(y_pos, top_30_stations[::-1])
plt.xlabel("Number of entries")
barlist[0].set_color('r')
barlist[1].set_color('r')
barlist[2].set_color('r')
barlist[3].set_color('r')
barlist[4].set_color('r')
plt.axis_bgcolor('white')
plt.autoscale(enable=True, axis='y', tight=True)
x = [0, 500000, 1000000, 1500000,2000000,2500000]
#plt.xticks(x, labels, rotation='vertical')
plt.xticks(x,['0','0.5M', '1.0M', '1.5M', '2M','2.5M'])
ax = plt.gca()
ax.set_axis_bgcolor('white')

plt.grid(True)
plt.show()