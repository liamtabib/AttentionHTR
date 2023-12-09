import os
import shutil
import argparse

def copy_images(input_folder, output_folder, input_file, threshold):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the input file and copy images with score > threshold
    output_file = open(f'{output_folder}../gt_threshold_{threshold}.txt', 'w')
    with open(input_file, 'r') as file:
        for line in file:
            # Split the line into columns
            #image_name, word, score_str = line.split()
            writer_image, word, score_str = line.split()
            image_name = writer_image.split(',')[1] + '.png'

            # Convert score to float
            score = float(score_str)

            # Check if the score is greater than the threshold
            if score >= threshold:
                # Construct the source and destination paths
                source_path = os.path.join(input_folder, image_name)
                destination_path = os.path.join(output_folder, image_name)

                # Copy the image to the new folder
                shutil.copy(source_path, destination_path)

                output_file.write(f'{image_name} {word} {score}\n')


    print(f"Images with a score greater than {threshold} copied to {output_folder}.")

def main():
    parser = argparse.ArgumentParser(description="Copy images based on score threshold.")
    parser.add_argument("--input_folder", help="Path to the input folder containing images.")
    parser.add_argument("--output_folder", help="Path to the output folder for copied images.")
    parser.add_argument("--input_file", help="Path to the input file containing image details.")
    parser.add_argument("--threshold", type=float, default=0.5, help="Score threshold (default is 0.5).")

    args = parser.parse_args()
    copy_images(args.input_folder, args.output_folder, args.input_file, args.threshold)

if __name__ == "__main__":
    main()
