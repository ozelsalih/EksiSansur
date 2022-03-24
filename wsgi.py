from app.app import app, scheduler
from tools import database_maker

if __name__ == "__main__":
    @scheduler.task('cron', id='update_database', hour=23, minute=50)
    def updade_database():
        database_maker.create_database()
        
    scheduler.start()
    app.run()