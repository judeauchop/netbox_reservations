from extras.plugins import PluginConfig


class NetBoxReservationsConfig(PluginConfig):
    name = 'netbox_reservations'
    verbose_name = 'NetBox Reservations'
    description = 'Manage reservations in NetBox'
    author = 'Dale Johnson'
    author_email = 'johnson.dale.e@gmail.com'
    version = '1.3.1'
    base_url = 'reservations'
    min_version = '3.6.0'
    max_version = '3.7.99'
    default_settings = {
        'top_level_menu': True,
    }


config = NetBoxReservationsConfig
