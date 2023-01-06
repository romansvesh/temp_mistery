class ServiceMeta(type):
    def __init__(cls, name, bases, members):
        super().__init__(name, bases, members)
        print(f'\nClassName: {name},\n Bases: {bases},\n Members: {members}\n\n')
        print('init ServiceMeta')


print('create Service')
Service = ServiceMeta('base', tuple(), {})
