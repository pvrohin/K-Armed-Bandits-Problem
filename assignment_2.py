import numpy as np

import matplotlib.pyplot as plt 


mn = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
vr = np.ones(10)

time = 1000
n_runs = 2000
means = np.zeros([n_runs,10])

# for i in range(0,n_runs):
# 	means[i] = np.random.normal(loc = mn, scale = vr)



Q = np.zeros(10)
num_times_action_taken = np.zeros(10)
epsilon_set = [0.0,0.01,0.1]

Rewards = np.zeros([len(epsilon_set),time])
Percentage_correct_choice = np.zeros([len(epsilon_set),time])


for test_num,epsilon in enumerate(epsilon_set):

	for i in range(0,n_runs):
		bandit_means = np.random.normal(loc = mn, scale = vr)

		num_times_action_taken = np.zeros(10)
		Q = np.zeros(10)

		for t in range(0,time):
			Rt = np.random.normal(loc=bandit_means,scale = vr)

			explore_prob = np.random.uniform(low = 0.0, high = 1.0)

			if (explore_prob<= epsilon):
				 action_arm = np.random.choice(10)

			else:
				action_arm = np.argmax(Q)

			action_value = Rt[action_arm]
			num_times_action_taken[action_arm] +=1


			Q[action_arm] = Q[action_arm] + (action_value - Q[action_arm])/(num_times_action_taken[action_arm])

			Rewards[test_num][t] += action_value

			if np.argmax(bandit_means) == action_arm :
				Percentage_correct_choice[test_num][t] +=1


Rewards = Rewards/n_runs

Percentage_correct_choice = 100*Percentage_correct_choice/n_runs

plt.plot(Rewards[0],color ='g',label='epsilon0')
plt.plot(Rewards[1],color='r',label='epsilon0.01')
plt.plot(Rewards[2],color='b',label='epsilon0.1')

plt.title("Average reward over the testbed")
plt.xlabel("Steps")
plt.ylabel("Average reward")
plt.legend()
plt.show()


plt.plot(Percentage_correct_choice[0],color ='g',label='epsilon0')
plt.plot(Percentage_correct_choice[1],color='r',label='epsilon0.01')
plt.plot(Percentage_correct_choice[2],color='b',label='epsilon0.1')

plt.title("Percentage of runs with optimal action taken")
plt.xlabel("Steps")
plt.ylabel("% Optimal action")
plt.ylim(0,100)
plt.legend()
plt.show()