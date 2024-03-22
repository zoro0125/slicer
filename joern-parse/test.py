
from reader import *


if __name__ == '__main__':
    data = get_lines_from_txt('C:\exp_data\exp_data\slice_dir_0313\good\\62670-v1.0.0\DEBUG_slice_forward_df.txt')
    print(data)
    print(len(data))
    count = 0
    # for directory in tqdm(os.listdir('C:\exp_data\exp_data\slice_dir_0313\\bad'), desc='hahahahaha'):
    #     if os.path.exists('C:\exp_data\exp_data\slice_dir_0313\\bad\\' + directory + '\DEBUG_slice_forward_df.txt'):
    #         data = get_lines_from_txt('C:\exp_data\exp_data\slice_dir_0313\\bad\\' + directory + '\DEBUG_slice_forward_df.txt')
    #         if len(data) == 0:
    #             count += 1
    #             with open('..\..\data\miss_1.txt', 'a+') as f:
    #                 f.write(directory + '\r')
    #     else:
    #         count += 1
    #         with open('..\..\data\miss_1.txt', 'a+') as f:
    #             f.write(directory + '\r')
    # print(count)