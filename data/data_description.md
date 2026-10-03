Employee:
- id: унікальний ідентифікатор сутності, який дозволяє однозначно відрізняти її від інших та створювати зв'язки між таблицями.
- name: щоб ідентифікувати працівника та персоналізувати результат
- role: визначити relevance
- team: команда, до якої належить працівник; використовується як один із сигналів для визначення релевантності activity

Team:
- id: унікальний ідентифікатор сутності
- name: і'мя для команди 

Project:
- id: унікальний ідентифікатор сутності
- name: і'мя для проекту
- description: опис проекту

Activity:
- id: унікальний ідентифікатор сутності
- creator: автор 
- project: до якого проекту належить  
- description: опис виконаної роботи
- created_at: дата створення 



### employee:
- id: 
- - 1,2,3,4,5
- name:
-  - Alise, Bob, Carl, Denny, Faride
- role:
-  - bcakend-developer, frontend-developer, data-scientist, qa-tester, product-manager
- team:
-  - web-service,web-dervice,data-processing,web-service,data-processing

### Team:
- id
-  - 1,2
- name 
- - web_creators, data_analyst


### Project:
- id
-  - 1,2
- name
-  - web-dervice,data-processing
- description
-  - creating web platform, observing data to increase profit


### Activity:
- id:
- - 1,2,3,4,5,6,7,8,9,10
- creator
- - Alise,Bob,Bob,Carl,Denny,Alise,Carl,Faride,Denny,Faride
- project
- - web-service,data-processing,web-service,web-service,data-processing,data-processing,web-service,data-processing,web-service
- description
- - l
- created_at
- - 
