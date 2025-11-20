class ModelTrainer:
    def __init__(self, model, training_data, validation_data):
        self.model = model
        self.training_data = training_data
        self.validation_data = validation_data

    def train(self, epochs=10, batch_size=32):
        history = self.model.fit(
            self.training_data,
            validation_data=self.validation_data,
            epochs=epochs,
            batch_size=batch_size
        )
        return history

    def evaluate(self):
        evaluation = self.model.evaluate(self.validation_data)
        return evaluation

    def save_model(self, filepath):
        self.model.save(filepath)

    def load_model(self, filepath):
        from tensorflow.keras.models import load_model
        self.model = load_model(filepath)