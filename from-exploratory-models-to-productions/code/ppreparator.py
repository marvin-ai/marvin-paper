class PredictionPreparator(EngineBasePrediction):
    
    def execute(self, input_message, **kwargs):
        return self.model['vectorizer'].transform([input_message['msg']])