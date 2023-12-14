import numpy as np
import os
import shutil
import argparse

def copy_images(input_folder, input_file):

    # Create an array using np.arange that starts at 0, ends at 1 (inclusive), with a step of 0.1
    numbers = np.arange(0, 1.1, 0.1)

    for i in range(len(numbers)-1):
        print(i)
        output_folder = f'{input_folder}/../{str(round(numbers[i], 1))}-{str(round(numbers[i+1], 1))}_confidence/'
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        with open(input_file, 'r') as file:
            for line in file:
                # Split the line into columns
                #image_name, word, score_str = line.split()
                writer_image, word, score_str = line.split()
                image_name = writer_image.split(',')[1] + '.png'

                # Convert score to float
                score = float(score_str)

                if score >= numbers[i] and score <= numbers[i+1]:
                    source_path = os.path.join(input_folder, image_name)
                    destination_path = os.path.join(output_folder, image_name)

                    # Copy the image to the new folder
                    shutil.copy(source_path, destination_path)


def main():
    parser = argparse.ArgumentParser(description="Copy images based on score threshold.")
    parser.add_argument("--input_folder", help="Path to the input folder containing images.")
    parser.add_argument("--input_file", help="Path to the input file containing image details.")

    args = parser.parse_args()
    copy_images(args.input_folder, args.input_file)

if __name__ == "__main__":
    main()
