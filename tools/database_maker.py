import sqlite3

from eksisozluk.EksiSozluk import EksiApi
from tqdm import tqdm

def create_database():
    client = EksiApi()

    con = sqlite3.connect("db/database.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS topics;")
    cur.execute("CREATE TABLE topics (id TEXT, title TEXT, created TEXT);")

    for i in tqdm(
        range(1, client.get_user_entries("ekşisözlük").user_entries.page_count + 1)
    ):
        for entry in client.get_user_entries("ekşisözlük", page=i).user_entries.entries:
            if "sulh ceza" in entry.entry.content:
        # This way of filtering is prone to false positives.
                topic_id = entry.topic_id.id
                topic_title = entry.topic_id.topic_title.title
                created = entry.entry.created
                cur.execute(
                    f'INSERT INTO topics VALUES ("{topic_id}","{topic_title}","{created}")'
                )

    con.commit()
    con.close()