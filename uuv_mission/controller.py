class PDController:
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        """
        Initialize the PD controller with given proportional (kp) and derivative (kd) gains.
        Defaults are set to KP = 0.15 and KD = 0.6.
        """
        self.kp = kp  # Proportional gain
        self.kd = kd  # Derivative gain
        self.previous_error = 0  # Initialize previous error as zero

    def compute_control_action(self, reference: float, current_output: float) -> float:
        """
        Compute the control action u[t] based on the reference signal (desired depth) and
        the current output (current depth) using the PD control formula:
        
        u[t] = KP * e[t] + KD * (e[t] - e[t-1])
        
        Where:
        - e[t] is the error at time t (reference - current output)
        - e[t-1] is the error at the previous time step
        """
        # Calculate the current error (difference between reference and current output)
        current_error = reference - current_output

        # Compute the derivative of the error (change in error)
        derivative_error = current_error - self.previous_error

        # PD control action formula
        control_action = (self.kp * current_error) + (self.kd * derivative_error)

        # Update previous error for the next time step
        self.previous_error = current_error

        return control_action