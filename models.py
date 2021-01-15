## Define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
     ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        # self.conv1 = nn.Conv2d(1, 32, 5)
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) 
        # to avoid overfitting
        
        # Convolutional net part
        # Detect edges and corners
        self.conv1 = nn.Conv2d(1, 32, kernel_size=5)
        self.pool1 = nn.MaxPool2d(kernel_size=2)
        self.drop1 = nn.Dropout2d(p=0.05)
        
        self.features = nn.Sequential(
            # Detect simple shapes
            nn.Conv2d(32, 64, kernel_size=3),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Dropout2d(p=0.05),

            # Detect complex shapes
            nn.Conv2d(64, 128, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Dropout2d(p=0.05),

            nn.Conv2d(128, 256, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Dropout2d(p=0.05),
            
            nn.Conv2d(256, 512, kernel_size=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Dropout2d(p=0.05)
        )
        
        
        # Fully connected layer part
        self.regression = nn.Sequential(
            nn.Linear(512*6*6, 1024),
            nn.Tanh(),
            nn.Dropout(p=0.2),
            nn.Linear(1024, 512),
            nn.Tanh(),
            nn.Dropout(p=0.2),
            nn.Linear(512, 68*2)
            )

        
        
    def forward(self, x):
        ## Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        
        x = self.drop1(self.pool1(F.relu(self.conv1(x))))
        self.conv1_res = x
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.regression(x)
        
        return x