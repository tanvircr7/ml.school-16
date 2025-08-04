from metaflow import FlowSpec, step


class Introduction(FlowSpec):
    """A basic, linear flow with four steps."""

    @step
    def start(self):
        """Every flow must start with a 'start' step."""
        print("Starting the flow")
        self.x = 0
        self.vals = [self.x]
        self.next(self.step_a)

    @step
    def step_a(self):
        """Follows the 'start' step."""
        self.x = self.x + 2
        self.vals.append(self.x)
        print("Step A")
        self.next(self.step_b)

    @step
    def step_b(self):
        """Follows Step A."""
        self.x = self.x * self.x
        self.vals.append(self.x)
        print("Step B")
        self.next(self.end)

    @step
    def end(self):
        """Every flow must end with an 'end' step."""
        for val in self.vals:
            print(val)
        print(self.x)
        print("Ending the flow")


if __name__ == "__main__":
    Introduction()
