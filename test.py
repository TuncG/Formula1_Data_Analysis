import fastf1 as ff1
ff1.Cache.enable_cache('./Cache')
monza_quali = ff1.get_session(2019, 'Monza', 'Q')
vettel = monza_quali.get_driver('VET')
print(f"Pronto {vettel.name}?")