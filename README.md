**Dependencies:** 
- docker 17
- docker-compose 1.16

**To run:**
- git clone
- docker-compose up

There is test database with premade users, groups, clients, creditors, credits, applications. 

Run server and use one of premade accounts to test any part of api.

- Administrators can visit api sites and admin.
- Creditors have access to creditor api only.
- Partners have access to partner api only.

**User:Password:Group**

super:supersuper:

admin:adminadmin:Administrators

creditor:creditorcredotir:Creditors

partner:partnerpartner:Partners



**Schema url:**

http://127.0.0.1:8000/api/v1/schema/



**Admin url:**

http://127.0.0.1:8000/admin/

**Partner api url:**

http://127.0.0.1:8000/api/v1/partner/client/

http://127.0.0.1:8000/api/v1/partner/application/

**Creditor api url:**

http://127.0.0.1:8000/api/v1/creditor/application/
