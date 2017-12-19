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

2. http://127.0.0.1:8000/api/v1/partner/application/

To create several applications for credit on behalf of premade clients

NOTE: to ease debugging I added ListView, so it's possible to view here all id of applications.

3. http://127.0.0.1:8000/api/v1/creditor/application/

Must be empty. As we don't send any applications.

4. Choose any id to send application to creditor.

http://127.0.0.1:8000/api/v1/partner/application/send/here-paste-pk

Just click PATCH button. There is no need to specify field to patch,
as this view performs automatic patch.

5. http://127.0.0.1:8000/api/v1/creditor/application/

There must be SENT applications now, visible to creditor.

6. http://127.0.0.1:8000/api/v1/creditor/application/here-paste-pk

To view any of application choose pk and visit this url.
Status of application must be changed automatically to VIEWED.

7. http://127.0.0.1:8000/api/v1/creditor/application/

The list of applications is decreased by viewed.


8. To create or view list or view details of clients. 

http://127.0.0.1:8000/api/v1/partner/client/

http://127.0.0.1:8000/api/v1/partner/client/here-paste-pk

9. Try to visit partner api as creditor or creditor api as partner.

There must be Forbidden error.

10. http://127.0.0.1:8000/admin/

Visit as super user. All models are available (Users, Groups).

Visit as admin user. Only business models are available.


**Admin url:**

http://127.0.0.1:8000/admin/

**Partner api url:**

http://127.0.0.1:8000/api/v1/partner/client/

http://127.0.0.1:8000/api/v1/partner/application/

**Creditor api url:**

http://127.0.0.1:8000/api/v1/creditor/application/
