from PIL import Image


class Model:
    def __init__(self):
        pass

    def train(self):
        pass

    def predict(self, filepath):
        image = Image.open(filepath)
        image = image.convert('L')
        image.save(filepath)
