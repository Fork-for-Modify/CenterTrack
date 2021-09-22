import os


# params
orig_names = ['bus', 'car', 'football',
              'run', 'tennis']

suffixs = ['', '_sci10', '_sci20']

# run
for suffix in suffixs:
    for orig_name in orig_names:
        data_dir = './results/'
        data_path = data_dir+orig_name+suffix+'/' + \
            'test_'+orig_name+suffix+'_ResData.json'
        save_dir = data_dir+orig_name+suffix+'/'

        cmd_str = f'python dist2sentence.py --data_path {data_path} --save_dir {save_dir}'
        os.system(cmd_str)
        print('***** Finish ' + orig_name + suffix + ' *****\n\n')
