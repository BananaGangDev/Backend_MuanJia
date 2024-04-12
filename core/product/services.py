import os
import gspread
from typing import List
from django.conf import settings

def initialize_gspread() -> gspread.client.Client:
  """
  Initialize a gspread client with the given credentials.
  """
  return gspread.service_account_from_dict(get_credentials())  # Note: we could move this to settings to do this once.

def get_credentials() -> dict:
  """
  Return gspread credentials.
  """
  return {
    "type": "service_account",
    "project_id": "muanjia",
    "private_key_id": "81cde9689c0d301ebb5e1c0bb782e9afa522f601",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC8/1PGaYMJwViK\nQmj+zs+J5hsgJgnccYcgz+ytaz94oNYCV4actCBXnpkhVBlwIs8emc7IUgi07KoJ\nDOa5hGKmMSua++HOOqCq6YTk9/rcq5yoyeYJ0lr0X1yE3VVPIL/6nWLOgoS3Mu0b\nJ+e9gn/BtbAe5dv3lsA+hq0GnzEr8mUausxhpAX6DV/ytNPgU0OZOOOucuHHpQ5k\n5qiVbOMLZ2O71I6U8u6AIkhxIMXQdqTN+iiLzks5VMuxR+3KYL0heNtkqGIqhgQU\nzg+X38yZpFoW3tZLfxEc4rh81QLRDQ4p0MjECDfl1MkGaI1JTJr+aKmzqsHX26W/\n+iArl0yrAgMBAAECggEAJNaHl7bdKbub7GcBXBknbrOBOgTwCx29vvGIKk0rM/H1\nhMNWo5igbTOmmU5xHuBKCqbkHTuQIuO2SMlQ93wMVmRjIXRTEQVwZ5/YnWCQbw6s\nHGIuCmAMBnHH8MXLaP7zLIAc0C+0epjcilx+2Ptkt3cYew1GkL27fvR1KUNCLFRe\n91QUeS1N/xsuiauxqUeelmOFUg8iewFWaAhqikBshFVerBfwgYV3aycMKDw/klHp\nNQ+HoNVE2TP2yDFJEPokdP2seOgF8BT8uYBVUD4hSgUM8ss4mR2PLi3YiFm5QjHa\n2F1odMkYBHIxdNznlPrkyWakTlRs4B0FnkX0X+DX4QKBgQDl97m6KB92nlP//iwS\nU+cRvA4A7RrXYZAcWoOBDI5VxIUViwfKFZtkJVxGca5FYDE4uxIQxqpGBKfxg3uj\nndEKesDno+ANlQxZAg6OJX5VyDC+WM3+LlqfGgKVHlf5CiTuSeux/A2LMJXR1gm5\n7BmIXvYBBzQbsfDoMqRuowXnaQKBgQDSZFDglCV2nq0yfF2Pybi2fkCn4lJg2gA8\nNCz+MoPAhp2gNTyVLA2mzMu2lDirCKGJ6j/RODJLsxNhfZlH7Jtz+zUjHh9KR+Yx\nS82Ej8WESFOGGgJYzvr+yEvIVxu6dR5LMrzzdy8gCAzJHT6NGojaBaB6UfHqUNih\nBzsbRYcE8wKBgQDRbRd7u3xjxu5SjANQsY4WLX9HQqaWDKhz2c42oNuiqfRU2Sc/\n1wuLWSa+lFqTnXVV568dDf8VArp7DDV1nIw5ke7JRQkO9XSoPmJI+0YhEs2pGzCF\nUWt/xu0hJeAR0TYut6zoitU+tAFMdjKnWacq9OftqcS/j/4HR89NXjNLOQKBgQDP\nPHTV4ddNEltzwUC/o2lIiO/S7oFKWTGmG5a+BK/2ciLNbeLw5OXFiTCX9UQkZGoJ\n2S1nPj18hzXt77OOPyeYhLcAkmkr18qMgCg+DQf3lu5+xxvMsoRVdqH/Ap6TeU2P\nsLih8KIAoS1G5IF6p8ppRuWd1x29OklHxEGaSVAHtQKBgQDBYYMnKQQpZwuktdT9\nsvZJq0MuRoSgVa/miUZqpaDSQStrksX0/M2xbFFuAhjbwQQTpO8K4dX/GD0gz9TN\nQ2HeElNkmXSK0tNazTHc7UYjtm7K62i/5kIks0g/z0rrdxG54dTiGBJ2TsQEV87O\nPhX/KS69d61Fv13uheFyXSaAqA==\n-----END PRIVATE KEY-----\n",
    "client_email": "spy-241@muanjia.iam.gserviceaccount.com",
    "client_id": "116373356867446353378",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/spy-241%40muanjia.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
    }


def get_all_rows(doc_name: str, sheet_name: str = None) -> List[dict]:
  sh = settings.GSPREAD_CLIENT.open(doc_name)
  worksheet = sh.worksheet(sheet_name) if sheet_name else sh.get_worksheet(0)
  return worksheet.get_all_records()
