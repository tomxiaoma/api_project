
"""
定义所有测试数据

"""
import os
from params import tools
from common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPagesTeacher().get_page_list()
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


class ActivityExampleQuery:
    """
    选择活动范例库
    """
    def __init__(self):
        params = get_parameter('ActivityExampleQuery')
        self.yaml_data = YamlData(params=params)


class BoxesQuery:
    def __init__(self):
        params = get_parameter('BoxesQuery')
        self.yaml_data = YamlData(params=params)


class UseActivityExampleLogMutation:
    def __init__(self):
        params = get_parameter('UseActivityExampleLogMutation')
        self.yaml_data = YamlData(params=params)


class ClazzFeedListQuery:
    def __init__(self):
        params = get_parameter('ClazzFeedListQuery')
        self.yaml_data = YamlData(params=params)


class ClazzStudentsQuery:
    def __init__(self):
        params = get_parameter('ClazzStudentsQuery')
        self.yaml_data = YamlData(params=params)


class EvaluationAttributeQuery:
    def __init__(self):
        params = get_parameter('EvaluationAttributeQuery')
        self.yaml_data = YamlData(params=params)


class EvaluationDetailQuery:
    """
    根据评价ID查询评价详情
    """
    def __init__(self):
        params = get_parameter('EvaluationDetailQuery')
        self.yaml_data = YamlData(params=params)


class EvaluationPreviewQuery:
    """
    根据ID查看评价预览
    """
    def __init__(self):
        params = get_parameter('EvaluationPreviewQuery')
        self.yaml_data = YamlData(params=params)


class EvaluationsQuery:
    """
    根据班级ID查询评价列表
    """
    def __init__(self):
        params = get_parameter("EvaluationsQuery")
        self.yaml_data = YamlData(params=params)


class FeedListQuery:
    """
    根据班级ID查询在园时光列表
    """
    def __init__(self):
        params = get_parameter("FeedListQuery")
        self.yaml_data = YamlData(params=params)


class FeedQuery:
    """
    根据ID查询在园时光详情
    """
    def __init__(self):
        params = get_parameter("FeedQuery")
        self.yaml_data = YamlData(params=params)


class GardenLibraryQuery:
    """
    园本库详情查询
    """
    def __init__(self):
        params = get_parameter("GardenLibraryQuery")
        self.yaml_data = YamlData(params=params)


class GardenLibrarySubjectsQuery:
    """
    园本库主题列表查询
    """
    def __init__(self):
        params = get_parameter("GardenLibrarySubjectsQuery")
        self.yaml_data = YamlData(params=params)


class GardenSubjectLibrariesQuery:
    """
    园本库主题下的内容列表查询
    """
    def __init__(self):
        params = get_parameter("GardenSubjectLibrariesQuery")
        self.yaml_data = YamlData(params=params)


class GuardianFeedQuery:
    """
    根据feed_id查询亲子完成情况
    """
    def __init__(self):
        params = get_parameter("GuardianFeedQuery")
        self.yaml_data = YamlData(params=params)


class GuardianTasksQuery:
    """
    根据teacherTaskID分页查询主题列表
    """
    def __init__(self):
        params = get_parameter("GuardianTasksQuery")
        self.yaml_data = YamlData(params=params)


class KindAdminQuery:
    """
    幼儿园管理员查询
    """
    def __init__(self):
        params = get_parameter("KindAdminQuery")
        self.yaml_data = YamlData(params=params)


class KindergartenStudentsQuery:
    """
    根据kindergarten_id查询幼儿园所有学生
    """
    def __init__(self):
        params = get_parameter("KindergartenStudentsQuery")
        self.yaml_data = YamlData(params=params)


class KindergartenTeachersQuery:
    """
    根据kindergarten_id查询幼儿园所有老师
    """
    def __init__(self):
        params = get_parameter("KindergartenTeachersQuery")
        self.yaml_data = YamlData(params=params)


