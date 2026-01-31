# DB Integration Agent - MSSQL Database Connection Guide

**Name:** db_integration_agent  
**Description:** Expert guide for connecting VS Code and GitHub Copilot to MSSQL databases

## Overview

This guide provides comprehensive instructions for AI agents on how to establish connections between Visual Studio Code (VS Code) and MSSQL databases, enabling GitHub Copilot to interact with database systems. The integration supports both manual SQL queries and programmatic Python-based database access.

## CRITICAL: Prerequisites and Requirements

⚠️ **IMPORTANT: Verify these requirements before attempting any database connection!**

### 1. Required VS Code Extensions
**MUST HAVE:**
```
SQL Server (mssql) - ms-mssql.mssql
```

**Installation verification:**
- MSSQL icon should appear in Activity Bar (left sidebar)
- Command Palette should have "MSSQL:" commands available
- GitHub Copilot can access MSSQL-specific tools

### 2. Required Python Packages
**For programmatic database access:**
```txt
pyodbc>=5.0.0
sqlalchemy>=2.0.0
```

**Installation command:**
```powershell
pip install pyodbc sqlalchemy
```

### 3. Required System Components
**ODBC Driver for SQL Server:**
- Minimum version: ODBC Driver 17 for SQL Server
- Download: https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server
- Verify installation: Check Windows ODBC Data Sources (64-bit)

### 4. Network and Server Requirements
**MUST VERIFY:**
- SQL Server is running and accessible
- TCP/IP protocol is enabled in SQL Server Configuration Manager
- Windows Firewall allows SQL Server connections (default port 1433)
- You have proper authentication credentials (Windows or SQL Auth)

## Connection Methods

There are TWO primary methods to connect VS Code to MSSQL databases:

### Method 1: VS Code MSSQL Extension (Recommended for Copilot)

**Why this method?**
- Native integration with GitHub Copilot
- Copilot can directly use MSSQL tools (mssql_connect, mssql_run_query, etc.)
- Visual Object Explorer for schema browsing
- T-SQL IntelliSense support

**Step-by-Step Connection Process:**

#### Step 1: Open Connection Dialog
```
1. Click SQL Server icon in Activity Bar (left sidebar)
2. Click "Add Connection" button (+ icon)
   OR
   Command Palette (Ctrl+Shift+P) → "MSSQL: Connect"
```

#### Step 2: Enter Connection Details
**Required Information:**
- **Server name:** e.g., `SERVER2022`, `localhost`, `192.168.1.100`
- **Authentication Type:** Choose one:
  - `Integrated` - Windows Authentication (no username/password needed)
  - `SQL Login` - SQL Server Authentication (requires username/password)
  - `Azure Active Directory` - For Azure SQL databases

**Example Configuration:**
```
Server name: SERVER2022
Authentication Type: Integrated (Windows Authentication)
Database: master (or leave empty for default)
Connection name: SERVER2022-Local (optional friendly name)
```

#### Step 3: Save and Test Connection
- Connection appears in CONNECTIONS panel
- Expand connection to see databases
- Right-click → "New Query" to test

**Test Query:**
```sql
-- Verify connection
SELECT @@VERSION AS ServerVersion;
SELECT @@SERVERNAME AS ServerName;
SELECT GETDATE() AS ServerTime;

-- List all databases
SELECT name AS DatabaseName
FROM sys.databases
ORDER BY name;
```

### Method 2: Python with pyodbc (Programmatic Access)

**Why this method?**
- Programmatic data manipulation
- Integration with Python applications
- Batch processing and automation
- Data export and transformation

**Connection String Components:**

```python
import pyodbc

# Basic structure
server = 'SERVER2022'          # Server name or IP
database = 'master'            # Database name (optional)
driver = '{ODBC Driver 17 for SQL Server}'

# Windows Authentication
connection_string = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'Database={database};'
    f'Trusted_Connection=yes;'  # Windows Auth
)

# SQL Server Authentication
connection_string = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'Database={database};'
    f'UID=username;'            # SQL username
    f'PWD=password;'            # SQL password
)
```

**Complete Connection Example:**

