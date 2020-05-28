#The main run method to launch our app on the CLI
from app import create_app

if __name__ == '__main__':
	the_app =  create_app('development', 'my_app')
	the_app.run()
