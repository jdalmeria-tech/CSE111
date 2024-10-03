def water_column_height(tower_height, tank_height):
  """calculates and returns the height of a column of water
  from a tower_height and a tank_height."""

  h_water_column = tower_height + (3 * tank_height / 4)
  return h_water_column

def pressure_gain_from_water_height(height):
  """calculates and returns the pressure caused by Earth’s
  gravity pulling on the water stored in an elevated tank."""
  density_water = 998.2 # kg/meter^3
  g_force = 9.80665 # m/s^2

  pressure_in_kp = (density_water * g_force * height) / 1000
  return pressure_in_kp

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
  """calculates and returns the water pressure lost because of
  the friction between the water and the walls of a pipe that it flows through."""
  density_water = 998.2 # kg/meter^3

  lost_pressure_in_kp = (-friction_factor * pipe_length * density_water * (fluid_velocity**2)) / (2000 * pipe_diameter)
  return lost_pressure_in_kp