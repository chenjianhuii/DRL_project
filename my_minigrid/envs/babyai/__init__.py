from __future__ import annotations

from my_minigrid.envs.babyai.goto import (
    GoTo,
    GoToDoor,
    GoToImpUnlock,
    GoToLocal,
    GoToObj,
    GoToObjDoor,
    GoToRedBall,
    GoToRedBallGrey,
    MyGoToRedBallGrey,
    GoToRedBallNoDists,
    GoToRedBlueBall,
    GoToSeq,
)
from my_minigrid.envs.babyai.open import (
    Open,
    OpenDoor,
    OpenDoorsOrder,
    OpenRedDoor,
    OpenTwoDoors,
)
from my_minigrid.envs.babyai.other import (
    ActionObjDoor,
    FindObjS5,
    KeyCorridor,
    MoveTwoAcross,
    OneRoomS8,
)
from my_minigrid.envs.babyai.pickup import (
    Pickup,
    PickupAbove,
    PickupDist,
    PickupLoc,
    UnblockPickup,
)
from my_minigrid.envs.babyai.putnext import PutNext, PutNextLocal
from my_minigrid.envs.babyai.synth import (
    BossLevel,
    BossLevelNoUnlock,
    MiniBossLevel,
    Synth,
    SynthLoc,
    SynthSeq,
)
from my_minigrid.envs.babyai.unlock import (
    BlockedUnlockPickup,
    KeyInBox,
    Unlock,
    UnlockLocal,
    UnlockPickup,
    UnlockToUnlock,
)
