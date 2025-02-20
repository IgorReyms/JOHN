from core.api.Task import TicketTask
from core.api.Problem_User import Problem_User


class FirstAccessDescriptor_Problem:
    Problem_body = {}

    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __get__(self, instance, owner):
        if instance is None:
            return self  # Поддержка доступа к атрибуту класса напрямую

        # Проверяем наличие флага для этого атрибута на экземпляре
        access_flag_name = f'_has_accessed_{self.attr_name}'
        if not hasattr(instance, access_flag_name):
            instance.flag = 'True'  # Устанавливаем флаг
            setattr(instance, access_flag_name, 'True')  # Задаем флаг для атрибута
            # if self.attr != None:
            self.pakovchik()

        return getattr(instance, f'_{self.attr_name}')

    def __set__(self, instance, value):
        # Проверяем наличие флага для этого атрибута на экземпляре

        access_flag_name = f'_has_accessed_{self.attr_name}'
        if not hasattr(instance, access_flag_name):
            instance.flag = 'True'  # Устанавливаем флаг
            setattr(instance, access_flag_name, 'True')  # Задаем флаг для атрибута
            # if self.attr != None:
            self.pakovchik(value)

        setattr(instance, f'_{self.attr_name}', value)

    def pakovchik(self,value):
        #if self.attr_name in self.Ticket_body:
        self.Problem_body[self.attr_name] = value
        print('Slovarik Problem = ',self.Problem_body)

class Problem:
    flag: str = 'False'
    itemtype: str = 'Problem'
    id = FirstAccessDescriptor_Problem("id")
    name = FirstAccessDescriptor_Problem("name")
    entities_id = FirstAccessDescriptor_Problem("entities_id")
    is_recursive = FirstAccessDescriptor_Problem("is_recursive")
    is_deleted = FirstAccessDescriptor_Problem("is_deleted")
    status = FirstAccessDescriptor_Problem("status")
    content = FirstAccessDescriptor_Problem("content")
    date_mod = FirstAccessDescriptor_Problem("date_mod")
    date = FirstAccessDescriptor_Problem("date")
    solvedate = FirstAccessDescriptor_Problem("solvedate")
    closedate = FirstAccessDescriptor_Problem("closedate")
    time_to_resolve = FirstAccessDescriptor_Problem("time_to_resolve")
    users_id_recipient = FirstAccessDescriptor_Problem("users_id_recipient")
    users_id_lastupdater = FirstAccessDescriptor_Problem("users_id_lastupdater")
    urgency = FirstAccessDescriptor_Problem("urgency")
    impact = FirstAccessDescriptor_Problem("impact")
    priority = FirstAccessDescriptor_Problem("priority")
    itilcategories_id = FirstAccessDescriptor_Problem("itilcategories_id")
    impactcontent = FirstAccessDescriptor_Problem("impactcontent")
    causecontent = FirstAccessDescriptor_Problem("causecontent")
    symptomcontent = FirstAccessDescriptor_Problem("symptomcontent")
    actiontime = FirstAccessDescriptor_Problem("actiontime")
    begin_waiting_date = FirstAccessDescriptor_Problem("begin_waiting_date")
    waiting_duration = FirstAccessDescriptor_Problem("waiting_duration")
    close_delay_stat = FirstAccessDescriptor_Problem("close_delay_stat")
    solve_delay_stat = FirstAccessDescriptor_Problem("solve_delay_stat")
    date_creation = FirstAccessDescriptor_Problem("date_creation")
    locations_id = FirstAccessDescriptor_Problem("locations_id")


    def __init__(self):
        self.task = TicketTask
        self.Problem_User = Problem_User()

    def problem_body(self):
        self.id = 12 # ID Проблемы
        self.name = 'Информационная - 1111111111111111111' # Заголовок проблемы
        self.entities_id = 0 # Номер организации к которой отновится проблема
        self.is_recursive = 0 # Хз что это
        self.is_deleted = 0 # Логический флаг, указывающий, удалена ли проблема
        self.status = 2 # Статус проблемы
        self.content = '&#60;p&#62;аывфывааывваыывф&#60;/p&#62;' # Описание проблемы
        self.date_mod = '2025-02-12 12:47:42' # Дата и время последнего изменения проблемы
        self.date = '2025-02-04 14:50:05'# Дата заведения проблемы
        self.solvedate = None # Дата решения проблемы
        self.closedate = None # Дата закрытия проблемы
        self.time_to_resolve = '2025-02-06 16:55:17' # Время для решения проблемы по SLA
        self.users_id_recipient = 2 # Идентификатор пользователя (или группы пользователей) GLPI, которому назначена эта проблема на выполнение
        self.users_id_lastupdater = 2 # ID пользователя, который последний изменил проблему
        self.urgency = 3 # Срочность проблемы
        self.impact = 2 # Влияние проблемы
        self.priority = 2 # Приоритет проблемы
        self.itilcategories_id = 1 # ITIL категория
        self.impactcontent = ''
        self.causecontent = ''
        self.symptomcontent = ''
        self.actiontime = 0 # Общее время (в секундах), затраченное на выполнение каких-либо действий, связанных с заявкой (например, работа специалиста над заявкой)
        self.begin_waiting_date = None # Дата и время, когда проблемы была поставлена в состояние ожидания (например, когда требуется ответ от пользователя)
        self.waiting_duration = 46795 # Суммарное время (в секундах), в течение которого проблемы находилась в состоянии ожидания (независимо от того, связано ли это с SLA или OLA)
        self.close_delay_stat = 0 # Задержка в секундах между фактической датой закрытия проблемы и ожидаемой датой закрытия, рассчитанной на основе SLA или OLA
        self.solve_delay_stat = 0 # Задержка в секундах между фактической датой решения (например, когда проблема была устранена) и ожидаемой датой решения, рассчитанной на основе SLA или OLA
        self.date_creation = '2025-02-04 14:50:05' # Дата и время создания проблемы
        self.locations_id = 0 # Идентификатор местоположения (location), связанного с проблемой