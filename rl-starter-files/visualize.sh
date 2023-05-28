# env=BabyAI-MyGoToRedBallGrey-v1
# env=BabyAI-PickupLoc-v2
env=BabyAI-GoTo-v0
# python3 -m scripts.visualize --env BabyAI-GoToLocalS16N14-v0 --model BabyAI-GoToLocalS16N14-v0
python3 -m scripts.visualize --env $env --model ${env}-$1 --text
# python3 -m scripts.visualize --env BabyAI-GoToRedBallGrey-v3 --model BabyAI-GoToRedBallGrey-v3