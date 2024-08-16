import requests
import unittest
import time

class CountryAPITest(unittest.TestCase):
    BASE_URL = "https://api.countrylayer.com/v2"
    API_KEY = "c3a8e19b80ad260d93d38fb9c12d4480"  

    def get_country(self, country_code):
        # Get country by code
        url = f"{self.BASE_URL}/alpha/{country_code}?access_key={self.API_KEY}"
        response = requests.get(url)
        # Delay to avoid rate limit issues (for free suscription)
        time.sleep(2)
        return response

    def test_get_country_US_DE_GB(self):
        # Get  (US, DE and GB) individually and validation
        country_codes = ["US", "DE", "GB"]
        for code in country_codes:
            response = self.get_country(code)
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(data['alpha2Code'], code)
            print(f"> {data['name']} -  {data['alpha2Code']}")

    def test_get_non_existent_country(self):
        # Get info for inexistent countries
        invalid_country_code = "ZZ"
        response = self.get_country(invalid_country_code)
        self.assertEqual(response.status_code, 404)  
        data = response.json()
        print(f"\n> ZZ -  {data['message']}")
        self.assertIn('message', data)

    def test_post_new_country(self):
        # Validate post fail
        url = f"{self.BASE_URL}"
        body = {
            "name": "Test Country",
            "alpha2Code": "TC",
            "alpha3Code": "TCY"
        }
        response = requests.post(url, json=body, params={'access_key': self.API_KEY})
        self.assertEqual(response.status_code, 200) 
        data = response.json()
        self.assertIn('error', data)
        print(f"\nResponse Body: {response.text}")
        print(f"Response Status Code: {response.status_code}")

if __name__ == "__main__":
    unittest.main()