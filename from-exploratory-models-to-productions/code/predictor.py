class Predictor(EngineBasePrediction):
    
    def execute(self, input_message, **kwargs):
        return np.array_str(self.model["clf"].predict(input_message))