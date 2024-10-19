from dynamic import Mission


mission = Mission.from_csv('data/mission.csv')

# Print the first few elements of each attribute to verify
print(mission.reference[:5])  # Check the first 5 reference points
print(mission.cave_height[:5])  # Check the first 5 cave height values
print(mission.cave_depth[:5])  # Check the first 5 cave depth values
