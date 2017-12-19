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

**Instruction for testing**
1. Login as 'super'

2. Visit partner api to create several applications for credit on behalf of premade clients.

NOTE: to ease debugging I added ListView, so it's possible to view here all ids of applications.

http://127.0.0.1:8000/api/v1/partner/application/


3. Visit creditor api to view SENT applications. 

It must be empty. As we don't send any applications.

http://127.0.0.1:8000/api/v1/creditor/application/

4. Choose any id, paste it in url and vitis it to send application to creditor.

Just click PATCH button. There is no need to specify field to patch, as this view performs automatic patch.

http://127.0.0.1:8000/api/v1/partner/application/send/here-paste-pk

5. Visit creditor api to view SENT applications.

There must be SENT applications now, visible to creditor.

http://127.0.0.1:8000/api/v1/creditor/application/

6. Visit creditor api to view details of SENT application. Choose id and paste it in url.

Status of application must be changed automatically to RECEIVED.

http://127.0.0.1:8000/api/v1/creditor/application/here-paste-pk

7. Now in creditor api list of applications must be decreased by viewed.

http://127.0.0.1:8000/api/v1/creditor/application/

8. To create or to view list or to view details of clients. 

http://127.0.0.1:8000/api/v1/partner/client/

http://127.0.0.1:8000/api/v1/partner/client/here-paste-pk

9. Try to visit partner api as creditor or creditor api as partner.

There must be Forbidden error.

10. http://127.0.0.1:8000/admin/

Visit as super user. All models are available (Users, Groups).

Visit as admin user. Only some business models are available (from partner api).


**Admin url:**

http://127.0.0.1:8000/admin/

**Partner api url:**

http://127.0.0.1:8000/api/v1/partner/client/

http://127.0.0.1:8000/api/v1/partner/application/

http://127.0.0.1:8000/api/v1/partner/application/send/here-must-be-pk

**Creditor api url:**

http://127.0.0.1:8000/api/v1/creditor/application/
