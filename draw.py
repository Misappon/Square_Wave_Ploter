import matplotlib.pyplot as plt

cp = [0]+[i%2 for i in range(2*26)]+[0]  # 26 pulses
s0 = [0]+[0]*19+[1]*7
s1 = [0]+[1]*19+[0]*7
sa = [0]+[1]*4+[0]*10+[1]+[0]*5+[1]+[0]*5
sb = [0]+[0]*4+[1]*4+[0]*6+[1]+[0]*5+[1]+[0]*5

def widen(lst):
    rlt = [0]*(len(lst)*2)
    for i in range(len(lst)):
        rlt[2*i] = rlt[2*i+1] = lst[i]

    return rlt

figs = [s0,s1,sa,sb]

for i in range(len(figs)):
    figs[i] = widen(figs[i])

figs.append(cp)

for i,fig in enumerate(figs):
    for j in range(len(fig)):
        fig[j] += 1.2*i
    plt.plot(fig, color='black',drawstyle='steps-pre')

# plt.xticks([])
# plt.yticks([])
plt.axis('off')
plt.show()