```python
"""
MSSQL Connection Test Script
"""
import pyodbc
from datetime import datetime

def test_connection():
    """Test database connection and retrieve basic information"""
    
    # Connection parameters
    server = 'SERVER2022'
    driver = '{ODBC Driver 17 for SQL Server}'
    
    # Connection string (Windows Authentication)
    connection_string = (
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'Database=master;'
        f'Trusted_Connection=yes;'
    )
    
    try:
        # Establish connection
        print("Connecting to database...")
        conn = pyodbc.connect(connection_string, timeout=5)
        cursor = conn.cursor()
        print("✓ Connection successful!")
        
        # Test 1: Get SQL Server version
        cursor.execute("SELECT @@VERSION AS Version")
        version = cursor.fetchone()[0]
        print(f"SQL Server Version: {version.split(chr(10))[0]}")
        
        # Test 2: Get current server time and database
        cursor.execute("SELECT GETDATE() AS ServerTime, DB_NAME() AS CurrentDB")
        row = cursor.fetchone()
        print(f"Server Time: {row[0]}")
        print(f"Current Database: {row[1]}")
        
        # Test 3: List available databases
        cursor.execute("""
            SELECT name, database_id, create_date 
            FROM sys.databases 
            ORDER BY name
        """)
        
        print("\nAvailable Databases:")
        databases = cursor.fetchall()
        for db in databases:
            print(f"  • {db[0]} (ID: {db[1]}, Created: {db[2].strftime('%Y-%m-%d')})")
        
        # Close connection
        cursor.close()
        conn.close()
        
        return True
        
    except pyodbc.Error as e:
        print(f"✗ Database Error: {str(e)}")
        return False
    
    except Exception as e:
        print(f"✗ Unexpected Error: {str(e)}")
        return False

# Run the test
if __name__ == "__main__":
    test_connection()
```

## GitHub Copilot MSSQL Tools

When GitHub Copilot has access to a connected database, it can use these native tools:

### Available Copilot Database Tools

#### 1. Connection Management
```
mssql_list_servers()        - List all available SQL Server instances
mssql_connect()             - Establish connection to server/database
mssql_disconnect()          - Close database connection
mssql_get_connection_details() - Get info about active connection
mssql_change_database()     - Switch to different database
```

#### 2. Schema Exploration
```
mssql_list_databases()      - List all databases on server
mssql_list_tables()         - List all tables in current database
mssql_list_views()          - List all views
mssql_list_functions()      - List all functions
mssql_list_schemas()        - List all schemas
mssql_show_schema()         - Open visual schema designer
```

#### 3. Query Execution
```
mssql_run_query()           - Execute SQL query and return results
```

### Using Copilot Tools: Example Workflow

**Example 1: Connect and query database**
```
User: "Connect to SERVER2022 and show me all databases"

Copilot will:
1. Call mssql_list_servers() to verify SERVER2022 exists
2. Call mssql_connect(serverName="SERVER2022")
3. Call mssql_list_databases(connectionId="<returned-id>")
4. Present formatted list of databases
```

**Example 2: Query specific data**
```
User: "Show me the top 10 rows from the Users table"

Copilot will:
1. Use existing connection or establish new one
2. Call mssql_run_query(
     connectionId="<id>",
     query="SELECT TOP 10 * FROM Users",
     queryTypes=["SELECT"],
     queryIntent="data_exploration"
   )
3. Format and display results
```

### Important: Query Parameters

When using `mssql_run_query()`, you MUST provide:

**queryTypes** - Array of SQL operation types:
```
SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP,
TRUNCATE, MERGE, JOIN, CTE, STORED_PROCEDURE, FUNCTION,
VIEW, INDEX, TRANSACTION, GRANT, REVOKE, BACKUP, RESTORE,
EXEC, DECLARE, IF, WHILE, TRY_CATCH, TEMP_TABLE, 
CONSTRAINT, TRIGGER, SET, OTHER
```

**queryIntent** - Primary use case:
```
data_exploration      - Browsing/viewing data
data_analysis         - Analyzing patterns
data_migration        - Moving data
troubleshooting       - Debugging issues
schema_creation       - Creating objects
schema_modification   - Altering objects
schema_exploration    - Understanding structure
data_maintenance      - Updates/deletes
data_seeding          - Inserting test data
testing_validation    - Running tests
backup_restore        - Backup operations
performance_tuning    - Optimization
learning_education    - Educational purposes
other                 - Other scenarios
```

