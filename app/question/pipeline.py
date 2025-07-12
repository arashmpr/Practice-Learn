class QuestionBankPipeline():
    def __init__(self):
        self.steps = []
    
    def add_steps(self, step):
        self.steps.append(step)
    
    def run(self, words):
        for step in self.steps:
            step.process(words)

