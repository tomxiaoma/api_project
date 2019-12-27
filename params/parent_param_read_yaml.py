"""
author:xiaoma
datetime:2019/12/19 14:48
describe:

"""
import os
from params import tools
from common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPagesParent.get_page_list()
    param = data[name]
    return param


class YamlData:
    def __init__(self,params):
        self.url = []
        self.data = []
        self.header = []
        self.yaml_input(params)

    def yaml_input(self,params):
        for i in range(0, len(params)):
            self.url.append(params[i]['url'])
            self.data.append(params[i]['data'])
            self.header.append(params[i]['header'])


class Login:
    """
    登录读取yaml文件
    """
    def __init__(self):
        params = get_parameter('Login')
        self.yaml_data = YamlData(params=params)


class AddCollectionMutation:
    """
    放入成长册
    """
    def __init__(self):
        params = get_parameter('AddCollectionMutation')
        self.yaml_data = YamlData(params=params)


class CancelGuardianInvitation:
    """
    取消邀请家人
    """
    def __init__(self):
        params = get_parameter('CancelGuardianInvitation')
        self.yaml_data = YamlData(params=params)


class CreateAccessCard:
    """
    取消邀请家人
    """
    def __init__(self):
        params = get_parameter('CreateAccessCard')
        self.yaml_data = YamlData(params=params)


class CreateAlbumShareMutation:
    """
    分享成长册
    """
    def __init__(self):
        params = get_parameter('CreateAlbumShareMutation')
        self.yaml_data = YamlData(params=params)


class CreateChildFeed:
    """
    家长创建个人动态
    """
    def __init__(self):
        params = get_parameter('CreateChildFeed')
        self.yaml_data = YamlData(params=params)


class CreateParentCommentMutation:
    """
    家长评论
    """
    def __init__(self):
        params = get_parameter('CreateParentCommentMutation')
        self.yaml_data = YamlData(params=params)


class CreateGuardianInvitation:
    """
    邀请家人
    """
    def __init__(self):
        params = get_parameter('CreateGuardianInvitation')
        self.yaml_data = YamlData(params=params)


class CheckPhoneAndSendSmsMutation:
    """
    检测手机号码是否可用
    """
    def __init__(self):
        params = get_parameter('CheckPhoneAndSendSmsMutation')
        self.yaml_data = YamlData(params=params)


class CreateGuardianRemarkMutation:
    """
    素质评价在家表现评语
    """
    def __init__(self):
        params = get_parameter('CreateGuardianRemarkMutation')
        self.yaml_data = YamlData(params=params)


class CreateGuardianTask:
    """
    完成亲子任务
    """
    def __init__(self):
        params = get_parameter('CreateGuardianTask')
        self.yaml_data = YamlData(params=params)


class CreateHobbyMutation:
    """
    创建爱好
    """
    def __init__(self):
        params = get_parameter('CreateHobbyMutation')
        self.yaml_data = YamlData(params=params)


class CreateParentLikeMutation:
    """
    点赞
    """
    def __init__(self):
        params = get_parameter('CreateParentLikeMutation')
        self.yaml_data = YamlData(params=params)


class DeleteCollectionMutation:
    """
    取消放入成长册
    """
    def __init__(self):
        params = get_parameter('DeleteCollectionMutation')
        self.yaml_data = YamlData(params=params)


class DeleteParentCommentMutation:
    """
    删除评论
    """
    def __init__(self):
        params = get_parameter('DeleteParentCommentMutation')
        self.yaml_data = YamlData(params=params)


class DeleteFeedMutation:
    """
    删除个人动态
    """
    def __init__(self):
        params = get_parameter('DeleteFeedMutation')
        self.yaml_data = YamlData(params=params)


class DeleteGuardianRemarkMutation:
    """
    删除素质评价家长评语
    """
    def __init__(self):
        params = get_parameter('DeleteGuardianRemarkMutation')
        self.yaml_data = YamlData(params=params)


class DeleteLikeParentMutation:
    """
    取消点赞
    """
    def __init__(self):
        params = get_parameter('DeleteLikeParentMutation')
        self.yaml_data = YamlData(params=params)


class PurchaseAlbumMutation:
    """
    购买成长册
    """
    def __init__(self):
        params = get_parameter('PurchaseAlbumMutation')
        self.yaml_data = YamlData(params=params)


class RemarkNotificationJump:
    """
    待办消息标记已读
    """
    def __init__(self):
        params = get_parameter('remarkNotificationJump')
        self.yaml_data = YamlData(params=params)


class SendSmsMutation:
    """
    发送短信
    """
    def __init__(self):
        params = get_parameter('SendSmsMutation')
        self.yaml_data = YamlData(params=params)


class SwitchChild:
    """
    切换宝贝
    """
    def __init__(self):
        params = get_parameter('switchChild')
        self.yaml_data = YamlData(params=params)


class UnbindAccessCardMutation:
    """
    注销我的考勤卡
    """
    def __init__(self):
        params = get_parameter('UnbindAccessCardMutation')
        self.yaml_data = YamlData(params=params)


class UpdateChildMutation:
    """
    更新学生资料
    """
    def __init__(self):
        params = get_parameter('UpdateChildMutation')
        self.yaml_data = YamlData(params=params)


class UpdateFeedMutation:
    """
    编辑个人动态
    """
    def __init__(self):
        params = get_parameter('UpdateFeedMutation')
        self.yaml_data = YamlData(params=params)


class UpdateGuardianRemarkMutation:
    """
    编辑素质评价家长评语
    """
    def __init__(self):
        params = get_parameter('UpdateGuardianRemarkMutation')
        self.yaml_data = YamlData(params=params)


