from metaflow import FlowSpec, step


class Introduction(FlowSpec):
    """A basic, linear flow with four steps."""

    @step
    def start(self):
        self.nums = [2, 3, 2]
        self.next(self.square, foreach = "nums")

    @step
    def square(self):
        self.x = self.input * self.input
        self.next(self.step_join)

    @step
    def step_join(self, inputs):
        self.list = [input.x for input in inputs]
        self.sum = sum(input.x for input in inputs)
        self.next(self.end)

    @step
    def end(self):
        print(self.list)
        print(self.sum)



if __name__ == "__main__":
    Introduction()
