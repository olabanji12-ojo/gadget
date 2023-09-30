from django.contrib import admin
from .models import Hplaptop
from .models import Dell_laptop
from .models import Toshiba_laptop
from .models import Techno_phone
from .models import Infinix_phone
from .models import Redmi_phone

admin.site.register(Hplaptop)
admin.site.register(Dell_laptop)
admin.site.register(Toshiba_laptop)
admin.site.register(Techno_phone)
admin.site.register(Infinix_phone)
admin.site.register(Redmi_phone)

# Register your models here.
