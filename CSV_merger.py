import os
import pandas as pd

# Directory where the files are stored
base_dir = os.path.join(os.getcwd(),"Group-2")
motions = ["left_large", "straight_large", "right_large"]
motion_prefixes = {"left_large": "ll_", "straight_large": "sl_", "right_large": "rl_"}
num_trials = 25

# Prepare the columns for the combined DataFrame
columns = [
    'Left_X', 'Left_Y', 'Left_theta',
    'Straight_X', 'Straight_Y', 'Straight_theta',
    'Right_X', 'Right_Y', 'Right_theta'
]

# Initialize an empty list to collect rows of data
combined_data = []

# Loop through each trial number
for trial in range(1, num_trials + 1):
    row = []  # Start with the trial number

    # Loop through each motion type and gather the final row's data
    for motion in motions:

        file_path = os.path.join(base_dir, motion, 'csv', f"{motion_prefixes[motion]}{trial:02}.csv")
        # Read the CSV file
        try:
            df = pd.read_csv(file_path)
            last_row = df.iloc[0]  # Get the last row
            # Append (X, Y, theta) for this motion to the row
            row.extend([last_row.iloc[0] * 100, last_row.iloc[1] * 100, last_row.iloc[2]])

        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            row.extend([None, None, None])  # In case of any error, fill with None

    # Append the row for this trial to combined_data
    combined_data.append(row)

# Create a DataFrame from combined_data
combined_df = pd.DataFrame(combined_data, columns=columns)

# Save the combined DataFrame to a CSV file
combined_df.to_csv('startpose_large.csv', index=False)

print("Combined CSV file created successfully as 'combined_output.csv'")
