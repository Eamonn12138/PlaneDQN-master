import os
import matplotlib.pyplot as plt

path='D:\my python code\\train_AI_playgame\PlaneDQN-master-myself\PlaneDQN-master_myself\game\\reward_list_byday.txt'
fileread=open(path,'r')
temp=fileread.readlines()
#print(fileread.readlines())
fileread.close()
length=len(temp)
print('totally play: ',length)
score_everyone=[]
for c in range(length):
    score_everyone.append(float(temp[c].split(' ')[-1][:-2]))


i=0
score=[]
while (i<length):
    count=0
    sum_score_every_100=0
    while count<100 and i<length:
        sum_score_every_100+=float(temp[i].split(' ')[-1][:-2])
        count+=1
        i+=1
    score.append(round(sum_score_every_100/count,2))
now=length//100
for j in range(length//100):
    print('第{}*100---{}*100次平均得分: '.format(j,j+1),score[j])
print('第{}*100---{}次平均得分: '.format(now,length),score[now])

x_axis_data=[i+1 for i in range(length)]
y_axis_data=score_everyone
plt.plot(x_axis_data,y_axis_data,'o',alpha=0.5,linewidth=1,label='score',color='red')
plt.legend()
plt.xlabel('the number of games played')
plt.ylabel('the score each time')
plt.title("Scatter plot of score change as a function of number of games played")
plt.show()

x_axis_data_1=[]
for g in range(len(score)):
    x_axis_data_1.append(100*(g+1))        #'第{}*100---{}*100次'.format(j,j+1)
p1=plt.bar(x_axis_data_1,score,width=40)
plt.bar_label(p1,label_type='edge')
plt.xlabel('the number of games played')
plt.ylabel('the score per hundred')
plt.title("histogram of the average score change over the number of games played")
plt.show()