## Common Use Cases and Patterns

### Use Case 1: Initial Database Exploration

**Goal:** Understand database structure and content

```sql
-- 1. Get server information
SELECT @@VERSION AS Version, @@SERVERNAME AS ServerName;

-- 2. List all databases with sizes
SELECT 
    name AS DatabaseName,
    state_desc AS State,
    recovery_model_desc AS RecoveryModel,
    create_date AS Created
FROM sys.databases
ORDER BY name;

-- 3. Explore specific database schema
USE YourDatabaseName;
GO

-- List all tables
SELECT 
    SCHEMA_NAME(schema_id) AS SchemaName,
    name AS TableName,
    create_date AS Created
FROM sys.tables
ORDER BY SchemaName, TableName;

-- Get table row counts
SELECT 
    OBJECT_NAME(object_id) AS TableName,
    SUM(rows) AS RowCount
FROM sys.partitions
WHERE index_id IN (0,1)
GROUP BY object_id
ORDER BY RowCount DESC;

-- Get column information for a table
SELECT 
    c.name AS ColumnName,
    t.name AS DataType,
    c.max_length AS MaxLength,
    c.is_nullable AS IsNullable,
    c.is_identity AS IsIdentity
FROM sys.columns c
JOIN sys.types t ON c.user_type_id = t.user_type_id
WHERE object_id = OBJECT_ID('YourTableName')
ORDER BY c.column_id;
```

### Use Case 2: Python Data Analysis Integration

**Goal:** Extract data for Python processing

```python
import pyodbc
import pandas as pd

def get_data_as_dataframe(query):
    """Execute query and return results as pandas DataFrame"""
    
    server = 'SERVER2022'
    database = 'YourDatabase'
    driver = '{ODBC Driver 17 for SQL Server}'
    
    connection_string = (
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'Database={database};'
        f'Trusted_Connection=yes;'
    )
    
    try:
        # Connect and execute
        conn = pyodbc.connect(connection_string)
        df = pd.read_sql(query, conn)
        conn.close()
        
        return df
        
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
query = """
    SELECT 
        CustomerID,
        CustomerName,
        TotalOrders,
        TotalRevenue
    FROM CustomerSummary
    WHERE TotalRevenue > 10000
    ORDER BY TotalRevenue DESC
"""

df = get_data_as_dataframe(query)
if df is not None:
    print(f"Retrieved {len(df)} rows")
    print(df.head())
```

### Use Case 3: Safe Data Modification

**Goal:** Update data with transaction safety

```python
def safe_update(update_query, rollback_on_error=True):
    """Execute update with transaction control"""
    
    server = 'SERVER2022'
    database = 'YourDatabase'
    driver = '{ODBC Driver 17 for SQL Server}'
    
    connection_string = (
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'Database={database};'
        f'Trusted_Connection=yes;'
    )
    
    try:
        conn = pyodbc.connect(connection_string)
        conn.autocommit = False  # Enable manual transaction control
        cursor = conn.cursor()
        
        # Execute update
        cursor.execute(update_query)
        affected_rows = cursor.rowcount
        
        # Commit if successful
        conn.commit()
        print(f"✓ Successfully updated {affected_rows} rows")
        
        cursor.close()
        conn.close()
        
        return True, affected_rows
        
    except Exception as e:
        if rollback_on_error:
            conn.rollback()
            print(f"✗ Error occurred, changes rolled back: {e}")
        else:
            print(f"✗ Error occurred: {e}")
        
        return False, 0

# Example usage
update_query = """
    UPDATE Products
    SET Price = Price * 1.05
    WHERE CategoryID = 3
    AND Price < 100
"""

success, rows = safe_update(update_query)
```

## Troubleshooting Guide

### Issue 1: "Cannot find ODBC Driver"

**Error:**
```
pyodbc.Error: ('01000', "[01000] [Microsoft][ODBC Driver Manager] 
Data source name not found and no default driver specified")
```

