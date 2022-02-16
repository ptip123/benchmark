import simpy
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
def script9_func():
    start = timer()
    print(f'STARTING SIMULATION COMP 3 3 MODEL')
    print(f'CALCULATING')

    # -------------------------------------------------
    # Parameters
    #------------------------------------------------
    #####time######
    #minutes in hour
    minutes = 60
    # working hours
    hours = 8
    # business days
    days = 30000
    # total working time (hours)
    total_time = hours * days * minutes
    #-------------------------------------------------
    #Distribution of cycle timings
    #spread of timings
    sigma = 0.5
    #-------------------------------------------------
    #####containers#####
    store_capacity = 10000
    initial_qty = 10000
    dispatch_capacity =10000
    queue_capacity = 1
    queue_init_qty = 1
    #-------------------------------------------------
    #process times
    # Process 1
    mean_model1_process1_time = 10
    mean_model2_process1_time = 12
    mean_model3_process1_time = 13

    # Process 2
    mean_model1_process2_time = 8
    mean_model2_process2_time = 9
    mean_model3_process2_time = 10

    # Process 3
    mean_model1_process3_time = 6
    mean_model2_process3_time = 6
    mean_model3_process3_time = 6

    # Process 4
    mean_model1_process4_time = 12
    mean_model2_process4_time = 15
    mean_model3_process4_time = 17

    # Process 5
    mean_model1_process5_time = 10
    mean_model2_process5_time = 8
    mean_model3_process5_time = 9

    # Process 6
    mean_model1_process6_time = 15
    mean_model2_process6_time = 12
    mean_model3_process6_time = 13

    # Process 7
    mean_model1_process7_time = 10
    mean_model2_process7_time = 8
    mean_model3_process7_time = 9

    # Process 8
    mean_model1_process8_time = 6
    mean_model2_process8_time = 5
    mean_model3_process8_time = 5

    # Process 9
    mean_model1_process9_time = 8
    mean_model2_process9_time = 10
    mean_model3_process9_time = 11

    # Process 10
    mean_model1_process10_time = 14
    mean_model2_process10_time = 11
    mean_model3_process10_time = 12

    # Process 11
    mean_model1_process11_time = 11
    mean_model2_process11_time = 8
    mean_model3_process11_time = 9

    # Process 12
    mean_model1_process12_time = 13
    mean_model2_process12_time = 12
    mean_model3_process12_time = 13
    # Process 13
    mean_model1_process13_time = 18
    mean_model2_process13_time = 15
    mean_model3_process13_time = 13
    # Process 14
    mean_model1_process14_time = 6
    mean_model2_process14_time = 4
    mean_model3_process14_time = 4
    # Process 15
    mean_model1_process15_time = 15
    mean_model2_process15_time = 12
    mean_model3_process15_time = 13
    # Process 16
    mean_model1_process16_time = 14
    mean_model2_process16_time = 16
    mean_model3_process16_time = 18
    # Process 17
    mean_model1_process17_time = 13
    mean_model2_process17_time = 10
    mean_model3_process17_time = 11
    # Process 18
    mean_model1_process18_time = 9
    mean_model2_process18_time = 7
    mean_model3_process18_time = 8
    # Process 19
    mean_model1_process19_time = 7
    mean_model2_process19_time = 9
    mean_model3_process19_time = 10
    # Process 20
    mean_model1_process20_time = 12
    mean_model2_process20_time = 9
    mean_model3_process20_time = 10
    # Process 21
    mean_model1_process21_time = 8
    mean_model2_process21_time = 6
    mean_model3_process21_time = 6
    # Process 22
    mean_model1_process22_time = 11
    mean_model2_process22_time = 10
    mean_model3_process22_time = 11
    # Process 23
    mean_model1_process23_time = 6
    mean_model2_process23_time = 4
    mean_model3_process23_time = 4
    # Process 24
    mean_model1_process24_time = 16
    mean_model2_process24_time = 12
    mean_model3_process24_time = 13
    # Process 25
    mean_model1_process25_time = 12
    mean_model2_process25_time = 11
    mean_model3_process25_time = 12
    # Process 26
    mean_model1_process26_time = 6
    mean_model2_process26_time = 4
    mean_model3_process26_time = 4
    # Process 27
    mean_model1_process27_time = 8
    mean_model2_process27_time = 6
    mean_model3_process27_time = 6
    # Process 28
    mean_model1_process28_time = 11
    mean_model2_process28_time = 9
    mean_model3_process28_time = 10
    # Process 29
    mean_model1_process29_time = 12
    mean_model2_process29_time = 9
    mean_model3_process29_time = 10
    # Process 30
    mean_model1_process30_time = 7
    mean_model2_process30_time = 5
    mean_model3_process30_time = 5
    # Process 31
    mean_model1_process31_time = 5
    mean_model2_process31_time = 6
    mean_model3_process31_time = 6
    # Process 32
    mean_model1_process32_time = 11
    mean_model2_process32_time = 8
    mean_model3_process32_time = 9
    # Process 33
    mean_model1_process33_time = 13
    mean_model2_process33_time = 10
    mean_model3_process33_time = 11
    # Process 34
    mean_model1_process34_time = 11
    mean_model2_process34_time = 12
    mean_model3_process34_time = 13
    # Process 35
    mean_model1_process35_time = 9
    mean_model2_process35_time = 7
    mean_model3_process35_time = 8
    # Process 36
    mean_model1_process36_time = 6
    mean_model2_process36_time = 9
    mean_model3_process36_time = 10
    # Process 37
    mean_model1_process37_time = 17
    mean_model2_process37_time = 13
    mean_model3_process37_time = 14
    # Process 38
    mean_model1_process38_time = 12
    mean_model2_process38_time = 9
    mean_model3_process38_time = 10
    # Process 39
    mean_model1_process39_time = 14
    mean_model2_process39_time = 14
    mean_model3_process39_time = 16
    # Process 40
    mean_model1_process40_time = 6
    mean_model2_process40_time = 4
    mean_model3_process40_time = 4
    #----------------------------------------------------
    ################## PLOT VARIABLES ################
    # Process 1
    model1_process1_time = np.random.normal(mean_model1_process1_time, sigma, 1)
    model2_process1_time = np.random.normal(mean_model2_process1_time, sigma, 1)
    model3_process1_time = np.random.normal(mean_model3_process1_time, sigma, 1)

    # Process 2
    model1_process2_time = np.random.normal(mean_model1_process2_time, sigma, 1)
    model2_process2_time = np.random.normal(mean_model2_process2_time, sigma, 1)
    model3_process2_time = np.random.normal(mean_model3_process2_time, sigma, 1)

    # Process 3
    model1_process3_time = np.random.normal(mean_model1_process3_time, sigma, 1)
    model2_process3_time = np.random.normal(mean_model2_process3_time, sigma, 1)
    model3_process3_time = np.random.normal(mean_model3_process3_time, sigma, 1)

    # Process 4
    model1_process4_time = np.random.normal(mean_model1_process4_time, sigma, 1)
    model2_process4_time = np.random.normal(mean_model2_process4_time, sigma, 1)
    model3_process4_time = np.random.normal(mean_model3_process4_time, sigma, 1)

    # Process 5
    model1_process5_time = np.random.normal(mean_model1_process5_time, sigma, 1)
    model2_process5_time = np.random.normal(mean_model2_process5_time, sigma, 1)
    model3_process5_time = np.random.normal(mean_model3_process5_time, sigma, 1)

    # Process 6
    model1_process6_time = np.random.normal(mean_model1_process6_time, sigma, 1)
    model2_process6_time = np.random.normal(mean_model2_process6_time, sigma, 1)
    model3_process6_time = np.random.normal(mean_model3_process6_time, sigma, 1)

    # Process 7
    model1_process7_time = np.random.normal(mean_model1_process7_time, sigma, 1)
    model2_process7_time = np.random.normal(mean_model2_process7_time, sigma, 1)
    model3_process7_time = np.random.normal(mean_model3_process7_time, sigma, 1)

    # Process 8
    model1_process8_time = np.random.normal(mean_model1_process8_time, sigma, 1)
    model2_process8_time = np.random.normal(mean_model2_process8_time, sigma, 1)
    model3_process8_time = np.random.normal(mean_model3_process8_time, sigma, 1)

    # Process 9
    model1_process9_time =  np.random.normal(mean_model1_process9_time, sigma, 1)
    model2_process9_time =  np.random.normal(mean_model2_process9_time, sigma, 1)
    model3_process9_time =  np.random.normal(mean_model3_process9_time, sigma, 1)

    # Process 10
    model1_process10_time =  np.random.normal(mean_model1_process10_time, sigma, 1)
    model2_process10_time =  np.random.normal(mean_model2_process10_time, sigma, 1)
    model3_process10_time =  np.random.normal(mean_model3_process10_time, sigma, 1)


    # Process 11
    model1_process11_time =  np.random.normal(mean_model1_process11_time, sigma, 1)
    model2_process11_time =  np.random.normal(mean_model2_process11_time, sigma, 1)
    model3_process11_time =  np.random.normal(mean_model3_process11_time, sigma, 1)
    # Process 12
    model1_process12_time =  np.random.normal(mean_model1_process12_time, sigma, 1)
    model2_process12_time =  np.random.normal(mean_model2_process12_time, sigma, 1)
    model3_process12_time =  np.random.normal(mean_model3_process12_time, sigma, 1)

    # Process 13
    model1_process13_time = np.random.normal(mean_model1_process13_time, sigma, 1)
    model2_process13_time = np.random.normal(mean_model2_process13_time, sigma, 1)
    model3_process13_time = np.random.normal(mean_model3_process13_time, sigma, 1)
    # Process 14
    model1_process14_time = np.random.normal(mean_model1_process14_time, sigma, 1)
    model2_process14_time = np.random.normal(mean_model2_process14_time, sigma, 1)
    model3_process14_time = np.random.normal(mean_model3_process14_time, sigma, 1)
    # Process 15
    model1_process15_time = np.random.normal(mean_model1_process15_time, sigma, 1)
    model2_process15_time = np.random.normal(mean_model2_process15_time, sigma, 1)
    model3_process15_time = np.random.normal(mean_model3_process15_time, sigma, 1)
    # Process 16
    model1_process16_time = np.random.normal(mean_model1_process16_time, sigma, 1)
    model2_process16_time = np.random.normal(mean_model2_process16_time, sigma, 1)
    model3_process16_time = np.random.normal(mean_model3_process16_time, sigma, 1)
    # Process 17
    model1_process17_time = np.random.normal(mean_model1_process17_time, sigma, 1)
    model2_process17_time = np.random.normal(mean_model2_process17_time, sigma, 1)
    model3_process17_time = np.random.normal(mean_model3_process17_time, sigma, 1)

    # Process 18
    model1_process18_time = np.random.normal(mean_model1_process18_time, sigma, 1)
    model2_process18_time = np.random.normal(mean_model2_process18_time, sigma, 1)
    model3_process18_time = np.random.normal(mean_model3_process18_time, sigma, 1)

    # Process 19
    model1_process19_time = np.random.normal(mean_model1_process19_time, sigma, 1)
    model2_process19_time = np.random.normal(mean_model2_process19_time, sigma, 1)
    model3_process19_time = np.random.normal(mean_model3_process19_time, sigma, 1)

    # Process 20
    model1_process20_time = np.random.normal(mean_model1_process20_time, sigma, 1)
    model2_process20_time = np.random.normal(mean_model2_process20_time, sigma, 1)
    model3_process20_time = np.random.normal(mean_model3_process20_time, sigma, 1)

    # Process 21
    model1_process21_time = np.random.normal(mean_model1_process21_time, sigma, 1)
    model2_process21_time = np.random.normal(mean_model2_process21_time, sigma, 1)
    model3_process21_time = np.random.normal(mean_model3_process21_time, sigma, 1)

    # Process 22
    model1_process22_time = np.random.normal(mean_model1_process22_time, sigma, 1)
    model2_process22_time = np.random.normal(mean_model2_process22_time, sigma, 1)
    model3_process22_time = np.random.normal(mean_model3_process22_time, sigma, 1)

    # Process 23
    model1_process23_time = np.random.normal(mean_model1_process23_time, sigma, 1)
    model2_process23_time = np.random.normal(mean_model2_process23_time, sigma, 1)
    model3_process23_time = np.random.normal(mean_model3_process23_time, sigma, 1)

    # Process 24
    model1_process24_time = np.random.normal(mean_model1_process24_time, sigma, 1)
    model2_process24_time = np.random.normal(mean_model2_process24_time, sigma, 1)
    model3_process24_time = np.random.normal(mean_model3_process24_time, sigma, 1)

    # Process 25
    model1_process25_time = np.random.normal(mean_model1_process25_time, sigma, 1)
    model2_process25_time = np.random.normal(mean_model2_process25_time, sigma, 1)
    model3_process25_time = np.random.normal(mean_model3_process25_time, sigma, 1)

    # Process 26
    model1_process26_time = np.random.normal(mean_model1_process26_time, sigma, 1)
    model2_process26_time = np.random.normal(mean_model2_process26_time, sigma, 1)
    model3_process26_time = np.random.normal(mean_model3_process26_time, sigma, 1)

    # Process 27
    model1_process27_time = np.random.normal(mean_model1_process27_time, sigma, 1)
    model2_process27_time = np.random.normal(mean_model2_process27_time, sigma, 1)
    model3_process27_time = np.random.normal(mean_model3_process27_time, sigma, 1)

    # Process 28
    model1_process28_time = np.random.normal(mean_model1_process28_time, sigma, 1)
    model2_process28_time = np.random.normal(mean_model2_process28_time, sigma, 1)
    model3_process28_time = np.random.normal(mean_model3_process28_time, sigma, 1)

    # Process 29
    model1_process29_time = np.random.normal(mean_model1_process29_time, sigma, 1)
    model2_process29_time = np.random.normal(mean_model2_process29_time, sigma, 1)
    model3_process29_time = np.random.normal(mean_model3_process29_time, sigma, 1)

    # Process 30
    model1_process30_time = np.random.normal(mean_model1_process30_time, sigma, 1)
    model2_process30_time = np.random.normal(mean_model2_process30_time, sigma, 1)
    model3_process30_time = np.random.normal(mean_model3_process30_time, sigma, 1)

    # Process 31
    model1_process31_time = np.random.normal(mean_model1_process31_time, sigma, 1)
    model2_process31_time = np.random.normal(mean_model2_process31_time, sigma, 1)
    model3_process31_time = np.random.normal(mean_model3_process31_time, sigma, 1)

    # Process 32
    model1_process32_time = np.random.normal(mean_model1_process32_time, sigma, 1)
    model2_process32_time = np.random.normal(mean_model2_process32_time, sigma, 1)
    model3_process32_time = np.random.normal(mean_model3_process32_time, sigma, 1)

    # Process 33
    model1_process33_time = np.random.normal(mean_model1_process33_time, sigma, 1)
    model2_process33_time = np.random.normal(mean_model2_process33_time, sigma, 1)
    model3_process33_time = np.random.normal(mean_model3_process33_time, sigma, 1)

    # Process 34
    model1_process34_time = np.random.normal(mean_model1_process34_time, sigma, 1)
    model2_process34_time = np.random.normal(mean_model2_process34_time, sigma, 1)
    model3_process34_time = np.random.normal(mean_model3_process34_time, sigma, 1)

    # Process 35
    model1_process35_time = np.random.normal(mean_model1_process35_time, sigma, 1)
    model2_process35_time = np.random.normal(mean_model2_process35_time, sigma, 1)
    model3_process35_time = np.random.normal(mean_model3_process35_time, sigma, 1)

    # Process 36
    model1_process36_time = np.random.normal(mean_model1_process36_time, sigma, 1)
    model2_process36_time = np.random.normal(mean_model2_process36_time, sigma, 1)
    model3_process36_time = np.random.normal(mean_model3_process36_time, sigma, 1)

    # Process 37
    model1_process37_time = np.random.normal(mean_model1_process37_time, sigma, 1)
    model2_process37_time = np.random.normal(mean_model2_process37_time, sigma, 1)
    model3_process37_time = np.random.normal(mean_model3_process37_time, sigma, 1)

    # Process 38
    model1_process38_time = np.random.normal(mean_model1_process38_time, sigma, 1)
    model2_process38_time = np.random.normal(mean_model2_process38_time, sigma, 1)
    model3_process38_time = np.random.normal(mean_model3_process38_time, sigma, 1)

    # Process 39
    model1_process39_time = np.random.normal(mean_model1_process39_time, sigma, 1)
    model2_process39_time = np.random.normal(mean_model2_process39_time, sigma, 1)
    model3_process39_time = np.random.normal(mean_model3_process39_time, sigma, 1)

    # Process 40
    model1_process40_time = np.random.normal(mean_model1_process40_time, sigma, 1)
    model2_process40_time = np.random.normal(mean_model2_process40_time, sigma, 1)
    model3_process40_time = np.random.normal(mean_model3_process40_time, sigma, 1)

    #-----------------------------------------------------
    #Plot variables
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    x7 = []
    x8 = []
    x9 = []
    x10 = []
    x11 = []
    x12 = []
    x13 = []
    x14 = []
    x15 = []
    x16 = []
    x17 = []
    x18 = []
    x19 = []
    x20 = []
    x21 = []
    x22 = []
    x23 = []
    x24 = []
    x25 = []
    x26 = []
    x27 = []
    x28 = []
    x29 = []
    x30 = []
    x31 = []
    x32 = []
    x33 = []
    x34 = []
    x35 = []
    x36 = []
    x37 = []
    x38 = []
    x39 = []
    x40 = []
    x41 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    y7 = []
    y8 = []
    y9 = []
    y10 = []
    y11 = []
    y12 = []
    y13 = []
    y14 = []
    y15 = []
    y16 = []
    y17 = []
    y18 = []
    y19 = []
    y20 = []
    y21 = []
    y22 = []
    y23 = []
    y24 = []
    y25 = []
    y26 = []
    y27 = []
    y28 = []
    y29 = []
    y30 = []
    y31 = []
    y32 = []
    y33 = []
    y34 = []
    y35 = []
    y36 = []
    y37 = []
    y38 = []
    y39 = []
    y40 = []
    y41 = []

    #-------------------------------------------------------------------------------------

    class Factory:
        def __init__(self,env):
            self.material1 = simpy.Container(env, capacity=store_capacity, init=initial_qty)
            self.material2 = simpy.Container(env, capacity=store_capacity, init=initial_qty)
            self.dispatch = simpy.Container(env, capacity=dispatch_capacity, init=0)
            self.queue1 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue2 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue3 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue4 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue5 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue6 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue7 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue8 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue9 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue10 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue11 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue12 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue13 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue14 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue15 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue16 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue17 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue18 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue19 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue20 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue21 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue22 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue23 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue24 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue25 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue26 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue27 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue28 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue29 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue30 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue31 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue32 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue33 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue34 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue35 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue36 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue37 = simpy.Container(env, capacity=queue_capacity, init=0)
            self.queue38 = simpy.Container(env, capacity=queue_capacity, init=queue_init_qty)
            self.queue39 = simpy.Container(env, capacity=queue_capacity, init=0)
            self.queue40 = simpy.Container(env, capacity=queue_capacity, init=0)
            self.count1 = 1
            self.count2 = 1
            self.count3 = 1
            self.count4 = 1
            self.count5 = 1
            self.count6 = 1
            self.count7 = 1
            self.count8 = 1
            self.count9 = 1
            self.count10 = 1
            self.count11 = 1
            self.count12 = 1
            self.count13 = 1
            self.count14 = 1
            self.count15 = 1
            self.count16 = 1
            self.count17 = 1
            self.count18 = 1
            self.count19 = 1
            self.count20 = 1
            self.count21 = 1
            self.count22 = 1
            self.count23 = 1
            self.count24 = 1
            self.count25 = 1
            self.count26 = 1
            self.count27 = 1
            self.count28 = 1
            self.count29 = 1
            self.count30 = 1
            self.count31 = 1
            self.count32 = 1
            self.count33 = 1
            self.count34 = 1
            self.count35 = 1
            self.count36 = 1
            self.count37 = 1
            self.count38 = 1
            self.count39 = 1
            self.count40 = 1
            self.count41 = 1
            self.model1 = 0
            self.model2 = 0
            self.model3 = 0
            self.pc1 = 0
            self.pc2 = 0
            self.pc3 = 0
            self.pc4 = 0
            self.pc5 = 0
            self.pc6 = 0
            self.pc7 = 0
            self.pc8 = 0
            self.pc9 = 0
            self.pc10 = 0
            self.pc11 = 0
            self.pc12 = 0
            self.pc13 = 0
            self.pc14 = 0
            self.pc14 = 0
            self.pc15 = 0
            self.pc16 = 0
            self.pc17 = 0
            self.pc18 = 0
            self.pc19 = 0
            self.pc20 = 0
            self.pc21 = 0
            self.pc22 = 0
            self.pc23 = 0
            self.pc24 = 0
            self.pc25 = 0
            self.pc26 = 0
            self.pc27 = 0
            self.pc28 = 0
            self.pc29 = 0
            self.pc30 = 0
            self.pc31 = 0
            self.pc32 = 0
            self.pc33 = 0
            self.pc34 = 0
            self.pc35 = 0
            self.pc36 = 0
            self.pc37 = 0
            self.pc38 = 0
            self.pc39 = 0
            self.pc40 = 0
            self.pc41 = 0


    env = simpy.Environment()
    factory = Factory(env)

    #------------------------------------------------------------------------------------------
    #Processes
    def process1(env,factory):
        while True:
            yield factory.material1.get(1)
            if factory.count1 == 1:
                yield env.timeout(model1_process1_time)
                factory.count1 += 1
            elif factory.count1 == 2:
                yield env.timeout(model2_process1_time)
                factory.count1 += 1
            elif factory.count1 == 3:
                yield env.timeout(model3_process1_time)
                factory.count1 = 1
            else:
                print("count1 error")
                raise SystemExit(0)
            yield factory.queue1.put(1)
            factory.pc1 += 1
            x1.append(float(env.now))
            y1.append(factory.queue1.level)

    def process2(env,factory):
        while True:
            yield factory.material2.get(1)
            if factory.count2 == 1:
                yield env.timeout(model1_process2_time)
                factory.count2 += 1
            elif factory.count2 == 2:
                yield env.timeout(model2_process2_time)
                factory.count2 += 1
            elif factory.count2 == 3:
                yield env.timeout(model3_process2_time)
                factory.count2 = 1
            else:
                print("count2 error")
                raise SystemExit(0)
            yield factory.queue2.put(1)
            factory.pc2 += 1
            x2.append(float(env.now))
            y2.append(factory.queue2.level)

    def process3(env,factory):
        while True:
            yield factory.queue1.get(1)
            yield factory.queue2.get(1)
            if factory.count3 == 1:
                yield env.timeout(model1_process3_time)
                factory.count3 += 1
            elif factory.count3 == 2:
                yield env.timeout(model2_process3_time)
                factory.count3 += 1
            elif factory.count3 == 3:
                yield env.timeout(model3_process3_time)
                factory.count3 = 1
            else:
                print("count3 error")
                raise SystemExit(0)
            yield factory.queue3.put(1)
            factory.pc3 += 1
            x3.append(float(env.now))
            y3.append(factory.queue3.level)

    def process4(env,factory):
        while True:
            yield factory.queue1.get(1)
            if factory.count4 == 1:
                yield env.timeout(model1_process4_time)
                factory.count4 += 1
            elif factory.count4 == 2:
                yield env.timeout(model2_process4_time)
                factory.count4 += 1
            elif factory.count4 == 3:
                yield env.timeout(model3_process4_time)
                factory.count4 = 1
            else:
                print("count4 error")
                raise SystemExit(0)
            yield factory.queue4.put(1)
            factory.pc4 += 1
            x4.append(float(env.now))
            y4.append(factory.queue4.level)

    def process5(env,factory):
        while True:
            yield factory.queue4.get(1)
            if factory.count5 == 1:
                yield env.timeout(model1_process5_time)
                factory.count5 += 1
            elif factory.count5 == 2:
                yield env.timeout(model2_process5_time)
                factory.count5 += 1
            elif factory.count5 == 3:
                yield env.timeout(model3_process5_time)
                factory.count5 = 1
            else:
                print("count5 error")
                raise SystemExit(0)
            yield factory.queue5.put(1)
            factory.pc5 += 1
            x5.append(float(env.now))
            y5.append(factory.queue5.level)

    def process6(env,factory):
        while True:
            yield factory.queue3.get(1)
            if factory.count6 == 1:
                yield env.timeout(model1_process6_time)
                factory.count6 += 1
            elif factory.count6 == 2:
                yield env.timeout(model2_process6_time)
                factory.count6 += 1
            elif factory.count6 == 3:
                yield env.timeout(model3_process6_time)
                factory.count6 = 1
            else:
                print("count6 error")
                raise SystemExit(0)
            yield factory.queue6.put(1)
            factory.pc6 += 1
            x6.append(float(env.now))
            y6.append(factory.queue6.level)

    def process7(env,factory):
        while True:
            yield factory.queue2.get(1)
            if factory.count7 == 1:
                yield env.timeout(model1_process7_time)
                factory.count7 += 1
            elif factory.count7 == 2:
                yield env.timeout(model2_process7_time)
                factory.count7 += 1
            elif factory.count7 == 3:
                yield env.timeout(model3_process7_time)
                factory.count7 = 1
            else:
                print("count7 error")
                raise SystemExit(0)
            yield factory.queue7.put(1)
            factory.pc7 += 1
            x7.append(float(env.now))
            y7.append(factory.queue7.level)

    def process8(env,factory):
        while True:
            yield factory.queue7.get(1)
            if factory.count8 == 1:
                yield env.timeout(model1_process8_time)
                factory.count8 += 1
            elif factory.count8 == 2:
                yield env.timeout(model2_process8_time)
                factory.count8+= 1
            elif factory.count8 == 3:
                yield env.timeout(model3_process8_time)
                factory.count8 = 1
            else:
                print("count8 error")
                raise SystemExit(0)
            yield factory.queue8.put(1)
            factory.pc8 += 1
            x8.append(float(env.now))
            y8.append(factory.queue8.level)

    def process9(env,factory):
        while True:
            yield factory.queue7.get(1)
            if factory.count9 == 1:
                yield env.timeout(model1_process9_time)
                factory.count9 += 1
            elif factory.count9 == 2:
                yield env.timeout(model2_process9_time)
                factory.count9 += 1
            elif factory.count9 == 3:
                yield env.timeout(model3_process9_time)
                factory.count9 = 1
            else:
                print("count9 error")
                raise SystemExit(0)
            yield factory.queue9.put(1)
            factory.pc9 += 1
            x9.append(float(env.now))
            y9.append(factory.queue9.level)

    def process10(env,factory):
        while True:
            yield factory.queue8.get(1)
            yield factory.queue9.get(1)
            if factory.count10 == 1:
                yield env.timeout(model1_process10_time)
                factory.count10 += 1
            elif factory.count10 == 2:
                yield env.timeout(model2_process10_time)
                factory.count10 += 1
            elif factory.count10 == 3:
                yield env.timeout(model3_process10_time)
                factory.count10 = 1
            else:
                print("count10 error")
                raise SystemExit(0)
            yield factory.queue10.put(1)
            factory.pc10 += 1
            x10.append(float(env.now))
            y10.append(factory.queue10.level)

    def process11(env,factory):
        while True:
            yield factory.queue6.get(1)
            if factory.count11 == 1:
                yield env.timeout(model1_process11_time)
                factory.count11 += 1
            elif factory.count11 == 2:
                yield env.timeout(model2_process11_time)
                factory.count11 += 1
            elif factory.count11 == 3:
                yield env.timeout(model3_process11_time)
                factory.count11 = 1
            else:
                print("count11 error")
                raise SystemExit(0)
            yield factory.queue11.put(1)
            factory.pc11 += 1
            x11.append(float(env.now))
            y11.append(factory.queue11.level)

    def process12(env,factory):
        while True:
            yield factory.queue5.get(1)
            if factory.count12 == 1:
                yield env.timeout(model1_process12_time)
                factory.count12 += 1
            elif factory.count12 == 2:
                yield env.timeout(model2_process12_time)
                factory.count12 += 1
            elif factory.count12 == 3:
                yield env.timeout(model3_process12_time)
                factory.count12 = 1
            else:
                print("count12 error")
                raise SystemExit(0)
            yield factory.queue12.put(1)
            factory.pc12 += 1
            x12.append(float(env.now))
            y12.append(factory.queue12.level)

    def process13(env,factory):
        while True:
            yield factory.queue5.get(1)
            if factory.count13 == 1:
                yield env.timeout(model1_process13_time)
                factory.count13 += 1
            elif factory.count13 == 2:
                yield env.timeout(model2_process13_time)
                factory.count13 += 1
            elif factory.count13 == 3:
                yield env.timeout(model3_process13_time)
                factory.count13 = 1
            else:
                print("count13 error")
                raise SystemExit(0)
            yield factory.queue13.put(1)
            factory.pc13 += 1
            x13.append(float(env.now))
            y13.append(factory.queue13.level)


    def process14(env,factory):
        while True:
            yield factory.queue11.get(1)
            yield factory.queue13.get(1)
            if factory.count14 == 1:
                yield env.timeout(model1_process14_time)
                factory.count14 += 1
            elif factory.count14 == 2:
                yield env.timeout(model2_process14_time)
                factory.count14 += 1
            elif factory.count14 == 3:
                yield env.timeout(model3_process14_time)
                factory.count14 = 1
            else:
                print("count14 error")
                raise SystemExit(0)
            yield factory.queue14.put(1)
            factory.pc14 += 1
            x14.append(float(env.now))
            y14.append(factory.queue14.level)

    def process15(env,factory):
        while True:
            yield factory.queue12.get(1)
            if factory.count15 == 1:
                yield env.timeout(model1_process15_time)
                factory.count15 += 1
            elif factory.count15 == 2:
                yield env.timeout(model2_process15_time)
                factory.count15 += 1
            elif factory.count15 == 3:
                yield env.timeout(model3_process15_time)
                factory.count15 = 1
            else:
                print("count15 error")
                raise SystemExit(0)
            yield factory.queue15.put(1)
            factory.pc15 += 1
            x15.append(float(env.now))
            y15.append(factory.queue15.level)


    def process16(env,factory):
        while True:
            yield factory.queue10.get(1)
            if factory.count16 == 1:
                yield env.timeout(model1_process16_time)
                factory.count16 += 1
            elif factory.count16 == 2:
                yield env.timeout(model2_process16_time)
                factory.count16 += 1
            elif factory.count16 == 3:
                yield env.timeout(model3_process16_time)
                factory.count16 = 1
            else:
                print("count16 error")
                raise SystemExit(0)
            yield factory.queue16.put(1)
            factory.pc16 += 1
            x16.append(float(env.now))
            y16.append(factory.queue16.level)

    def process17(env,factory):
        while True:
            yield factory.queue15.get(1)
            yield factory.queue14.get(1)
            if factory.count17 == 1:
                yield env.timeout(model1_process17_time)
                factory.count17 += 1
            elif factory.count17 == 2:
                yield env.timeout(model2_process17_time)
                factory.count17 += 1
            elif factory.count17 == 3:
                yield env.timeout(model3_process17_time)
                factory.count17 = 1
            else:
                print("count17 error")
                raise SystemExit(0)
            yield factory.queue17.put(1)
            factory.pc17 += 1
            x17.append(float(env.now))
            y17.append(factory.queue17.level)

    def process18(env,factory):
        while True:
            yield factory.queue16.get(1)
            if factory.count18 == 1:
                yield env.timeout(model1_process18_time)
                factory.count18 += 1
            elif factory.count18 == 2:
                yield env.timeout(model2_process18_time)
                factory.count18 += 1
            elif factory.count18 == 3:
                yield env.timeout(model3_process18_time)
                factory.count18 = 1
            else:
                print("count18 error")
                raise SystemExit(0)
            yield factory.queue18.put(1)
            factory.pc18 += 1
            x18.append(float(env.now))
            y18.append(factory.queue18.level)

    def process19(env,factory):
        while True:
            yield factory.queue18.get(1)
            if factory.count19 == 1:
                yield env.timeout(model1_process19_time)
                factory.count19 += 1
            elif factory.count19 == 2:
                yield env.timeout(model2_process19_time)
                factory.count19 += 1
            elif factory.count19 == 3:
                yield env.timeout(model3_process19_time)
                factory.count19 = 1
            else:
                print("count19 error")
                raise SystemExit(0)
            yield factory.queue19.put(1)
            factory.pc19 += 1
            x19.append(float(env.now))
            y19.append(factory.queue19.level)


    def process20(env,factory):
        while True:
            yield factory.queue18.get(1)
            if factory.count20 == 1:
                yield env.timeout(model1_process20_time)
                factory.count20 += 1
            elif factory.count20 == 2:
                yield env.timeout(model2_process20_time)
                factory.count20 += 1
            elif factory.count20 == 3:
                yield env.timeout(model3_process20_time)
                factory.count20 = 1
            else:
                print("count20 error")
                raise SystemExit(0)
            yield factory.queue20.put(1)
            factory.pc20 += 1
            x20.append(float(env.now))
            y20.append(factory.queue20.level)

    def process21(env,factory):
        while True:
            yield factory.queue17.get(1)
            if factory.count21 == 1:
                yield env.timeout(model1_process21_time)
                factory.count21 += 1
            elif factory.count21 == 2:
                yield env.timeout(model2_process21_time)
                factory.count21 += 1
            elif factory.count21 == 3:
                yield env.timeout(model3_process21_time)
                factory.count21 = 1
            else:
                print("count21 error")
                raise SystemExit(0)
            yield factory.queue21.put(1)
            factory.pc21 += 1
            x21.append(float(env.now))
            y21.append(factory.queue21.level)

    def process22(env,factory):
        while True:
            yield factory.queue17.get(1)
            if factory.count22 == 1:
                yield env.timeout(model1_process22_time)
                factory.count22 += 1
            elif factory.count22 == 2:
                yield env.timeout(model2_process22_time)
                factory.count22 += 1
            elif factory.count22 == 3:
                yield env.timeout(model3_process22_time)
                factory.count22 = 1
            else:
                print("count22 error")
                raise SystemExit(0)
            yield factory.queue22.put(1)
            factory.pc22 += 1
            x22.append(float(env.now))
            y22.append(factory.queue22.level)

    def process23(env,factory):
        while True:
            yield factory.queue22.get(1)
            yield factory.queue21.get(1)
            if factory.count23 == 1:
                yield env.timeout(model1_process23_time)
                factory.count23 += 1
            elif factory.count23 == 2:
                yield env.timeout(model2_process23_time)
                factory.count23 += 1
            elif factory.count23 == 3:
                yield env.timeout(model3_process23_time)
                factory.count23 = 1
            else:
                print("count23 error")
                raise SystemExit(0)
            yield factory.queue23.put(1)
            factory.pc23 += 1
            x23.append(float(env.now))
            y23.append(factory.queue23.level)

    def process24(env,factory):
        while True:
            yield factory.queue21.get(1)
            if factory.count24 == 1:
                yield env.timeout(model1_process24_time)
                factory.count24 += 1
            elif factory.count24 == 2:
                yield env.timeout(model2_process24_time)
                factory.count24 += 1
            elif factory.count24 == 3:
                yield env.timeout(model3_process24_time)
                factory.count24 = 1
            else:
                print("count24 error")
                raise SystemExit(0)
            yield factory.queue24.put(1)
            factory.pc24 += 1
            x24.append(float(env.now))
            y24.append(factory.queue24.level)

    def process25(env,factory):
        while True:
            yield factory.queue19.get(1)
            yield factory.queue20.get(1)
            if factory.count25 == 1:
                yield env.timeout(model1_process25_time)
                factory.count25 += 1
            elif factory.count25 == 2:
                yield env.timeout(model2_process25_time)
                factory.count25 += 1
            elif factory.count25 == 3:
                yield env.timeout(model3_process25_time)
                factory.count25 = 1
            else:
                print("count25 error")
                raise SystemExit(0)
            yield factory.queue25.put(1)
            factory.pc25 += 1
            x25.append(float(env.now))
            y25.append(factory.queue25.level)

    def process26(env,factory):
        while True:
            yield factory.queue25.get(1)
            if factory.count26 == 1:
                yield env.timeout(model1_process26_time)
                factory.count26 += 1
            elif factory.count26 == 2:
                yield env.timeout(model2_process26_time)
                factory.count26 += 1
            elif factory.count26 == 3:
                yield env.timeout(model3_process26_time)
                factory.count26 = 1
            else:
                print("count26 error")
                raise SystemExit(0)
            yield factory.queue26.put(1)
            factory.pc26 += 1
            x26.append(float(env.now))
            y26.append(factory.queue26.level)

    def process27(env,factory):
        while True:
            yield factory.queue25.get(1)
            if factory.count27 == 1:
                yield env.timeout(model1_process27_time)
                factory.count27 += 1
            elif factory.count27 == 2:
                yield env.timeout(model2_process27_time)
                factory.count27 += 1
            elif factory.count27 == 3:
                yield env.timeout(model3_process27_time)
                factory.count27 = 1
            else:
                print("count27 error")
                raise SystemExit(0)
            yield factory.queue27.put(1)
            factory.pc27 += 1
            x27.append(float(env.now))
            y27.append(factory.queue27.level)

    def process28(env,factory):
        while True:
            yield factory.queue25.get(1)
            if factory.count28 == 1:
                yield env.timeout(model1_process28_time)
                factory.count28 += 1
            elif factory.count28 == 2:
                yield env.timeout(model2_process28_time)
                factory.count28 += 1
            elif factory.count28 == 3:
                yield env.timeout(model3_process28_time)
                factory.count2 = 1
            else:
                print("count28 error")
                raise SystemExit(0)
            yield factory.queue28.put(1)
            factory.pc28 += 1
            x28.append(float(env.now))
            y28.append(factory.queue28.level)


    def process29(env,factory):
        while True:
            yield factory.queue28.get(1)
            yield factory.queue24.get(1)
            if factory.count29 == 1:
                yield env.timeout(model1_process29_time)
                factory.count29 += 1
            elif factory.count29 == 2:
                yield env.timeout(model2_process29_time)
                factory.count29 += 1
            elif factory.count29 == 3:
                yield env.timeout(model3_process29_time)
                factory.count29 = 1
            else:
                print("count29 error")
                raise SystemExit(0)
            yield factory.queue29.put(1)
            factory.pc29 += 1
            x29.append(float(env.now))
            y29.append(factory.queue29.level)

    def process30(env,factory):
        while True:
            yield factory.queue23.get(1)
            if factory.count30 == 1:
                yield env.timeout(model1_process30_time)
                factory.count30 += 1
            elif factory.count30 == 2:
                yield env.timeout(model2_process30_time)
                factory.count30 += 1
            elif factory.count30 == 3:
                yield env.timeout(model3_process30_time)
                factory.count30 = 1
            else:
                print("count30 error")
                raise SystemExit(0)
            yield factory.queue30.put(1)
            factory.pc30 += 1
            x30.append(float(env.now))
            y30.append(factory.queue30.level)


    def process31(env,factory):
        while True:
            yield factory.queue30.get(1)
            if factory.count31 == 1:
                yield env.timeout(model1_process31_time)
                factory.count31 += 1
            elif factory.count31 == 2:
                yield env.timeout(model2_process31_time)
                factory.count31 += 1
            elif factory.count31 == 3:
                yield env.timeout(model3_process31_time)
                factory.count31 = 1
            else:
                print("count31 error")
                raise SystemExit(0)
            yield factory.queue31.put(1)
            factory.pc31 += 1
            x31.append(float(env.now))
            y31.append(factory.queue31.level)


    def process32(env,factory):
        while True:
            yield factory.queue27.get(1)
            if factory.count32 == 1:
                yield env.timeout(model1_process32_time)
                factory.count32 += 1
            elif factory.count32 == 2:
                yield env.timeout(model2_process32_time)
                factory.count32 += 1
            elif factory.count32 == 3:
                yield env.timeout(model3_process32_time)
                factory.count32 = 1
            else:
                print("count32 error")
                raise SystemExit(0)
            yield factory.queue32.put(1)
            factory.pc32 += 1
            x32.append(float(env.now))
            y32.append(factory.queue32.level)

    def process33(env,factory):
        while True:
            yield factory.queue26.get(1)
            if factory.count33 == 1:
                yield env.timeout(model1_process33_time)
                factory.count33 += 1
            elif factory.count33 == 2:
                yield env.timeout(model2_process33_time)
                factory.count33 += 1
            elif factory.count33 == 3:
                yield env.timeout(model3_process33_time)
                factory.count33 = 1
            else:
                print("count33 error")
                raise SystemExit(0)
            yield factory.queue33.put(1)
            factory.pc33 += 1
            x33.append(float(env.now))
            y33.append(factory.queue33.level)

    def process34(env,factory):
        while True:
            yield factory.queue32.get(1)
            yield factory.queue29.get(1)
            if factory.count34 == 1:
                yield env.timeout(model1_process34_time)
                factory.count34 += 1
            elif factory.count34 == 2:
                yield env.timeout(model2_process34_time)
                factory.count34 += 1
            elif factory.count34 == 3:
                yield env.timeout(model3_process34_time)
                factory.count34 = 1
            else:
                print("count34 error")
                raise SystemExit(0)
            yield factory.queue34.put(1)
            factory.pc34 += 1
            x34.append(float(env.now))
            y34.append(factory.queue34.level)

    def process35(env,factory):
        while True:
            yield factory.queue31.get(1)
            if factory.count35 == 1:
                yield env.timeout(model1_process35_time)
                factory.count35 += 1
            elif factory.count35 == 2:
                yield env.timeout(model2_process35_time)
                factory.count35 += 1
            elif factory.count35 == 3:
                yield env.timeout(model3_process35_time)
                factory.count35 = 1
            else:
                print("count35 error")
                raise SystemExit(0)
            yield factory.queue35.put(1)
            factory.pc35 += 1
            x35.append(float(env.now))
            y35.append(factory.queue35.level)

    def process36(env,factory):
        while True:
            yield factory.queue35.get(1)
            yield factory.queue34.get(1)
            if factory.count36 == 1:
                yield env.timeout(model1_process36_time)
                factory.count36 += 1
            elif factory.count36 == 2:
                yield env.timeout(model2_process36_time)
                factory.count36 += 1
            elif factory.count36 == 3:
                yield env.timeout(model3_process36_time)
                factory.count36 = 1
            else:
                print("count36 error")
                raise SystemExit(0)
            yield factory.queue36.put(1)
            factory.pc36 += 1
            x36.append(float(env.now))
            y36.append(factory.queue36.level)

    def process37(env,factory):
        while True:
            yield factory.queue32.get(1)
            if factory.count37 == 1:
                yield env.timeout(model1_process37_time)
                factory.count37 += 1
            elif factory.count37 == 2:
                yield env.timeout(model2_process37_time)
                factory.count37 += 1
            elif factory.count37 == 3:
                yield env.timeout(model3_process37_time)
                factory.count37 = 1
            else:
                print("count37 error")
                raise SystemExit(0)
            yield factory.queue37.put(1)
            factory.pc37 += 1
            x37.append(float(env.now))
            y37.append(factory.queue37.level)

    def process38(env,factory):
        while True:
            yield factory.queue33.get(1)
            if factory.count38 == 1:
                yield env.timeout(model1_process38_time)
                factory.count38 += 1
            elif factory.count38 == 2:
                yield env.timeout(model2_process38_time)
                factory.count38 += 1
            elif factory.count38 == 3:
                yield env.timeout(model3_process38_time)
                factory.count38 = 1
            else:
                print("count38 error")
                raise SystemExit(0)
            yield factory.queue38.put(1)
            factory.pc38 += 1
            x38.append(float(env.now))
            y38.append(factory.queue38.level)

    def process39(env,factory):
        while True:
            yield factory.queue38.get(1)
            if factory.count39 == 1:
                yield env.timeout(model1_process39_time)
                factory.count39 += 1
            elif factory.count39 == 2:
                yield env.timeout(model2_process39_time)
                factory.count39 += 1
            elif factory.count39 == 3:
                yield env.timeout(model3_process39_time)
                factory.count39 = 1
            else:
                print("count39 error")
                raise SystemExit(0)
            yield factory.queue39.put(1)
            factory.pc39 += 1
            x39.append(float(env.now))
            y39.append(factory.queue39.level)

    def process40(env,factory):
        while True:
            yield factory.queue36.get(1)
            if factory.count40 == 1:
                yield env.timeout(model1_process40_time)
                factory.count40 += 1
            elif factory.count40 == 2:
                yield env.timeout(model2_process40_time)
                factory.count40 += 1
            elif factory.count40 == 3:
                yield env.timeout(model3_process40_time)
                factory.count40 = 1
            else:
                print("count40 error")
                raise SystemExit(0)
            yield factory.queue40.put(1)
            factory.pc40 += 1
            x40.append(float(env.now))
            y40.append(factory.queue40.level)



    def process41(env,factory):
        while True:
            yield factory.queue37.get(1)
            yield factory.queue39.get(1)
            yield factory.queue40.get(1)
            if factory.count41 == 1:
                factory.count41 += 1
                factory.model1 += 1
            elif factory.count41 == 2:
                factory.count41 += 1
                factory.model2 += 1
            elif factory.count41 == 3:
                factory.count41 = 1
                factory.model3 +=1
            else:
                print("count40 error")
                raise SystemExit(0)
            yield factory.dispatch.put(1)
            factory.pc41 += 1
            x41.append(float(env.now))
            y41.append(factory.dispatch.level)

    process1_process = env.process(process1(env, factory))
    process2_process = env.process(process2(env, factory))
    process3_process = env.process(process3(env, factory))
    process4_process = env.process(process4(env, factory))
    process5_process = env.process(process5(env, factory))
    process6_process = env.process(process6(env, factory))
    process7_process = env.process(process7(env, factory))
    process8_process = env.process(process8(env, factory))
    process9_process = env.process(process9(env, factory))
    process10_process = env.process(process10(env, factory))
    process11_process = env.process(process11(env, factory))
    process12_process = env.process(process12(env, factory))
    process13_process = env.process(process13(env, factory))
    process14_process = env.process(process14(env, factory))
    process15_process = env.process(process15(env, factory))
    process16_process = env.process(process16(env, factory))
    process17_process = env.process(process17(env, factory))
    process18_process = env.process(process18(env, factory))
    process19_process = env.process(process19(env, factory))
    process20_process = env.process(process20(env, factory))
    process21_process = env.process(process21(env, factory))
    process22_process = env.process(process22(env, factory))
    process23_process = env.process(process23(env, factory))
    process24_process = env.process(process24(env, factory))
    process25_process = env.process(process25(env, factory))
    process26_process = env.process(process26(env, factory))
    process27_process = env.process(process27(env, factory))
    process28_process = env.process(process28(env, factory))
    process29_process = env.process(process29(env, factory))
    process30_process = env.process(process30(env, factory))
    process31_process = env.process(process31(env, factory))
    process32_process = env.process(process32(env, factory))
    process33_process = env.process(process33(env, factory))
    process34_process = env.process(process34(env, factory))
    process35_process = env.process(process35(env, factory))
    process36_process = env.process(process36(env, factory))
    process37_process = env.process(process37(env, factory))
    process38_process = env.process(process38(env, factory))
    process39_process = env.process(process39(env, factory))
    process40_process = env.process(process40(env, factory))
    process41_process = env.process(process41(env, factory))

    env.run(until=total_time)
    end = timer()
    t = (end - start)

    # print(f'%d parts in queue' % factory.queue1.level)
    # print(f'%d parts in queue' % factory.queue2.level)
    # print(f'%d parts in queue' % factory.queue3.level)
    # print(f'%d parts in queue' % factory.queue4.level)
    # print(f'%d parts in queue' % factory.queue5.level)
    # print(f'%d parts in queue' % factory.queue6.level)
    # print(f'%d parts in queue' % factory.queue7.level)
    # print(f'%d parts in queue' % factory.queue8.level)
    # print(f'%d parts in queue' % factory.queue9.level)
    # print(f'%d parts in queue' % factory.queue10.level)
    # print(f'%d parts in queue' % factory.queue11.level)
    # print(f'%d parts in queue' % factory.queue12.level)
    # print(f'%d parts in queue' % factory.queue13.level)
    # print(f'%d parts in queue' % factory.queue14.level)
    # print(f'%d parts in queue' % factory.queue15.level)
    # print(f'%d parts in queue' % factory.queue16.level)
    # print(f'%d parts in queue' % factory.queue17.level)
    # print(f'%d parts in queue' % factory.queue18.level)
    # print(f'%d parts in queue' % factory.queue19.level)
    # print(f'%d parts in queue' % factory.queue20.level)
    # print(f'%d parts in queue' % factory.queue21.level)
    # print(f'%d parts in queue' % factory.queue22.level)
    # print(f'%d parts in queue' % factory.queue23.level)
    # print(f'%d parts in queue' % factory.queue24.level)
    # print(f'%d parts in queue' % factory.queue25.level)
    # print(f'%d parts in queue' % factory.queue26.level)
    # print(f'%d parts in queue' % factory.queue27.level)
    # print(f'%d parts in queue' % factory.queue28.level)
    # print(f'%d parts in queue' % factory.queue29.level)
    # print(f'%d parts in queue' % factory.queue30.level)
    # print(f'%d parts in queue' % factory.queue31.level)
    # print(f'%d parts in queue' % factory.queue32.level)
    # print(f'%d parts in queue' % factory.queue33.level)
    # print(f'%d parts in queue' % factory.queue34.level)
    # print(f'%d parts in queue' % factory.queue35.level)
    # print(f'%d parts in queue' % factory.queue36.level)
    # print(f'%d parts in queue' % factory.queue37.level)
    # print(f'%d parts in queue' % factory.queue38.level)
    # print(f'%d parts in queue' % factory.queue39.level)
    # print(f'%d parts in queue' % factory.queue40.level)

    # print(f'Dispatch has %d parts ready to go!' % factory.dispatch.level)
    # print('Total quatity make up = ',factory.model1,'Model_1', factory.model2, 'Model_2', factory.model3, 'Model_3')
    # #
    # # print(f'----------------------------------')
    # print("simulation time =",t)
    print(f'SIMULATION COMPLETED')
    #
    # arr = (x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9,
    #        x10, y10, x11, y11, x12, y12, x13, y13, x14, y14, x15, y15, x16, y16, x17, y17, x18, y18, x19, y19,
    #        x20, y20, x21, y21, x22, y22, x23, y23, x24, y24, x25, y25, x26, y26, x27, y27, x28, y28, x29, y29,
    #        x30, y30, x31, y31, x32, y32, x33, y33, x34, y34, x35, y35, x36, y36, x37, y37, x38, y38, x39, y39,
    #        x40, x40, x41, y41)
    #
    # np.savetxt('TIME_DIST_PLOT_COMP_3_3_MODEL.csv',
    #            arr,
    #            delimiter=", ",
    #            fmt='% s')
    #
    #
    # plt.figure(1)
    # plt.subplot(2,4,1)
    # plt.plot(x1,y1, label= 'Process 1')
    # plt.legend()
    # plt.subplot(2,4,2)
    # plt.plot(x2,y2, label= 'Process 2')
    # plt.legend()
    # plt.subplot(2,4,3)
    # plt.plot(x3,y3, label= 'Process 3')
    # plt.legend()
    # plt.subplot(2,4,4)
    # plt.plot(x4,y4, label= 'Process 4')
    # plt.legend()
    # plt.subplot(2,4,5)
    # plt.plot(x5,y5, label= 'Process 5')
    # plt.legend()
    # plt.subplot(2,4,6)
    # plt.plot(x6,y6, label= 'Process 6')
    # plt.legend()
    # plt.subplot(2,4,7)
    # plt.plot(x7,y7, label= 'Process 7')
    # plt.legend()
    # plt.subplot(2,4,8)
    # plt.plot(x8,y8, label= 'Process 8')
    # plt.legend()
    #
    # plt.figure(2)
    # plt.subplot(2,4,1)
    # plt.plot(x9,y9, label= 'Process 9')
    # plt.legend()
    # plt.subplot(2,4,2)
    # plt.plot(x10,y10, label= 'Process 10')
    # plt.legend()
    # plt.subplot(2,4,3)
    # plt.plot(x11,y11, label= 'Process 11')
    # plt.legend()
    # plt.subplot(2,4,4)
    # plt.plot(x12,y12, label= 'Process 12')
    # plt.legend()
    # plt.subplot(2,4,5)
    # plt.plot(x13,y13, label= 'Process 13')
    # plt.legend()
    # plt.subplot(2,4,6)
    # plt.plot(x14,y14, label= 'Process 14')
    # plt.legend()
    # plt.subplot(2,4,7)
    # plt.plot(x15,y15, label= 'Process 15')
    # plt.legend()
    # plt.subplot(2,4,8)
    # plt.plot(x16,y16, label= 'Process 16')
    # plt.legend()
    #
    # plt.figure(3)
    # plt.subplot(2,4,1)
    # plt.plot(x17,y17, label= 'Process 17')
    # plt.legend()
    # plt.subplot(2,4,2)
    # plt.plot(x18,y18, label= 'Process 18')
    # plt.legend()
    # plt.subplot(2,4,3)
    # plt.plot(x19,y19, label= 'Process 19')
    # plt.legend()
    # plt.subplot(2,4,4)
    # plt.plot(x20,y20, label= 'Process 20')
    # plt.legend()
    # plt.subplot(2,4,5)
    # plt.plot(x21,y21, label= 'Process 21')
    # plt.legend()
    # plt.subplot(2,4,6)
    # plt.plot(x22,y22, label= 'Process 22')
    # plt.legend()
    # plt.subplot(2,4,7)
    # plt.plot(x23,y23, label= 'Process 23')
    # plt.legend()
    # plt.subplot(2,4,8)
    # plt.plot(x24,y24, label= 'Process 24')
    # plt.legend()
    #
    # plt.figure(4)
    # plt.subplot(2,4,1)
    # plt.plot(x25,y25, label= 'Process 25')
    # plt.legend()
    # plt.subplot(2,4,2)
    # plt.plot(x26,y26, label= 'Process 26')
    # plt.legend()
    # plt.subplot(2,4,3)
    # plt.plot(x27,y27, label= 'Process 27')
    # plt.legend()
    # plt.subplot(2,4,4)
    # plt.plot(x28,y28, label= 'Process 28')
    # plt.legend()
    # plt.subplot(2,4,5)
    # plt.plot(x29,y29, label= 'Process 29')
    # plt.legend()
    # plt.subplot(2,4,6)
    # plt.plot(x30,y30, label= 'Process 30')
    # plt.legend()
    # plt.subplot(2,4,7)
    # plt.plot(x31,y31, label= 'Process 31')
    # plt.legend()
    # plt.subplot(2,4,8)
    # plt.plot(x32,y32, label= 'Process 32')
    # plt.legend()
    #
    # plt.figure(5)
    # plt.subplot(2,4,1)
    # plt.plot(x33,y33, label= 'Process 33')
    # plt.legend()
    # plt.subplot(2,4,2)
    # plt.plot(x34,y34, label= 'Process 34')
    # plt.legend()
    # plt.subplot(2,4,3)
    # plt.plot(x35,y35, label= 'Process 35')
    # plt.legend()
    # plt.subplot(2,4,4)
    # plt.plot(x36,y36, label= 'Process 36')
    # plt.legend()
    # plt.subplot(2,4,5)
    # plt.plot(x37,y37, label= 'Process 37')
    # plt.legend()
    # plt.subplot(2,4,6)
    # plt.plot(x38,y38, label= 'Process 38')
    # plt.legend()
    # plt.subplot(2,4,7)
    # plt.plot(x39,y39, label= 'Process 39')
    # plt.legend()
    # plt.subplot(2,4,8)
    # plt.plot(x40,y40, label= 'Process 40')
    # plt.legend()
    # plt.figure(6)
    # plt.plot(x41,y41, label= 'Dispatch')
    # plt.legend()
    #
    #
    # plt.show()
    return t



