import sqlite3
import MySQLdb
import yaml

with open('config.yaml') as conf_file:
    config = yaml.load(conf_file)

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

conn2 = MySQLdb.connect(
    db=config['database']['name'],
    user=config['database']['user'],
    passwd=config['database']['password'],
    port=3306,
    host=config['database']['host'],
    charset='utf8'
)
cursor2 = conn2.cursor()

get_blog_sql = 'select `id`,`title`,`content`,`create_time`,`summary` from blog_blog;'

insert_blog_sql = 'replace into blog(`id`,`title`,`content`,`create_time`,`summary`,`update_time`) values (%s,%s,%s,%s,%s,now());'

get_comments_sql = 'select `id`,`username`,`userimage`,`blog_id`,`content`,`create_time`,`parent_id`,`comment_id`,`comment_username` from blog_comments;'

insert_commets_sql = 'replace into comments(`id`,`username`,`userimage`,`blog_id`,`content`,`create_time`,`parent_id`,`comment_id`,`comment_username`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);'

get_user_sql = 'select `id`,`name`,`passwd`,`account`,`image` from blog_user;'

insert_user_sql = 'replace into user(`id`,`name`,`passwd`,`account`,`image`) values(%s,%s,%s,%s,%s);'

def get_sqlite_data(sql):
    cursor.execute(sql)
    datas = cursor.fetchall()
    return datas

def insert_mysql(sql, params):
    try:
        for param in params:
            cursor2.execute(sql, param)
        conn2.commit()
    except Exception as e:
        print(e)
        conn2.rollback()


if __name__ == "__main__":
    blog_datas = get_sqlite_data(get_blog_sql)
    insert_mysql(insert_blog_sql, blog_datas)

    comment_datas = get_sqlite_data(get_comments_sql)
    insert_mysql(insert_commets_sql, comment_datas)

    user_datas = get_sqlite_data(get_user_sql)
    insert_mysql(insert_user_sql, user_datas)

    print("success")





