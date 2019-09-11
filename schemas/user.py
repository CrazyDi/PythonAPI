from ma import ma
from marshmallow import pre_dump

from models.user import UserModel


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id", "activated")

    @pre_dump(pass_many=False)
    def _pre_dump(self, user: UserModel, many, **kwargs):
        user.confirmation = [user.most_recent_confirmation]
        return user
