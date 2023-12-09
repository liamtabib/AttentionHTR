import matplotlib.pyplot as plt
import numpy as np

# Function to extract numerical values from a line
def extract_numbers(line):
    # Split the line into words
    words = line.split()
    
    # Extract the numerical value (assuming it's the last token on the line)
    try:
        value = float(words[-1])
        return value
    except ValueError:
        return None

# Read the text file and extract numerical values
file_path = 'synthetic_GW/log_confidence_scores.txt'  # Replace with the actual file path
GW = 'GW'
IAM = 'IAM'
IMGUR5k = 'IMGUR5k'
datasets = [IAM, IMGUR5k, GW]
names = ['IAM', 'IMGUR5K', 'Washington']
# Set up the figure and adjust subplot spacing
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
plt.subplots_adjust(wspace=0.3)  # Adjust the width space between subplots

for i, dataset in enumerate(datasets):
    values = []
    with open(f'synthetic_{dataset}/log_confidence_scores.txt', 'r') as file:
        for line in file:
            number = extract_numbers(line)
            if number is not None:
                values.append(number)

    # Generate a histogram
    axes[i].hist(values, bins=20, color='blue', edgecolor='black')
    axes[i].set_title(f'Synthetic {names[i]}')
    axes[i].set_xlabel('AttentionHTR Confidence Score')
    axes[i].set_ylabel('Frequency')

    values_array = np.array(values)
    print(f'{dataset} results:')
    print(f'Mean: {values_array.mean()}')
    print(f'Median: {np.median(values_array)}')
    print(f'Variance: {np.var(values_array)}')
    print('\n')

plt.savefig('plots/datasets_histogram.png')
plt.show()
