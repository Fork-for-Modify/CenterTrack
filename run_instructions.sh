# conda_env: dl
cd src 

# nuScenes_3Dtracking
python demo.py tracking,ddd --load_model ../models/nuScenes_3Dtracking.pth --dataset nuscenes --pre_hm --track_thresh 0.1 --demo ../dataset/videos/pipeline_test/bus_sci20.mp4 --test_focal_length 633 --save_results --save_image --save_video --save_framerate 5 --exp_id test

python demo.py tracking,ddd --load_model ../models/nuScenes_3Dtracking.pth --dataset nuscenes --pre_hm --track_thresh 0.1 --demo ../dataset/images/chasing --test_focal_length 633 --save_results --save_image --save_video --save_framerate 5 --exp_id nuscenes


# coco_tracking
## tmp-images
python demo.py tracking --load_model ../models/coco_tracking.pth --save_results --save_image --save_video --save_framerate 5 --demo ../dataset/images/ 

## tmp-videos
python demo.py tracking --load_model ../models/coco_tracking.pth --save_results --save_image --save_video --save_framerate 5 --demo ../dataset/videos/

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


## FAQ
# 1. warning: Error opening file (/build/opencv/modules/videoio/src/cap_ffmpeg_impl.hpp:856)
# unable to open the video: perhaps wrong video path, check it! ; or unknown video format (even ending with .mp4), format it with HandBrake software