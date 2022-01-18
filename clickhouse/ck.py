# coding: utf-8
#!/usr/bin/python

from clickhouse_driver import Client

if __name__ == "__main__":
    client=Client(host="***", database="***", user="***", password="***", settings={'max_threads': 2, 'priority': 10})
    rs = client.execute("select count(1),creator_company_name from workflow where dt = '2021-06-10' and create_year = 2021 and create_month = 6 group by creator_company_name")
    print(rs)
