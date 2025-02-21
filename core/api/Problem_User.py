
class FirstAccessDescriptor_Problem_User:
    Problem_User_body = {}

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
        self.Problem_User_body[self.attr_name] = value
        print('Slovarik Problem_User = ',self.Problem_User_body)

class Problem_User:
    # flag: str = 'False'
    # id = FirstAccessDescriptor_Problem_User("id")
    # problems_id = FirstAccessDescriptor_Problem_User("problems_id")
    # users_id = FirstAccessDescriptor_Problem_User("users_id")
    # type = FirstAccessDescriptor_Problem_User("type")
    # use_notification = FirstAccessDescriptor_Problem_User("use_notification")
    # alternative_email = FirstAccessDescriptor_Problem_User("alternative_email")


    def __init__(self):
        pass

    def Problem_User_body(self,id):
        self.id : int
        self.problems_id : int
        self.users_id : int
        self.type : int # 1 = иницатор, 2 - исполнитель
        self.use_notification : int
        self.alternative_email : str