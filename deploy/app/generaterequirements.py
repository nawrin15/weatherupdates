import sys
djangoRestFramework="djangorestframework==3.11.1"
psycopg2="psycopg2-binary==2.8.3"
watchdog="watchdog==0.8.3"
celery="celery==5.0.2"
redis="redis==3.5.3"
corsheaders='django-cors-headers'
requests='requests==2.25.1'
gevent='gevent==21.1.2'
click='click==7.1.1'

requirements = [
	djangoRestFramework,
	watchdog,
	celery,
	redis,
	corsheaders,
	requests,
	gevent,
	click,
	psycopg2
]

def getRequirement():
	print(*requirements, sep='\n')

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("No environment given for requirement.txt!")
		sys.exit(-1)
	env = sys.argv[1]

	if env == 'localdev':
		getRequirement()
	elif env == 'localstage':
		requirements.append(gunicorn)
		getRequirement()
	else:
		print("Invalid environment given for requirement.txt!")
		sys.exit(-1)
