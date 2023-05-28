# env=BabyAI-MyGoToRedBallGrey-v1
# env=BabyAI-PickupLoc-v2
env=BabyAI-GoTo-v0
frames=500000

# python3 -m scripts.train --algo ppo --env BabyAI-GoToLocalS16N14-v0 --model BabyAI-GoToLocalS16N14-v0 --save-interval 10 --frames 500000 
# python3 -m scripts.train --algo ppo --env BabyAI-GoToRedBallGrey-v1 --model BabyAI-GoToRedBallGrey-v1 --save-interval 10 --frames 200000 
rm -rf storage/${env}-$1
python3 -m scripts.train --algo $1 --env $env --model ${env}-$1 --save-interval 10 --frames $frames --text
# python3 -m scripts.train --algo ppo --env BabyAI-GoToRedBallGrey-v3 --model BabyAI-GoToRedBallGrey-v3 --save-interval 10 --frames 500000 