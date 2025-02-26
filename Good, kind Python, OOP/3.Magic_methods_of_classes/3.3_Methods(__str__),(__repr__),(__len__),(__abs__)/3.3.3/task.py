class Model:
    def __init__(self):
        self.fields = None

    def __str__(self):
        if self.fields is not None:
            return f"Model: " + ", ".join(f"{k} = {v}" for k, v in self.fields.items())
        return "Model"

    def query(self, **kwargs):
        self.fields = kwargs


model = Model()
model.query(id=1, fio='Sergey', old=33)
