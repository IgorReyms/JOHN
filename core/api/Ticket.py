from core.api.Task import TicketTask
from core.api.Ticket_User import Ticket_User

class FirstAccessDescriptor_Ticket:
    Ticket_body = {}

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
        self.Ticket_body[self.attr_name] = value
        print('Slovarik Ticket = ',self.Ticket_body)

class Ticket:
    flag: str = 'False'
    itemtype: str = 'Ticket'
    id = FirstAccessDescriptor_Ticket("id")
    entities_id = FirstAccessDescriptor_Ticket("entities_id")
    name = FirstAccessDescriptor_Ticket("name")
    date = FirstAccessDescriptor_Ticket("date")
    closedate = FirstAccessDescriptor_Ticket("closedate")
    solvedate = FirstAccessDescriptor_Ticket("solvedate")
    takeintoaccountdate = FirstAccessDescriptor_Ticket("takeintoaccountdate")
    date_mod = FirstAccessDescriptor_Ticket("date_mod")
    users_id_lastupdater = FirstAccessDescriptor_Ticket("users_id_lastupdater")
    status = FirstAccessDescriptor_Ticket("status")
    users_id_recipient = FirstAccessDescriptor_Ticket("users_id_recipient")
    requesttypes_id = FirstAccessDescriptor_Ticket("requesttypes_id")
    content = FirstAccessDescriptor_Ticket("content")
    urgency = FirstAccessDescriptor_Ticket("urgency")
    impact = FirstAccessDescriptor_Ticket("impact")
    priority = FirstAccessDescriptor_Ticket("priority")
    itilcategories_id = FirstAccessDescriptor_Ticket("itilcategories_id")
    type = FirstAccessDescriptor_Ticket("type")
    global_validation = FirstAccessDescriptor_Ticket("global_validation")
    slas_id_ttr = FirstAccessDescriptor_Ticket("slas_id_ttr")
    slas_id_tto = FirstAccessDescriptor_Ticket("slas_id_tto")
    slalevels_id_ttr = FirstAccessDescriptor_Ticket("slalevels_id_ttr")
    time_to_resolve = FirstAccessDescriptor_Ticket("time_to_resolve")
    time_to_own = FirstAccessDescriptor_Ticket("time_to_own")
    begin_waiting_date = FirstAccessDescriptor_Ticket("begin_waiting_date")
    sla_waiting_duration = FirstAccessDescriptor_Ticket("sla_waiting_duration")
    ola_waiting_duration = FirstAccessDescriptor_Ticket("ola_waiting_duration")
    olas_id_tto = FirstAccessDescriptor_Ticket("olas_id_tto")
    olas_id_ttr = FirstAccessDescriptor_Ticket("olas_id_ttr")
    olalevels_id_ttr = FirstAccessDescriptor_Ticket("olalevels_id_ttr")
    ola_tto_begin_date = FirstAccessDescriptor_Ticket("ola_tto_begin_date")
    ola_ttr_begin_date = FirstAccessDescriptor_Ticket("ola_ttr_begin_date")
    internal_time_to_resolve = FirstAccessDescriptor_Ticket("internal_time_to_resolve")
    internal_time_to_own = FirstAccessDescriptor_Ticket("internal_time_to_own")
    waiting_duration = FirstAccessDescriptor_Ticket("waiting_duration")
    close_delay_stat = FirstAccessDescriptor_Ticket("close_delay_stat")
    solve_delay_stat = FirstAccessDescriptor_Ticket("solve_delay_stat")
    takeintoaccount_delay_stat = FirstAccessDescriptor_Ticket("takeintoaccount_delay_stat")
    actiontime = FirstAccessDescriptor_Ticket("actiontime")
    is_deleted = FirstAccessDescriptor_Ticket("is_deleted")
    locations_id = FirstAccessDescriptor_Ticket("locations_id")
    validation_percent = FirstAccessDescriptor_Ticket("validation_percent")
    date_creation = FirstAccessDescriptor_Ticket("date_creation")


    def __init__(self):
        self.Ticket_Task = TicketTask()
        self.Ticket_User = Ticket_User()

    def ticket_body(self):
        self._id = 3741 # ID заявки
        self._entities_id = 0 # Номер организации к которой отновится заявка
        self._name = 'Заголовок' # Заголовок заявки
        self._date = '2025-01-23 15:15:55' # Дата заведения заявки
        self._closedate = None # Дата закрытия заявки
        self._solvedate = None # Дата решения заявки
        self._takeintoaccountdate = '2025-01-28 10:09:30' # Дата и время, когда заявка была принята к рассмотрению (взята в работу) техническим специалистом или командой
        self._date_mod = '2025-01-28 10:09:30' # Дата и время последнего изменения заявки
        self._users_id_lastupdater = 38 # ID пользователя, который последний изменил заявку
        self._status = 1 # Статус заявки
        self._users_id_recipient = 39 # Идентификатор пользователя (или группы пользователей) GLPI, которому назначена эта заявка на выполнение
        self._requesttypes_id = 1 # ID типа запроса
        self._content = '&#60;p&#62;dchgsfdhgdf&#60;/p&#62;' # Текст заявки
        self._urgency = 5 # Срочность заявки
        self._impact = 3 # Влияние заявки
        self._priority = 4 # Приоритет заявки
        self._itilcategories_id = 1 # ITIL категория
        self._type = 2 # Тип заявки (Запрос или инцидент)
        self._global_validation = 1 # Какая-то душная валидация
        self._slas_id_ttr = 2 # SLA_TTR
        self._slas_id_tto = 0 # SLA_TTO
        self._slalevels_id_ttr = 1 # Идентификатор уровня SLA (соглашения об уровне обслуживания), который применяется к заявке для расчета TTR (времени до решения проблемы)
        self._time_to_resolve = '2025-01-24 14:15:55' # Время для решения заявки по SLA
        self._time_to_own = None # Максимальное время (в секундах), в течение которого заявка должна быть принята в работу (рассмотрена) в соответствии с назначенным SLA
        self._begin_waiting_date = None # Дата и время, когда заявка была поставлена в состояние ожидания (например, когда требуется ответ от пользователя)
        self._sla_waiting_duration = 0 # Суммарное время (в секундах), в течение которого заявка находилась в состоянии ожидания в рамках SLA. Обычно исключается из времени, затраченного на решение.
        self._ola_waiting_duration = 0 # Суммарное время (в секундах), в течение которого заявка находилась в состоянии ожидания в рамках OLA. Обычно исключается из времени, затраченного на решение.
        self._olas_id_tto = 1 # OLA_TTO
        self._olas_id_ttr = 0 # OLA_TTR
        self._olalevels_id_ttr = 0 # Идентификатор уровня OLA (соглашения об уровне обслуживания), который применяется к заявке для расчета внутреннего времени до решения (TTR)
        self._ola_tto_begin_date = '2025-01-23 15:15:55' # Время добавление OLA_TTO
        self._ola_ttr_begin_date = None # Время добавление OLA_TTR
        self._internal_time_to_resolve = None # Максимальное время (в секундах), в течение которого заявка должна быть обработана внутренними ресурсами в соответствии с назначенным OLA
        self._internal_time_to_own = '2025-01-23 15:20:55' # Максимальное время (в секундах), в течение которого заявка должна быть принята в работу внутренними ресурсами в соответствии с назначенным OLA
        self._waiting_duration = 0 # Суммарное время (в секундах), в течение которого заявка находилась в состоянии ожидания (независимо от того, связано ли это с SLA или OLA)
        self._close_delay_stat = 0 # Задержка в секундах между фактической датой закрытия заявки и ожидаемой датой закрытия, рассчитанной на основе SLA или OLA
        self._solve_delay_stat = 0 # Задержка в секундах между фактической датой решения (например, когда проблема была устранена) и ожидаемой датой решения, рассчитанной на основе SLA или OLA
        self._takeintoaccount_delay_stat = 78815
        self._actiontime = 0 # Общее время (в секундах), затраченное на выполнение каких-либо действий, связанных с заявкой (например, работа специалиста над заявкой)
        self._is_deleted = 0 # Логический флаг, указывающий, удалена ли заявка
        self._locations_id = 0 # Идентификатор местоположения (location), связанного с заявкой
        self._validation_percent = 0 # Идентификатор местоположения (location), связанного с заявкой
        self._date_creation = '2025-01-23 15:15:55' # Дата и время создания заявки

    def ticketUPD_status(self,status:int):
        """
        Принимает значение int
        1 - Новая
        2 - В работе назначена
        3 - В работе (запланирована)
        4 - в Ожидании (В разработке)
        5 - Решена
        6 - Закрыто
        """
        pass