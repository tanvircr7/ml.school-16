from metaflow import FlowSpec, step


class Introduction(FlowSpec):
    """A basic, linear flow with four steps."""

    @step
    def start(self):
        self.x = 0
        self.next(self.step_a, self.step_b)

    @step
    def step_a(self):
        self.x = self.x + 1
        self.next(self.step_join)

    @step
    def step_b(self):
        self.x = self.x + 5
        self.next(self.step_join)

    @step
    def step_join(self, inputs):
        print("a is %s" % inputs.step_a.x)
        print("a is %s" % inputs.step_b.x)
        print("total is %d" % sum(input.x for input in inputs))
        self.next(self.end)

    @step
    def end(self):
        pass



if __name__ == "__main__":
    Introduction()
