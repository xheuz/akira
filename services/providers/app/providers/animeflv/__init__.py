from config import ANIMEFLV_BASE_URL
from app.providers.animeflv.core import AnimeFLV

animeflv = AnimeFLV(base_url=ANIMEFLV_BASE_URL)

__all__ = [animeflv]
