class Model(object):
    """Represents a model that describes a robot.

    This is very similar to ROS’s tf tree. A model is created using a
    `fido.robot.model.Stack`. Currently, the only way to create a valid
    model is to use `fido.robot.model.Stack.model()`.
    """

    def ros_urdf(self, path):
        """Export a ROS compatible URDF representation of the robot.

        Internally, when converting the model to a URDF, this method
        first converts the model’s stack into `ros/urdf_parser_py`’s
        urdf nodes. Then, once a new tree of urdf nodes is created, it
        calls to_xml to convert into a URDF file at the given path.
        """
        pass


def from_ros_urdf(path):
    """Read and parse a ROS URDF file as `fido.robot.model.Model`.
    """
    pass

