import pymysql
from bottle import route, request, run, template

db = pymysql.connect('mysqllzy', 'root', 'woaini123', 'lzy')
cursor = db.cursor()
cursor.execute('''
create table if not exists user(
    name varchar(255),
    password varchar(20),
    age int(2) default 20
);
''')


@route('/sqla')
def login_form():
    return template('form_mysql')


@route('/sqla', method='POST')
def login():
    name = request.forms.get('username')
    passwd = request.forms.get('password')
    cursor.execute("insert into user (name, password) values ('%s', '%s')" % (name, passwd))
    db.commit()


@route('/sqlq')
def dispaly_user():
    name = request.query.name
    debug = request.query.debug
    sql = "select * from user where name='%s'" % (name,)
    cursor.execute(sql)
    values = cursor.fetchall()

    if debug == '1':
        return template('用户信息：{{values}} <br /> 执行的 SQL 语句：{{sql}}', values=values, sql=sql)
    else:
        return str(values)


@route('/sqlu')
def update():
    name = request.query.name
    age = int(request.query.age)
    cursor.execute("update user set age='%s' where name='%s'" % (age, name))
    db.commit()

    cursor.execute('select * from user')
    values = cursor.fetchall()
    for v in values:
        print('查询结果：', v)


@route('/sqld')
def delete():
    age = int(request.query.age)
    cursor.execute("delete from user where age='%s'" % (age,))
    db.commit()

    cursor.execute('select * from user')
    values = cursor.fetchall()
    for v in values:
        print('查询结果：', v)

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)