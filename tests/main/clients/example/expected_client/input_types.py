from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import Color


class UserCreateInput(BaseModel):
    first_name: Optional[str] = Field(alias="firstName", default=None)
    last_name: Optional[str] = Field(alias="lastName", default=None)
    email: str
    favourite_color: Optional[Color] = Field(alias="favouriteColor", default=None)
    location: Optional["LocationInput"] = None


class LocationInput(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None


class UserPreferencesInput(BaseModel):
    lucky_number: Optional[int] = Field(alias="luckyNumber", default=7)
    favourite_word: Optional[str] = Field(alias="favouriteWord", default="word")
    color_opacity: Optional[float] = Field(alias="colorOpacity", default=1.0)
    excluded_tags: Optional[List[str]] = Field(
        alias="excludedTags", default_factory=lambda: ["offtop", "tag123"]
    )
    notifications_preferences: "NotificationsPreferencesInput" = Field(
        alias="notificationsPreferences",
        default_factory=lambda: globals()[
            "NotificationsPreferencesInput"
        ].model_validate(
            {
                "receiveMails": True,
                "receivePushNotifications": True,
                "receiveSms": False,
                "title": "Mr",
            }
        ),
    )


class NotificationsPreferencesInput(BaseModel):
    receive_mails: bool = Field(alias="receiveMails")
    receive_push_notifications: bool = Field(alias="receivePushNotifications")
    receive_sms: bool = Field(alias="receiveSms")
    title: str


UserCreateInput.model_rebuild()
LocationInput.model_rebuild()
UserPreferencesInput.model_rebuild()
NotificationsPreferencesInput.model_rebuild()
