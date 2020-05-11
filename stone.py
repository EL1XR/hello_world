import torch
import torch.nn as nn
from torch.nn import Module



class Network(nn.Module):
    def __init__(self):
        super().__init__()
        #adding the convolutional layers
        self.conv1=nn.Conv2d(in_channels=1,out_channels=8,kernel=7,bias=True)
        self.conv2=nn.Conv2d(in_channels=8,out_channels=15,kernel=7,bias=True)
        self.conv3=nn.Conv2d(in_channels=15,out_channels=22,kernel=7,bias=True)
        self.conv4=nn.Conv2d(in_channels=22,out_channels=29,kernel=7,bias=True)
        #adding the linear layeres
        #when we change from conv to linear layer we have to flatten the tensor
        self.fc1==nn.Linear(in_features=29*4*4,out_features=350,bias=True)
        self.fc1==nn.Linear(in_features=350,out_features=225,bias=True)
        self.fc1==nn.Linear(in_features=225,out_features=112,bias=True)
        self.out==nn.Linear(in_features=50,out_features=10,bias=True)#here out features is given by no of class of object we have
        
    def forward(self,t):
        t=self.layer(t)
        return t
    
network=Network
network
