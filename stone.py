print("hello world")
import torch
import torch.nn as nn
from torch.nn import Module

#first we build a class network
#which represents whole nn
class Network(nn.Module):
    def __init__(self):
        super().__init__()#we add this and the nn.module to get a descriptive output instead of <object at __main__0.237428462848>
        self.conv1=nn.Conv2d(in_channels=1,out_channels=8,kernel_size=7 )
        self.conv2=nn.Conv2d(in_channels=8,out_channels=15,kernel_size=7 )
        self.conv3=nn.Conv2d(in_channels=15,out_channels=22,kernel_size=7 )
        self.conv4=nn.Conv2d(in_channels=22,out_channels=29,kernel_size=7 )
        #adding the linear layeres
        #when we change from conv to linear layer we have to flatten the tensor
        self.fc1=nn.Linear(in_features=26*4*4,out_features=350 )
        self.fc2=nn.Linear(in_features=350,out_features=225 )
        self.fc3=nn.Linear(in_features=225,out_features=112 )
        self.out=nn.Linear(in_features=50,out_features=10 )#here out features is given by no of class of object we have
        
    def forward(self,t):
        t=self.layer(t)
        return t
net=Network()
print(net)
    
    
    