class LibrarySubjectQuery:
    """
    根据园本库ID查询园本库主题
    """
    def __init__(self):
        params = get_parameter("LibrarySubjectQuery")
        self.yaml_data = YamlData(params=params)


class MessageListQuery:
    """
    消息列表查询
    """
    def __init__(self):
        params = get_parameter("MessageListQuery")
        self.yaml_data = YamlData(params=params)

class MessageRemindQuery:
    """
    消息提醒查询
    """
    def __init__(self):
        params = get_parameter("MessageRemindQuery")
        self.yaml_data = YamlData(params=params)


class MonthlyInspirationQuery:
    """
    月度灵感库查询
    """
    def __init__(self):
        params = get_parameter("MonthlyInspirationQuery")
        self.yaml_data = YamlData(params=params)


class NewMessageListQuery:
    """
    新信息列表查询
    """
    def __init__(self):
        params = get_parameter("NewMessageListQuery")
        self.yaml_data = YamlData(params=params)


class NoticeQuery:
    """
    根据通知ID查询通知详情
    """
    def __init__(self):
        params = get_parameter("NoticeQuery")
        self.yaml_data = YamlData(params=params)


class PickedTextbookQuery:
    """
    根据班级ID查询精选教材
    """
    def __init__(self):
        params = get_parameter("PickedTextbookQuery")
        self.yaml_data = YamlData(params=params)


class PublishedTaskCountQuery:
    """
    根据班级ID查询发布亲子任务总数
    """
    def __init__(self):
        params = get_parameter("PublishedTaskCountQuery")
        self.yaml_data = YamlData(params=params)


class StudentEvaluationQuery:
    """
    根据评价ID以及学生ID查询评估信息
    """
    def __init__(self):
        params = get_parameter("StudentEvaluationQuery")
        self.yaml_data = YamlData(params=params)


class StudentsQuery:
    """
    根据clazz_id查询班级学生
    """
    def __init__(self):
        params = get_parameter("StudentsQuery")
        self.yaml_data = YamlData(params=params)


class TaskClassificationsQuery:
    """
    发布亲子任务库查询
    """
    def __init__(self):
        params = get_parameter("TaskClassificationsQuery")
        self.yaml_data = YamlData(params=params)


class TeacherTasksQuery:
    """
    教师端亲子任务列表查询
    """
    def __init__(self):
        params = get_parameter("TeacherTasksQuery")
        self.yaml_data = YamlData(params=params)


class TextBookListQuery:
    """
    课程列表查询
    """
    def __init__(self):
        params = get_parameter("TextBookListQuery")
        self.yaml_data = YamlData(params=params)


class DocumentsQuery:
    """
    帮助文档查询
    """
    def __init__(self):
        params = get_parameter("DocumentsQuery")
        self.yaml_data = YamlData(params=params)


class InspirationDetailQuery:
    """
    灵感库详情查询
    """
    def __init__(self):
        params = get_parameter("InspirationDetailQuery")
        self.yaml_data = YamlData(params=params)


class RecommendInspirationsQuery:
    """
    灵感库推荐查询
    """
    def __init__(self):
        params = get_parameter("RecommendInspirationsQuery")
        self.yaml_data = YamlData(params=params)


class SubjectQuery:
    """
    亲子任务库案例查询
    """
    def __init__(self):
        params = get_parameter("SubjectQuery")
        self.yaml_data = YamlData(params=params)


class TaskExamplesQuery:
    """
    根据clazz_id查询主题列表
    """
    def __init__(self):
        params = get_parameter("TaskExamplesQuery")
        self.yaml_data = YamlData(params=params)


class LatestKindergartenLibraries:
    """
    最新园本库列表查询
    """
    def __init__(self):
        params = get_parameter("LatestKindergartenLibraries")
        self.yaml_data = YamlData(params=params)


