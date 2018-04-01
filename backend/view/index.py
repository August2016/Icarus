import config
from aiohttp import web
from model.notif import NOTIF_TYPE
from model.post import POST_TYPES, POST_STATE, POST_VISIBLE
from model.user import USER_GROUP
from slim.base.view import BaseView
from slim.retcode import RETCODE
from view import route


@route('misc')
class TestBaseView(BaseView):
    @classmethod
    def interface(cls):
        cls.use('info', 'GET')

    async def info(self):
        self.finish(RETCODE.SUCCESS, {
            'POST_TYPES': POST_TYPES.to_dict(),
            'POST_STATE': POST_STATE.to_dict(),
            'POST_STATE_TXT': POST_STATE.txt,

            'USER_GROUP': USER_GROUP.to_dict(),
            'USER_GROUP_TXT': USER_GROUP.txt,

            'NOTIF_TYPE': NOTIF_TYPE.to_dict(),

            'NICKNAME_MIN': config.NICKNAME_MIN,
            'NICKNAME_MAX': config.NICKNAME_MAX,
            'NICKNAME_CN_FOR_REG_MIN': config.NICKNAME_CN_FOR_REG_MIN,
            'NICKNAME_FOR_REG_MIN': config.NICKNAME_FOR_REG_MIN,
            'NICKNAME_FOR_REG_MAX': config.NICKNAME_FOR_REG_MAX,
            'PASSWORD_MIN': config.PASSWORD_MIN,
            'PASSWORD_MAX': config.PASSWORD_MAX,

            'TOPIC_TITLE_LENGTH_MIN': config.TOPIC_TITLE_LENGTH_MIN,
            'TOPIC_TITLE_LENGTH_MAX': config.TOPIC_TITLE_LENGTH_MAX,
            'TOPIC_CONTENT_LENGTH_MAX': config.TOPIC_CONTENT_LENGTH_MAX,

            'retcode': RETCODE.to_dict(),
            'retinfo_cn': RETCODE.txt_cn,
        })