class UpdateGuardianRole:
    """
    家长修改身份
    """
    def __init__(self):
        params = get_parameter('UpdateGuardianRole')
        self.yaml_data = YamlData(params=params)


class UpdatePasswordByPasswordMutation:
    """
    通过旧密码修改密码
    """
    def __init__(self):
        params = get_parameter('UpdatePasswordByPasswordMutation')
        self.yaml_data = YamlData(params=params)


class UpdatePasswordBySmsMutation:
    """
    通过短信验证码修改密码
    """
    def __init__(self):
        params = get_parameter('UpdatePasswordBySmsMutation')
        self.yaml_data = YamlData(params=params)


class UpdatePhoneMutation:
    """
    修改手机号
    """
    def __init__(self):
        params = get_parameter('UpdatePhoneMutation')
        self.yaml_data = YamlData(params=params)


class VerifyPasswordMutation:
    """
    修改手机号通过密码校验身份
    """
    def __init__(self):
        params = get_parameter('VerifyPasswordMutation')
        self.yaml_data = YamlData(params=params)


class VerifySmsMutation:
    """
    校验短信验证码
    """
    def __init__(self):
        params = get_parameter('VerifySmsMutation')
        self.yaml_data = YamlData(params=params)


class ConfirmBoard:
    """
    确认通知
    """

    def __init__(self):
        params = get_parameter('ConfirmBoard')
        self.yaml_data = YamlData(params=params)


class AccessCardsQuery:
    """
    我的考勤卡查询
    """
    def __init__(self):
        params = get_parameter('AccessCardsQuery')
        self.yaml_data = YamlData(params=params)


class AlbumFeeds:
    """
    成长册动态查询
    """
    def __init__(self):
        params = get_parameter('AlbumFeeds')
        self.yaml_data = YamlData(params=params)


class AlbumGuideQuery:
    """
    相册指南查询
    """
    def __init__(self):
        params = get_parameter('AlbumGuideQuery')
        self.yaml_data = YamlData(params=params)


class AlbumIntroQuery:
    """
    相册简介查询
    """
    def __init__(self):
        params = get_parameter('AlbumIntroQuery')
        self.yaml_data = YamlData(params=params)


class AlbumListQuery:
    """
    成长册列表查询（书架）
    """
    def __init__(self):
        params = get_parameter('AlbumListQuery')
        self.yaml_data = YamlData(params=params)


class BacklogsQuery:
    """
    老师所发内容查询
    """
    def __init__(self):
        params = get_parameter('BacklogsQuery')
        self.yaml_data = YamlData(params=params)


class BoardQuery:
    """
    通知详情查询
    """
    def __init__(self):
        params = get_parameter('boardQuery')
        self.yaml_data = YamlData(params=params)


class BoardsQuery:
    """
    通知列表查询
    """
    def __init__(self):
        params = get_parameter('boardsQuery')
        self.yaml_data = YamlData(params=params)


class ContactsQuery:
    """
    发起聊天页面查询
    """
    def __init__(self):
        params = get_parameter('ContactsQuery')
        self.yaml_data = YamlData(params=params)


class EvaluationRemarkFeedQuery:
    """
    评语详情查询
    """
    def __init__(self):
        params = get_parameter('EvaluationRemarkFeedQuery')
        self.yaml_data = YamlData(params=params)


class FeedParentQuery:
    """
    家长动态查询
    """
    def __init__(self):
        params = get_parameter('feedParentQuery')
        self.yaml_data = YamlData(params=params)


class GrowthPlanFeeds:
    """
    成长计划动态查询
    """
    def __init__(self):
        params = get_parameter('GrowthPlanFeeds')
        self.yaml_data = YamlData(params=params)


class GrowthPlanGuidePlan:
    """
    成长计划指南
    """
    def __init__(self):
        params = get_parameter('GrowthPlanGuidePlan')
        self.yaml_data = YamlData(params=params)


class GuardianEvaluationQuery:
    """
    发展评估查询
    """
    def __init__(self):
        params = get_parameter('GuardianEvaluationQuery')
        self.yaml_data = YamlData(params=params)


class GuardianEvaluations:
    """
    素质评价查询
    """
    def __init__(self):
        params = get_parameter('GuardianEvaluations')
        self.yaml_data = YamlData(params=params)


class GuardianQuery:
    """
    查询孩子信息
    """
    def __init__(self):
        params = get_parameter('GuardianQuery')
        self.yaml_data = YamlData(params=params)


class GuardianTaskFeeds:
    """
    亲子任务完成查询
    """
    def __init__(self):
        params = get_parameter('GuardianTaskFeeds')
        self.yaml_data = YamlData(params=params)


class GuardiansQuery:
    """
    邀请家人页面查询
    """
    def __init__(self):
        params = get_parameter('GuardiansQuery')
        self.yaml_data = YamlData(params=params)


class HobbiesQuery:
    """
    爱好查询
    """
    def __init__(self):
        params = get_parameter('HobbiesQuery')
        self.yaml_data = YamlData(params=params)


class MessageParentListQuery:
    """
    消息列表查询
    """
    def __init__(self):
        params = get_parameter('MessageParentListQuery')
        self.yaml_data = YamlData(params=params)


class NewMessageParentListQuery:
    """
    新消息列表查询
    """
    def __init__(self):
        params = get_parameter('NewMessageParentListQuery')
        self.yaml_data = YamlData(params=params)


class PlatformNotificationDetail:
    """
    七七说消息详情查询
    """
    def __init__(self):
        params = get_parameter('platformNotificationDetail')
        self.yaml_data = YamlData(params=params)


class PlatformNotificationQuery:
    """
    七七说消息列表查询
    """
    def __init__(self):
        params = get_parameter('platformNotificationQuery')
        self.yaml_data = YamlData(params=params)
