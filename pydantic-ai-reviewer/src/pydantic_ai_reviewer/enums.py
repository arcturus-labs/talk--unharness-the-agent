from enum import Enum


class UpdateActor(str, Enum):
    AI_AGENT = "ai_agent"
    HUMAN_RECRUITER = "human_recruiter"
    CANDIDATE = "candidate"


class UpdateType(str, Enum):
    RECOMMEND_ADVANCE = "recommend_advance"
    RECOMMEND_DECLINE = "recommend_decline"
    RECOMMEND_FOLLOW_UP = "recommend_follow_up"
    ADVANCE = "advance"
    DECLINE = "decline"
    FOLLOW_UP = "follow_up"
    REQUEST_AI_SCREEN = "request_ai_screen"
    GENERAL_UPDATE = "general_update"
    WITHDRAW = "withdraw"
