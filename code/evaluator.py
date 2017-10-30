class MetricsEvaluator(EngineBaseTraining):

    def execute(self, **kwargs):
        pred = self.model['clf'].predict(self.dataset['X'][1])
        m1 = classification_report(self.dataset['y'][1], pred)
        m2 = confusion_matrix(self.dataset['y'][1], pred)
        self.metrics = [m1, m2]    