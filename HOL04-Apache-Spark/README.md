# Introduction to Apache Spark

1. Create Azure Data Science VM - [steps](https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/dsvm-ubuntu-intro)


- [OPTIONAL] change the port of Jupypter from default `8000` to `443` (https) - see below

2. Navigate to Jupyter Notebook in newly created VM

3. import notebook `1. Introduction to Apache Spark (MMA).ipynb`

4. follow the steps in the notebook



## Jupyter - change port
1. Stop running service
	`sudo service jupyterhub stop`
2. Change config PORT to 443
	`cd /etc/jupyterhub/` 
	`sudo nano jupyterhub_config.py`
	
	Add manually line:
	`c.JupyterHub.port = 443`

3. Start JupyterHub service
	`sudo service jupyterhub start`
	
4. [Allow inbound port](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/nsg-quickstart-portal) 443 in VM!!!
