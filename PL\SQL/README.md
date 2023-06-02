# Primay Key valditation

This project focuses on generating a check table that stores important information about table names, primary key columns, and their data types. It also includes functionality to clean the check table by removing primary keys that are not of integer type. Additionally, trigger sequences are created for the remaining tables based on their primary key columns.

The code demonstrates the use of cursors to iterate over query results and perform necessary updates and actions. It also utilizes dynamic SQL (`EXECUTE IMMEDIATE`) to handle tasks such as dropping existing sequences and creating new sequences based on maximum values of primary key columns.

By executing this code, you will be able to create a comprehensive check table that provides valuable insights into the primary key columns within your specified schema. This information can be used for further analysis or validation of your data model.