**Solutions:**
1. **Install ODBC Driver 17:**
   - Download from Microsoft: https://aka.ms/downloadmsodbcsql
   - Install with default options
   - Restart VS Code after installation

2. **Verify installed drivers:**
   ```powershell
   # PowerShell command
   Get-OdbcDriver | Where-Object {$_.Name -like "*SQL Server*"} | Select-Object Name, Platform
   ```

3. **Use correct driver name in connection string:**
   ```python
   # Try different driver versions
   '{ODBC Driver 17 for SQL Server}'  # Preferred
   '{ODBC Driver 13 for SQL Server}'
   '{SQL Server Native Client 11.0}'
   '{SQL Server}'  # Last resort, not recommended
   ```

### Issue 2: "Login failed" / Authentication Error

**Error:**
```
pyodbc.Error: ('28000', '[28000] [Microsoft][ODBC Driver 17 for SQL Server]
[SQL Server]Login failed for user...')
```

**Solutions:**
1. **For Windows Authentication:**
   ```python
   # Ensure Trusted_Connection=yes is set
   connection_string = (
       f'DRIVER={driver};'
       f'SERVER={server};'
       f'Trusted_Connection=yes;'  # Required for Windows Auth
   )
   ```

2. **For SQL Server Authentication:**
   ```python
   # Provide username and password
   connection_string = (
       f'DRIVER={driver};'
       f'SERVER={server};'
       f'Database={database};'
       f'UID=sa;'  # Username
       f'PWD=YourPassword;'  # Password
   )
   ```

3. **Check SQL Server Authentication Mode:**
   - Open SQL Server Management Studio (SSMS)
   - Right-click server → Properties → Security
   - Ensure "SQL Server and Windows Authentication mode" is enabled
   - Restart SQL Server service after changing

### Issue 3: "Server not found" / Network Error

**Error:**
```
pyodbc.Error: ('08001', '[08001] [Microsoft][ODBC Driver 17 for SQL Server]
Named Pipes Provider: Could not open a connection to SQL Server')
```

**Solutions:**
1. **Verify SQL Server is running:**
   ```powershell
   # Check SQL Server service status
   Get-Service -DisplayName "*SQL Server*"
   
   # Start SQL Server if stopped
   Start-Service MSSQLSERVER  # Replace with your instance name
   ```

2. **Enable TCP/IP protocol:**
   - Open SQL Server Configuration Manager
   - SQL Server Network Configuration → Protocols for [Instance]
   - Right-click TCP/IP → Enable
   - Restart SQL Server service

3. **Check Windows Firewall:**
   ```powershell
   # Add firewall rule for SQL Server (port 1433)
   New-NetFirewallRule -DisplayName "SQL Server" -Direction Inbound -Protocol TCP -LocalPort 1433 -Action Allow
   ```

4. **Test network connectivity:**
   ```powershell
   # Test if port is open
   Test-NetConnection -ComputerName SERVER2022 -Port 1433
   ```

### Issue 4: VS Code Extension Not Showing Databases

**Symptoms:**
- Connection appears successful
- But no databases shown in Object Explorer
- Cannot expand connection tree

**Solutions:**
1. **Refresh connection:**
   - Right-click connection → Refresh
   - OR disconnect and reconnect

2. **Check user permissions:**
   ```sql
   -- Verify your user has VIEW ANY DATABASE permission
   SELECT HAS_PERMS_BY_NAME(NULL, NULL, 'VIEW ANY DATABASE');
   -- Should return 1
   
   -- Grant permission if needed (requires admin)
   GRANT VIEW ANY DATABASE TO [YourUser];
   ```

3. **Manually specify database:**
   - Edit connection
   - Enter specific database name instead of leaving blank
   - Save and reconnect

### Issue 5: Timeout Errors

**Error:**
```
pyodbc.Error: ('HYT00', '[HYT00] [Microsoft][ODBC Driver 17 for SQL Server]
Login timeout expired')
```

**Solutions:**
1. **Increase connection timeout:**
   ```python
   conn = pyodbc.connect(connection_string, timeout=30)  # 30 seconds
   ```

2. **Increase query timeout:**
   ```python
   cursor = conn.cursor()
   cursor.execute("SET LOCK_TIMEOUT 60000")  # 60 seconds
   ```

