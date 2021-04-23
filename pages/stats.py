from listings.models import Listing
from realtors.models import Realtor

def totallistings():
    listingsCount = Listing.objects.count()
    return listingsCount

def totalrealtors():
    realtorsCount= Realtor.objects.count()
    return realtorsCount
