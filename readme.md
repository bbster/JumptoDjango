# 점프투장고 clone coding
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
-  didn't return an HttpResponse object. It returned None instead. -
try
    1. pybo/index 에 인덱스페이지에 대한 네임스페이스 지정해봄 - 해결안됨
    2. question_create 함수에서 return 값에 pybo/question_create.html 경로를 수정해봄 - 해결안됨
    3. 템플릿 경로 문제인가 싶어서 프로젝트 폴더에 있던 템플릿 폴더를 app폴더 내부로 옮겨봄 - 해결안됨
    4. post로 들어왔을때 return render(request, 'pybo/templates/question_list.html', context) 이렇게 바꿔봄 - 해결안됨
    5. if문 (POST방식 일때 / get방식 일때) 줄맞춤 문제 - 해결
```

### 정리
```bash
{{ form.as_p }}는 QuestionForm에 정의된 필드를 입력 폼으로 만들어 준다.

is_valid() / 값 유효성 검사
serializer, form에서 들어오는 값들에 대한 유효성 검사를 한다.

commit = False / 임시저장 
```
```python
def question_create(request):
    if request.method == "POST":  # request 메서드가 POST방식일때
        form = QuestionForm(request.POST)  # 폼 데이터를 post 방식으로 전달

        if form.is_valid():  # 폼데이터의 유효성 검사
            question = form.save(commit=False)  # 폼데이터 임시저장
            question.create_date = timezone.now() # 폼데이터 + 현재 시간정보 저장
            question.save() # DB에 저장
            return redirect('pybo:index') # 리다이렉트로 리스트 페이지로 반환

    else:
        form = QuestionForm()  # 입력폼 출력 / forms에 정의된 형태로
    context = {'form': form}
    return render(request, 'question_form.html', context) 
    # render도 HTTP 응답을 리턴하지만 첫번째 파라미터(request)에는 사용자 정보가 들어있고
    # 두번째 파라미터에는 응답으로 표시할 html파일(템플릿)이 들어있고
    # 세번째 파라미터에는 응답으로 넘기고 싶은 딕셔너리(context) 정보가 들어있다.
    # context의 용도 / form 이라는 쿼리셋을 dic형태로 담아 리턴 해준다
    # context에는 forms/QuestionForm에서 정의한 subject, content에 정보가 담겨서 넘어간다.
```