class LibraryGradesQuery:
    """
    园本库年级列表查询
    """
    def __init__(self):
        params = get_parameter("LibraryGradesQuery")
        self.yaml_data = YamlData(params=params)


class NoticeListQuery:
    """
    根据clazz_id查询通知列表
    """
    def __init__(self):
        params = get_parameter("NoticeListQuery")
        self.yaml_data = YamlData(params=params)


class TeacherQuery:
    """
    根据teacherid查询教师信息
    """
    def __init__(self):
        params = get_parameter("TeacherQuery")
        self.yaml_data = YamlData(params=params)


class KindClazzListQuery:
    """
    根据kindergarten_id查询班级列表
    """
    def __init__(self):
        params = get_parameter("KindClazzListQuery")
        self.yaml_data = YamlData(params=params)


class CarryIntoKindergartenLibrary:
    """
    放入园本库
    """
    def __init__(self):
        params = get_parameter("CarryIntoKindergartenLibrary")
        self.yaml_data = YamlData(params=params)


class CreateActivity:
    """
    创建在园时光
    """
    def __init__(self):
        params = get_parameter("CreateActivity")
        self.yaml_data = YamlData(params=params)


class CreateBoardMutation:
    """
    创建通知
    """
    def __init__(self):
        params = get_parameter("CreateBoardMutation")
        self.yaml_data = YamlData(params=params)


class CreateCollectionsMutation:
    """
    教师放入成长册
    """
    def __init__(self):
        params = get_parameter("CreateCollectionsMutation")
        self.yaml_data = YamlData(params=params)


class CreateTeacherCommentMutation:
    """
    教师评论
    """
    def __init__(self):
        params = get_parameter("CreateTeacherCommentMutation")
        self.yaml_data = YamlData(params=params)


class CreateEvaluationValueMutation:
    """
    老师评星
    """
    def __init__(self):
        params = get_parameter("CreateEvaluationValueMutation")
        self.yaml_data = YamlData(params=params)


class AppendImageMutation:
    """
    在园时光补发照片
    """
    def __init__(self):
        params = get_parameter("AppendImageMutation")
        self.yaml_data = YamlData(params=params)


class CreateLibrarySubject:
    """
    创建园本库主题
    """
    def __init__(self):
        params = get_parameter("CreateLibrarySubject")
        self.yaml_data = YamlData(params=params)


class CreateTeacherLikeMutation:
    """
    老师点赞动态
    """
    def __init__(self):
        params = get_parameter("CreateTeacherLikeMutation")
        self.yaml_data = YamlData(params=params)


class CreateTaskExampleSelectionMutation:
    """
    选用亲子任务库
    """
    def __init__(self):
        params = get_parameter("CreateTaskExampleSelectionMutation")
        self.yaml_data = YamlData(params=params)


class CreateTeacherTaskMutation:
    """
    创建亲子任务
    """
    def __init__(self):
        params = get_parameter("CreateTeacherTaskMutation")
        self.yaml_data = YamlData(params=params)


class DeleteActivityMutation:
    """
    删除在园时光
    """
    def __init__(self):
        params = get_parameter("DeleteActivityMutation")
        self.yaml_data = YamlData(params=params)


class DeleteTeacherCommentMutation:
    """
    删除评论
    """
    def __init__(self):
        params = get_parameter("DeleteTeacherCommentMutation")
        self.yaml_data = YamlData(params=params)


class DeleteEvaluationAttributeMutation:
    """
    删除单个发展评估主题
    """
    def __init__(self):
        params = get_parameter("DeleteEvaluationAttributeMutation")
        self.yaml_data = YamlData(params=params)


class DeleteEvaluationMutation:
    """
     根据发展评估ID删除整条评估
    """
    def __init__(self):
        params = get_parameter("DeleteEvaluationAttributeMutation")
        self.yaml_data = YamlData(params=params)


