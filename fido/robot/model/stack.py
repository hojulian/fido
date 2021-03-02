class Stack(object):
    """Represents a physical robot in stack form.

    Stack is used for building a `fido.robot.model.Model`. Intuitively,
    in Fido, a robot model is represented in a stack of layers, from
    bottom to top (think of it like a sandwich). Each layer has a
    certain size, and can attach various wheels and components. To form
    a stack, each layer is rigidly joined vertically.
    """

    def __init__(self, layers):
        self._layers = layers

    def model(self):
        """Converts the stack representation into a `fido.robot.model.Model`."""
        pass
