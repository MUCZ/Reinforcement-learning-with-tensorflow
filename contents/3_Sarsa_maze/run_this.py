"""
Sarsa is a online updating method for Reinforcement learning.

Unlike Q learning which is a offline updating method, Sarsa is updating while in the current trajectory.

You will see the sarsa is more coward when punishment is close because it cares about all behaviours,
while q learning is more brave because it only cares about maximum behaviour.
"""

from maze_env_changed import Maze
from RL_brain import SarsaTable
from plot import plot_Q


def update():
    for episode in range(1000):
        # initial observation
        observation = env.reset()

        # RL choose action based on observation
        action = RL.choose_action(str(observation))
        done = False
        while True:

            # fresh env
            env.render()
            
            # break while loop when end of this episode
            if done:
                break

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL choose action based on next observation
            action_ = RL.choose_action(str(observation_))

            # RL learn from this transition (s, a, r, s, a) ==> Sarsa
            RL.learn(str(observation), action, reward, str(observation_), action_)

            # swap observation and action
            observation = observation_
            action = action_

            
            

    # end of game
    print('game over')
    print(RL.q_table)

    plot_Q(RL.q_table)

    env.destroy()


if __name__ == "__main__":
    env = Maze()
    RL = SarsaTable(actions=list(range(env.n_actions)))

    env.after(1, update)
    env.mainloop()