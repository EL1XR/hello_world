print("hello world")
import torch
import torch.nn as nn
from torch.nn import Module


#whole of this class is a neural netwwork or think it as a single layer consisting all the other layers
class Network(nn.Module):
    

    def __init__(self):
        super().__init__()#we add this to extend the nn.Module
        self.conv1=nn.Conv2d(in_channels=1,out_channels=6,kernel_size=5)
        self.conv2=nn.Conv2d(in_channels=6,out_channels=12,kernel_size=5)
        self.conv3=nn.Conv2d(in_channels=12,out_channels=16,kernel_size=5)#there is also a stride(1,1) function stride tells that how far the conv should slide after each operation
    
        #here in_channels refers to the color channels since the input images are grey scale so we take its value as 1
        #and the output of one channel is the input of the next  channel(((((((6)))))))
        #this is the convolutional layer 
        
        #when we switch from conv to linear layer we have to flatten the tensor
        
        ##adding linearlayers 
        self.fc1 = nn.Linear(in_features=12*4*4,out_features=120)
        """ #4*4 means output of the last CNN is 4x4 image/filter:outputSizeOfCov = [(inputSize + 2*pad - filterSize)/stride] + 1"""
        self.fc2 = nn.Linear(in_features=120,out_features=60)
        self.out = nn.Linear(in_features=60,out_features=10)
        """there is also a bias function which can be set to be true or false by default to 
        true """
        #here out features refers to no of classes in the input images since mnist fashion lib has 10 objects
    
    def forward(self,t):
        t=self.layer(t)
        #we add this function to pass the layer forward
        return t
    
    
    
    net=Network()
    print(net)
