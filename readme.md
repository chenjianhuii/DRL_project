# 修改环境
my_minigrid/__init__.py 用register函数增加自定义环境
my_minigrid/envs/babyai/goto.py 里自定义环境MyGoToRedBallGrey, 主要是重写了step方法, 增加pick up动作的reward

# train/visualize/evaluate
见rl-starter-files内对应的脚本, storage文件夹保存所有的输出

# torch_ac
自带a2c和ppo实现的repo, 实现了algos/icmppo.py

# 目前的一些结果
1. pick up的reward太小时模型还是能正常学习, 太大时虽然会发生mode collapse但是这时最后的return是比完成任务还高的, 也不能说模型这样就是错的
2. icmppo里的intrinsic reward太小时还是会发生mode collapse, 太大时模型学不到任何东西
3. 考虑用加了intrinsic reward的model做exploration, 真正的model不加intrinsic reward（感觉希望不大