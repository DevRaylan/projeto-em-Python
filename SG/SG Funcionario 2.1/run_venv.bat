@echo off
echo Activating virtual environment...
call venv\Scripts\activate
if "%VIRTUAL_ENV%"=="" (
    echo Virtual environment activation failed.
    pause
    exit /b 1
)
echo Virtual environment activated.
echo Current virtual environment: %VIRTUAL_ENV%

echo Installing required modules...
pip install tabulate
pip list

echo Running main script...
python main.py
echo Script execution completed.
pause
