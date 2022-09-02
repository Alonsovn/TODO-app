# TODO application
TODO app 

Install the virtualenv package  
pip install virtualenv

Upgrade pip  
pip install --upgrade pip 

Create virtual environment  
virtualenv dev

Activate  
Windows  
dev\Scripts\activate  

Mac OS / Linux  
source mypython/bin/activate  

Alembic 
To init / create alembic folder run this:  
alembic init <folder_name>  
`` alembic init alembic
``  

Create revision  
```alembic revision --autogenerate -m "First revision"``` 

Run latest version  
``alembic upgrade head``  

Upgrade specific version  
``alembic upgrade 66b1 ``   

Downgrade -1 version  
``alembic downgrade -1 ``  