class DeleteEvaluationValuesMutation:
    """
    删除已评估的记录
    """
    def __init__(self):
        params = get_parameter("DeleteEvaluationValuesMutation")
        self.yaml_data = YamlData(params=params)


class DeleteImageMutation:
    """
    根据照片ID删除已上传的照片
    """
    def __init__(self):
        params = get_parameter("DeleteImageMutation")
        self.yaml_data = YamlData(params=params)


class DeleteKindergartenLibraryMutation:
    """
    根据内容ID删除园本库内容
    """
    def __init__(self):
        params = get_parameter("DeleteKindergartenLibraryMutation")
        self.yaml_data = YamlData(params=params)


class DeleteLibrarySubject:
    """
    根据主题ID删除园本库主题
    """
    def __init__(self):
        params = get_parameter("DeleteLibrarySubject")
        self.yaml_data = YamlData(params=params)


class DeleteLikeMutation:
    """
    老师取消点赞
    """
    def __init__(self):
        params = get_parameter("DeleteLikeMutation")
        self.yaml_data = YamlData(params=params)


class DeleteNoticeMutation:
    """
    老师删除通知
    """
    def __init__(self):
        params = get_parameter("DeleteNoticeMutation")
        self.yaml_data = YamlData(params=params)


class DeleteTeacherTaskMutation:
    """
    老师删除亲子任务
    """
    def __init__(self):
        params = get_parameter("DeleteTeacherTaskMutation")
        self.yaml_data = YamlData(params=params)


class UpdateEvaluationAttributeMutation:
    """
    编辑单条发展评估
    """
    def __init__(self):
        params = get_parameter("UpdateEvaluationAttributeMutation")
        self.yaml_data = YamlData(params=params)


class MarkGuardianTasksMutation:
    """
    将亲子任务标记为已读
    """
    def __init__(self):
        params = get_parameter("MarkGuardianTasksMutation")
        self.yaml_data = YamlData(params=params)


class PublishEvaluationMutation:
    """
    发展评估发送给家长
    """
    def __init__(self):
        params = get_parameter("PublishEvaluationMutation")
        self.yaml_data = YamlData(params=params)


class SwitchClazzMutation:
    """
    切换班级
    """
    def __init__(self):
        params = get_parameter("SwitchClazzMutation")
        self.yaml_data = YamlData(params=params)


class SwitchTextbook:
    """
    课程库切换课程
    """
    def __init__(self):
        params = get_parameter("SwitchTextbook")
        self.yaml_data = YamlData(params=params)


class UpdateEvaluationFinishedMutation:
    """
    完成评估
    """
    def __init__(self):
        params = get_parameter("UpdateEvaluationFinishedMutation")
        self.yaml_data = YamlData(params=params)


class UpdateImageMutation:
    """
    旋转照片
    """
    def __init__(self):
        params = get_parameter("UpdateImageMutation")
        self.yaml_data = YamlData(params=params)


class UpdateKindergartenLibraryMutation:
    """
    园本库切换主题
    """
    def __init__(self):
        params = get_parameter("UpdateKindergartenLibraryMutation")
        self.yaml_data = YamlData(params=params)


class UpdateLibrarySubject:
    """
    编辑园本库主题
    """
    def __init__(self):
        params = get_parameter("UpdateLibrarySubject")
        self.yaml_data = YamlData(params=params)


class UpdateStudentEvaluationMutation:
    """
    编辑更新评估
    """
    def __init__(self):
        params = get_parameter("UpdateStudentEvaluationMutation")
        self.yaml_data = YamlData(params=params)


class UpdateTeacherActivityMutation:
    """
    编辑在园时光动态
    """
    def __init__(self):
        params = get_parameter("UpdateTeacherActivityMutation")
        self.yaml_data = YamlData(params=params)


class UpdateTeacherMutation:
    """
    编辑老师资料
    """
    def __init__(self):
        params = get_parameter("UpdateTeacherMutation")
        self.yaml_data = YamlData(params=params)






