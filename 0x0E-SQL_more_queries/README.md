<h1>0x0E. SQL - More queries</h1>

![alt-text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg)

<h2>Resources</h2>
<p><strong>Read or watch:</strong></p>
<ul>
    <li><a href="https://intranet.alxswe.com/rltoken/RniBKj48bnIN8xpXhGl1yA" target="_blank">How To Create a New User and Grant Permissions in MySQL</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/FIiEIvA6IN_hSKM5TvgyxQ" target="_blank">How To Use MySQL GRANT Statement To Grant Privileges To a User</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/LrovGa6N-OE2ID_tpWZRaQ" target="_blank">MySQL constraints</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/kR71h5zjkPtx4kBoVf7q0g" target="_blank">SQL technique: subqueries</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/rNMJeQ1jbNTCljbvCSjf6w" target="_blank">Basic query operation: the join</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/HhZ6TJ1q5S0aR4lhfpKdOQ" target="_blank">SQL technique: multiple joins and the distinct keyword</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/T6FZUQdsMzr8hgNInBzudA" target="_blank">SQL technique: join types</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/Nd-sdM8QUpf0YKIlXzVv4w" target="_blank">SQL technique: union and minus</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/iSNyinU6SPWTGDUWMmcRkg" target="_blank">MySQL Cheat Sheet</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/-plhBsra0N7BOuFoEg--zg" target="_blank">The Seven Types of SQL Joins</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/I4Lws_eQrIrNTbkZvvk-oQ" target="_blank">MySQL Tutorial</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/051eAEP_rePBU7jeh879GA" target="_blank">SQL Style Guide</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/YavbYiraYFr8oTukT_N6eQ" target="_blank">MySQL 8.0 SQL Statement Syntax</a></li>
</ul>

<p>Extra resources around relational database model design:</p>
<ul>
    <li><a href="https://intranet.alxswe.com/rltoken/EWLRPeqr5sQ9AqfoG_KXxw" target="_blank">Design</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/mqBhYoSYbhH5ZZrhDcY0kA" target="_blank">Normalization</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/R0exkJmf-2ddKjGfa8D0dA" target="_blank">ER Modeling</a></li>
</ul>

<h2>Learning Objectives</h2>
<ul>
    <li>How to create a new MySQL user</li>
    <li>How to manage privileges for a user to a database or table</li>
    <li>What's a <code>PRIMARY KEY</code></li>
    <li>What's a <code>FOREIGN KEY</code></li>
    <li>How to use <code>NOT NULL</code> and <code>UNIQUE</code> constraints</li>
    <li>How to retrieve dats from multiple tables in one request</li>
    <li>What are subqueries</li>
    <li>What are <code>JOIN</code> and <code>UNION</code></li>
</ul>

<h2>More Info</h2>
<h3>How to import a SQL dump</h3>

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

<h2>Tasks :page_with_curl:</h2>
<h3>0. My privileges!</h3>
<p>Write a script that lists all privileges of the MySQL users <code>user_0d_1</code> and <code>user_0d_2</code> on your server (in <code>localhost</code>).</p>

<h3><strong>Files</strong></h3>
<p><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x0E-SQL_more_queries/0-privileges.sql" target="_blank">0-privileges.sql</a></p>

<hr>

<h3>1. Root user</h3>
<p>Write a script that creates the MySQL server user <code>user_0d_1</code>.</p>
<ul>
    <li><code>user_0d_1</code> should have all privileges on your MySQL server</li>
    <li>The <code>user_0d_1</code> password should be set to <code>user_0d_1_pwd</code></li>
    <li>If the user <code>user_0d_1</code> already exists, your script should not fail</li>
</ul>

<h3><strong>Files</strong></h3>
<p><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x0E-SQL_more_queries/1-create_user.sql" target="_blank">1-create_user.sql</a></p>

<hr>
