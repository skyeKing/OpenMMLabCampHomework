python mmyolo/demo/featmap_vis_demo.py demo/balloon/wh860.jpg demo/balloon//balloon_train_rtmdet.py work_dirs/balloon_train_rtmdet/epoch_40.pth  --target-layers backbone  --channel-reduction squeeze_mean


python mmyolo/demo/featmap_vis_demo.py demo/balloon/wh860.jpg demo/balloon//balloon_train_rtmdet.py work_dirs/balloon_train_rtmdet/epoch_40.pth  --target-layers neck  --channel-reduction squeeze_mean

python mmyolo/demo/boxam_vis_demo.py demo/balloon/wh860.jpg demo/balloon//balloon_train_rtmdet.py work_dirs/balloon_train_rtmdet/epoch_40.pth --target-layer neck.out_convs[2]

python mmyolo/demo/boxam_vis_demo.py demo/balloon/wh860.jpg demo/balloon//balloon_train_rtmdet.py work_dirs/balloon_train_rtmdet/epoch_40.pth --target-layer neck.out_convs[0]
