# >>> from shop.models import Item, Purchase
# >>> Item.objects.all()
# <QuerySet []>
# >>> from django.utils import timezone
# >>> i = Item(name = "aplle", price = 1000)
# >>> i.save()
# >>> i2 = Item(name = "acer", price = 300)
# >>> i2.save()
# >>> i3 = Item(name = 'asus', price = 600)
# >>> i3.save()
# >>> i4 = Item(name = 'hp', price = 350)
# >>> i4.save()
# >>> i5 = Item(name = "lenovo", price = 320)
# >>> i5.save()
# >>> i = Item.objects.get(id = 1)
# >>> p = Purchase(item=i, name = "Alisa Krey", age = 21, date_purchase = timezone.now())
# >>> p.save()
# >>> p1 = Purchase(item=i2,name="Rebecca Lee", age=27, date_purchase = timezone.now())
# >>> p1.save()
# >>> p2 = Purchase(item=i3, name="Bree Vandecamp", age=31, date_purchase = timezone.now())
# >>> p2.save()
# >>> p3=Purchase(item=i4, name="Linette Scavo", age=32, date_purchase=timezone.now())
# >>> p3.save()
# >>> p4=Purchase(item=i5, name="Syuzan Delfino", age=28, date_purchase=timezone.now())
# >>> p4.save()
# >>> p5=Purchase(item=i, name="Gabriel Solis", age=25, date_purchase=timezone.now())
# >>> p5.save()
# >>> p6=Purchase(item=i2, name="Tom Scavo", age=35, date_purchase=timezone.now())
# >>> p6.save()
# >>> p7=Purchase(item=i3, name="Juli Mayre", age=23, date_purchase=timezone.now())
# >>> p7.save()
# >>> p8=Purchase(item=i4, name="Sayran Karahan", age=22, date_purchase=timezone.now())
# >>> p8.save()
# >>> p9=Purchase(item=i5, name="Mike Delfino", age=34, date_purchase=timezone.now())
# >>> p9.save()
