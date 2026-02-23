from model.train import Model
from data.dataloader import dataloader

def train_service():
    
    x, Y, class_names = dataloader()
    model = Model().fit(x, Y, class_names)
    
    return model