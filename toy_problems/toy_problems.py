#!/usr/bin/env python
# coding: utf-8

# #### this notebook creates these toy problems:
# 1.  simple two and two\
#     simple two and two ground truth
# 2.  simple four and four\
#     simple four and four ground truth
# 3.  ground truth
# 4.  two horizontal lines at 0 and 1
# 5.  two horizontal lines at 0 and 4
# 6.  two horizontal lines at 0 and 5
# 7.  two interlocking circles
# 8.  two interlocking curves
# 9.  two subset circles
# 10. two lines crossing in an x

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# create simple two and two
def create_simple_two_and_two():
    problem = '01_simple_two_and_two.tp'
    f = open(problem, 'w+')
    count = 1
    for x in range(2):
        f.write('{:0d}'.format(1))
        f.write(' {:0d}\n'.format(count))
        count += 1
    count = 8
    for x in range(2):
        f.write('{:0d}'.format(9))
        f.write(' {:0d}\n'.format(count))
        count += 1
    f.close()
    print('\n', problem + ' created', sep='')
    f = open('01_simple_two_and_two_ground_truth.tp', "w+")
    for x in range(2):
        f.write(' {:0d}\n'.format(0))
    for x in range(2):
        f.write(' {:0d}\n'.format(1))
    f.close()
    print('\n', '01_simple_two_and_two_ground_truth.tp created', '\n', sep='')
#    gt = np.loadtxt('01_simple_two_and_two_ground_truth.tp').astype(np.int32)
#    X = np.loadtxt(problem)
#    plt.scatter(X[:,0], X[:,1], color = [["red", "blue"][i] for i in gt])
#    plt.title(problem)
#    plt.ylabel('y')
#    plt.xlabel('x')
#    plt.show()
# create_simple_two_and_two()


# In[3]:


# create simple four and four
def create_simple_four_and_four():
    problem = '02_simple_four_and_four.tp'
    f = open(problem, 'w+')
    count = 1
    for x in range(2):
        f.write('{:0d}'.format(1))
        f.write(' {:0d}\n'.format(count))
        count += 1
    count = 1
    for x in range(2):
        f.write('{:0d}'.format(2))
        f.write(' {:0d}\n'.format(count))
        count += 1
    count = 8
    for x in range(2):
        f.write('{:0d}'.format(8))
        f.write(' {:0d}\n'.format(count))
        count += 1
    count = 8
    for x in range(2):
        f.write('{:0d}'.format(9))
        f.write(' {:0d}\n'.format(count))
        count += 1
    f.close()
    print('\n', problem + ' created', sep='')
    f = open('02_simple_four_and_four_ground_truth.tp', 'w+')
    for x in range(4):
        f.write(' {:0d}\n'.format(0))
    for x in range(4):
        f.write(' {:0d}\n'.format(1))
    f.close()
    print('\n', '02_simple_four_and_four_ground_truth.tp created\n', sep='')
#    gt = np.loadtxt('02_simple_four_and_four_ground_truth.tp').astype(np.int32)
#    X = np.loadtxt(problem)
#    plt.scatter(X[:,0], X[:,1], color = [["red", "blue"][i] for i in gt])
#    plt.title(problem)
#    plt.ylabel('y')
#    plt.xlabel('x')
#    plt.show()
# create_simple_four_and_four()


# In[4]:


# create ground truth for the "toy problems"
def create_ground_truth():
    problem = '03_ground_truth.tp'
    f = open(problem, 'w+')
    for x in range(100):
        f.write(' {:0d}\n'.format(0))
    for x in range(100):
        f.write(' {:0d}\n'.format(1))
    f.close()
    print('\n', problem + ' created', '\n', sep='')
# create_ground_truth()


# In[5]:


def create_two_horizontal_lines_0_to_1():
    problem = '04_two_horizontal_lines_0_to_1.tp'
    count = 0.1
    f = open(problem, 'w')
    for x in range(100):
        f.write('{:2.2f}'.format(count))
        f.write(' {:0d}\n'.format(0))
        count += 0.1
    count = 0.1
    for x in range(100):
        f.write('{:2.2f}'.format(count))
        f.write(' {:0d}\n'.format(1))
        count += 0.1
    f.close()
    print('\n', problem + ' created', sep='')
    create_ground_truth()
