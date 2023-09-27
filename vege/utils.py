from django.utils.text import slugify
import uuid

def generate_slug(title:str)->str:

    """
    A function to generate Sluf for items in Recipe Model , returns str
    """

    title = slugify(title)
    from .models import Reci

    while (Reci.objects.filter(slug = title).exists()):
        title = f"{slugify(title)}-{str(uuid.uuid4())[0:4 ]}"

    return title