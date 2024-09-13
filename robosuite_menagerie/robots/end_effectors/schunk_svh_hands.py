"""
Dexterous hands for GR1 robot.
"""
import numpy as np

from robosuite.models.grippers import register_eef
from robosuite.models.grippers.gripper_model import GripperModel

from robosuite_menagerie import menagerie_path_completion

@register_eef
class SchunkSvhLeftHand(GripperModel):
    """
    Dexterous left SVH hand from Schunk.

    Args:
        idn (int or str): Number or some other unique identification string for this gripper instance
    """

    def __init__(self, idn=0):
        super().__init__(menagerie_path_completion("end_effectors/schunk_svh_left_hand.xml"), idn=idn)

    def format_action(self, action):
        return action

    @property
    def init_qpos(self):
        return np.array([0.0] * 20)

    @property
    def speed(self):
        return 0.15

    @property
    def dof(self):
        return 20

@register_eef
class SchunkSvhRightHand(GripperModel):
    """
    Dexterous right SVH hand from Schunk.

    Args:
        idn (int or str): Number or some other unique identification string for this gripper instance
    """

    def __init__(self, idn=0):
        super().__init__(menagerie_path_completion("end_effectors/schunk_svh_right_hand.xml"), idn=idn)

    def format_action(self, action):
        return action

    @property
    def init_qpos(self):
        return np.array([0.0] * 20)

    @property
    def speed(self):
        return 0.15

    @property
    def dof(self):
        return 20
