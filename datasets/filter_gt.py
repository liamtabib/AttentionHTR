import re
import string
batch_max_length = 25
character  = string.printable[:-6] #'0123456789abcdefghijklmnopqrstuvwxyz'
out_of_char = f'[^{character}]'
filtered_gt = open('IAM_test_lmdb/filtered_gt.txt', 'w')
with open('iam_rwth_partitions/RWTH.iam_word_gt_final.test.thresh.txt', 'r') as f:
    lines = f.readlines()
    words = [line.strip().split(' ',1)[1] for line in lines]
    image_names = [line.strip().split(' ',1)[0] for line in lines]

    for image_name, word in zip(image_names, words):

        if re.search(out_of_char, word.lower()) is not None:
            print(word)

        if not len(word) > batch_max_length and re.search(out_of_char, word.lower()) is None:
           filtered_gt.write(f'{image_name} {word}\n')



filtered_gt.close()
