from django.db.models.signals import  pre_save,post_save


def pre_save_func(sender,**kwargs):
    print(sender)
    print(kwargs)
    print(kwargs.get('instance'))

pre_save.connect(pre_save_func)