3. **Check network latency:**
   ```powershell
   # Test network delay
   Test-Connection -ComputerName SERVER2022 -Count 4
   ```

## Security Best Practices

### 1. Never Hardcode Credentials

**❌ WRONG - Hardcoded credentials:**
```python
connection_string = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'UID=sa;'
    f'PWD=MyPassword123;'  # NEVER DO THIS!
)
```

**✅ CORRECT - Use environment variables:**
```python
import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

connection_string = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'UID={os.getenv("SQL_USERNAME")};'
    f'PWD={os.getenv("SQL_PASSWORD")};'
)
```

**.env file (add to .gitignore!):**
```env
SQL_USERNAME=your_username
SQL_PASSWORD=your_password
SQL_SERVER=SERVER2022
SQL_DATABASE=YourDatabase
```

### 2. Use Windows Authentication When Possible

Windows Authentication is more secure than SQL Server Authentication:
- No password in connection string
- Integrated with Windows security
- Supports Kerberos and NTLM
- Easier credential management

```python
# Preferred: Windows Authentication
connection_string = f'DRIVER={driver};SERVER={server};Trusted_Connection=yes;'
```

### 3. Limit Database Permissions

Grant only necessary permissions to database users:
```sql
-- Create read-only user
CREATE LOGIN ReadOnlyUser WITH PASSWORD = 'StrongPassword123!';
CREATE USER ReadOnlyUser FOR LOGIN ReadOnlyUser;
GRANT SELECT ON SCHEMA::dbo TO ReadOnlyUser;

-- Create data entry user (no delete)
CREATE LOGIN DataEntryUser WITH PASSWORD = 'StrongPassword456!';
CREATE USER DataEntryUser FOR LOGIN DataEntryUser;
GRANT SELECT, INSERT, UPDATE ON SCHEMA::dbo TO DataEntryUser;
```

### 4. Use Parameterized Queries

**❌ WRONG - SQL Injection vulnerable:**
```python
customer_id = input("Enter customer ID: ")
query = f"SELECT * FROM Customers WHERE CustomerID = {customer_id}"
cursor.execute(query)  # DANGEROUS!
```

**✅ CORRECT - Parameterized query:**
```python
customer_id = input("Enter customer ID: ")
query = "SELECT * FROM Customers WHERE CustomerID = ?"
cursor.execute(query, (customer_id,))  # SAFE
```

### 5. Encrypt Connection

For sensitive data, always use encrypted connections:
```python
connection_string = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'Database={database};'
    f'Trusted_Connection=yes;'
    f'Encrypt=yes;'  # Force encryption
    f'TrustServerCertificate=no;'  # Validate certificate
)
```

## Testing Checklist

Before considering database integration complete, verify:

### Basic Connection Tests
- [ ] VS Code MSSQL Extension is installed
- [ ] Connection appears in CONNECTIONS panel
- [ ] Can expand connection to see databases
- [ ] Can execute simple `SELECT @@VERSION` query
- [ ] GitHub Copilot can access mssql_* tools

### Python Integration Tests
- [ ] `pyodbc` and `sqlalchemy` are installed
- [ ] ODBC Driver 17 is installed and detected
- [ ] Python script can connect successfully
- [ ] Can retrieve data and print results
- [ ] Can handle connection errors gracefully

### Copilot Interaction Tests
- [ ] Copilot can list available servers
- [ ] Copilot can connect to specified server
- [ ] Copilot can execute queries via mssql_run_query()
- [ ] Copilot can explore schema structure
- [ ] T-SQL IntelliSense works in .sql files

### Security Tests
- [ ] No credentials hardcoded in source files
- [ ] .env file is in .gitignore
- [ ] Using least-privilege database accounts
- [ ] Parameterized queries are used
- [ ] Connection encryption is enabled (if required)

## Quick Reference: Connection Strings

### Template Collection

