from metaflow import FlowSpec, step, retry, current
import random, time


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

    @retry(times = 3, minutes_between_retries = 0.1)
    @step
    def step_b(self):
        attmpt_counter = getattr(current, 'retry_count', 0)
        attmpt_counter += 1
        print(f"calling flaky service #{attmpt_counter}")
        time.sleep(1)

        if random.random() < 0.7:
            error_msg = f"service failed #{attmpt_counter}"
            print(error_msg)
            raise Exception(error_msg)
        else:
            print(f"Success on attempt #{attmpt_counter}")
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
