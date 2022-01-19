#!/usr/bin/env python
# coding: utf-8

# In[16]:


"""
value iteration algorithm for a specific case of Gridworld

By Nasim Faridnia




                   ******************
                   *   2    *    6  *
                   *        *  Win  *
            **********************************
            *   1   * ***** *   5   *   7    *
            *       * ***** *       * Lose   *
            **********************************
                    *    3  *    4  *
                    *       *       *
                    *****************
       
      
      The agent will successfully make a desired move with a chance of 70%
      If the agent fails to make a desired move, it will move diagonally with a change of 30%
      
"""




import operator



def valueIteration():
    
    #initialization

    S = [1,2,3,4,5,6,7]
    gamma = 0.7
    epsilon = float(input('Enter epsilon ='))
    reward = -0.2
    step=1

    #the possible result states for each state considering each action
    #in each dictionary, the first number in the list is \
    #the desired state condidering the action
    sp_one   = {'U' : [1,2],     'D' : [1,3],   'L' : [1],     'R' : [1,2,3]}
    sp_two   = {'U' : [2]  ,     'D' : [2,1,5], 'L' : [2,1],   'R' : [6,5]}
    sp_three = {'U' : [3,1,5]  , 'D' : [3],     'L' : [3,1],   'R' : [4,5]}
    sp_four  = {'U' : [5,4,7]  , 'D' : [4],     'L' : [3,4],   'R' : [4,7]}
    sp_five  = {'U' : [6,2]  ,   'D' : [4,3],   'L' : [5,2,3], 'R' : [7]}


    #keep all dictionaries in a list
    list_Sprimes=[sp_one, sp_two, sp_three, sp_four, sp_five]


    U = [0,0,0,0,0,0,0]
    U_prime = [0,0,0,0,0,0,0]
    directions = [0,0,0,0,0,None,None]







    def Bellman(i, state, gamma, reward, U):
        dict_q_results = {}

        #iterate all the actions(keys) in each state dictionary(sp_one,...)
        for action in list_Sprimes[i]:
            q_result = 0

            #calculate probabilities based on the number of s' values
            if len(list_Sprimes[i][action] ) == 3:
                probs = [0.7, 0.15, 0,15]
            elif len(list_Sprimes[i][action] ) == 2:
                probs = [0.7, 0.3]
            elif len(list_Sprimes[i][action] ) == 1:
                probs=[1]

            #iterate through the s' values
            for sp in list_Sprimes[i][action]:
                #index of sp in the key lists  of s' dictionaries
                #used for finding the right probability
                index_sp = list_Sprimes[i][action].index(sp)
                #calculate the q value for each action
                #index of s' in U is one unit less than sp value
                q_result = q_result + probs[index_sp]*(reward + gamma*U[sp - 1])

            dict_q_results[action] = q_result 

        #action with max q
        key_max, val_max = max(dict_q_results.items(), key = operator.itemgetter(1))


        return [val_max, key_max]







    #main algorithm using do while structure

    while(True):
        U = U_prime.copy()
        delta = 0
        print('\n\n *****************************************')
        print('step :', step)

        for i , state in enumerate(S):
            # the values of states 6 and 7 will not change \
            #because there are no s'(possible moves) for them
            if state == 6 or state == 7:
                continue
            #bellman func returns a list \
            #the first element is the value and the second one is the direction
            U_prime[i], directions[i] = Bellman(i, state, gamma, reward, U)#check???

            #update delta
            if abs(U_prime[i] - U[i]) > delta:
                delta = abs(U_prime[i] - U[i])

            #print
            print('\n\n -------------------------------------------')
            print('V = ',U_prime)
            print('directions are = ', directions)
            print('delta is = ', delta)

        step=step+1


        #termination condition for while
        if delta < (epsilon*(1-gamma)/gamma):
            print('\n\n *****************************************')
            print('step : ',step)
            print('V* =', U_prime)
            print('directions are = ', directions)
            break


        

        
       

if __name__ == "__main__":
    
    valueIteration()


            

