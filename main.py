from model.train import Model
from data.dataloader import dataloader


def main():
    
    x, Y, class_names = dataloader()
    
    model = Model().fit(x, Y, class_names)
    
    # print(model.__dict__)

    print(model.predict("Clean my desk"))    
    return

if __name__ =="__main__":
    main()