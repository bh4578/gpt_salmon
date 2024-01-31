**1.初始化数据库（demo并未连接数据库，此步跳过）**  
python manage.py makemigrations  
python manage.py migrate  
**2.修改setting配置文件，如static_root路径，allow_host等**  
**3.python manage.py collectstatic 生成静态文件**  
**4.配置nginx服务器，修改nginx.conf**  
如：  
	include /etc/nginx/sites-enabled/*;  
	    map $http_upgrade $connection_upgrade {  
        default upgrade;  
        '' close;  
    }  
	server{  
	listen 80;  
	server_name 110.41.48.238;  
	location /static/ {  
	    alias /var/web_static/;  
	}  
	location / {  
	proxy_pass http://localhost:8000;  
	            proxy_set_header Upgrade $http_upgrade;  
            proxy_set_header Connection $connection_upgrade;  
            proxy_set_header Host $host;  
            proxy_set_header X-Real-IP $remote_addr;  
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
            proxy_set_header X-Forwarded-Proto $scheme;  
	}  
	}  
}  
**5.运行daphne异步服务器 daphne -p 8000 -b 0.0.0.0 your_project_name.asgi:application**  
**6.运行nginx**  
**7.因为gpt需要境外网络访问，因此需要开启代理，这里是clash，如何配置clash可以百度**  
开启clash命令：nohup ./clash -f config.yaml  
  
__不懂的命令可以问chatgpt__  
  
demo示例地址：  
http://110.41.48.238/  
