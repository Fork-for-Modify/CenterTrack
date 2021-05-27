# conda_env: dl

python ./srcdemo.py tracking --load_model ./models/coco_tracking.pth --demo ./dataset/videos/nuscenes_mini.mp4
python ./src/demo.py tracking --load_model ./models/coco_tracking.pth --demo ./dataset/images/traffic --save_video