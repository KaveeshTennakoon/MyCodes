import matplotlib.pyplot as plt
'''
weights1 = [120,90,85,60]
weights2 = [100,120,30,40,100,20]
days1 = [1,2,3,4]


plt.plot(days1,weights1, label="line 1")
plt.plot([i+1 for i in range(len(weights2))],weights2, label="line 2")
plt.plot([0,3,1,2,],[0,39,102,30], label = "line 3")
plt.legend(loc="upper right")
plt.xlabel("Days")
plt.ylabel("Weights")
plt.title("Weight tracker")


plt.show()
'''

data = {'Kaveesh' : [120,110,30], 'Iamli' : [10,30]}

#names = list(data.keys())
#weights = list(data.values())

for name, weights in data.items():
    plt.plot([day + 1 for day in range(len(weights))], weights, label=name)
    
plt.xlabel("Days")
plt.ylabel("Weights")
plt.legend()
plt.title("Weight tracker")
plt.show()