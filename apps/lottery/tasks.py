from celery.task import task

@task()
def print_hello():
	return 'hello celery and django'

def add():
	return 'test add'