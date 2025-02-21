from __future__ import annotations
class FirstAccessDescriptor_Ticket_User:
    Ticket_User_body = {}

    def __init__(self, attr_name):
        self.attr_name = attr_name
        print(self)
    def __get__(self, instance, owner):
        if instance is None:
            return self  # Поддержка доступа к атрибуту класса напрямую

        # Проверяем наличие флага для этого атрибута на экземпляре
        access_flag_name = f'_has_accessed_{self.attr_name}'
        if not hasattr(instance, access_flag_name):
            instance.flag = 'True'  # Устанавливаем флаг
            setattr(instance, access_flag_name, 'True')  # Задаем флаг для атрибута
            # if self.attr != None:
            # self.pakovchik()

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
        self.Ticket_User_body[self.attr_name] = value
        print('Slovarik Ticket_User = ',self.Ticket_User_body)

class Ticket_User:
    flag: str = 'False'
    id = FirstAccessDescriptor_Ticket_User("id")
    tickets_id = FirstAccessDescriptor_Ticket_User("tickets_id")
    users_id = FirstAccessDescriptor_Ticket_User("users_id")
    type = FirstAccessDescriptor_Ticket_User("type")
    use_notification = FirstAccessDescriptor_Ticket_User("use_notification")
    alternative_email = FirstAccessDescriptor_Ticket_User("alternative_email")


    def __init__(self):
        pass

    def Ticket_User_body(self,id):
        self.id = 15
        self.tickets_id = 3777
        self.users_id = 184
        self.type = 1 # 1 = иницатор, 2 - исполнитель
        self.use_notification = 0
        self.alternative_email = ''
# o = FirstAccessDescriptor_Ticket_User("ooo")
# o1 = FirstAccessDescriptor_Ticket_User("ooo")
# print(o.Ticket_User_body)
# o1.Ticket_User_body["ok"] = "ok"
# print(o.Ticket_User_body)
