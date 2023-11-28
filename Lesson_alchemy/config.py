from pydantic import BaseConfig


class Settings(BaseConfig):
    DB_host: str = '127.0.0.1'
    DB_port: int = 5432
    DB_user: str = "postgres"
    DB_pass: str = "postgres"
    DB_name: str = "efimov_db"

    # database_url: str= "sqlite:///database_lesson.sqlite3"

    @property
    def database_url_asyncpg(self):
        # return  f"postgresql+asyncpg://{self.DB_user}:{self.DB_pass}@{self.DB_host}:{self.DB_port}/{self.DB_name}"
        return  f"postgresql+asyncpg://{self.DB_user}:{self.DB_pass}@{self.DB_host}:{self.DB_port}/{self.DB_name}"

        # return self.database_url

    @property
    def database_url_psycopg(self):
        # postgresql+psycopg://postgres:postgres@localhost:5432/sa
        return  f"postgresql+psycopg://{self.DB_user}:{self.DB_pass}@{self.DB_host}:{self.DB_port}/{self.DB_name}"
        # return self.database_url
settings=Settings()


