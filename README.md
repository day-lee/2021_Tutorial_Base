# ๐ ํํ ๋ฆฌ์ผ ๋ฒ ์ด์ค Tutorial Base

### ๐ [๋ฐฐ์ด์ &ํผ๋๋ฐฑ ๋ณด๋ฌ๊ฐ๊ธฐ](https://www.notion.so/ff25ee0bef7144be92ec4f2319a58b15)

### ๐ [Demo Video ๋ณด๋ฌ๊ฐ๊ธฐ](https://youtu.be/7yJysD6QQ08)

### ๐ ๊ธฐ๊ฐ Project Period
- 2021.02 - 2021.03 & Ongoing
 
### ๐ ํ๋ก์ ํธ ๊ฐ์ Description
ํํ ๋ฆฌ์ผ ๋ฒ ์ด์ค๋ ํ์ด์ฌ๊ณผ ์ฅ๊ณ  ํ์ต์๋ฅผ ์ํ ํ๋ก์ ํธ์๋๋ค. 
<br>ํ๋ก๊ทธ๋๋ฐ์ ๋ํํ๋ฉด์, ์๋ง์ ๋ฌด๋ฃ ํ์ต ์๋ฃ๋ฅผ ์ด์ฉํด๋ดค์ต๋๋ค. 
<br>์์ง์ ์๋ฃ๋ฅผ ์ฐพ๊ธฐ ์ํด ๋ง์ ์๊ฐ์ ์์ผ๋ฉด์, ์ ์ ๋ฆฌ๋๊ณ  ์ ๋ณ๋ ๋ฐ์ดํฐ๋ฒ ์ด์ค์ ํ์์ฑ์ ๋๊ผ์ต๋๋ค. 

ํํ ๋ฆฌ์ผ ๋ฒ ์ด์ค๋ ์จ๋ผ์ธ ๋ฌด๋ฃ ๊ฐ์ ๋ฐ์ดํฐ๋ฒ ์ด์ค๋ฅผ ๊ฒ์ํ๊ณ , ์ ์ฅํ์ฌ ์ปค์คํ ์ปค๋ฆฌํ๋ผ์ ๋ง๋ค ์ ์์ต๋๋ค.
<br>๋ํ ์ปค๋ฎค๋ํฐ ๊ฒ์ํ ๊ธฐ๋ฅ์ ์ ๊ณตํฉ๋๋ค.


Abundant tutorials on the internet greatly helped me to grow as a developer; 
<br>however, I often struggled with finding suitable ones and spent tons of time.
<br>Hence, I created a database of free online tutorial database for Django and Python learners.
<br>At Tutorial Base, you can search the right tutorial, build your own curriculum and post on community board. 


### ๐ ํ๋ก์ ํธ ์ค์  ์ฌํญ
- ๊ฒ์ํ, ์ปค๋ฆฌํ๋ผ(์ฅ๋ฐ๊ตฌ๋) CRUD ๊ธฐ๋ฅ | Board, Curriculum(Cart) CRUD
- Query String์ ์ฌ์ฉํ ๊ฒ์, ํ์ด์ง | Search with Query String and pagination  
- ๊ถํ์ ๋ฐ๋ฅธ ๊ธฐ๋ฅ ๊ตฌ๋ถ | Permission system
- ๊ฐ์ฒด์งํฅ ๋์์ธ ํจํด ์ ์ฉ | OOP design pattern
- ๋ฌธ์ํ |  Docstrings 

### ๐ ๊ธฐ์  ์คํ Stacks
- Python
- Django
- MySQL
- Heroku

๐ ํต์ฌ ๊ธฐ๋ฅ Features
-----------------
#### โ๏ธํ์๊ฐ์ & ๋ก๊ทธ์ธ | Register & Login
- ๊ฐ์ธ์ ๋ณด์ ๋น๋ฐ๋ฒํธ ์์  CRUD |  Edit user information and password   
<br>

![image](https://user-images.githubusercontent.com/73591588/124927770-f1d5a400-e039-11eb-82d2-2282912169bc.png)


#### โ๏ธํํ ๋ฆฌ์ผ ๋ฆฌ์คํธ | Tutorial list  
- ์ธ์ด, ์ฃผ์ , ๊ฐ์ฌ, ๋์ด๋ ๋ณ๋ก ์์ธ ํํฐ๋ฅผ ์ ์ฉ ๋ฐ ๊ฒ์ | Filter and search tutorials by language, instructor, title, difficulty
- ํํ ๋ฆฌ์ผ ์์  ํ์ด์ง, ๋ํ ์ ํ๋ธ ์์ ์ฝ์ | View tutorial detail page and embeded youtube video
- ํ์ด์ง | Pagination
<br>

![img_2](https://user-images.githubusercontent.com/73591588/124927617-cce13100-e039-11eb-9ea8-75bda1f4e3b8.png)

#### โ๏ธ์ปค๋ฆฌํ๋ผ (์ฅ๋ฐ๊ตฌ๋ ๊ธฐ๋ฅ) | Curriculum (similar to cart)
- ๋์ ์ปค๋ฆฌํ๋ผ์ ์ถ๊ฐํ ํํ ๋ฆฌ์ผ์ ๋ชจ์๋ณด๊ธฐ, ์ญ์ , ํ์ด์ง | View, add and delete cart items, Pagination
- ์ถ๊ฐํ ํํ ๋ฆฌ์ผ ํํฐ, ๊ฒ์ ๊ธฐ๋ฅ | Filter and search tutorials on curriculum page
- ๊ณต๋ถ ๋ชฉํ ๋ฉ๋ชจ CRUD | Add and edit a study goal memo 
<br>

![img](https://user-images.githubusercontent.com/73591588/124927495-a9b68180-e039-11eb-8c59-575e66f3da49.png)

#### โ๏ธ์ปค๋ฎค๋ํฐ ๋ณด๋ | Community Board
- ๊ธ๊ณผ ์ฝ๋ฉํธ ์์ฑ, ์์ , ์ญ์  | Create, edit and delete a post and comment
- CKEditor 
<br>

![image](https://user-images.githubusercontent.com/73591588/125044119-a02f2700-e0d6-11eb-801b-4c251e7af1d0.png)


