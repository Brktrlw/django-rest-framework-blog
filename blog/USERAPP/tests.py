from rest_framework.test import APITestCase
from django.urls import reverse


# DOĞRU VERİLER İLE KAYIT İŞLEMİ YAP
# ŞİFRE İNVALİD OLABİLİR
# KULLANICI ADI KULLANILMIS OLABİLİR
# ÜYE GİRİŞİ YAPTIYSAK O SAYFA GÖZÜKMEMELİ
# TOKEN İLE GİRİŞ YAPTIYSAK HATA ALMALIYIZ

class UserRegistrationTestCase(APITestCase):
    url       = reverse("account:createUser")
    url_login = reverse("token_obtain_pair")
    def test_user_registration(self):
        """
            DOĞRU VERİLER İLE KAYIT İŞLEMİ
        """
        data={
            "username":"testkullanicisi",
            "password":"123Bs123"
        }
        response=self.client.post(self.url,data=data)
        self.assertEqual(201,response.status_code)



    def test_user_invalid_registration(self):
        """
            GEÇERSİZ PASSWORD VERİSİ İLE KAYIT İŞLEMİ
        """
        data={
            "username":"testkullanicisi",
            "password":"12345"
        }
        response=self.client.post(self.url,data=data)
        self.assertEqual(400,response.status_code)
    def test_unique_name(self):
        """
            UNIQUE KULLANICI ADI KULLANILDI MI
        """
        self.test_user_registration()
        data={
            "username":"testkullanicisi",
            "password":"123Bs123456"
        }
        response=self.client.post(self.url,data=data)
        self.assertEqual(400,response.status_code)

    def test_user_authenticated_registration(self):
        """
            session ile giriş yapmıs kullanıcı sayfayı görememeli
        """
        self.test_user_registration()
        self.client.login(username="testkullanicisi",password="123Bs123")
        response=self.client.get(self.url)
        self.assertEqual(403,response.status_code)

    def test_user_authenticated_token_resgistration(self):
        """
            token ile giriş yapmıs kullanıcı sayfayı görememeli
        """
        self.test_user_registration()
        data = {
            "username": "testkullanicisi",
            "password": "123Bs123"
        }
        response = self.client.post(self.url_login,data=data)
        self.assertEqual(200,response.status_code)

        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer "+token)

        response_2 = self.client.get(self.url)
        self.assertEqual(403,response_2.status_code)
