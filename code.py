""" This is ANN-MODEL with no-lib
1 model
2 input - 2 output
1 hidden layer
fully connected
"""
import numpy as np

def net_out(a,b): 
    #1_using SIGMOID ACTIVATE FUNCTION
    #2_using RELU ACTIONVATE FUNCTION
    if b==1:
        return round(float(1.0/(1+np.exp(-a))),10)
    else:
        return round(float(max(0,a)),10)


input_array = [float(0.05), float(0.1)] 
expect_out =[float(0.01),float(0.99)] 

#input : 0.05 and 0.1
#want output: 0.01 and 0.99

hiddenNode_Array = [0,0]

weight_Array = [0.15, 0.2, 0.25, 0.3, 0.4, 0.45, 0.5, 0.55]

print(net_out(0.3775,1))