#    ground = np.loadtxt("03_ground_truth.tp").astype(np.int32)
#    lines = np.loadtxt(problem)
#    plt.scatter(lines[:,0], lines[:,1], color = [["red", "blue"][i] for i in ground])
#    plt.title(problem)
#    plt.ylabel('Y')
#    plt.xlabel('X')
#    plt.show()
# create_two_horizontal_lines_0_to_1()


# In[6]:


def create_two_horizontal_lines_0_to_4():
    problem = '05_two_horizontal_lines_0_to_4.tp'
    count = 0.1
    f = open(problem, 'w')
    for x in range(100):
        f.write('{:2.2f}'.format(count))
        f.write(' {:0d}\n'.format(0))
        count += 0.1
    count = 0.1
    for x in range(100):
        f.write('{:2.2f}'.format(count))
        f.write(' {:0d}\n'.format(4))
        count += 0.1
    f.close()
    print('\n', problem + ' created', sep='')
    create_ground_truth()
#    ground = np.loadtxt("03_ground_truth.tp").astype(np.int32)
#    lines = np.loadtxt(problem)
#    plt.scatter(lines[:,0], lines[:,1], color = [["red", "blue"][i] for i in ground])
#    plt.title(problem)
#    plt.ylabel('Y')
#    plt.xlabel('X')
#    plt.show()
# create_two_horizontal_lines_0_to_4()


# In[7]:


def create_two_horizontal_lines_0_to_5():
    problem = '06_two_horizontal_lines_0_to_5.tp'
    count = 0.1
    f = open(problem, 'w')
    for x in range(100):
        f.write('{:2.2f}'.format(count))
        f.write(' {:0d}\n'.format(0))
        count += 0.1
    count = 0.1
    for x in range(100):
        f.write('{:2.2f}'.format(count))
        f.write(' {:0d}\n'.format(5))
        count += 0.1
    f.close()
    print('\n', problem + ' created', sep='')
    create_ground_truth()
#    ground = np.loadtxt("03_ground_truth.tp").astype(np.int32)
#    lines = np.loadtxt(problem)
#    plt.scatter(lines[:,0], lines[:,1], color = [["red", "blue"][i] for i in ground])
#    plt.title(problem)
#    plt.ylabel('Y')
#    plt.xlabel('X')
#    plt.show()
# create_two_horizontal_lines_0_to_5()


# In[8]:


def create_two_interlocking_circles():
    problem = '07_two_interlocking_circles.tp'
    def points_in_circum(r,n):
        return [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r) for x in range(0,n+1)]
    def points_in_circum_shift_right(r,n):
        return [(math.cos(2*math.pi/n*x)*r + 2,math.sin(2*math.pi/n*x)*r) for x in range(0,n+1)]
    circle1 = points_in_circum(2, 100)
    circle2 = points_in_circum_shift_right(2, 100)
    f = open(problem, 'w')
    for x in range(100):
        f.write('{:0f} '.format(circle1[x][0]))
        f.write(' {:0f}\n'.format(circle1[x][1]))
    for x in range(100):
        f.write('{:0f} '.format(circle2[x][0]))
        f.write(' {:0f}\n'.format(circle2[x][1]))
    f.close()
    print('\n', problem + 'created', sep='')
    create_ground_truth()
#    ground = np.loadtxt("03_ground_truth.tp").astype(np.int32)
#    lines = np.loadtxt(problem)
#    plt.scatter(lines[:,0], lines[:,1], color = [["red", "blue"][i] for i in ground])
#    plt.title(problem)
#    plt.ylabel('Y')
#    plt.xlabel('X')
#    plt.show()
# create_two_interlocking_circles()


# In[9]:


def create_two_interlocking_curves():
    problem = '08_two_interlocking_curves.tp'
    def points_in_circum_shift_up(r,n):
        return [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r + 3) for x in range(0,n+1)]
    def points_in_circum(r,n):
            return [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r) for x in range(0,n+1)]
    u1 = points_in_circum_shift_up(2, 200)
    u2 = points_in_circum(2, 200)
    f = open(problem, 'w')
    for x in range(100):
        f.write('{:0f} '.format(u1[x+100][0]))
        f.write(' {:0f}\n'.format(u1[x+100][1]))
    for x in range(100):
        f.write('{:0f} '.format(u2[x][0]))
        f.write(' {:0f}\n'.format(u2[x][1]))
    f.close()
    print('\n', problem + ' created', sep='')
    create_ground_truth()
