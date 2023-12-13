<h1>0x0D. SQL - Introduction</h1>

<h2>Concepts</h2>
<p><em>For this project, we expect you to look at these concepts:</em></p>
<ul>
    <li><a href="https://intranet.alxswe.com/concepts/37" target="_blank">Databases</a></li>
</ul>

![alt-text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg)

<h2>Resources</h2>
<ul>
    <li><a href="https://intranet.alxswe.com/rltoken/yyRKTEdRkYEVlRgZPbasjw" target="_blank">What is Database & SQL?</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/sV2PtK5YfQsXWW1malRZ5Q" target="_blank">A Basic MySQL Tutorial</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/IUKo4-UaRZSKPvXr5u9oBw" target="_blank">Basic SQL statements: DDL and DML <em>(no need to read the chapter “Privileges”)</em></a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/rXKvu2u7vg1Hj6bnX7UgMg" target="_blank">Basic queries: SQL and RA</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/-Riv_dzSYsJyvy-LlaO6Mg" target="_blank">SQL technique: functions</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/QpIXoR--8eBIaidgSWYsBQ" target="_blank">SQL technique: subqueries</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/Gt0nFJPJRwW2Y0izzwbVrw" target="_blank">What makes the big difference between a backtick and an apostrophe?</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/1oU1LwCksQLXjs6fZYezrw" target="_blank">MySQL Cheat Sheet</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/HmdmLiYBM0Q34iCYPWd9XQ" target="_blank">MySQL 8.0 SQL Statement Syntax</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/IpYI9rgbwfjxOAQQgpHCmQ" target="_blank">installing MySQL in Ubuntu 20.04</a></li>
</ul>

<h2>Learning Objectives</h2>
<ul>
    <li>What's a database</li>
    <li>What's a relational database</li>
    <li>What does SQL stand for</li>
    <li>What's MySQL</li>
    <li>How to create a database in MySQL</li>
    <li>What does <code>DDL</code> and <code>DML</code> stand for</li>
    <li>How to <code>CREATE</code> or <code>ALTER</code> a table</li>
    <li>How to <code>SELECT</code> data from a table</li>
    <li>How to <code>INSERT</code>, <code>UPDATE</code> or <code>DELETE</code> data</li>
    <li>What are <code>subqueries</code></li>
    <li>How to use MySQL functions</li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
    <li>All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)</li>
    <li>All your files should end with a new line</li>
    <li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
    <li>All your files should start by a comment describing the task</li>
    <li>All SQL keywords should be in uppercase (SELECT, WHERE…)</li>
    <li>A README.md file, at the root of the folder of the project, is mandatory</li>
    <li>The length of your files will be tested using wc</li>
</ul>

<h2>More Info</h2>
<h3>Comments for your SQL file:</h3>

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

<h3>Install MySQL 8.0 on Ubuntu 20.04 LTS</h3>
```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

<p>Connect to your MySQL server:</p>

```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

<h3>Use "container-on-demand" to run MySQL</h3>
<p><strong>In the container, credentials are</strong> <code>root/root</code></p>
<ul>
    <li>Ask for container <code>Ubuntu 20.04</code></li>
    <li>Connect via SSH</li>
    <li>OR connect via the Web terminal</li>
    <li>In the container, you should start MySQL before playing with it:</li>
</ul>

```
$ service mysql start
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema  
sys       
$
```
<p><strong>In the container, credentials are</strong> <code>root/root</code></p>