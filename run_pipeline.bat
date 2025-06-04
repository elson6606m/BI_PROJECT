@echo off
cd C:\Users\YourUsername\your_project_directory

REM Activate virtual environment (if using one)
call venv\Scripts\activate

REM Run Airbyte sync via API or CLI
echo Running Airbyte sync...
airbyte deploy
airbyte sync your_connection_id

REM Wait if needed (optional)
timeout /t 10

REM Run dbt transformation
echo Running dbt models...
dbt run

echo Pipeline completed.
pause
