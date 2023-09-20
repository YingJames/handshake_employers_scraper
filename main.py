from bs4 import BeautifulSoup
import requests
import json
import csv

employer_list_URL = input("Example: https://usf.joinhandshake.com/career_fairs/42906/employers_list\n\tPaste Handshake Career Fair URL and press enter: ")

cookies = {
    'production_submitted_email_address': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltcGhiV1Z6ZVRFME9FQjFjMll1WldSMUlnPT0iLCJleHAiOiIyMDQzLTA5LTIwVDAzOjU4OjI1LjQ5N1oiLCJwdXIiOm51bGx9fQ%3D%3D--7d46c790faebb82fc57cba68375864b4b48acf41',
    'production_current_user': '32603307',
    'hss-global': 'eyJhbGciOiJkaXIiLCJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwidHlwIjoiSldUIn0..NK8-_q-SMjUf7FaM5WQBhw.j_OwmS7ziff_iqInB93NMyEcDIo6M79g8UiSIOI0nlZvTCyMtPuQaBiNh5niOAIKdHF81N-aThCOElZ9d5gGKCrwb0Aa0d7Lj_MwyJvIcby_X6cvdTVE3nhn0Qgbt8xmssXJfEmIpIYQ70RaXujeYM3p39Pk8dvL7cHJvUNizqucF1IPWBGRsxi5_oZtioapHZKLEAHEhy9cYtrAMduLdH2C_0_ZAcvNSYtJ8frV8VEBDdH9AWnfzFTuygBx9_dThdh5kqHJ7pYbZCP4_0QkvLCEtlYr59NP8MZyDTsExv2tViMz09f5TYFcLnC8bxHc-mJ--YKONhYS1lLRkwHrQt4grAJkKXCW7qiJPSuuY63IH9z-MEBm2VL7G0G5w70I.FeS0CBuexGJHOJRg5CxxWUEifOdXNdw6pojHlBUOw-Y',
    '_trajectory_session': 'ZjMxU2E3Z0ZJQkkxdnlQRGU1MENpa3JPOWdRMzJqeVpQbnJsYWt3RVorL2RhK3ZqbjBsMXROeE8yMGFJc21DZHpHWGsvRFhHaFN3bzgzemtCU01vbUQzMHdnNk8wYVBkdW1UOVJmM3ZEWDY5clZteEJCeFBVUWFsZmtjSlJwWWIzTFM4MEFJbzF2cm16bDlUT0VHVHZ5Qk9LdmJTTXBVSi9lOC9sVUk0VWlkQlBFTjlKc2h5NWV1OVQ5c1NTQmc5MTB5dlFXRW9GTGN4U3JkWlQrYVJkbVFRM0h3cnVPNmFhUnJMOWE0V3J2blpMYmRPYkV0dVczWUZwZjQ0SEdvby0tNTVCSE9NeFl5MEhQSUF3b3U1REFOdz09--d47a281d02ba446a48ef3d14a978f1c9d90b132c',
    'production_js_on': 'true',
    'production_32603307_incident-warning-banner-show': '%5B%5D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': employer_list_URL,
    'X-CSRF-Token': 'EZBPKgReIZtdTrzZPCgFllZglwkTa08w+Y7GRm2TuaNsblqMje8txK/WgQ4NYU3aY2hR+uBfRo+yy4S2ZwHshg==',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    # 'Cookie': 'production_submitted_email_address=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltcGhiV1Z6ZVRFME9FQjFjMll1WldSMUlnPT0iLCJleHAiOiIyMDQzLTA5LTIwVDAzOjU4OjI1LjQ5N1oiLCJwdXIiOm51bGx9fQ%3D%3D--7d46c790faebb82fc57cba68375864b4b48acf41; production_current_user=32603307; hss-global=eyJhbGciOiJkaXIiLCJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwidHlwIjoiSldUIn0..NK8-_q-SMjUf7FaM5WQBhw.j_OwmS7ziff_iqInB93NMyEcDIo6M79g8UiSIOI0nlZvTCyMtPuQaBiNh5niOAIKdHF81N-aThCOElZ9d5gGKCrwb0Aa0d7Lj_MwyJvIcby_X6cvdTVE3nhn0Qgbt8xmssXJfEmIpIYQ70RaXujeYM3p39Pk8dvL7cHJvUNizqucF1IPWBGRsxi5_oZtioapHZKLEAHEhy9cYtrAMduLdH2C_0_ZAcvNSYtJ8frV8VEBDdH9AWnfzFTuygBx9_dThdh5kqHJ7pYbZCP4_0QkvLCEtlYr59NP8MZyDTsExv2tViMz09f5TYFcLnC8bxHc-mJ--YKONhYS1lLRkwHrQt4grAJkKXCW7qiJPSuuY63IH9z-MEBm2VL7G0G5w70I.FeS0CBuexGJHOJRg5CxxWUEifOdXNdw6pojHlBUOw-Y; _trajectory_session=ZjMxU2E3Z0ZJQkkxdnlQRGU1MENpa3JPOWdRMzJqeVpQbnJsYWt3RVorL2RhK3ZqbjBsMXROeE8yMGFJc21DZHpHWGsvRFhHaFN3bzgzemtCU01vbUQzMHdnNk8wYVBkdW1UOVJmM3ZEWDY5clZteEJCeFBVUWFsZmtjSlJwWWIzTFM4MEFJbzF2cm16bDlUT0VHVHZ5Qk9LdmJTTXBVSi9lOC9sVUk0VWlkQlBFTjlKc2h5NWV1OVQ5c1NTQmc5MTB5dlFXRW9GTGN4U3JkWlQrYVJkbVFRM0h3cnVPNmFhUnJMOWE0V3J2blpMYmRPYkV0dVczWUZwZjQ0SEdvby0tNTVCSE9NeFl5MEhQSUF3b3U1REFOdz09--d47a281d02ba446a48ef3d14a978f1c9d90b132c; production_js_on=true; production_32603307_incident-warning-banner-show=%5B%5D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'ajax': 'true',
    'category': 'StudentRegistration',
    'including_all_facets_in_searches': 'true',
    'sort_direction': 'asc',
    'sort_column': 'default',
    'qualified_only': '',
    'per_page': '200',
}

