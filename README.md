# firstproject
## 공유 diary app 만들기
---
## 주요 기능
1. 회원가입 및 로그인
2. 사용자의 프로필
3. 일기 및 투두리스트 작성하기
4. 친구 신청
5. 친구가 맺어진 사람들의 게시글이 보이는 피드
6. 친구의 게시글에 댓글 달기
7. 친구의 게시글에 느낌 버튼 누르기
### 추가로 구현하고 싶은 내용
1. 프로필 아이디 검색 기능
2. 친구에게만 공개하는 비공개 계정 설정 기능
3. 상대방이 보낸 친구 신청을 수락해야만 서로 맺어지는 관계 
---
```
myapp > master app  
ㄴ settings.py  
ㄴ urls.py  
app  
templates  
  ㄴapp  
    ㄴ detail.html  
    ㄴ form.html  
    ㄴ index.html  
    ㄴ reply_form.html  
    ㄴ reply_list.html  
ㄴ forms.py  
ㄴ models.py  
ㄴ urls.py  
ㄴ views.py  
templates  
ㄴ _navbar.html  
ㄴ base.html  
accounts  
ㄴtemplates  
  ㄴaccounts  
    ㄴ profile.html  
    ㄴ profile_index.html  
    ㄴ friends_list.html
    ㄴ signin.html  
    ㄴ signup.html  
ㄴ forms.py  
ㄴ models.py  
ㄴ urls.py  
ㄴ views.py
```