"""Compute and print the storage efficiency of all 12 cans."""
# Import the standard math module so that
# math.pi can be used in this program.
# Stretch Challenge 1-4 are included :)

import math

def main():

  # Stretch Challenge no. 3
  # Four lists, one for each detail of the cans.
  can_names = [
    "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder",
    "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"
  ]

  can_radiuses = [
    6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40,
    6.83, 15.72, 6.83, 7.62, 8.10
  ]

  can_heights = [
    10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89,
    7.62, 17.78, 12.38, 11.27, 11.11
  ]

  can_costs = [
    0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26,
    1.53, 0.34, 0.38, 0.42
  ]

  best_storage_efficiency = None
  best_cost_efficiency = None
  max_store_efficiency = -1
  max_cost_efficiency = -1

  # For each can in the list, extract values and assign them
  # name, radius, height, and cost.
  for i in range(len(can_names)):
    name = can_names[i]
    radius = can_radiuses[i]
    height = can_heights[i]
    cost = can_costs[i]

    # Call the compute_storage_efficiency and
    # compute_cost_efficiency functions.
    storage_efficiency = compute_storage_efficiency(radius, height)
    cost_efficiency  = compute_cost_efficiency(radius, height, cost)

    # Print the details
    print(f"{name} {storage_efficiency:.2f} | ${cost_efficiency:.2f}")


    #Stretch challenge no.4
    # Save the current can's name and storage efficiency
    # if it exceeds the maximum storage efficiency.
    if storage_efficiency > max_store_efficiency:
      best_storage_efficiency = name
      max_store_efficiency = storage_efficiency

    # Save the current can’s name and cost efficiency
    # if it exceeds the maximum cost efficiency.
    if cost_efficiency > max_cost_efficiency:
      best_cost_efficiency = name
      max_cost_efficiency = cost_efficiency

  # Display the best storage and cost efficiencies.
  print("-----------------------------------------------")
  print(f"Top can size for storage efficiency: {best_storage_efficiency}")
  print(f"Top can size for storage efficiency: {best_cost_efficiency}")

    
  
def compute_volume(radius, height):
  """Compute and return the volume of the can."""
  volume = math.pi * radius**2 * height
  return volume

def compute_surface_area(radius, height):
  """Compute and return the surface area of the can."""
  surface = ((2*math.pi) * radius) * (radius + height)
  return surface

# Stretch Challenge no.1
# Computation of storage efficiency
def compute_storage_efficiency(radius, height):
  volume = compute_volume(radius, height)
  surface = compute_surface_area(radius, height)
  storage_efficiency = volume / surface
  return storage_efficiency

# Stretch Challenge no.2
# Computation of cost efficiency
def compute_cost_efficiency(radius, height, cost):
  volume = compute_volume(radius,height)
  cost_efficiency = volume / cost
  return cost_efficiency

# Call the main function so that
# this program will start executing.
main()