response = requests.get(
    employer_list_URL,
    params=params,
    cookies=cookies,
    headers=headers,
)
soup = BeautifulSoup(response.content, 'html.parser')
site_json = json.loads(soup.text)
# print(json.dumps(site_json, indent=4, sort_keys=True))
# print(json.dumps(site_json['results'][-1], indent=4, sort_keys=True))
# employers = soup.find("h2", attrs={"class": "style__heading___29i1Z"})
# # industry = soup.findAll("div", attrs={"div": ""})
# print("test")
fieldnames = [
    "Name",
    "Description",
    "Industry",
    "Logo URL",
    "Website",
    "Job Titles",
    "Job Types",
    "Employment Types",
]
with open("employers_list.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for employer_data in site_json['results']:
        print(f"Name: {employer_data['employer_name']}")
        print(f"Description: {employer_data['company_description']}")
        print(f"Industry: {employer_data['employer']['industry']['name']}")
        print(f"Logo URL: {employer_data['employer']['logo_url']}")
        print(f"Website: {employer_data['employer']['website']}")
        print(f"Job Titles: {employer_data['job_titles']}\n")
        print(f"Job Types:")
        for job_type in employer_data['job_types']:
            print(f"\t{job_type['name']}")
        print(f"Employment Types:")
        for employment_type in employer_data['employment_types']:
            print(f"\t{employment_type['name']}")
        print("=====================================================")

        job_types = [job_type['name'] for job_type in employer_data['job_types']]
        all_job_types = ' - '.join(job_types)

        employment_type = [employment_type['name'] for employment_type in employer_data['employment_types']]
        all_employment_types = ' - '.join(employment_type)

        writer.writerow(
            {
                "Name": employer_data["employer_name"],
                "Description": employer_data["company_description"],
                "Industry": employer_data["employer"]["industry"]["name"],
                "Logo URL": employer_data["employer"]["logo_url"],
                "Website": employer_data["employer"]["website"],
                "Job Titles": employer_data["job_titles"],
                "Job Types": all_job_types,
                "Employment Types": all_employment_types,
            }
        )

print("employers_list.csv Spreadsheet created!")