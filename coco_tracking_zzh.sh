# conda_env: dl
cd src 

# nuScenes_3Dtracking
python demo.py tracking,ddd --load_model ../models/nuScenes_3Dtracking.pth --dataset nuscenes --pre_hm --track_thresh 0.1 --demo ../dataset/videos/nuscenes_mini.mp4 --test_focal_length 633 --save_results --save_image --save_video --save_framerate 5

# coco_tracking
## tmp
python demo.py tracking --load_model ../models/coco_tracking.pth --save_results --save_image --save_video --save_framerate 5 --demo ../dataset/images/

## test
python demo.py tracking --load_model ../models/coco_tracking.pth --demo ../dataset/images/gaptv+fastdvdnet_ReadySteadyGo_1024_Cr10_gray --save_results --save_image --save_video --save_framerate 5
## traffic
python demo.py tracking --load_model ../models/coco_tracking.pth --demo ../dataset/images/traffic --save_results --save_image --save_video --save_framerate 5
## kobe
python demo.py tracking --load_model ../models/coco_tracking.pth --demo ../dataset/images/kobe --save_results --save_image --save_video --save_framerate 5
## football_1024_rgb
python demo.py tracking --load_model ../models/coco_tracking.pth --demo ../dataset/images/football_1024_rgb --save_results --save_image --save_video --save_framerate 5
## messi_1024_rgb
python demo.py tracking --load_model ../models/coco_tracking.pth --demo ../dataset/images/messi_1024_rgb --save_results --save_image --save_video --save_framerate 5