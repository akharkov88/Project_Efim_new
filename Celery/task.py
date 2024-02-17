from test import celery_app

# To be processed asynchronous task 1
@celery_app.task
def filter_befor_save():
    '''
         The final filtration is performed before the data is collected.
    '''
    print('Execute Filter_Befor_Save')
    return 1+1