import os

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign

APP_ID = os.getenv("FB_APP_ID")
APP_SECRET = os.getenv("FB_APP_SECRET")
ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")
AD_ACCOUNT_ID = os.getenv("FB_AD_ACCOUNT_ID")


def create_campaign(name: str) -> Campaign:
    """Cria uma campanha simples pausada."""
    FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN)
    account = AdAccount(AD_ACCOUNT_ID)
    params = {
        "name": name,
        "objective": "LINK_CLICKS",
        "status": "PAUSED",
    }
    campaign = account.create_campaign(params=params)
    return campaign


if __name__ == "__main__":
    nome = os.environ.get("FB_CAMPAIGN_NAME", "Campanha de Exemplo")
    campanha = create_campaign(nome)
    print("Campanha criada:", campanha)
