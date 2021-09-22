import os


# params
orig_names = ['bus', 'car', 'football',
              'run', 'tennis']

suffixs = ['', '_sci10', '_sci20']

# run
for suffix in suffixs:
    for orig_name in orig_names:
        cmd_str = f'python demo.py tracking,ddd --load_model ../models/nuScenes_3Dtracking.pth --dataset nuscenes --pre_hm --track_thresh 0.1 --demo ../dataset/videos/pipeline_test/{orig_name + suffix}.mp4 --test_focal_length 633 --save_results --save_image --save_video --save_framerate 5 --exp_id test'
        os.system(cmd_str)
        print('***** Finish ' + orig_name + suffix + ' *****\n\n')
        
