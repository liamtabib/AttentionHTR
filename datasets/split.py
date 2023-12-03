from sklearn.model_selection import train_test_split
import os
import shutil

# Step 1: Read data from the .txt file
with open('gan.iam.tr_va.gt.filter27', 'r') as file:
    data = file.readlines()

# Step 2: Split the data into training and validation sets
train_data, valid_data = train_test_split(data, test_size=0.2)  # 20% for validation

train_lines= []
for line in train_data:
    correct_path = 'train_images/' + line.strip().split(',')[1].split()[0] + '.png' + '\t' + line.strip().split(',')[1].split()[1]
    train_lines.append(correct_path + '\n')

valid_lines= []
for line in valid_data:
    correct_path = 'valid_images/' + line.strip().split(',')[1].split()[0] + '.png'+ '\t' + line.strip().split(',')[1].split()[1]
    valid_lines.append(correct_path + '\n')

# Step 3: Write the training and validation data to separate .txt files
with open('synthetic_IAM_gt_train.txt', 'w') as file:
    file.writelines(train_lines)

with open('synthetic_IAM_gt_val.txt', 'w') as file:
    file.writelines(valid_lines)

train_dir = 'train_images'
valid_dir = 'valid_images'

os.makedirs(train_dir, exist_ok=True)
os.makedirs(valid_dir, exist_ok=True)

for line in train_lines:
    image_path = line.strip().split('\t')[0]
    image_path = 'images/'+image_path.split('/')[1]
    shutil.move(image_path, train_dir)


for line in valid_lines:
    image_path = line.strip().split('\t')[0]
    image_path = 'images/'+image_path.split('/')[1]
    shutil.move(image_path, valid_dir)