#    ground = np.loadtxt("03_ground_truth.tp").astype(np.int32)
#    lines = np.loadtxt(problem)
#    plt.scatter(lines[:,0], lines[:,1], color = [["red", "blue"][i] for i in ground])
#    plt.title(problem)
#    plt.ylabel('Y')
#    plt.xlabel('X')
#    plt.show()
# create_interlocking_curves()


# In[10]:


def create_two_subset_circles():
    problem = '09_two_subset_circles.tp'
    def points_in_circum_subset(r,n):
        return [((math.cos(2*math.pi/n*x)*r), math.sin(2*math.pi/n*x)*r) for x in range(0,n+1)]
    circle1 = points_in_circum_subset(2, 100)
    circle2 = points_in_circum_subset(6, 100)
    f = open(problem, 'w')
    for x in range(100):
        f.write('{:0f} '.format(circle1[x][0]))
        f.write(' {:0f}\n'.format(circle1[x][1]))
    for x in range(100):
        f.write('{:0f} '.format(circle2[x][0]))
        f.write(' {:0f}\n'.format(circle2[x][1]))
    f.close()
    print('\n', problem + ' created', sep='')
    create_ground_truth()
#    ground = np.loadtxt("03_ground_truth.tp").astype(np.int32)
#    lines = np.loadtxt(problem)
#    plt.scatter(lines[:,0], lines[:,1], color = [["red", "blue"][i] for i in ground])
#    plt.title(problem)
#    plt.ylabel('Y')
#    plt.xlabel('X')
#    plt.show()
# create_two_subset_circles()


# In[11]:


def create_x():
    problem = '10_x.tp'
    count = -50
    f = open(problem, 'w')
    for x in range(100):
        f.write('{:2.2f}'.format(count))
        f.write(' {:2.2f}\n'.format(count))
        count += 1
    count = -50
    y = 0
    for x in range(100):
        y = (-1)*(count)
        f.write('{:2.2f}'.format(count))
        f.write(' {:2.2f}\n'.format(y))
        count += 1
    f.close()
    print('\n', problem + ' created', sep='')
    create_ground_truth()
#    ground = np.loadtxt("03_ground_truth.tp").astype(np.int32)
#    lines = np.loadtxt(problem)
#    plt.scatter(lines[:,0], lines[:,1], color = [["red", "blue"][i] for i in ground])
#    plt.title(problem)
#    plt.ylabel('Y')
#    plt.xlabel('X')
#    plt.show()
# create_x()


# In[12]:


if __name__ == '__main__':
    # output list of toy problems to create
    print('\nselect a toy problem to create:')
    print('\n 0. check python version')
    print(' 1. tp_01_simple_two_and_two')
    print(' 2. tp_02_simple_four_and_four')
    print(' 3. tp_03_ground_truth')
    print(' 4. tp_04_two_horizontal_lines_0_to_1')
    print(' 5. tp_05_two_horizontal_lines_0_to_4')
    print(' 6. tp_06_two_horizontal_lines_0_to_5')
    print(' 7. tp_07_interlocking_circles')
    print(' 8. tp_08_interlocking_curves')
    print(' 9. tp_09_subset_circles')
    print('10. tp_10_x')
    print('11. create all toy problems\n')

    val = input("Enter number: ")

    if val == str(0):
        import sys
        print('\n', 'Python Version: ', sys.version, '\n', sep='')
    if val == str(1):
        create_simple_two_and_two()
    if val == str(2):
        create_simple_four_and_four()
    if val == str(3):
        create_ground_truth()
    if val == str(4):
        create_two_horizontal_lines_0_to_1()
    if val == str(5):
            create_two_horizontal_lines_0_to_4()
    if val == str(6):
            create_two_horizontal_lines_0_to_5()
    if val == str(7):
            create_two_interlocking_circles()
    if val == str(8):
            create_two_interlocking_curves()
    if val == str(9):
            create_two_subset_circles()
    if val == str(10):
            create_x()
    if val == str(11):
        create_simple_two_and_two()
        create_simple_four_and_four()
        create_ground_truth(),
        create_two_horizontal_lines_0_to_1(),
        create_two_horizontal_lines_0_to_4(),
        create_two_horizontal_lines_0_to_5(),
        create_two_interlocking_circles(),
        create_two_interlocking_curves(),
        create_two_subset_circles(),
        create_x()
    print('enjoy')


# In[ ]:




