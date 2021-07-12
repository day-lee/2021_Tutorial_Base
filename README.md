# 📚 튜토리얼 베이스 Tutorial Base

### 📌 [배운점&피드백 보러가기](https://www.notion.so/ff25ee0bef7144be92ec4f2319a58b15)

### 📌 [Demo Video 보러가기](https://youtu.be/7yJysD6QQ08)

### 📌 기간 Project Period
- 2021.02 - 2021.03 & Ongoing
 
### 📌 프로젝트 개요 Description
튜토리얼 베이스는 파이썬과 장고 학습자를 위한 프로젝트입니다. 
<br>프로그래밍을 독학하면서, 수많은 무료 학습 자료를 이용해봤습니다. 
<br>양질의 자료를 찾기 위해 많은 시간을 쏟으면서, 잘 정리되고 선별된 데이터베이스의 필요성을 느꼈습니다. 

튜토리얼 베이스는 온라인 무료 강의 데이터베이스를 검색하고, 저장하여 커스텀 커리큘럼을 만들 수 있습니다.
<br>또한 커뮤니티 게시판 기능을 제공합니다.


Abundant tutorials on the internet greatly helped me to grow as a developer; 
<br>however, I often struggled with finding suitable ones and spent tons of time.
<br>Hence, I created a database of free online tutorial database for Django and Python learners.
<br>At Tutorial Base, you can search the right tutorial, build your own curriculum and post on community board. 


### 📌 프로젝트 중점 사항
- 게시판, 커리큘럼(장바구니) CRUD 기능 | Board, Curriculum(Cart) CRUD
- Query String을 사용한 검색, 페이징 | Search with Query String and pagination  
- 권한에 따른 기능 구분 | Permission system
- 객체지향 디자인 패턴 적용 | OOP design pattern
- 문서화 |  Docstrings 

### 📌 기술 스택 Stacks
- Python
- Django
- MySQL
- Heroku

📌 핵심 기능 Features
-----------------
#### ✔️회원가입 & 로그인 | Register & Login
- 개인정보와 비밀번호 수정 CRUD |  Edit user information and password   
<br>

![image](https://user-images.githubusercontent.com/73591588/124927770-f1d5a400-e039-11eb-82d2-2282912169bc.png)


#### ✔️튜토리얼 리스트 | Tutorial list  
- 언어, 주제, 강사, 난이도 별로 상세 필터를 적용 및 검색 | Filter and search tutorials by language, instructor, title, difficulty
- 튜토리얼 상제 페이지, 대표 유튜브 영상 삽입 | View tutorial detail page and embeded youtube video
- 페이징 | Pagination
<br>

![img_2](https://user-images.githubusercontent.com/73591588/124927617-cce13100-e039-11eb-9ea8-75bda1f4e3b8.png)

#### ✔️커리큘럼 (장바구니 기능) | Curriculum (similar to cart)
- 나의 커리큘럼에 추가한 튜토리얼을 모아보기, 삭제, 페이징 | View, add and delete cart items, Pagination
- 추가한 튜토리얼 필터, 검색 기능 | Filter and search tutorials on curriculum page
- 공부 목표 메모 CRUD | Add and edit a study goal memo 
<br>

![img](https://user-images.githubusercontent.com/73591588/124927495-a9b68180-e039-11eb-8c59-575e66f3da49.png)

#### ✔️커뮤니티 보드 | Community Board
- 글과 코멘트 작성, 수정, 삭제 | Create, edit and delete a post and comment
- CKEditor 
<br>

![image](https://user-images.githubusercontent.com/73591588/125044119-a02f2700-e0d6-11eb-801b-4c251e7af1d0.png)


