# Scripts for the Demo


To get into the shell

```shell
docker exec -it yb-tserver-n1 /bin/bash
```

DDL script
```
curl https://raw.githubusercontent.com/yugabyte/yugabyte-db/master/sample/northwind_ddl.sql | ./bin/ysqlsh 
```

Data Insertion
```
curl https://raw.githubusercontent.com/yugabyte/yugabyte-db/master/sample/northwind_data.sql | ./bin/ysqlsh 
```


