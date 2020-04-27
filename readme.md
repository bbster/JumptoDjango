# Wikidocs Django clone coding
## 환경설정
```bash
verision
python == 3.8.1
Django==3.0.5
django-test-plus==1.4.0
flake8==3.7.9
ipython==7.13.0
mysqlclient==1.4.6
pytest-django==3.9.0
```
### Error 
```bash
 - mysql access denied user - 
try
    1. Database 다시생성, DB user 다시생성 - 해결안됨
    2. 프로젝트 재생성 - 해결안됨
    3. 포트 확인 / mysql - SHOW GLOBAL VARIABLES LIKE 'PORT'; - 해결됨
        - 장고 세팅에 3306port / mysql port 3307 - 에러발생
```
```bash

```