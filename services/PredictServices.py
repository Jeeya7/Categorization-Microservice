from model.train import Model

def prediction_service(title : str, model : Model):
    return model.predict(title)