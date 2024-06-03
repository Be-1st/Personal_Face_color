# **1조 프로젝트 color insight_facecolor** <br>
**팀장: 박준희** <br>
**팀원: 백태균, 강예원, 이효원**

* 깃허브 정리 한번 하기!

## color-insight code - Junparking
### src에 있는 코드는아래와 같은 결과를 볼 수 있음.
1. color_extract.py
2. detect_face.py
3. personal_color.py
4. tone_analysis.py
5. main.py

![image](https://github.com/Be-1st/Personal_Face_color/assets/141213047/5eb23fe3-020c-49ac-9c85-ea4653c83d85)

**Option**
* 사진 경로 변경 -- image로
* main.py가 실행이 안되면 main.py의 경로도 설정해주면 될 수 있음. 경로확인은 getwcd()코드로 확인.


### web에 있는 main.py 를 이용해서 실행하면 webpage에서 실행 가능

* main.py 가 2가지가 있음. web/main.py를 실행시켜야 flask 이용해서 볼 수 있음.

**현재 까지의 실행 결과**
* web.html

![image](https://github.com/Be-1st/Personal_Face_color/assets/141213047/8d56b610-bbc7-42d7-8120-7dcff44664d2)

* result.html
  
![image](https://github.com/Be-1st/Personal_Face_color/assets/141213047/1ac7df53-bc78-43da-9e76-6ad787c3a68f)


## frontend(Web page) 
### web/template에 있는 것들로 디자인함. 

 ![image](https://github.com/Be-1st/Personal_Face_color/assets/141213047/e3b52df5-5b41-4521-be08-f950e7dad924)


- web.html과 web.css를 수정하여 디자인적으로 업그레이드함. 그외 result.html,css를 전부 수정하여 퍼스널컬러 결과별로 다르게 결과 출력 할 수 있게 수정하였음. 

![image](https://github.com/Be-1st/Personal_Face_color/assets/141213047/a1592d18-f0cf-4028-ab71-d1819b2da65b)
![image](https://github.com/Be-1st/Personal_Face_color/assets/141213047/67a29aed-cc23-42ca-ad85-0b58227b0d72)



- face detect error가 나올 경우 Backend에서는 ValueError처리후, 웹페이지에서는 얼굴 인식 할 수 없다는 메시지와 함께 다른 사진 업로드 요청하는 페이지를 만듬.
![image](https://github.com/Be-1st/Personal_Face_color/assets/141213047/ce1b32e2-2077-4f92-8a9a-40ad08d1ecee)

2) 퍼스널 컬러에 대한 정보 자료 웹 페이지에 구현
- 퍼스널 컬러 관련된 기본 정보 조사( 의미, 장점, 컬러의 종류 등)
- 스타일링을 참고할 수 있는 해당 퍼스널 컬러 대표 연예인 사진 첨부 

![image](https://github.com/Be-1st/Personal_Face_color/assets/141213047/de137071-645e-4ec5-aedc-3ed3e6917c4e)
![image](https://github.com/Be-1st/Personal_Face_color/assets/141213047/571742ff-c05e-4c23-baaf-e393840ac604)
![image](https://github.com/Be-1st/Personal_Face_color/assets/141213047/41e505e9-8c40-46fa-a5f2-a571fda7bf06)