```python
# Windows Authentication (Local Server)
f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};Trusted_Connection=yes;'

# Windows Authentication (Specific Database)
f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};Database={database};Trusted_Connection=yes;'

# SQL Server Authentication
f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};Database={database};UID={username};PWD={password};'

# With Encryption
f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};Database={database};Trusted_Connection=yes;Encrypt=yes;TrustServerCertificate=no;'

# Azure SQL Database
f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server}.database.windows.net;Database={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;'

# Named Instance
f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server}\\{instance};Database={database};Trusted_Connection=yes;'

# IP Address with Port
f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={ip_address},{port};Database={database};Trusted_Connection=yes;'
```

## Resources and Documentation

### Official Documentation
- **MSSQL Extension:** https://marketplace.visualstudio.com/items?itemName=ms-mssql.mssql
- **pyodbc Documentation:** https://github.com/mkleehammer/pyodbc/wiki
- **SQLAlchemy for MSSQL:** https://docs.sqlalchemy.org/en/14/dialects/mssql.html
- **ODBC Driver Download:** https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server

### Useful SQL Server Queries
- **System Information:** `SELECT @@VERSION, @@SERVERNAME, SERVERPROPERTY('ProductVersion')`
- **List Databases:** `SELECT name FROM sys.databases`
- **List Tables:** `SELECT name FROM sys.tables`
- **Table Row Counts:** `SELECT OBJECT_NAME(object_id), SUM(rows) FROM sys.partitions WHERE index_id IN (0,1) GROUP BY object_id`
- **Database Size:** `SELECT DB_NAME(database_id), SUM(size * 8.0 / 1024) AS SizeMB FROM sys.master_files GROUP BY database_id`

## Instructions for AI Agents

When helping users establish MSSQL database connections:

1. **Verify prerequisites first** - Check extensions, drivers, and packages before attempting connection
2. **Choose appropriate method** - VS Code Extension for Copilot integration, Python for programmatic access
3. **Guide through connection setup** - Provide step-by-step instructions with clear parameters
4. **Test connection immediately** - Run simple queries to verify connectivity
5. **Handle errors gracefully** - Provide specific troubleshooting steps based on error messages
6. **Consider security** - Always recommend secure practices (no hardcoded credentials, parameterized queries)
7. **Document the configuration** - Help users document their working setup for future reference

### ⚠️ CRITICAL CHECKLIST - Always verify:

- [ ] **MSSQL Extension**: Installed and visible in Activity Bar
- [ ] **ODBC Driver**: Version 17 or higher is installed
- [ ] **Server Access**: SQL Server is running and accessible
- [ ] **Authentication**: Correct method chosen (Windows vs SQL Auth)
- [ ] **Network**: TCP/IP enabled, firewall allows connections
- [ ] **Permissions**: User has appropriate database permissions
- [ ] **Python Packages**: pyodbc and sqlalchemy installed if using Python
- [ ] **Test Query**: Connection verified with simple SELECT statement

### Common Workflow Pattern:

```
1. User requests database connection
   ↓
2. Agent checks prerequisites (extensions, drivers, etc.)
   ↓
3. Agent uses mssql_list_servers() to find available servers
   ↓
4. Agent calls mssql_connect() with appropriate parameters
   ↓
5. Agent tests connection with mssql_run_query("SELECT @@VERSION")
   ↓
6. Agent explores schema with mssql_list_databases(), mssql_list_tables()
   ↓
7. Agent performs requested database operations
   ↓
8. Agent provides summary and next steps
```

### Error Handling Strategy:

```python
# Always wrap database operations in try-except blocks
try:
    # Attempt connection
    conn = pyodbc.connect(connection_string, timeout=5)
    
except pyodbc.Error as db_error:
    # Database-specific error
    # Analyze error code and provide specific solution
    
except Exception as general_error:
    # Unexpected error
    # Log and provide general troubleshooting steps
    
finally:
    # Always clean up resources
    if 'conn' in locals():
        conn.close()
```

## Version Information

**Document Version:** 1.0  
**Last Updated:** November 2025  
**Tested With:**
- Visual Studio Code 1.90+
- MSSQL Extension (ms-mssql.mssql)
- Python 3.8+
- pyodbc 5.0+
- SQLAlchemy 2.0+
- ODBC Driver 17 for SQL Server
- SQL Server 2019+
- Windows 10/11

**Note:** Procedures may vary slightly with different versions. Always refer to official documentation for version-specific features.
